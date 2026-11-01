# YouTube Creator Analysis

**A Data Science & AI Project for Understanding YouTube Performance and Creator Style**

An ongoing project that uses Python, SQL, and statistical analysis to investigate YouTube channel performance and identify patterns in successful content.

The current implementation collects and analyzes over **7,000 YouTube videos**, examining video duration, title length, upload frequency, and view distribution.

The long-term goal is to extend the analysis to transcripts, thumbnails, and language patterns, eventually developing a **Retrieval-Augmented Generation (RAG) chatbot and AI video script generator** that explore how well AI can reproduce measurable characteristics of a creator's communication style.

## Project Overview

Many YouTube creators develop recognizable styles through their language, video structure, topics, and presentation.

But how much of that style can be measured through data?

This project explores three questions:

1. What patterns are associated with successful YouTube videos?
2. Can a creator's content and communication style be described quantitatively?
3. Can these findings support an AI system that generates responses and video scripts reflecting those characteristics?

The project currently focuses on the **penguinz0 (MoistCr1TiKaL)** YouTube channel as a case study.

The aim is not to claim that AI can perfectly reproduce a real person, but to investigate what can and cannot be learned from publicly available content.

## Current Development Status

**Status: In Progress — Data Collection & Exploratory Analysis**


| Component                                  | Status      |
| ------------------------------------------ | ----------- |
| YouTube Data API integration               | Completed   |
| Video metadata collection                  | Completed   |
| CSV and SQLite storage                     | Completed   |
| SQL-based channel statistics               | Completed   |
| View distribution analysis                 | Completed   |
| Upload frequency analysis                  | Completed   |
| Video duration analysis                    | Completed   |
| Title length analysis                      | Completed   |
| Data visualization                         | Completed   |
| Combined duration/title analysis           | In progress |
| Thumbnail and transcript analysis          | Planned     |
| Creator-style chatbot and script generator | Planned     |


The data collection and analysis components have been implemented in Python. The generative AI components remain future development goals.

---

## Technology Stack


| Category        | Technologies             |
| --------------- | ------------------------ |
| Programming     | Python                   |
| Data processing | pandas, NumPy            |
| Database        | SQLite, SQL              |
| Visualization   | matplotlib               |
| Data collection | YouTube Data API v3      |
| API integration | Google API Python Client |
| Configuration   | python-dotenv            |
| Development     | Git, GitHub              |


### Planned Technologies

For later AI development:

- Hugging Face Transformers and sentence-transformers
- NLP and text embeddings
- Computer vision for thumbnail analysis
- FAISS or Chroma for vector search
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- FastAPI or Flask for application APIs

These technologies are part of the roadmap and are not yet implemented in this repository.

---

# 1. Data Collection and Processing

## YouTube Data API Integration

The project uses the YouTube Data API v3 to retrieve information about the target channel and its uploaded videos.

Collected metadata includes:

- Video ID and title
- Publication date
- View count
- Like and comment counts
- Video duration
- Thumbnail URL

### Collection Process

The data pipeline follows this workflow:

```
YouTube Data API
       |
       v
Retrieve channel information
       |
       v
Retrieve uploaded video IDs
       |
       v
Fetch video metadata in batches
       |
       v
Create pandas DataFrame
       |
       v
Export to CSV
       |
       v
Import into SQLite
       |
       v
SQL queries and statistical analysis
       |
       v
Visualization with matplotlib
```

### Implementation Details

**Pagination**

YouTube playlist requests return a limited number of results per page.

The data collection script uses `nextPageToken` to iterate through the channel's upload playlist until all available video IDs have been retrieved.

**Batch Requests**

Rather than requesting metadata for each video separately, the implementation processes video IDs in batches of up to 50.

This reduces the number of API requests needed to retrieve metadata for thousands of videos.

**Environment Variables**

The YouTube API key is loaded from an environment variable using `python-dotenv` instead of being hardcoded in the source.

## Data Storage

The collected metadata is exported to CSV and then imported into a local SQLite database.

```
data/
  videos.csv
  videos.db
```

SQLite is used to organize records and execute queries for channel statistics, rankings, and exploratory analysis.

The database is generated locally and is not committed to GitHub.

---

# 2. Exploratory Data Analysis

The current analysis examines the relationship between video characteristics and channel performance.

## 2.1 Channel Overview

The analyzed dataset contains approximately 7,241 videos.


| Metric                  | Recorded result |
| ----------------------- | --------------- |
| Videos analyzed         | 7,241           |
| Total video views       | 13.66 billion   |
| Average views per video | 1.89 million    |


