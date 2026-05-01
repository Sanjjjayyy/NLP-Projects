import argparse
import sys
import os
import re
from tqdm import tqdm
from nltk.corpus import stopwords
import nltk

# Pre-load resources outside the loop for speed
nltk.download('stopwords', quiet=True)
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text):
    # 1. Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # 2. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # 3. Tokenize & Lowercase
    tokens = re.findall(r'\b\w+\b', text.lower())
    # 4. Remove stopwords
    cleaned_tokens = [word for word in tokens if word not in STOP_WORDS]
    return " ".join(cleaned_tokens)

def main():
    parser = argparse.ArgumentParser(description=" A Simple Text Cleaner CLI")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("-o", "--output", help="Path to output file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
        sys.exit(1)

    file_size = os.path.getsize(args.input)
    
    # Open output stream
    out_file = open(args.output, 'w', encoding='utf-8') if args.output else sys.stdout

    with open(args.input, 'r', encoding='utf-8') as in_file:
        with tqdm(total=file_size, unit='B', unit_scale=True, desc="Cleaning") as pbar:
            for line in in_file:
                cleaned = clean_text(line)
                if cleaned:
                    out_file.write(cleaned + "\n")
                
                # Update progress bar by the number of bytes in the current line
                pbar.update(len(line.encode('utf-8')))

    if args.output:
        out_file.close()
        print(f"\nDone! Processed {args.input}")

if __name__ == "__main__":
    main()