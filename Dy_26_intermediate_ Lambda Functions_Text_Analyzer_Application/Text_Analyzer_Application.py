import re
import tkinter as tk
from collections import Counter
from functools import reduce


def analyze_text():
    user_text = text_entry.get("1.0", "end-1c")
    clean_text = re.sub(r'[^\w\s]', '', user_text).lower()
    words = clean_text.split()
    sentences = user_text.split('.')

    # Word count using 'reduce' and 'lambda'
    word_count = reduce(lambda x, _: x + 1, words, 0)

    # Character count
    character_count = len(clean_text)

    # Average word length using 'map' and 'lambda'
    average_word_length = sum(map(lambda w: len(w), words)) / word_count if word_count > 0 else 0

    # Word frequencies sorted by frequency
    word_frequencies = sorted(Counter(words).items(), key=lambda x: x[1], reverse=True)

    # Most common words
    most_common_words = word_frequencies[:5]

    # Unique words using a for loop and list comprehension, limit to 5 unique words
    unique_words = [word for word, frequency in word_frequencies if frequency == 1][:5]

    # Longest word
    longest_word = max(words, key=len)

    # Average sentence length
    average_sentence_length = len(words) / len(sentences)

    result_text.delete("1.0", "end")
    result_text.insert("1.0", f"Word Count: {word_count}\n")
    result_text.insert("end", f"Character Count: {character_count}\n")
    result_text.insert("end", f"Average Word Length: {average_word_length:.2f}\n")
    result_text.insert("end", f"Most Common Words: {', '.join([w[0] for w in most_common_words])}\n")
    result_text.insert("end", f"Unique Words: {', '.join(unique_words)}\n")
    result_text.insert("end", f"Longest Word: {longest_word}\n")
    result_text.insert("end", f"Average Sentence Length: {average_sentence_length:.2f}\n")


# Create the main application window
app = tk.Tk()
app.title("Text Analyzer")

# Text entry field
text_label = tk.Label(app, text="Enter Text:")
text_label.pack()
text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

# Analyze button
analyze_button = tk.Button(app, text="Analyze Text", command=analyze_text)
analyze_button.pack()

# Result display area
result_label = tk.Label(app, text="Analysis Results:")
result_label.pack()
result_text = tk.Text(app, height=10, width=40)
result_text.pack()

app.mainloop()
