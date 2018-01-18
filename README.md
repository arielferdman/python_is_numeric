# python_is_numeric
A python module that adds the function is_numeric which is implemented in c,
and checks if a given string represents a number.

The difference between this method
and pythons str.isnumeric or str.isalnum is that this implementation also returns True
for strings representing floating point numbers and negative numbers (but false for negative zero both in decimal and floating point format).

strextnd.is_numeric returns True if str represents a number
and False if it does not.
strextnd.is_numeric also returns False for an empty string.

example usage:

from strextnd import is_numeric

is_numeric('4')

True

is_numeric('abc')

False

is_numeric('545.45')

True

is_numeric('-3')

True

is_numeric('-0')

False

is_numeric('-0.000')

False


