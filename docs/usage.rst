Usage
=====

Installation
------------

To use Test, first install it using pip:

.. code-block:: console

   (.venv) $ pip install test

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``test.test()`` function:

.. autofunction:: test.test(kind=None)

.. code-block:: python

   >>> import test
   >>> test.test()
   ['milk', 'eggs', 'flour', 'sugar', 'butter', 'salt', 'pepper', 'water', 'oil', 'vinegar']

You can also specify a kind of ingredient to retrieve:

.. code-block:: python

   >>> test.test(kind='fruit')
   ['apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'lemon', 'lime']
   