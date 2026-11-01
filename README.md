# YouTube Creator Analysis

A data science and AI project that analyzes a large YouTube channel to understand the patterns behind its performance, content style, and creator characteristics.

The current dataset is based on the **penguinz0** YouTube channel and contains metadata for more than 7,000 videos.

The long-term goal is not only to analyze the channel, but also to use the collected data and analysis results to build a **creator-style chatbot** and **video script generator** using embeddings, retrieval, and large language models.

---

## Project Goals

This project has three main stages:

1. **Collect and analyze YouTube channel data**
2. **Identify patterns in content, language, thumbnails, and performance**
3. **Use those findings to build AI systems that can generate creator-style responses and video scripts**

The project is inspired by the idea that some characteristics of a successful YouTube channel can be studied quantitatively using data science and machine learning.

---

## Current Progress

### 1. YouTube Data Collection

The YouTube Data API is used to collect video metadata from the channel.

The current dataset includes:

- Video ID
- Video title
- Publication date
- View count
- Like count
- Comment count
- Video duration
- Thumbnail URL

More than **7,000 videos** have been collected and processed.

The raw metadata is first stored in CSV format and then imported into a local SQLite database for analysis.

---

### 2. Data Storage

The project currently uses:

- CSV for exported datasets
- SQLite for structured local storage
- SQL for querying the dataset

The SQLite database makes it easier to analyze thousands of videos efficiently.

---

### 3. Channel Scale Analysis

The current analysis includes:

- Total number of videos
- Total channel views
- Average views per video
- Top-performing videos
- Distribution of views across the video catalog
- Upload frequency over time

Current dataset results:

- Videos analyzed: approximately **7,241**
- Total views: approximately **13.66 billion**
- Average views per video: approximately **1.89 million**

One important result is that approximately **45.33% of the channel's videos account for 80% of total views**.

This suggests that the channel's performance is not driven only by a small number of viral videos. A relatively large part of the video catalog contributes significantly to overall views.

---

## Upload Frequency Analysis

Upload frequency has also been analyzed by year.

The data shows that the creator's upload frequency increased significantly over time.

This supports the idea that consistency is an important characteristic of the channel.

---

## Video Duration Analysis

YouTube video durations are originally returned in ISO 8601 format, for example:

```
PT12M34S
PT1H2M15S
```

These values are converted into minutes so that they can be analyzed numerically.

Videos are currently grouped into the following ranges:

- 0–5 minutes
- 5–10 minutes
- 10–15 minutes
- 15–20 minutes
- 20–30 minutes
- 30–60 minutes

Current results show that videos around **15–20 minutes** have a relatively high average view count compared with other duration groups.

This is currently treated as a correlation rather than evidence that video length directly causes higher views.

---

## Title Length Analysis

The project also analyzes the relationship between title length and video performance.

Titles are grouped by character count:

- 0–20 characters
- 20–30 characters
- 30–40 characters
- 40–50 characters
- 50–60 characters
- 60–80 characters
- 80–120 characters

Current results show that titles around **20–30 characters** tend to have relatively high average views.

Again, this is treated as a correlation rather than a causal relationship.

---

## Combined Packaging Analysis

The next step is to combine:

- Video duration
- Title length
- Average views

into a two-dimensional heatmap.

This will help identify whether particular combinations of title length and video duration are associated with stronger performance.

---

# Future Development

## 1. Thumbnail Analysis

The project will analyze thumbnails using computer vision techniques.

Planned approaches include:

- Image downloading and preprocessing
- Color distribution analysis
- RGB histogram comparison
- Spatial image segmentation
- Image embeddings
- Similarity analysis
- Identification of representative thumbnail styles

The goal is to understand whether the creator uses recurring visual patterns and whether those patterns are associated with video performance.

---

## 2. Transcript Collection

Video transcripts will be collected and connected to the corresponding video metadata.

The future database structure will contain both:

```
videos
```

and:

```
transcripts
```

linked using the video ID.

This will allow analysis of what the creator actually says rather than only analyzing video metadata.

---

## 3. Topic Analysis

Natural language processing will be used to identify the main topics discussed across thousands of videos.

Possible methods include:

- Keyword extraction
- Text embeddings
- Clustering
- Transformer-based classification
- LLM-based topic classification

The project will then compare topic categories with video performance.

---

## 4. Emotion Analysis

The transcripts will also be analyzed for emotional tone.

Potential categories may include:

- Amusement
- Anger
- Outrage
- Mockery
- Positivity
- Negativity
- Surprise

The goal is to investigate whether particular emotional patterns are associated with stronger video performance.

---

