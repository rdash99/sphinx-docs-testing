# Usage

## Installation

To use Test, first install it using pip:

```console
(.venv) $ pip install test
```

## Creating recipes

To retrieve a list of random ingredients,
you can use the `test.test()` function:

### test.test(kind=None)

This is a test function.

* **Parameters:**
  **kind** (*list**[**str**] or* *None*) – Optional “kind” of ingredients.
* **Returns:**
  The ingredients list.
* **Return type:**
  list[str]

```pycon
>>> test()
['spam', 'eggs', 'bacon']
```

```python
>>> import test
>>> test.test()
['milk', 'eggs', 'flour', 'sugar', 'butter', 'salt', 'pepper', 'water', 'oil', 'vinegar']
```

You can also specify a kind of ingredient to retrieve:

```python
>>> test.test(kind='fruit')
['apple', 'banana', 'orange', 'grape', 'strawberry', 'blueberry', 'raspberry', 'blackberry', 'lemon', 'lime']
```
