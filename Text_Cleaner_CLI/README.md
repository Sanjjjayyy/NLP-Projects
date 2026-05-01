# Modular Text Cleaner CLI

A SImple Python-based command-line tool designed for Natural Language Processing (NLP) preprocessing. This tool sanitizes raw text by removing "noise" like HTML, URLs, stopwords, and punctuation.

# Key Features

**Deep Cleaning:**  Removes HTML tags and URLs using optimized Regular Expressions.  
**Stopword Removal:**  Integrates with NLTK for English stopword removal.  
**Memory Efficient:**  Processes files line-by-line streaming for handling largefiles  
**User Feedback:**  Features a real-time progress bar powered by tqdm.  
**Professional CLI:**  Built with argparse for a standard terminal experience.   


# Installation
## 1. Clone the repository
```bash
git clone https://github.com/Sanjjjayyy/NLP-Projects.git
cd NLP-Projects/Text_Cleaner_CLI
```
## 2. Set up a Virtual Environment
```bash 
python3 -m venv .venv
source .venv/bin/activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
# Usage
## Cleaning
Print the cleaned version of a file directly to your terminal.
```bash
python3 cleaner.py input.txt
```

## Export to File
Save the results to a specific output file.
```bash
python3 cleaner.py input.txt -o cleaned_data.txt
```
# Example Input/Output

## Input:
```bash
"Hello World! Welcome to the NLP cleaning test. 
Check out the project repository at https://github.com/sanjay/text-cleaner for more details. 
<div>
  <p>This is a paragraph wrapped in HTML tags. It should be stripped! 12345</p>
</div>
Wait... does it handle punctuation like "don't", "NLP-focused", and "high-end"? 
Visit www.fintech-news.com/2026 to see the latest stock trends. 
The quick brown fox jumps over the lazy dog. 
Is the progress bar working? Let's find out!."
```

## Output:
```bash
hello world welcome nlp cleaning test
check project repository details
paragraph wrapped html tags stripped 12345
wait handle punctuation like nlp focused high end
visit see latest stock trends
quick brown fox jumps lazy dog
progress bar working let find
```

# Requirements

Python 3.10+  
NLTK  
tqdm  