## 5. Language Style Analysis

The project will analyze characteristics of the creator's speaking style.

Planned features include:

- Sentence length
- Vocabulary complexity
- Reading level
- Profanity frequency
- Sarcasm
- Exaggeration
- Non-literal language
- Repeated expressions
- Language predictability

This analysis will later be used to create a structured **creator style profile**.

---

## 6. Perplexity and Predictability Analysis

Transformer models may be used to study how predictable the creator's language is.

Next-token probabilities can be used to estimate whether the creator tends to use predictable language or frequently produces unexpected phrases and expressions.

This may help quantify characteristics such as humor, absurdity, or unpredictability.

---

# Creator-Style AI System

The final stage of the project is to move from analysis to generation.

## 1. Transcript Chunking

Collected transcripts will be divided into smaller text chunks.

Example:

```
Video transcript
↓
Chunk 1
Chunk 2
Chunk 3
...
```

Each chunk will represent a small section of something the creator previously said.

---

## 2. Embeddings

Each transcript chunk will be converted into a numerical embedding using an embedding model.

The embeddings represent the semantic meaning of the text.

Possible tools include:

- sentence-transformers
- Hugging Face Transformers
- embedding APIs

---

## 3. Vector Database

The embeddings will be stored in a vector database.

Possible technologies include:

- FAISS
- Chroma

This will allow fast similarity searches across thousands of transcript chunks.

---

## 4. Retrieval-Augmented Generation

The project will use a Retrieval-Augmented Generation (RAG) architecture.

The planned workflow is:

```
User question
↓
Convert question to embedding
↓
Search vector database
↓
Retrieve relevant past creator statements
↓
Combine retrieved statements with creator style profile
↓
Send context to an LLM
↓
Generate response
```

This allows the model to reference relevant things the creator has actually said instead of relying only on a general prompt.

---

## 5. Creator-Style Chatbot

The first generative AI application will be a chatbot.

The chatbot will combine:

- Relevant historical statements
- Creator language patterns
- Emotional tendencies
- Vocabulary
- Sarcasm and exaggeration patterns
- Example responses

The goal is to generate responses that resemble the creator's communication style while still being grounded in retrieved transcript data.

---

## 6. Video Script Generator

A second system will generate complete video scripts.

The user will provide a topic, for example:

```
Topic:
A new AI product launch
```

The system will:

```
Topic
↓
Retrieve related creator statements
↓
Apply creator style profile
↓
Generate structured script
```

The generated output will then be evaluated against real video transcripts.

---

# Evaluation

The project will not assume that an AI system can fully recreate a human creator.

The final evaluation will investigate:

- How similar generated language is to real transcripts
- Whether vocabulary and sentence structure match
- Whether emotional tone is similar
- Whether sarcasm and exaggeration are reproduced naturally
- Whether generated scripts have coherent structure
- Where AI-generated imitation becomes unnatural or forced

An important research question is:

> How much of a creator's style can be reconstructed from their public content, and what aspects cannot be captured from data alone?

---

# Technologies

Current technologies:

- Python
- pandas
- SQLite
- SQL
- matplotlib
- YouTube Data API
- python-dotenv
- Google API Python Client

Planned technologies:

- Hugging Face Transformers
- sentence-transformers
- LLM APIs or local LLMs
- FAISS or Chroma
- RAG
- NLP
- Computer Vision
- FastAPI or Flask

---

# Project Structure

```
youtube_creator_analysis/
│
├── data/
│   ├── videos.csv
│   └── youtube.db
│
├── notebooks/
│
├── src/
│   ├── test_youtube_api.py
│   ├── create_database.py
│   └── analyze_channel.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

The `data/`, `.env`, and `.venv/` directories/files are excluded from GitHub using `.gitignore`.

---

# Current Status

The project is currently **in progress**.

Completed:

- YouTube API setup
- Channel metadata collection
- Collection of 7,000+ video records
- CSV storage
- SQLite database creation
- SQL analysis
- View distribution analysis
- Upload frequency analysis
- Video duration analysis
- Title length analysis
- Data visualization

In progress:

- Combined duration/title analysis
- Packaging analysis

Planned:

- Thumbnail analysis
- Transcript collection
- Topic analysis
- Emotion analysis
- Language style analysis
- Embeddings
- Vector search
- RAG
- Creator-style chatbot
- Video script generator
- Evaluation

---

## Important Note

This project is intended as a data science and AI learning project.

The goal is to study measurable patterns in public YouTube content and explore the capabilities and limitations of AI-based creator-style generation, not to claim that an AI system can fully reproduce the real person behind the channel.