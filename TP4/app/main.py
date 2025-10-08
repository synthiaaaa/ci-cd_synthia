def count_words(words):
    """Retourne le nombre de mots dans la liste."""
    return len(words)


def longest_word(words):
    """Retourne le mot le plus long de la liste ou une chaîne vide si la liste est vide."""
    if not words:
        return ""
    return max(words, key=len)


def contains_word(words, word):
    """Vérifie si 'word' est présent dans la liste 'words'."""
    return word in words
