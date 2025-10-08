# app/main.py

def count_words(words_list):
    """Retourne le nombre de mots dans la liste."""
    return len(words_list)


def longest_word(words_list):
    """Retourne le mot le plus long. Si plusieurs ont la même longueur, retourne le premier."""
    if not words_list:
        return ""
    return max(words_list, key=len)


def contains_word(words_list, word):
    """Vérifie si un mot est présent dans la liste."""
    return word in words_list
