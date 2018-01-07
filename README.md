# python_is_numeric
A python module that adds the function is_numeric which is implemented in c,
and checks if a given string represents a number.

The difference between this method
and pythons str.isnumeric or str.isalnum is that this implementation also returns true
for strings representing floating point numbers.

strextnd.is_numeric returns 1 if str represents a number
and 0 if it does not.
strextnd.is_numeric also returns 0 for an empty string.

exmaple usage:

>>> from strextnd import is_numeric
>>> is_numeric('4')
1
>>> is_numeric('abc')
0
>>> is_numeric('545.45')
1

