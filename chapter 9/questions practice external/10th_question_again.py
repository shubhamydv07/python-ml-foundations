
with open("hello.txt") as f:
    content = f.read().lower()

words = content.split()

word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, count in word_frequency.items():
    print(f"'{word}' → {count} times")