These figures describe a snapshot of the collected dataset. They are not live channel statistics and will change if the dataset is refreshed.

## 2.2 View Distribution Analysis

**Research question:** How much of the channel's total view count comes from its highest-performing videos?

Videos are sorted by view count, and cumulative views are calculated to examine the distribution of audience attention.

**Result:** Approximately 45.33% of the analyzed videos account for 80% of the dataset's total views.

This suggests that the channel's accumulated views are distributed across a substantial portion of its video catalog, rather than being concentrated in only a very small number of viral videos.

The result is specific to the analyzed dataset and does not establish a general pattern for YouTube channels.

## 2.3 Upload Frequency Analysis

**Research question:** How has the creator's upload frequency changed over time?

Publication dates are converted into datetime values and grouped by year to calculate annual upload counts.

The analysis shows that upload frequency increased substantially during the channel's development.

This provides a basis for investigating the relationship between publishing consistency and channel performance.

However, upload frequency alone cannot establish what caused changes in viewership.

## 2.4 Video Duration Analysis

**Research question:** Are certain video lengths associated with higher average views?

The YouTube Data API returns video durations in ISO 8601 format.

For example:

```
PT12M34S  → 12.57 minutes
PT1H2M15S → 62.25 minutes
```

The analysis script converts these durations into numerical minutes and groups videos into ranges.


| Duration group |
| -------------- |
| 0–5 minutes    |
| 5–10 minutes   |
| 10–15 minutes  |
| 15–20 minutes  |
| 20–30 minutes  |
| 30–60 minutes  |


Videos longer than 60 minutes are excluded from the grouped duration comparison, although they can still appear in the overall duration scatter plot.

**Preliminary finding:** Videos around 15–20 minutes show relatively high average views in the analyzed dataset.

This is an observed association, not evidence that making a video a particular length will cause more views.

## 2.5 Title Length Analysis

**Research question:** Is video title length associated with video performance?

Title lengths are calculated using Python and compared with view counts.

Titles are also grouped into character-length ranges to compare average views.

**Preliminary finding:** Titles around 20–30 characters have relatively high average views compared with several other groups in the current dataset.

This pattern may be influenced by topic, publication date, audience size at the time of upload, and other factors.

### Title Length vs. Views



*Figure 1. Scatter plot examining the relationship between video title length and view count.*

### Average Views by Title Length



*Figure 2. Comparison of average views across title-length groups.*

---

# 3. Technical Challenges and Solutions

## Challenge 1: Collecting Thousands of Video Records

**Problem**

The YouTube Data API limits the number of items returned by individual requests, making large-scale collection difficult using a single request.

**Approach**

I implemented pagination to retrieve video IDs across multiple pages, then organized the metadata requests into batches.

This allowed the collection process to handle thousands of videos without requiring a separate metadata request for every video.

## Challenge 2: Converting Video Durations into Usable Data

**Problem**

The API provides durations as ISO 8601 strings rather than directly usable numerical values.

**Approach**

I implemented a Python function using regular expressions to extract hours, minutes, and seconds and convert them into minutes.

This made it possible to perform numerical comparisons, group videos by duration, and generate visualizations.

## Challenge 3: Analyzing and Interpreting View Distribution

**Problem**

Simple averages do not explain how total views are distributed across a channel's entire video catalog.

**Approach**

I sorted videos by view count, calculated cumulative view totals, and identified the proportion of videos contributing to 80% of overall views.

This made it possible to investigate whether channel performance is concentrated in a small number of highly successful videos or distributed more broadly.

## Challenge 4: Separating Correlation from Causation

**Problem**

A relationship between video characteristics and views does not necessarily mean that those characteristics cause higher performance.

**Approach**

I treat findings from duration and title analysis as exploratory correlations rather than causal conclusions.

Future analysis will consider additional variables such as publication year, topic, engagement, and channel growth.

---

# 4. Project Structure

```
youtube_creator_analysis/
|
├── src/
│   ├── test_youtube_api.py
│   ├── create_database.py
│   ├── check_database.py
│   └── analyze_channel.py
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── Figure_1.png
├── Figure_2.png
├── Figure_3.png
├── Figure_4.png
├── Figure_5.png
│
└── ...additional analysis figures
```

The project generates its local `data/` directory during setup.

The `data/`, `.env`, and `.venv/` paths are ignored by Git to avoid committing local datasets, secrets, and virtual environments.

---

# 5. Running the Project Locally

## Requirements

- Python 3
- YouTube Data API v3 key
- Installed project dependencies

## Step 1 — Clone the Repository

```
git clone https://github.com/HubbaBubba64/youtube-creator-analysis.git
cd youtube-creator-analysis
```

