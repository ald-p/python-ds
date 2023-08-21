def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase_list = phrase.lower().split(' ')
    capitalized_list = []

    for word in phrase_list:
        capitalized_list.append(word.capitalize())

    return ' '.join(capitalized_list)