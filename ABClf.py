import pickle
import logging
import pandas as pd
from parse import compile
from transliterate import translit
from typing import Set, List, Dict
chars_to_remove = {
    '!',
    '"',
    '#',
    '%',
    '&',
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '[',
    ']',
    '_',
    '`',
    '«',
    '°',
    '²',
    '³',
    'µ',
    '·',
    '»',
    '½',
    '‑',
    '–',
    '‘',
    '’',
    '“',
    '”',
    '„',
    '•',
    '…',
    '‰',
    '″',
    '₂',
    '₃',
    '€',
    '™',
    '→',
    '−',
    '∕',
    '😀',
    '😉',
    '🙁',
    '🙂'

}


def is_alpha(token: str) -> bool:
    """Checks if the input string is strictly lowercase without numerals.

    Args:
        token (str): Input text.

    Returns:
        bool: Result of checking.
    """    
    import re
    pattern = "^[a-zšđčćž]+$"
    compiled_pattern = re.compile(pattern)
    return bool(compiled_pattern.match(token))

def preprocess(s: str) -> str:
    """Removes unusual characters and lowercases the string.

    Args:
        s (str): input string.

    Returns:
        str: output string.
    """
    for c in chars_to_remove:
        s = s.replace(c, "")
    s = s.casefold()
    return s


def count_variants(s: str, lex: dict):
    """Counts the variant specific words in the preprocessed input string based on the lexicon lex.

    Returns tuple (counts, per_token_breakdown).
    Counts look like this:
        {"A":3, "B":0}.
    per_token is a dictionary with all the words detected, their counts and their variant:
        {"word1":
            {"count":3, "variant":"A"}
        }

    Args:
        s (str): Input string.
        lex (dict): Lexicon.

    Returns:
        results (tuple): (counts, per_token).
    """
    counts = dict()
    per_token = dict()
    for word in preprocess(s).split():
        if not is_alpha(word):
            continue
        variant = lex.get(word, None)
        if not variant:
            continue
        logging.debug(f"Found word {word}, presumed variant: {variant}.")
        counts[variant] = counts.get(variant, 0) + 1
        if word in per_token.keys():
            per_token[word]["count"] += 1
        else:
            per_token[word] = {"variant": variant, "count": 1}
    return counts, per_token



def counts_to_category(counts: dict) -> str:
    """Discretizes counts like {"A": 2, "B":0} to
    categories A, B, MIX, UNK.

    Args:
        counts (dict): result of count_variants function.

    Returns:
        str: category.
    """    
    A = counts.get("A", 0)
    B = counts.get("B",0)

    if A > 2*B:
        return "A"
    elif B > 2*A:
        return "B"
    elif A == B == 0:
        return "UNK"
    else:
        return "MIX"


def load_lexicon(balanced=False)-> dict:
    """Loads 'lexicon.pickle'.
    Args:
        balanced (bool, optional): Whether or not to use balanced lexicon (equal number of A and B keys).
        Defaults to False. 
    Returns:
        dict: lexicon for variety identification.

    """ 
    with open(f"lexicon{'_balanced' if balanced else ''}.pickle", "rb") as f:
        lex = pickle.load(f)
    return lex

def get_variant(text: str, lex=None) -> str:
    """Quick way to classify text. 

    Loads the lexicon, preprocesses the string. Returns the predicted 
    category {'A', 'B', 'UNK', 'MIX'}.

    Args:
        text (str): input string.

    Returns:
        str: category {'A', 'B', 'UNK', 'MIX'}
    """    
    if not lex:
        lex = load_lexicon()
    variant_detector_count = count_variants(text, lex)[0]
    return counts_to_category(variant_detector_count) 

