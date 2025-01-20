# Smart App: AI-Powered Chatbot, Email Checker & NLP  

This repository showcases an advanced **AI-powered desktop application** built with **Python** and **QtCreator**. Designed with a focus on seamless human-computer interaction, the app incorporates:  
- A **trainable chatbot** using **Retrieval-Augmented Generation (RAG)** architecture.  
- An **email checker** for efficient email management.  
- **Natural Language Processing (NLP)** capabilities, including voice-to-text and text-to-voice features.  

The app is designed to eventually integrate with a humanoid robot for enhanced administrative tasks and human-computer interaction.  

---

## **Key Features**  
1. **Chatbot with RAG Architecture**:  
   - Uses RAG to retrieve and generate accurate responses based on embedded documents.  
   - Trained and run on **GroqCloud** for high-performance inference.  

2. **Email Checker**:  
   - Efficiently manages email content, checking for specific patterns and generating responses.  

3. **NLP Capabilities**:  
   - Voice-to-text for seamless dictation.  
   - Text-to-voice for reading emails or chatbot responses aloud.  

4. **Future Integration**:  
   - Designed for implementation on humanoid robots for administrative tasks such as replying to emails and answering queries.  

---

## **How It Works**  

### **1. Core Components**  
- **System Prompt**:  
  Located in **`prompts.py`**, the system prompt ensures that the chatbot reasons through the user’s query to extract and deliver accurate information.  

- **Key Functions**:  
  Two primary functions in **`functions.py`** handle response generation:  
  - **`generate_text()`**: Retrieves the most relevant document based on the user query.  
  - **`gen()`**: Processes the extracted information and formulates a precise, context-aware answer.  

### **2. Iterative Context Feeding**  
- The chatbot uses a **message list** to append intermediate reasoning steps, feeding this context back into the model for enhanced response accuracy.  

---

## **Getting Started**  

### **Prerequisites**  
- **Python 3.8 or higher**.  
- Install dependencies with:  
  ```bash
  pip install -r requirements.txt
