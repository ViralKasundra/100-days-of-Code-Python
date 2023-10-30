import os
import string

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""

def process_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    text = text.translate(translator)
    # Tokenize the text
    words = text.split()
    return words

def analyze_directory(directory, num_common_words):
    word_frequency = {}

    # List comprehension to read and process text files in the directory
    texts = [process_text(text) for text in (read_text_file(os.path.join(directory, file)) for file in os.listdir(directory) if file.endswith(".txt"))]

    # List comprehension to count word frequencies
    for words in texts:
        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1

    # Sort the word frequency dictionary by frequency in descending order
    sorted_word_frequency = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}

    # List comprehension to get the top N common words
    top_words = [(word, freq) for word, freq in list(sorted_word_frequency.items())[:num_common_words]]

    return top_words

def main():
    # Get the directory of the currently running script
    script_directory = os.path.dirname(os.path.abspath(__file__)) if __file__ is not None else os.path.realpath(__file__)

    num_common_words = 10  # Change this value to the desired number of common words

    top_words = analyze_directory(script_directory, num_common_words)

    print(f"Top {num_common_words} Common Words:")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
