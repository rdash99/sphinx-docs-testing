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

.. py:function:: test.test(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :return: The ingredients list.
   :rtype: list[str]