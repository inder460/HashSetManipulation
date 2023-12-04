
# Imports
from Word import Word


def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in file_variable and inserts into
    a Hash_Set. Each Word object in hash_set contains the number
    of comparisons required to insert that Word object from
    file_variable into hash_set.
    Use: insert_words(file_variable, hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """

    line = fv.readline()

    while line:
        words_in_line = line.split()

        for x in words_in_line:
            new_word = Word(x)

            if hash_set.insert(new_word):
                hash_set.find(x).comparisons += 1

        line = fv.readline()


def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    Use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """

    total = 0
    max_word = None

    count = 0

    for slot in hash_set._table:

        for word in slot:
            total += word.comparisons

            if word.comparisons > count:
                count = word.comparisons
                max_word = word

    return total, max_word
