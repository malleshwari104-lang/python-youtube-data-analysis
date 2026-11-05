# YouTube Data Analysis Using Python

## Project Overview

This project focuses on analyzing YouTube trending video data and comments using Python. The objective is to explore video performance, understand audience engagement, analyze comment sentiment, and identify useful insights through data analysis and visualization.

## Project Objectives

- Analyze YouTube comments and trending video data.
- Clean and prepare datasets for analysis.
- Explore audience engagement through likes, views, and comments.
- Apply VADER sentiment scoring to comments.
- Identify the most frequently used emojis in comments.
- Compare video views across different categories.
- Create visualizations to communicate findings.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- NLTK (VADER Sentiment Analysis)
- Emoji
- Squarify
- JSON

## Dataset

The project uses:

- `US_comments.csv` – YouTube comments data.
- Regional trending video CSV files – trending video information.
- `US_category_id.json` – category ID and category name mapping.

## Data Cleaning & Preparation

- Inspected dataset structure, columns, and data types.
- Checked missing values and duplicate records.
- Removed missing comment records.
- Combined multiple regional datasets using Pandas.
- Converted trending dates into datetime format.
- Mapped category IDs to category names using JSON.

## Analysis Performed

### 1. YouTube Comments Analysis

- Explored comments and video IDs.
- Created a VADER sentiment analysis function to classify comments as positive, negative, or neutral.
- Extracted emojis from comments.
- Identified the most frequently used emojis.

### 2. Video Performance Analysis

- Analyzed total views by category.
- Identified the top five categories by views.
- Analyzed category-wise views over time.
- Compared video views and engagement rates.

### 3. Engagement Analysis

Calculated engagement rate using:

**Engagement Rate (%) = ((Likes + Comments) / Views) × 100**

- Calculated average engagement rate by category.
- Compared engagement across categories.
- Generated descriptive statistics for engagement rates.

## Visualizations

The project includes:

- Top 10 Most Used Emojis – Bar Chart
- Total Views by Category Over Time – Area Chart
- Top 5 Categories by Total Views – Bar Chart
- Views vs Engagement Rate – Scatter Plot
- Average Engagement Rate by Category – Bar Chart
- Category-wise Total Views – Treemap
- Distribution of Views – Box Plot

## Project Structure

```text
python_youtube_data_analysis/
│
├── visuals/
│   ├── avg engagement rate.png
│   ├── category_treemap.png
│   ├── distribution_of_views.png
│   ├── engagement_rate.png
│   ├── most used emojis.png
│   └── total views by category.png
│
├── US_comments.csv
├── youtube_analysis.py
└── README.md
```

*Note: Regional trending CSV files and the category JSON file are used as input datasets from your additional data folder.*

## Key Learning Outcomes

- Data cleaning and preprocessing using Pandas.
- Working with multiple CSV files and JSON data.
- Applying sentiment analysis using NLTK VADER.
- Extracting and analyzing emojis from text data.
- Performing groupby operations and statistical analysis.
- Creating charts and visualizations using Matplotlib.
- Generating insights from real-world datasets.

## Conclusion

This project helped develop practical Python data analysis skills by exploring YouTube comments, trending videos, category performance, and audience engagement. The visualizations make it easier to understand video trends and compare category performance.