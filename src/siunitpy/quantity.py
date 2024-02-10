
def qty(number, unit, uncertainty=None):
    if not isinstance(number, str):
        raise TypeError("number must be a string.")
    if uncertainty is None:
        return r"$" + number + r"\," + unit + r"$"
    else:
        if not isinstance(uncertainty, str):
            raise TypeError("uncertainty must be a string.")
        return r"$(" + number + r" \pm " + uncertainty + r")\," \
                + unit + r"$"