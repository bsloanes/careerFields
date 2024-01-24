import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams
from collections import Counter

# Download NLTK resources (if not already downloaded)
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def process_text(text):
    # Tokenize the text
    words = word_tokenize(text.lower())

    # Remove stopwords and non-alphabetic words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    return words

def main():
    # Replace 'your_file.xlsx' with the actual path to your Excel file
    excel_file = 'CFETPs.xlsx'

    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Combine text from all rows into a single string
    all_text = ' '.join(df['summary'].astype(str))

    # Process the text
    processed_words = process_text(all_text)

    # Count word frequencies
    word_freq = Counter(processed_words)

    # Print word frequencies
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

    # Create bigrams
    bigram_freq = Counter(bigrams(processed_words))

    # Print bigram frequencies
    print("\nBigram frequencies:")
    for bigram, freq in bigram_freq.items():
        print(f'{bigram}: {freq}')

if __name__ == "__main__":
    main()
