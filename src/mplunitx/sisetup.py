"""sisetup

"""
from typing import Any, Dict, Literal

from . number import _number
from . unit import _parse_unit, _unit_kw



class sisetup():
    """
    
    """
    per_mode_options = ["power", "fraction", "symbol", "single-symbol",
                        "power-positive-first"]
    label_unit_mode_options = ["/", "[]"]

    def __init__(
        self,
        declare_unit: Dict[str, str] = None,
        inter_unit_product: str = r"\,",
        per_mode: Literal["power", "fraction", "symbol", "single-symbol",
                          "power-positive-first"] = "power",
        per_symbol: str = "/",
        bracket_unit_denominator: bool = True,
        per_symbol_script_correction: str = r"\!",
        sticky_per: bool = False,
        parse_units: bool = True,
        unit_font_command: str = r"\mathrm",
        quantity_product: str = r"\,",
        label_unit_mode: Literal["/", "[]"] = "/"
    ):
        # declare units
        if declare_unit is not None:
            if not isinstance(declare_unit, dict):
                raise TypeError("declare_unit must be a dict.")
            for k, v in declare_unit.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    raise TypeError("declare_unit must be a dict of str.")
        self.declare_unit = declare_unit

        # options unit
        self.unit_kw = _unit_kw(
            inter_unit_product=inter_unit_product,
            per_mode=per_mode,
            per_symbol=per_symbol,
            bracket_unit_denominator=bracket_unit_denominator,
            per_symbol_script_correction=per_symbol_script_correction,
            sticky_per=sticky_per,
            parse_units=parse_units,
            unit_font_command=unit_font_command
        )

        # options qty
        self.quantity_product = quantity_product

        # options label
        self.label_unit_mode = label_unit_mode


    @property
    def quantity_product(self) -> str:
        return self._quantity_product

    @quantity_product.setter
    def quantity_product(self, val: str):
        if isinstance(val, str):
            self._quantity_product = val
        else:
            raise ValueError("quantity_product must be a str.")


    @property
    def label_unit_mode(self) -> Literal["/", "[]"]:
        return self._label_unit_mode

    @label_unit_mode.setter
    def label_unit_mode(self, val: Literal["/", "[]"]):
        if val in self.label_unit_mode_options:
            self._label_unit_mode = val
        else:
            raise ValueError("label_unit_mode must be on of "
                             "label_unit_mode_options.")


    def num(number: str) -> str:
        """Returns the LaTeX representation of the given number.

        """
        number = _number(number)
        return "$" + number.tex_str + "$"


    def unit(
        self,
        unit: str,
        **unit_kw,
    ) -> str:
        """Returns the LaTeX representation of the given unit.

        """
        if not isinstance(unit, str):
            raise TypeError("unit must be a string.")
        
        kw = _unit_kw(**self.unit_kw._unit_kw)
        if unit_kw is not None:
            kw.update(unit_kw)

        if not kw.parse_units:
            return unit

        unit = unit.split(";")

        if kw.per_mode != "power":
            # If per_mode is fraction add \frac{ 
            if kw.per_mode == "fraction":
                tex_str = r"\frac{"
            else:
                tex_str = ""

            # Add all units to str with positive power
            count_pos = 0
            for i, u in enumerate(unit):
                utex, power = _parse_unit(
                    u, user_declared_units=self.declare_unit)
                if power > 0:
                    tex_str += utex
                    if power != 1:
                        tex_str += "^{" + str(power) + "}"
                    tex_str += kw.inter_unit_product
                    count_pos += 1

            # Add str between pos and neg power
            if kw.per_mode == "fraction":
                tex_str = tex_str[:-len(kw.inter_unit_product)]
                tex_str += "}{"
            elif kw.per_mode in ["symbol", "single-symbol"]:
                tex_str = tex_str[:-len(kw.inter_unit_product)]
                if tex_str[-2].isdigit():
                    tex_str += kw.per_symbol_script_correction
                tex_str += kw.per_symbol
                if kw.bracket_unit_denominator:
                    tex_str += "("

            # Add all units to str with negative power
            count_neg = 0
            for i, u in enumerate(unit):
                utex, power = _parse_unit(
                    u, user_declared_units=self.declare_unit)
                if power < 0:
                    tex_str += utex
                    if (kw.per_mode in 
                        ["symbol", "single-symbol", "fraction"]):
                        if power != -1:   
                            tex_str += "^{" + str(-power) + "}"
                    else:      
                        tex_str += "^{" + str(power) + "}"
                    tex_str += kw.inter_unit_product
                    count_neg += 1

            tex_str = tex_str[:-len(kw.inter_unit_product)]
            if kw.per_mode == "fraction":
                tex_str += "}"
            if (kw.per_mode in ["symbol", "single-symbol"] 
                and kw.bracket_unit_denominator):
                if count_neg > 1:
                    tex_str += ")"
                else:
                    tex_str = tex_str.replace("(", "")

        # If per_mode is power or single-symbol and count_neg > 1
        if kw.per_mode == "power" or (kw.per_mode == "single-symbol"
                                        and count_neg > 1):
            tex_str = ""
            for i, u in enumerate(unit):
                utex, power = _parse_unit(
                    u, user_declared_units=self.declare_unit)
                tex_str += utex
                if power != 1:
                    tex_str += "^{" + str(power) + "}"
                if i < len(unit) - 1:
                    tex_str += kw.inter_unit_product
        
        return "$" + tex_str + "$"


    def qty(
        self,
        number: str,
        unit: str,
        unit_kw: Dict[str, Any] = None,
        **qty_kw,
    ) -> str:
        """Returns the LaTeX representation of the given quantity.

        """
        number = self.num(number).replace("$", "")

        if unit_kw is None:
            unit = self.unit(unit).replace("$", "")
        else:
            unit = self.unit(unit, **unit_kw).replace("$", "")

        first_unit = unit.find("{") + 1
        if unit[first_unit] == "'":
            return "$" + number + unit + "$"
        elif unit[first_unit] == "◦" and unit[first_unit+1] != "C":
            return "$" + number + unit + "$"

        return "$" + number + self.quantity_product + unit + "$"


    def label(self, var: str, unit: str) -> str:
        """Returns the LaTeX representation of the given label.

        """
        if not isinstance(var, str):
            raise TypeError("var must be a string.")

        unit = self.unit(unit).replace("$", "")

        if self.label_unit_mode == "/":
            return var + r"$\;/\;" + unit + "$"
        elif self.label_unit_mode == "[]":
            return var + r"\;[" + unit + r"]"
