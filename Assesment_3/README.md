# Design Document: Offline Document Processing & Online Voice Interaction Pipelines

## 1. Overview

This architecture is divided into two main pipelines:

- **Offline Document Processing Pipeline:**  
  Responsible for ingesting, processing, and indexing TCM documents so that their content can be efficiently retrieved later.

- **Online Voice Interaction Pipeline:**  
  Handles user voice input in real time, interprets the query, retrieves relevant information from the indexed documents, and generates a spoken response.

Both pipelines work together by sharing a common vector database to ensure consistent and relevant results during user interactions.

## 2. Offline Document Processing Pipeline

### Components and Data Flow

#### Raw TCM Documents
- **Input:**  
  Source documents in various formats (PDFs, text files, manuals).
- **Reasoning:**  
  These documents contain the raw data that needs to be made searchable.

#### Preprocessing
- **Function:**  
  Cleans and prepares the raw documents, e.g., removing noise and formatting issues.
- **Reasoning:**  
  Ensures the data is in a uniform state for subsequent processing.

#### Text Chunking
- **Component:**  
  LangChain Recursive Splitter.
- **Function:**  
  Splits large documents into smaller, coherent text chunks that maintain context.
- **Reasoning:**  
  Chunking allows for more effective and granular retrieval later, ensuring that the embedding process captures meaningful segments of the text.

#### Embedding Model
- **Component:**  
  SentenceTransformer with the all-MiniLM-L6-v2 model.
- **Function:**  
  Converts text chunks into vector representations.
- **Reasoning:**  
  A consistent embedding method allows both document chunks and user queries to be represented in the same vector space, facilitating accurate similarity searches.

#### Vector Database
- **Component:**  
  Options such as Pinecone or FAISS.
- **Function:**  
  Stores the generated embeddings and enables efficient similarity searches during query time.
- **Reasoning:**  
  A dedicated vector database ensures scalable and fast retrieval of relevant chunks based on user queries.

## 3. Online Voice Interaction Pipeline

### Components and Data Flow

#### User Voice Input
- **Input:**  
  The user’s spoken query.
- **Reasoning:**  
  Provides an intuitive and natural way for users to interact with the system.

#### Speech-to-Text
- **Component:**  
  OpenAI Whisper.
- **Function:**  
  Transcribes the user's voice input into text.
- **Reasoning:**  
  Whisper is known for its robust transcription capabilities, ensuring accurate conversion of speech to text.

#### Query NLU
- **Component:**  
  Rasa NLU.
- **Function:**  
  Extracts the intent and entities from the transcribed query.
- **Reasoning:**  
  Understanding the user's intent helps in accurately formulating the retrieval and response generation processes.

#### Query Embedding
- **Component:**  
  SentenceTransformer with the all-MiniLM-L6-v2 model (same as used in the offline pipeline).
- **Function:**  
  Transforms the query text into an embedding vector.
- **Reasoning:**  
  Using the same embedding model for both document chunks and queries ensures compatibility in the vector space for accurate similarity matching.

#### Vector Database Query
- **Function:**  
  Retrieves the top-K most relevant document chunks based on the query embedding.
- **Reasoning:**  
  Enables focused retrieval of contextually relevant information that can be synthesized into an answer.

#### LLM Synthesis
- **Component:**  
  OpenAI GPT-4.
- **Function:**  
  Synthesizes a response by integrating the retrieved context with the user query.
- **Reasoning:**  
  GPT-4’s advanced language capabilities help generate coherent and context-aware responses.

#### Response Generation
- **Function:**  
  Combines the LLM output with the query context to form the final textual answer.
- **Reasoning:**  
  Ensures that the generated response is both contextually rich and directly relevant to the user's question.

#### Text-to-Speech
- **Component:**  
  Google Cloud TTS.
- **Function:**  
  Converts the textual response back into a natural-sounding voice output.
- **Reasoning:**  
  Provides a seamless voice interaction experience, closing the loop from user input to response.

#### Voice Response
- **Output:**  
  The final spoken answer delivered back to the user.
- **Reasoning:**  
  Completes the cycle by delivering information in the same medium as the input, maintaining the intuitive voice interaction.

## 4. Data Flow and Design Rationale

### Consistency in Embeddings
Both document chunks and user queries are embedded using the same SentenceTransformer model. This design choice is critical as it ensures that the similarity search in the vector database operates over a unified representation, which enhances retrieval accuracy.

### Component Specialization
Each component is chosen based on its strength in its specific function. For instance, OpenAI Whisper for speech-to-text leverages state-of-the-art transcription technology, while GPT-4 is used for its advanced synthesis capabilities. This modular design not only optimizes performance but also allows for independent scaling and upgrades.

### Efficient Data Retrieval
By pre-processing and indexing the documents offline, the system ensures that the online query processing is fast and efficient. The use of a vector database like Pinecone or FAISS supports rapid similarity searches, which is essential for real-time interactions.

### User Experience Focus
The online pipeline converts voice input to text and back to voice output, ensuring that the interaction remains as natural as possible. Coupled with robust natural language understanding (via Rasa NLU), the system aims to deliver precise and context-aware responses.
