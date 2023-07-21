Usage
=====

Installation
------------

To use Test, first install it using pip:

.. code-block:: console

   (.venv) $ pip install test2

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``test2.test()`` function:

.. autofunction:: test2.test(kind=None)

.. code-block:: python

   >>> import test2
   >>> test2.test()
   ['milk', 'eggs', 'flour', 'sugar', 'butter', 'salt', 'pepper', 'water', 'oil', 'vinegar']

You can also specify a kind of ingredient to retrieve:

.. code-block:: python

   >>> test2.test(kind='fruit')
   ['apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'lemon', 'lime']
   