# Netflix_data_analysis

## Exploratory Data Analysis (EDA) project using Python to analyze a Netflix content dataset and identify patterns across content type, ratings, genres, countries, release years, and duration.

## Project Overview

This project performs an end-to-end exploratory analysis of Netflix content using Pandas, NumPy, Matplotlib, and Seaborn.

The goal is to transform raw Netflix data into meaningful insights through data cleaning, exploration, statistical analysis, and visualization.

## Objectives
Understand the structure and characteristics of the dataset
Clean and prepare the data for analysis
Analyze Movies vs. TV Shows
Explore content ratings
Analyze release-year distribution
Examine genres and countries
Analyze movie duration and TV-show seasons
Identify patterns through visualizations
Practice a complete Python-based EDA workflow
Dataset

The dataset contains Netflix content records with the following attributes:

## Column	Description
show_id	Unique identifier for each title
type	Movie or TV Show
title	Title of the content
director	Director of the content
cast	Cast members
country	Country associated with the content
release_year	Original release year
rating	Content rating
duration	Movie runtime or number of seasons
listed_in	Genres/categories
description	Description of the title
Technologies Used
Python
NumPy
Pandas
Matplotlib
Seaborn
Jupyter Notebook
Project Workflow
Raw Dataset
     ↓
Data Loading
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Data Type Conversion
     ↓
Exploratory Data Analysis
     ↓
Statistical Analysis
     ↓
Data Visualization
     ↓
Insights & Conclusions
## Analysis Performed
1. Data Inspection
Dataset dimensions
Column names
Data types
Missing values
Duplicate records
Basic statistical information
2. Content Type Analysis

Comparison of:

Movies
TV Shows
3. Content Rating Analysis

Analysis of ratings such as:

TV-MA
R
PG-13
TV-14
Not Rated
4. Release Year Analysis

Distribution of titles across different release years to understand the composition of the dataset over time.

5. Genre Analysis

Analysis of Netflix categories using the listed_in column.

6. Country Analysis

Exploration of the countries represented in the dataset.

7. Duration Analysis

Movies and TV Shows are interpreted differently:

Movies → runtime in minutes
TV Shows → number of seasons
Key Findings

## Within this dataset:

Both Movies and TV Shows are represented.
TV-MA and R are the most frequently occurring content ratings.
The dataset contains content across multiple genres and countries.
Movie duration and TV-show duration require different interpretations.
The analysis demonstrates how categorical and numerical variables can be explored using Python visualization tools.

Note: This project uses a dataset containing 30 records. Therefore, the findings describe this dataset specifically and should not be interpreted as representative of Netflix's entire content library.

## Project Structure
Netflix_data_analysis/
│
├── Netflix_prj_1.ipynb
├── generate_netflix_dataset.py
├── netflix_movies_dataset.csv
├── .gitignore
└── README.md
## How to Run
1. Clone the repository
git clone https://github.com/Khushi005-mi/Netflix_data_analysis.git
2. Navigate to the project
cd Netflix_data_analysis
3. Install dependencies
pip install numpy pandas matplotlib seaborn jupyter
4. Launch Jupyter Notebook
jupyter notebook

Open:

Netflix_prj_1.ipynb

and run the notebook cells sequentially.

Learning Outcomes

This project demonstrates practical experience with:

## Data loading and preprocessing
Pandas DataFrame operations
Handling categorical data
Missing-value analysis
Data type conversion
Descriptive statistics
Grouping and aggregation
Data visualization
Exploratory Data Analysis
Interpreting analytical results
Future Improvements

## Potential extensions include:

Increasing the dataset size
More advanced statistical analysis
Interactive dashboards
Country-level analysis
Genre-level trend analysis
Time-series analysis
Recommendation-system development
Predictive modeling
# Author

# Khushi Mishra

# Data Science | AI | FinTech | Data Analytics
