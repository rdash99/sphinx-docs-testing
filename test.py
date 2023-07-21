def test(kind=None):
    """This is a test function.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :return: The ingredients list.
    :rtype: list[str]
    
    >>> test()
    ['spam', 'eggs', 'bacon']
    """
    print('test.py')
    return ['spam', 'eggs', 'bacon']