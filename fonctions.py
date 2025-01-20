#import ollama
from imap_tools import MailBox, A
from PySide6.QtGui import QStandardItem
from email.utils import parseaddr
import speech_recognition as sr
from PySide6.QtCore import QThread, Signal, QTimer,QMutex, QMutexLocker
import pyttsx3
from groq import Groq
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QFileInfo
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
#from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import threading
from langchain.schema import Document
from prompt import react_system_prompt

client = Groq(api_key="YOUR_API_KEY")
# Text-to-Speech (TTS) Thread
class SpeakThread(QThread):
    stop_signal = Signal()

    def __init__(self, engine, emails):
        super().__init__()
        self.engine = engine
        self.emails = emails
        self.running = True
        self.mutex = QMutex()
        self.stop_requested = False  # Flag to indicate stop request

    def run(self):
        for email in self.emails:
            if not self.running:
                break
            text = f"From: {email.from_}\nSubject: {email.subject}\n\n{email.text}"
            text = text.encode('ascii', 'ignore').decode('ascii')

            for chunk in self.chunk_text(text, 100):
                if self.stop_requested:  # Check if stop was requested
                    break
                self.engine.say(chunk)
                self.engine.runAndWait()
                # Ensure the stop flag is checked periodically

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stop_requested = True  # Request stop
            self.running = False  # Stop the run loop
            if self.engine.isBusy():
                self.engine.stop()  # Stop the TTS engine if it's busy
            self.quit()  # Stop the QThread event loop
        self.wait()  # Wait for the thread to finish
        print("SpeakThread stopped")

    def chunk_text(self, text, chunk_size):
        """Helper method to chunk text into manageable pieces."""
        return (text[i:i + chunk_size] for i in range(0, len(text), chunk_size))

# Speech Recognition Thread
class ListenThread(QThread):
    command_recognized = Signal(str)
    update_line_edit = Signal(str)

    def __init__(self, recognizer):
        super().__init__()
        self.recognizer = recognizer
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            try:
                print("Listening...")
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source, timeout=3)
                    MyText = self.recognizer.recognize_google(audio).lower()
                    print("Heard:", MyText)
                    self.command_recognized.emit(MyText)
                    # Emit the recognized text to update the QLineEdit
                    self.update_line_edit.emit(MyText)
            except sr.WaitTimeoutError:
                print("Listening timed out, stopping microphone.")
                self.running = False  # Stop listening on timeout
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                self.running = False  # Stop listening on request error
            except sr.UnknownValueError:
                print("Cannot understand text")
                # Continue listening if unable to understand text

    def stop(self):
        self.running = False
        self.wait()  # Wait for the thread to finish properly


class DocumentProcessor(QThread):
    progress_updated = Signal(int)
    processing_done = Signal()

    def __init__(self, documents, embedding_model):
        super().__init__()
        self.documents = documents
        self.embedding_model = embedding_model

    def chunk_documents(self, documents, chunk_size=500, overlap=50):
        """
        Splits documents into smaller chunks to improve embedding and retrieval.

        Args:
            documents (list): List of documents as text.
            chunk_size (int): Maximum size of each chunk (in tokens or characters).
            overlap (int): Number of overlapping characters between chunks for context preservation.

        Returns:
            List of chunks with context preserved.
        """
        chunks = []
        for doc in documents:
            text = doc.page_content  # Assuming doc has an attribute `page_content`
            start = 0
            while start < len(text):
                end = min(start + chunk_size, len(text))
                chunk = text[start:end]
                chunks.append({"page_content": chunk, "metadata": doc.metadata})
                start += chunk_size - overlap  # Move the window with overlap
        return chunks

    def run(self):
        # Chunk the documents before embedding
        chunked_documents = self.chunk_documents(self.documents, chunk_size=500, overlap=50)

        # Convert chunked documents into embeddings
        vector_store = FAISS.from_documents(
            [Document(page_content=chunk["page_content"], metadata=chunk["metadata"]) for chunk in chunked_documents],
            self.embedding_model
        )
        self.vector_store = vector_store  # Store vector_store as instance variable for later use
        self.retriever = vector_store.as_retriever()

        # Save the FAISS index locally for future use
        vector_store.save_local("faiss_index")

        # Emit signal to indicate processing is done
        self.processing_done.emit()




