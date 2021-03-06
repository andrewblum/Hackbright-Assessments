"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    unique_words = {}
    words_from_phrase = phrase.split()
    for word in words_from_phrase:
        unique_words[word] = unique_words.get(word, 0) + 1
    return unique_words


def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
    melon_prices = {
    "Honeydew" : 2.50,
    "Cantaloupe" : 2.50,
    "Watermelon" : 2.95,
    "Musk" : 3.25,
    "Crenshaw" : 3.25,
    "Christmas" : 14.25
    }
    same_price_melons = []
    for melon in melon_prices:
        if melon_prices[melon] == price:
            same_price_melons.append(melon)
    if same_price_melons:
        for melon in sorted(same_price_melons):
            print(melon)
    else:
        print("None found")
    return

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_to_pirate_translation = {
        "sir" : "matey",
        "hotel" : "fleabag inn",
        "student" : "swabbie",
        "man" : "matey",
        "professor" : "foul blaggart",
        "restaurant" : "galley",
        "your" : "yer",
        "excuse" : "arr",
        "students" : "swabbies",
        "are" : "be",
        "restroom" : "head",
        "my" : "me",
        "is" : "be",
    }
    english_words = phrase.split()
    pirate_phrase = []
    for word in english_words:
        pirate_phrase.append(english_to_pirate_translation.get(word,word))
    return " ".join(pirate_phrase)


def kids_game(names):
    """2 hrs 20 mins on this single one. The first time aorund I misread what
    it was asking for. Now I'm rewriting it but I'm still taking a while"""
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    """def generate_names_dictionary(names):
        creates names into dictionary using the first letter
        of each word as the key, value will be list of words that start with
        first letter (the key).
        names_look_up_dictionary = {}
        for word in names:
            names_look_up_dictionary[word[0]] = names_look_up_dictionary.get(word[0],[])
            names_look_up_dictionary[word[0]].append(word)
        return names_look_up_dictionary

    def find_first_matching_word(last_letter,names):
        finds first word whose first letter matches the last letter of the
        previous word
        for word in names:
            if last_letter == word[0]:
                return word

    def update_name_list(current_word, names):
        updates name_list so we will not pick that name again
        names.remove(current_word)
        return names
    names = update_name_list(word, names)

    # try to loop using boolean of the various list. Once key in names_list is
    #empty then return false. 
    names_list = generate_names_dictionary(names)
    word_chain = []
    word_chain.append(names_list[0])

    matching_word = find_first_matching_word(word[-1],names)
    names = update_name_list(matching_word, names)
    word_chain.append(matching_word)

        word_chain.update([word])
        names_list[word[-1]].remove(word)
        names.remove(word)
    print(word_chain)


    return []"""

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print("{" + ", ".join(
            "'{}': {}".format(k, d[k]) for k in sorted(d)) + "}")
    else:
        print(d)


if __name__ == "__main__":
    print()
    import doctest
    if doctest.testmod().failed == 0:
        print("*** ALL TESTS PASSED ***")
    print()
