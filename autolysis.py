# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "chardet",
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "openai",
#   "requests",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import chardet

# Step 1: Load the AIPROXY_TOKEN
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN") or "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjIwMDEwNjJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.VCDzV4cBgQuKEk3BWWEFotvGy2BOrlA3eTtCYMChPWI"
if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN is not set.")
    sys.exit(1)

# Step 2: Configure OpenAI Proxy
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}",
}

# Step 3: Detect Encoding and Load CSV File
def detect_encoding(file_path):
    """Detect the encoding of a CSV file."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def load_csv_with_detected_encoding(file_path):
    """Load a CSV file with the detected encoding."""
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except UnicodeDecodeError:
        print(f"Failed to decode {file_path} with encoding {encoding}. Trying 'utf-8-sig'.")
        df = pd.read_csv(file_path, encoding='utf-8-sig')  # Fallback to 'utf-8-sig'
        return df

if len(sys.argv) < 2:
    print("Usage: python autolysis.py <dataset.csv>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    data = load_csv_with_detected_encoding(file_path)
    print(f"DataFrame loaded successfully. First few rows:\n{data.head()}")
except Exception as e:
    print(f"Error loading file {file_path}: {e}")
    sys.exit(1)

# Step 4: Basic Data Analysis
summary = {
    "columns": list(data.columns),
    "dtypes": data.dtypes.astype(str).to_dict(),
    "summary_stats": data.describe(include='all').to_dict(),
    "missing_values": data.isnull().sum().to_dict(),
}

# Step 5: Interact with LLM for Insights
def ask_llm(prompt):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

llm_prompt = f"Analyze the following dataset summary and suggest key insights and visualizations: {summary}"
try:
    analysis_insights = ask_llm(llm_prompt)
except Exception as e:
    analysis_insights = f"Error fetching insights: {e}"

# Step 6: Generate Visualizations
def visualize_data(data):
    """Generate and save visualizations."""
    sns.set(style="whitegrid")
    visualization_files = []

    # Histograms for numerical columns
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    for column in numerical_columns:
        plt.figure()
        sns.histplot(data[column].dropna(), kde=True, bins=30, color="blue")
        plt.title(f'Distribution of {column}')
        filename = f'{column}_distribution.png'
        plt.savefig(filename)
        plt.close()
        visualization_files.append(filename)

    # Correlation heatmap for numerical columns
    if len(numerical_columns) > 1:
        plt.figure(figsize=(10, 8))
        correlation_matrix = data[numerical_columns].corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Heatmap")
        filename = "correlation_heatmap.png"
        plt.savefig(filename)
        plt.close()
        visualization_files.append(filename)

    # Bar chart for missing values
    if data.isnull().sum().sum() > 0:
        plt.figure(figsize=(10, 6))
        data.isnull().sum().plot(kind='bar', color='skyblue')
        plt.title("Missing Values per Column")
        plt.xlabel("Columns")
        plt.ylabel("Number of Missing Values")
        filename = "missing_values.png"
        plt.savefig(filename)
        plt.close()
        visualization_files.append(filename)

    return visualization_files

visualization_files = visualize_data(data)

# Step 7: Generate Markdown Report
def dict_to_markdown_table(data_dict, title, headers=None):
    """Convert a dictionary to markdown table format."""
    table = f"## {title}\n\n"
    if headers:
        table += " | ".join(headers) + "\n"
        table += "|---" * len(headers) + "|\n"
    for key, value in data_dict.items():
        table += f"{key} | {value}\n"
    table += "\n"
    return table

# Convert sections to Markdown
data_types_md = dict_to_markdown_table(
    summary['dtypes'], "Data Types",
    headers=["Column", "Data Type"]
)

summary_stats_md = dict_to_markdown_table(
    summary['summary_stats'], "Summary Statistics",
    headers=["Column", "Summary"]
)

missing_values_md = dict_to_markdown_table(
    summary['missing_values'], "Missing Values",
    headers=["Column", "Missing Count"]
)

visualizations_md = "## Visualizations\n\n"
for file in visualization_files:
    visualizations_md += f"![{file}]({file})\n\n"

# Combine all sections into the README content
readme_content = f"""# Automated Analysis Results

## Dataset Overview
Columns: {', '.join(summary['columns'])}

{data_types_md}
{summary_stats_md}
{missing_values_md}

## Insights
{analysis_insights}

{visualizations_md}
"""

# Save Markdown File
with open("README.md", "w") as f:
    f.write(readme_content)

print("Analysis complete. Outputs saved as README.md and *.png files.")
