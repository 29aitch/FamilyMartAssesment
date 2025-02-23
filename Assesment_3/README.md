{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid101\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid102\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid201\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid202\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid301\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid4}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa321\partightenfactor0

\f0\b\fs48 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Design Document: Offline Document Processing & Online Voice Interaction Pipelines\
\pard\pardeftab720\sa298\partightenfactor0

\fs36 \cf0 1. Overview\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf0 This architecture is divided into two main pipelines:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Offline Document Processing Pipeline:
\f1\b0  Responsible for ingesting, processing, and indexing TCM documents so that their content can be efficiently retrieved later.\
\ls1\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Online Voice Interaction Pipeline:
\f1\b0  Handles user voice input in real time, interprets the query, retrieves relevant information from the indexed documents, and generates a spoken response.\
\pard\pardeftab720\sa240\partightenfactor0
\cf0 Both pipelines work together by sharing a common vector database to ensure consistent and relevant results during user interactions.\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 2. Offline Document Processing Pipeline\
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf0 Components and Data Flow\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Raw TCM Documents:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Input:
\f1\b0  Source documents in various formats (PDFs, text files, manuals).\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  These documents contain the raw data that needs to be made searchable.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Preprocessing:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Cleans and prepares the raw documents, e.g., removing noise and formatting issues.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Ensures the data is in a uniform state for subsequent processing.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Text Chunking:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  LangChain Recursive Splitter.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Splits large documents into smaller, coherent text chunks that maintain context.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Chunking allows for more effective and granular retrieval later, ensuring that the embedding process captures meaningful segments of the text.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	4	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Embedding Model:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  SentenceTransformer with the all-MiniLM-L6-v2 model.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Converts text chunks into vector representations.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  A consistent embedding method allows both document chunks and user queries to be represented in the same vector space, facilitating accurate similarity searches.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls2\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	5	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Vector Database:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls2\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  Options such as Pinecone or FAISS.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Stores the generated embeddings and enables efficient similarity searches during query time.\
\ls2\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  A dedicated vector database ensures scalable and fast retrieval of relevant chunks based on user queries.\
\pard\tx720\tx1440\pardeftab720\partightenfactor0
\cf0 \
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 3. Online Voice Interaction Pipeline\
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf0 Components and Data Flow\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 User Voice Input:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Input:
\f1\b0  The user\'92s spoken query.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Provides an intuitive and natural way for users to interact with the system.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Speech-to-Text:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  OpenAI Whisper.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Transcribes the user's voice input into text.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Whisper is known for its robust transcription capabilities, ensuring accurate conversion of speech to text.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Query NLU:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  Rasa NLU.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Extracts the intent and entities from the transcribed query.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Understanding the user's intent helps in accurately formulating the retrieval and response generation processes.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	4	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Query Embedding:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  SentenceTransformer with the all-MiniLM-L6-v2 model (same as used in the offline pipeline).\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Transforms the query text into an embedding vector.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Using the same embedding model for both document chunks and queries ensures compatibility in the vector space for accurate similarity matching.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	5	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Vector Database Query:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Retrieves the top-K most relevant document chunks based on the query embedding.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Enables focused retrieval of contextually relevant information that can be synthesized into an answer.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	6	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 LLM Synthesis:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  OpenAI GPT-4.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Synthesizes a response by integrating the retrieved context with the user query.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  GPT-4\'92s advanced language capabilities help generate coherent and context-aware responses.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	7	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Response Generation:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Combines the LLM output with the query context to form the final textual answer.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Ensures that the generated response is both contextually rich and directly relevant to the user's question.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	8	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Text-to-Speech:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component:
\f1\b0  Google Cloud TTS.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Function:
\f1\b0  Converts the textual response back into a natural-sounding voice output.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Provides a seamless voice interaction experience, closing the loop from user input to response.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls3\ilvl0
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	9	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Voice Response:
\f1\b0 \
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls3\ilvl1
\f0\b \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Output:
\f1\b0  The final spoken answer delivered back to the user.\
\ls3\ilvl1
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u9702 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Reasoning:
\f1\b0  Completes the cycle by delivering information in the same medium as the input, maintaining the intuitive voice interaction.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf0 \
4. Data Flow and Design Rationale\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa240\partightenfactor0
\ls4\ilvl0
\fs24 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Consistency in Embeddings:
\f1\b0 \uc0\u8232 Both document chunks and user queries are embedded using the same SentenceTransformer model. This design choice is critical as it ensures that the similarity search in the vector database operates over a unified representation, which enhances retrieval accuracy.\
\ls4\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Component Specialization:
\f1\b0 \uc0\u8232 Each component is chosen based on its strength in its specific function. For instance, OpenAI Whisper for speech-to-text leverages state-of-the-art transcription technology, while GPT-4 is used for its advanced synthesis capabilities. This modular design not only optimizes performance but also allows for independent scaling and upgrades.\
\ls4\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Efficient Data Retrieval:
\f1\b0 \uc0\u8232 By pre-processing and indexing the documents offline, the system ensures that the online query processing is fast and efficient. The use of a vector database like Pinecone or FAISS supports rapid similarity searches, which is essential for real-time interactions.\
\ls4\ilvl0
\f0\b \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 User Experience Focus:
\f1\b0 \uc0\u8232 The online pipeline converts voice input to text and back to voice output, ensuring that the interaction remains as natural as possible. Coupled with robust natural language understanding (via Rasa NLU), the system aims to deliver precise and context-aware responses.\
}