class Fonctions(QThread):
    # Define a signal to communicate with the main thread
    update_line_edit = Signal(str)  # Signal to update the QLineEdit


    def __init__(self, widget):
        super().__init__()
        self.widget = widget

        # Initialize QTimer for gradual text display
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label_text)
        # Initialize folder_path as an instance variable
        self.folder_path = ""
        #instances for progres bar and timer
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress_bar)
        self.progress = 0
        self.processing_thread = None
        #text to spech instances
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.unseen_emails = []
        self.speak_thread = None
        self.listen_thread = None
        # Listen thread      
        self.stop_event = threading.Event()


    def response_text(self):
        query = self.widget.ui.lineEdit.text()
        messages = [
            {"role": "system", "content": react_system_prompt},
            {"role": "user", "content": query}]
        # Set the path to the saved FAISS index
        index_path = r"C:\Users\sadfi\OneDrive\Bureau\E-tafakna\test design\testDesign\faiss_index"

        # Recreate the embeddings model (must match the model used during saving)
        embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
        embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)

        try:
            # Load the FAISS index
            vector_store = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

            # Create a retriever from the loaded vector store
            retriever = vector_store.as_retriever()

            # Perform retrieval using the loaded index
            documents = retriever.get_relevant_documents(query)

            if documents:
                # Combine the retrieved documents into a single string
                retrieved_text = " ".join([doc.page_content for doc in documents])
                messages.append({"role": "assistant", "content": "Here's what I found in the documents:"})
                messages.append({"role": "user", "content": retrieved_text})
                # Generate a response using the retrieved text
                response=self.gen(messages)
                self.widget.ui.plainTextEdit.setPlainText(response)
            else:
                # No relevant documents found, generate a response based on the query
                print("No relevant documents found. Generating response based on query.")
                response=self.gen(messages)
                self.widget.ui.plainTextEdit.setPlainText(response)

        except RuntimeError as e:
            # Handle the case where the index file is not found or another error occurs
            if "Error: 'f' failed" in str(e):
                print(f"RuntimeError: Could not open FAISS index file. Generating response based on query instead. Details: {e}")
                response=self.gen(messages)
                self.widget.ui.plainTextEdit.setPlainText(response)
            else:
                # Re-raise the exception if it's a different kind of RuntimeError
                raise e

        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
            # Handle the case where the index file is not found or another error occurs
            response=self.gen(messages)
            self.widget.ui.plainTextEdit.setPlainText(response)

    def gen(self, messages):
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192",
            )

            # Print the entire response for debugging
            #print("Full API Response:", chat_completion)

            # Access the message content correctly
            if chat_completion and chat_completion.choices:
                message_content = chat_completion.choices[0].message.content
                #print("Message Content:", message_content)

                return message_content
            else:
                print("No valid response received.")
                return None

        except Exception as e:
            print("Error in generate_response:", e)  # Debug statement
            return None
    
    
    def gen_email_response(self, input_text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": input_text,
                    }
                ],
                model="llama3-8b-8192",
            )

            # Print the entire response for debugging
            #print("Full API Response:", chat_completion)

            # Access the message content correctly
            if chat_completion and chat_completion.choices:
                message_content = chat_completion.choices[0].message.content
                #print("Message Content:", message_content)
                self.widget.ui.plainTextEdit2.setPlainText(message_content)
            else:
                print("No valid response received.")

        except Exception as e:
            print("Error in generate_response:", e)  # Debug statement
    def response_email(self):
        # Get the selected row in the table
        selected_indexes = self.widget.ui.emailTable.selectionModel().selectedRows()

        if not selected_indexes:
            print("No email selected.")
            return

        # Get the content of the selected email
        selected_row = selected_indexes[0].row()
        email_content = self.widget.model.item(selected_row, 3).text()  # Column 3 contains the email text

        if not email_content:
            print("Selected email has no content.")
            return

        # Generate a response using the email content
        content = email_content + "   Reply to that email as you're an Engineer Named Yassin Sadfi specialist in AI and embedded systems "

        # Call the gen function with the prepared content
        self.gen_email_response(content)




    def checkemail(self):
        mail = self.widget.ui.mailE.text()
        mdp = self.widget.ui.mdpE.text()
        global text
        try:
            with MailBox("imap.gmail.com", port=993).login(mail, mdp, "Inbox") as mb:
                self.widget.model.setRowCount(0)  # Clear any existing rows
                self.unseen_emails = []  # Clear the unseen_emails list

                for msg in mb.fetch(A(seen=True), limit=20, reverse=True):  # Fetch unseen emails, limit to 20
                    # Filtering logic
                    if not self.is_primary_email(msg):
                        continue

                    date_str = str(msg.date)
                    name, email = parseaddr(msg.from_)
                    sender = name if name else email
                    subject_str = msg.subject
                    text = msg.text

                    # Handle potential encoding issues
                    try:
                        subject_str = subject_str.encode('utf-8').decode('utf-8')
                    except UnicodeEncodeError:
                        subject_str = subject_str.encode('latin1').decode('utf-8')

                    row = [
                        QStandardItem(date_str),
                        QStandardItem(sender),
                        QStandardItem(subject_str),
                        QStandardItem(text)
                    ]
                    self.widget.model.appendRow(row)
                    self.unseen_emails.append(msg)  # Store the unseen email

        except Exception as e:
            print("Error in checkemail:", e)  # Debug statement

    def is_primary_email(self, msg):
            # Simple filtering logic to exclude common promotion and social keywords
            promotion_keywords = ["sale", "discount", "deal", "offer", "promotion", "purchase"]
            social_keywords = ["social", "network", "friend", "like", "connexion", "conversation"]

            subject = msg.subject.lower()
            sender = parseaddr(msg.from_)[1].lower()

            if any(keyword in subject for keyword in promotion_keywords):
                return False
            if any(keyword in subject for keyword in social_keywords):
                return False
            if "no-reply" in sender or "noreply" in sender:
                return False
            if "newsletter" in sender:
                return False

            return True


    def start_microphone(self):
        if not self.listen_thread or not self.listen_thread.isRunning():
            # Create and start the ListenThread
            self.listen_thread = ListenThread(self.r)
            self.listen_thread.update_line_edit.connect(self.update_line_edit_method)
            self.listen_thread.start()

    def stop_microphone(self):
        if self.listen_thread and self.listen_thread.isRunning():
            self.listen_thread.stop()
            self.listen_thread = None  # Remove the reference to the thread

    def handle_command(self, command):
        if "skip" in command:
            self.StopSpeakText()
        elif "stop" in command:
            self.StopSpeakText()
            self.stop_microphone()

    def update_line_edit_method(self, text):
        """Update the QLineEdit with recognized text."""
        if self.widget and self.widget.ui:
            self.widget.ui.lineEdit_2.setText(text)
        else:
            print("Widget or UI reference is not valid.")


    def listen_for_commands(self):
        while self.running:
            try:
                with sr.Microphone() as source2:
                    print("Listening for 'skip' or 'stop'...")
                    self.r.adjust_for_ambient_noise(source2)
                    audio2 = self.r.listen(source2)
                    MyText = self.r.recognize_google(audio2).lower()
                    print("Heard:", MyText)
                    self.r.pause_threshold = 1

                    if "skip" in MyText:
                        self.stop_event.set()  # Signal to stop reading the current email
                        break
                    elif "stop" in MyText:
                        self.running = False  # Signal to stop reading emails entirely
                        self.stop_event.set()  # Signal to stop reading the current email
                        return
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                continue
            except sr.UnknownValueError :
                print("Cannot understand audio")
                continue

    def SpeakText(self):
        if not self.unseen_emails:
            # No unseen emails to read
            self.engine.say("Pas de nouvelles mails")
            self.engine.runAndWait()
            return

        self.running = True  # Set running to True to start reading emails

        for email in self.unseen_emails:
            if not self.running:
                break

            # Replace problematic characters
            text = f"From: {email.from_}\nSubject: {email.subject}\n\n{email.text}"
            text = text.encode('ascii', 'ignore').decode('ascii')  # Remove non-ASCII characters

            print("Reading email:", text)  # Debug statement

            # Start a new thread for listening to commands
            self.listening_thread = threading.Thread(target=self.listen_for_commands)
            self.listening_thread.start()

            # Read the email in chunks to allow interruption
            for chunk in self.chunk_text(text, 100):  # Read in chunks of 100 characters
                if not self.running:
                    break  # Exit if the running flag is false

                if self.stop_event.is_set():
                    self.stop_event.clear()  # Reset the event
                    break  # Break out of the chunk reading loop

                self.engine.say(chunk)
                self.engine.runAndWait()

            # Wait for the listening thread to finish before continuing to the next email
            self.listening_thread.join()

            # Clear the stop event for the next email
            self.stop_event.clear()

            if not self.running:
                break
        # Reset state after finishing all emails
        self.running = False
        self.listening_thread = None

    def chunk_text(self, text, chunk_size):
        """Helper method to chunk text into manageable pieces."""
        return (text[i:i + chunk_size] for i in range(0, len(text), chunk_size))

    def StopSpeakText(self):
        self.running = False
        self.stop_event.set()
        if self.listening_thread is not None:
            self.listening_thread.join()
        #Reset
        self.stop_event.clear()




    #wait fucnt
    def wait(self):
        folder_path = self.ui_train.lineEdit.text()
        if not folder_path:
            QMessageBox.warning(self.widget, "Missing Folder Path", "Please select a folder by uploading a file.")
            return
        self.ui_train.progressBar.setValue(0)
        self.ui_train.plainTextEdit.setPlainText("")
        self.ui_train.plainTextEdit.show()
        self.text_to_display = "Just a few minutes... your documents are in process..."
        self.current_index = 0
        self.timer.start(100)

    #update the text progressively
    def update_label_text(self):
        if self.current_index < len(self.text_to_display):
            current_text = self.ui_train.plainTextEdit.toPlainText()
            self.ui_train.plainTextEdit.setPlainText(current_text + self.text_to_display[self.current_index])
            self.current_index += 1
        else:
            self.timer.stop()  # Stop the timer when the full text is displayed

    def upload_file(self):
        options = QFileDialog.Options()
        filters = "PDF Files (*.pdf);;Excel Files (*.xls *.xlsx)"
        file_names, _ = QFileDialog.getOpenFileNames(self.dialog, "Select Files", "", filters, options=options)

        if file_names:
            valid_files = []
            invalid_files = []

            # Check the extension of each file
            for file_name in file_names:
                file_extension = os.path.splitext(file_name)[1].lower()
                if file_extension in ['.pdf', '.xls', '.xlsx']:
                    valid_files.append(file_name)
                    self.folder_path = QFileInfo(file_name).absolutePath()
                    self.ui_train.lineEdit.setText(self.folder_path)  # Set folder path to QLineEdit
                else:
                    invalid_files.append(file_name)

            if invalid_files:
                # Show a message box for invalid file types
                invalid_files_str = ', '.join(invalid_files)
                QMessageBox.warning(self.dialog, "Invalid File Type",
                    f"The following files are not allowed:\n{invalid_files_str}\nPlease select only PDF or Excel files.")

            # Handle valid files as needed (e.g., process them)
            if valid_files:
                # Add code to handle valid files
                pass


    #load docs funcs
    def load_documents(self):
        # Use PDFLoader to load PDF files
        loader = DirectoryLoader(self.folder_path, glob="*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        return docs
    #Start training Btn
    def start_training(self):
        self.wait()
        documents = self.load_documents()
        total_docs = len(documents)
        if total_docs == 0:
            QMessageBox.warning(self.widget, "No Documents", "No documents were loaded for processing.")
            return

        embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
        embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)

        # Start the progress timer
        self.progress = 0
        self.ui_train.progressBar.setValue(self.progress)
        self.progress_timer.start(300)  # Update every 100 milliseconds

        # Create and start the document processing thread
        self.processing_thread = DocumentProcessor(documents, embedding_model)
        self.processing_thread.progress_updated.connect(self.update_progress_bar)
        self.processing_thread.processing_done.connect(self.processing_done)
        self.processing_thread.start()

    def processing_done(self):
        # Stop the progress timer when processing is done
        self.progress_timer.stop()
        self.ui_train.progressBar.setValue(100)
        # Show a message box to notify the user that the process is complete
        QMessageBox.information(self.widget, "Process Complete", "The documents have been processed and the FAISS index has been saved.")

    def process_documents(self, documents, embedding_model, total_docs):
        # Convert documents into embeddings
        vector_store = FAISS.from_documents(documents, embedding_model)
        self.vector_store = vector_store  # Store vector_store as instance variable for later use
        self.retriever = vector_store.as_retriever()

        # Save the FAISS index to the specified path
        #save_path = r"C:\Users\sadfi\OneDrive\Bureau\E-tafakna\faiss_indexxxx"
        self.vector_store.save_local("faiss_indexxxx")

        # Call the processing_done method to indicate completion
        self.processing_done()

        # Signal completion to stop the timer
        self.timer.stop()

    def update_progress_bar(self):
        if self.processing_thread:
            # Update the progress based on some logic
            # Here, we're just simulating progress
            self.progress += 1
            self.ui_train.progressBar.setValue(self.progress)
            if self.progress >= 100:
                self.progress_timer.stop()

    #****connecting the uiTrain file with the open_train_window fucntion
    def set_train_ui(self, ui_train, dialog):
        self.ui_train = ui_train
        self.dialog = dialog  # Store the QDialog instance
        # Connect the train button to the start_training method
        self.ui_train.trainB.clicked.connect(self.start_training)
        # Connect the upload button
        self.ui_train.uploadBtn.clicked.connect(self.upload_file)
