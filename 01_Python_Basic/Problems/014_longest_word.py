# Question 6: Find the longest word

words = ["tree", "computer", "cat", "elephant", "book"]


# ------------------------------------------------------------
# Method 1: for loop
# ------------------------------------------------------------

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)


# ------------------------------------------------------------
# Method 2: max() with key=len
# ------------------------------------------------------------

longest_word = max(words, key=len)
print("Longest word:", longest_word)


# ------------------------------------------------------------
# Method 3: sort()
# NOTE: sort() changes the original list
# ------------------------------------------------------------

words_copy = words.copy()
words_copy.sort(key=len, reverse=True)

print("Longest word:", words_copy[0])


# ------------------------------------------------------------
# Method 4: sorted()
# NOTE: sorted() creates a new list
# ------------------------------------------------------------

longest_word = sorted(words, key=len, reverse=True)[0]
print("Longest word:", longest_word)


# ------------------------------------------------------------
# Method 5: while loop
# ------------------------------------------------------------

longest_word = words[0]
i = 1

while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    i += 1

print("Longest word:", longest_word)


# ------------------------------------------------------------
# Method 6: reduce()
# ------------------------------------------------------------

from functools import reduce

longest_word = reduce(
    lambda x, y: x if len(x) >= len(y) else y,
    words
)

print("Longest word:", longest_word)
