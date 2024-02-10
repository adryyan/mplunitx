"""Parsing of numbers.

"""


class _number():
    """
    This class is used to parse number.

    """

    def __init__(self, number):
        if isinstance(number, str):
            self.tex_str = number
        else:
            try:
                if int(number) == number:
                    self.tex_str = str(int(number))
                else:
                    self.tex_str = str(number)
            except ValueError:
                raise ValueError("number must be a string or a number.")