## Step 2 — Create a Virtual Environment

```
python -m venv .venv
```

On Windows PowerShell:

```
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```
source .venv/bin/activate
```

## Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

## Step 4 — Configure Your API Key

Create a `.env` file in the project root:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
```

Do not commit your API key to GitHub.

## Step 5 — Create the Data Directory

```
mkdir data
```

## Step 6 — Collect YouTube Data

```
python src/test_youtube_api.py
```

This script retrieves channel metadata, collects uploaded video IDs, fetches video metadata, and saves the collected records to:

```
data/videos.csv
```

Running the collection requires access to the YouTube Data API and uses API quota.

## Step 7 — Create the SQLite Database

```
python src/create_database.py
```

This imports the CSV data into:

```
data/videos.db
```

To check the number of stored videos:

```
python src/check_database.py
```

## Step 8 — Run the Analysis

```
python src/analyze_channel.py
```

The script executes SQL queries and displays statistical results and matplotlib visualizations.

Run these commands from the project root directory because the scripts use relative paths to access local data.

---

# 6. Future Development Roadmap

The next stages will gradually extend the project from metadata analysis to AI-based language understanding and generation.

## Phase 1 — Expanded Performance Analysis

**Next milestone**

- Combine title length and video duration into a two-dimensional heatmap
- Compare engagement indicators such as likes and comments
- Examine trends by publication year
- Investigate additional variables that may influence view performance

## Phase 2 — Thumbnail Analysis

**Planned**

Apply computer vision methods to study recurring visual patterns.

Potential approaches include color histograms, image embeddings, and similarity comparisons.

The objective is to determine whether the channel uses identifiable thumbnail styles and how those characteristics relate to video performance.

## Phase 3 — Transcript and Language Analysis

**Planned**

Collect available transcripts and connect them to video records through video IDs.

Analyze:

- Common topics and keywords
- Vocabulary and sentence structure
- Emotional tone
- Repeated expressions
- Language complexity
- Sarcasm and exaggeration patterns

The results will be used to build a structured description of the creator's communication style.

## Phase 4 — Creator-Style AI System

**Planned**

Build an experimental RAG system using available transcripts and a language model.

### Proposed Architecture

```
YouTube Transcripts
        |
        v
Text Cleaning and Chunking
        |
        v
Embedding Model
        |
        v
Vector Database
        |
        v
Semantic Search
        |
        v
Retrieve Relevant Excerpts
        |
        v
Creator Style Profile + LLM
        |
        v
Generated Response or Script
```

The system will have two primary applications.

**Creator-Style Chatbot**

A chatbot that retrieves relevant source material and attempts to generate responses reflecting measurable characteristics of the creator's public communication style.

**AI Video Script Generator**

A tool that accepts a video topic and produces a structured draft using retrieved content and the creator-style profile.

Generated outputs will be identified as AI-generated, not authentic statements by the creator.

## Phase 5 — Evaluation

**Planned**

Evaluate the generated content using several criteria:

- Semantic relevance to the user request
- Faithfulness to retrieved sources
- Vocabulary and sentence-structure similarity
- Style consistency
- Coherence and readability
- Unsupported or fabricated claims

A central research question is:

**How accurately can AI reconstruct measurable elements of a creator's communication style, and which aspects remain difficult to reproduce?**

---

# 7. Limitations

This is an exploratory research and development project.

Current limitations include:

- Analysis of one selected YouTube channel
- Historical statistics that change as video counts and engagement metrics evolve
- Possible confounding factors such as publication date, topic, and audience growth
- No established causal relationship between title length, duration, and views
- No transcript-based or AI-generated functionality in the current implementation
- Locally stored datasets that are not included in the public repository

Future improvements will address data reproducibility, model evaluation, and analysis across additional channels.

---

# 8. Key Learning Outcomes

Through this project, I have practiced:

- Integrating an external REST API using Python
- Handling pagination and batch data collection
- Processing and organizing thousands of records
- Using SQLite and SQL for exploratory data analysis
- Transforming raw metadata into numerical features
- Visualizing statistical relationships using matplotlib
- Interpreting analytical results and recognizing limitations
- Designing a longer-term data and AI application architecture

The project has strengthened my interest in combining data engineering, machine learning, and practical AI development to build applications based on real-world data.

---

## Project Status

**Ongoing personal development project**

Current focus: Improving multivariable video-performance analysis before moving into transcript processing and language modeling.

**Repository:** [https://github.com/HubbaBubba64/youtube-creator-analysis](https://github.com/HubbaBubba64/youtube-creator-analysis)

**License:** No license file is currently included in this repository.

