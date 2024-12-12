# Automated Analysis (Autolysis)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Overview
The Autolysis project is an analytical tool designed to extract insights from datasets through visualization and basic statistical methods. By leveraging popular Python libraries, this project processes data to reveal trends, correlations, and actionable insights. It serves as a practical exercise in data manipulation, visualization, and storytelling with data.

---

## Features
- **Data Cleaning and Preprocessing:** Handles various data formats and detects encoding issues using the `chardet` library.
- **Visualization:** Creates meaningful visualizations using Matplotlib and Seaborn to present trends and relationships in the data.
- **Automation:** Automates the analysis process for specific datasets, offering a repeatable framework for exploratory data analysis (EDA).
- **Adaptable Framework:** The script is designed to work with multiple datasets, including Goodreads, Happiness, and Media data.

---

## What I Did
1. **Data Handling:**
   - Imported and processed datasets using pandas.
   - Detected and resolved encoding issues with the help of the `chardet` library.
2. **Data Visualization:**
   - Used Matplotlib and Seaborn to create histograms, scatter plots, and correlation heatmaps.
   - Saved visualizations as PNG files for documentation and presentation purposes.
3. **Exploratory Analysis:**
   - Conducted statistical analysis to identify key patterns and outliers.
   - Designed a repeatable structure for analyzing datasets.
4. **Code Optimization:**
   - Structured the code into clear, logical steps for reusability and readability.

---

## How to Run the Project

### Prerequisites
- Python 3.8 or higher
- Virtual Environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Karanshrivastav/tds_project_2.git
   cd tds_project_2
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # For Windows
   source .venv/bin/activate   # For Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the main script with a dataset of your choice:
   ```bash
   uv autolysis.py <dataset_path>
   ```
   Replace `<dataset_path>` with the path to your dataset, e.g., `data/happiness.csv`.
2. Visualizations and results will be saved in the `output/` directory.

---

## Learnings
- **Python Libraries:** Gained proficiency in pandas, Matplotlib, and Seaborn for data manipulation and visualization.
- **Data Wrangling:** Developed techniques for handling messy datasets, including detecting and resolving encoding issues.
- **Visualization Best Practices:** Learned how to effectively communicate insights through visuals.
- **Automation:** Understood how to build a repeatable and scalable analysis framework.

---

## Findings
- **Goodreads Dataset:** Revealed trends in book ratings and the relationship between reviews and average scores.
- **Happiness Dataset:** Identified key factors contributing to happiness scores across countries.
- **Media Dataset:** Analyzed consumption trends and their correlation with demographic data.

---

## Acknowledgments
- **Inspiration:** This project is part of the Tools in Data Science course.
- **Libraries Used:** pandas, Matplotlib, Seaborn, chardet, and Python's standard library.

---

## Future Work
- **Dynamic Prompting:** Introduce user inputs to dynamically adjust analysis parameters.
- **Advanced Visualizations:** Experiment with interactive dashboards using Plotly or Bokeh.
- **Enhanced Analysis:** Incorporate predictive modeling and clustering techniques.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Problem statement
https://github.com/sanand0/tools-in-data-science-public/blob/tds-2024-t3/project-2-automated-analysis.md
