"""sisetup

"""
import warnings
from . unit import _unit


class sisetup():
    """
    
    """

    def __init__(self, inter_unit_product=r"\,", per_mode="power",
                 per_symbol="/", bracket_unit_denominator=True,
                 per_symbol_script_correction=r"\!", sticky_per=False,
                 parse_units=True, unit_font_command=r"\mathrm"):
        """
        
        """
        self.per_mode = per_mode
        self.per_symbol = per_symbol
        self.inter_unit_product = inter_unit_product
        self.bracket_unit_denominator = bracket_unit_denominator
        self.per_symbol_script_correction = per_symbol_script_correction
        self.sticky_per = sticky_per
        self.parse_units = parse_units
        self.unit_font_command = unit_font_command


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
            raise ValueError("per_mode must be either 'power', 'fraction', "
                             "'power-positive-first', 'symbol' or "
                             "'single-symbol'.")


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
    def per_symbol_script_correction(self):
        return self._per_symbol_script_correction

    @per_symbol_script_correction.setter
    def per_symbol_script_correction(self, per_symbol_script_correction):
        if isinstance(per_symbol_script_correction, str):
            self._per_symbol_script_correction = per_symbol_script_correction
        else:
            raise TypeError("per_symbol_script_correction must be a string.")


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
    def sticky_per(self):
        return self._sticky_per

    @sticky_per.setter
    def sticky_per(self, sticky_per):
        if isinstance(sticky_per, bool):
            if sticky_per:
                warnings.warn("sticky_per is not implemented yet.")
            else:
                self._sticky_per = sticky_per
        else:
            raise TypeError("sticky_per must be a boolean.")


    @property
    def parse_units(self):
        return self._parse_units

    @parse_units.setter
    def parse_units(self, parse_units):
        if isinstance(parse_units, bool):
            self._parse_units = parse_units
        else:
            raise TypeError("parse_units must be a boolean.")


    @property
    def inter_unit_product(self):
        return self._inter_unit_product

    @inter_unit_product.setter
    def inter_unit_product(self, inter_unit_product):
        if isinstance(inter_unit_product, str):
            self._inter_unit_product = inter_unit_product
        else:
            raise TypeError("inter_unit_product must be a string.")


    @property
    def unit_font_command(self):
        return self._unit_font_command

    @unit_font_command.setter
    def unit_font_command(self, unit_font_command):
        if isinstance(unit_font_command, str):
            self._unit_font_command = unit_font_command
        else:
            raise TypeError("unit_font_command must be a string.")


    def unit(self, unit):
        """Returns the LaTeX representation of the given unit.

        """
        if not isinstance(unit, str):
            raise TypeError("unit must be a string.")

        if not self.parse_units:
            return unit

        unit = unit.split(";")

        if self.per_mode != "power":
            # If per_mode is fraction add \frac{ 
            if self.per_mode == "fraction":
                tex_str = r"\frac{"
            else:
                tex_str = ""

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
                if tex_str[-2].isdigit():
                    tex_str += self.per_symbol_script_correction
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
