"""sisetup

"""
from siunitpy.unit import _unit


class sisetup():
    """
    
    """

    def __init__(self, inter_unit_product=r"\,", per_mode="power",
                 per_symbol="/", bracket_unit_denominator=True):
        """
        
        """
        self.per_mode = per_mode
        self.per_symbol = per_symbol
        self.inter_unit_product = inter_unit_product
        self.bracket_unit_denominator = bracket_unit_denominator


    @property
    def per_mode(self):
        return self._per_mode

    @per_mode.setter
    def per_mode(self, per_mode):
        if per_mode is None or per_mode == "power":
            self._per_mode = "power"
        elif per_mode == "fraction":
            self._per_mode = "fraction"
        elif per_mode == "symbol":
            self._per_mode = "symbol"
        elif per_mode == "single-symbol":
            self._per_mode = "single-symbol"
        elif per_mode == "power-positive-first":
            self._per_mode = "power-positive-first"
        else:
            raise ValueError("per_mode must be either 'power', 'fraction' "
                             "or 'symbol'.")


    @property
    def per_symbol(self):
        return self._per_symbol

    @per_symbol.setter
    def per_symbol(self, per_symbol):
        if isinstance(per_symbol, str):
            self._per_symbol = per_symbol
        else:
            raise TypeError("per_symbol must be a string.")


    @property
    def bracket_unit_denominator(self):
        return self._bracket_unit_denominator

    @bracket_unit_denominator.setter
    def bracket_unit_denominator(self, bracket_unit_denominator):
        if isinstance(bracket_unit_denominator, bool):
            self._bracket_unit_denominator = bracket_unit_denominator
        else:
            raise TypeError("bracket_unit_denominator must be a boolean.")


    @property
    def inter_unit_product(self):
        return self._inter_unit_product

    @inter_unit_product.setter
    def inter_unit_product(self, inter_unit_product):
        if isinstance(inter_unit_product, str):
            self._inter_unit_product = inter_unit_product
        else:
            raise TypeError("inter_unit_product must be a string.")


    def unit(self, unit):
        """Returns the LaTeX representation of the given unit.

        """
        if not isinstance(unit, str):
            raise TypeError("unit must be a string.")

        unit = unit.split(";")

        #for i in range(len(unit)):
        #    unit[i] = _unit(unit[i])

        tex_str = ""
        if self.per_mode != "power":
            # If per_mode is fraction add \frac{ 
            if self.per_mode == "fraction":
                tex_str = r"\frac{"

            # Add all units to str with positive power
            count_pos = 0
            for i, u in enumerate(unit):
                u = _unit(u)
                if u.power > 0:
                    tex_str += u.tex_str
                    if u.power != 1:
                        tex_str += "^{" + str(u.power) + "}"
                    tex_str += self.inter_unit_product
                    count_pos += 1

            # Add str between pos and neg power
            if self.per_mode == "fraction":
                tex_str = tex_str[:-len(self.inter_unit_product)]
                tex_str += "}{"
            elif self.per_mode in ["symbol", "single-symbol"]:
                tex_str = tex_str[:-len(self.inter_unit_product)]
                tex_str += self.per_symbol
                if self.bracket_unit_denominator:
                    tex_str += "("

            # Add all units to str with negative power
            count_neg = 0
            for i, u in enumerate(unit):
                u = _unit(u)
                if u.power < 0:
                    tex_str += u.tex_str
                    if (self.per_mode in 
                        ["symbol", "single-symbol", "fraction"]):
                        if u.power != -1:   
                            tex_str += "^{" + str(-u.power) + "}"
                    else:      
                        tex_str += "^{" + str(u.power) + "}"
                    tex_str += self.inter_unit_product
                    count_neg += 1

            tex_str = tex_str[:-len(self.inter_unit_product)]
            if self.per_mode == "fraction":
                tex_str += "}"
            if (self.per_mode in ["symbol", "single-symbol"] 
                and self.bracket_unit_denominator):
                if count_neg > 1:
                    tex_str += ")"
                else:
                    tex_str = tex_str.replace("(", "")

        # If per_mode is power or single-symbol and count_neg > 1
        if self.per_mode == "power" or (self.per_mode == "single-symbol"
                                        and count_neg > 1):
            tex_str = ""
            for i, u in enumerate(unit):
                u = _unit(u)
                tex_str += u.tex_str
                if u.power != 1:
                    tex_str += "^{" + str(u.power) + "}"
                if i < len(unit) - 1:
                    tex_str += self.inter_unit_product
        
        return "$" + tex_str + "$"
