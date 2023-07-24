# Usage

## Installation

To use Test, first install it using pip:

```console
(.venv) $ pip install test2
```

## Creating recipes

To retrieve a list of random ingredients,
you can use the `test2.test()` function:

### test2.test(kind=None)

This is a copy of the test function.

* **Parameters:**
  **kind** (*list**[**str**] or* *None*) – Optional “kind” of ingredients.
* **Returns:**
  The ingredients list.
* **Return type:**
  list[str]

```python
>>> import test2
>>> test2.test()
['milk', 'eggs', 'flour', 'sugar', 'butter', 'salt', 'pepper', 'water', 'oil', 'vinegar']
```

You can also specify a kind of ingredient to retrieve:

```python
>>> test2.test(kind='fruit')
['apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'lemon', 'lime']
```
