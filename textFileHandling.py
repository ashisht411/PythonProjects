#to count the top 3 words from a text file
from collections import Counter
def top_three_words(filepath):
  with open(filepath,"r") as file:
    text = file.read().lower()
    words = text.split()
    word_count = Counter(words)
    top_three = word_count.most_common(3)
    return top_three

if __name__ == "__main__":
  filepath = "sad.txt"  # Replace with your text file path
  print("Top 3 words:", top_three_words(filepath))