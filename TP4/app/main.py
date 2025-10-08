def count_words(words):
    return len(words)


def longest_word(words):
    return max(words, key=len) if words else ""


def contains_word(words, target):
    return target in words
