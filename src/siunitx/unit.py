"""Parsing of units.

"""
import warnings
from typing import Any, Dict, Literal



class _unit_kw():
    """
    
    """
    per_mode_options = ["power", "fraction", "symbol", "single-symbol",
                        "power-positive-first"]

    def __init__(
        self,
        inter_unit_product: str = r"\,",
        per_mode: Literal["power", "fraction", "symbol", "single-symbol",
                          "power-positive-first"] = "power",
        per_symbol: str = "/",
        bracket_unit_denominator: bool = True,
        per_symbol_script_correction: str = r"\!",
        sticky_per: bool = False,
        parse_units: bool = True,
        unit_font_command: str = r"\mathrm"
    ):
        # options dictionary
        self._unit_kw = {}

        # options unit
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
        return self._unit_kw["per_mode"]

    @per_mode.setter
    def per_mode(self, val):
        if val in self.per_mode_options:
            self._unit_kw["per_mode"] = val
        else:
            raise ValueError("per_mode must be one of per_mode_options.")


    @property
    def per_symbol(self):
        return self._unit_kw["per_symbol"]

    @per_symbol.setter
    def per_symbol(self, val):
        if isinstance(val, str):
            self._unit_kw["per_symbol"] = val
        else:
            raise TypeError("per_symbol must be a string.")


    @property
    def per_symbol_script_correction(self):
        return self._unit_kw["per_symbol_script_correction"]

    @per_symbol_script_correction.setter
    def per_symbol_script_correction(self, val):
        if isinstance(val, str):
            self._unit_kw["per_symbol_script_correction"] = val
        else:
            raise TypeError("per_symbol_script_correction must be a string.")


    @property
    def bracket_unit_denominator(self):
        return self._unit_kw["bracket_unit_denominator"]

    @bracket_unit_denominator.setter
    def bracket_unit_denominator(self, val):
        if isinstance(val, bool):
            self._unit_kw["bracket_unit_denominator"] = val
        else:
            raise TypeError("bracket_unit_denominator must be a boolean.")


    @property
    def sticky_per(self):
        return self._unit_kw["sticky_per"]

    @sticky_per.setter
    def sticky_per(self, val):
        if isinstance(val, bool):
            if val:
                warnings.warn("sticky_per is not implemented yet.")
            else:
                self._unit_kw["sticky_per"] = val
        else:
            raise TypeError("sticky_per must be a boolean.")


    @property
    def parse_units(self):
        return self._unit_kw["parse_units"]

    @parse_units.setter
    def parse_units(self, val):
        if isinstance(val, bool):
            self._unit_kw["parse_units"] = val
        else:
            raise TypeError("parse_units must be a boolean.")


    @property
    def inter_unit_product(self):
        return self._unit_kw["inter_unit_product"]

    @inter_unit_product.setter
    def inter_unit_product(self, val):
        if isinstance(val, str):
            self._unit_kw["inter_unit_product"] = val
        else:
            raise TypeError("inter_unit_product must be a string.")


    @property
    def unit_font_command(self):
        return self._unit_kw["unit_font_command"]

    @unit_font_command.setter
    def unit_font_command(self, val):
        if isinstance(val, str):
            self._unit_kw["unit_font_command"] = val
        else:
            raise TypeError("unit_font_command must be a string.")


    def __repr__(self):
        return f"_unit_kw({self._unit_kw})"


    def __str__(self):
        return f"_unit_kw({self._unit_kw})"


    def update(self, kw: Dict[str, Any]):
        """Update the unit_kw options.

        """
        for k, v in kw.items():
            if k in self._unit_kw:
                setattr(self, k, v)
            else:
                raise ValueError(f"{k} is not a valid option.")



class _unit():
    """
    This class is used to parse units.

    """
    units = {
# SI base units
        "ampere": "A",
        "candela": "cd",
        "kelvin": "K",
        "kilogram": "kg",
        "metre": "m",
        "mole": "mol",
        "second": "s",
# SI derived units
        "becquerel": "Bq",
        "degreeCelsius": "◦C",
        "coulomb": "C",
        "farad": "F",
        "gray": "Gy",
        "hertz": "Hz",
        "henry": "H",
        "joule": "J",
        "lumen": "lm",
        "katal": "kat",
        "lux": "lx",
        "ohm": "Ω",
        "pascal": "Pa",
        "radian": "rad",
        "siemens": "S",
        "sievert": "Sv",
        "steradian": "sr",
        "tesla": "T",
        "volt": "V",
        "watt": "W",
        "weber": "Wb",
# Non-SI units accepted for use with the SI
        "astronomicalunit": "au",
        "bel": "B",
        "dalton": "Da",
        "day": "d",
        "decibel": "dB",
        "degree": "◦",
        "electronvolt": "eV",
        "hectare": "ha",
        "hour": "h",
        "litre": "L",
        "liter": "L",
        "arcminute": "'",
        "minute": "min",
        "arcsecond": "''",
        "neper": "Np",
        "tonne": "t",
    }

    si_prefixes = {
        "quecto": "q",  # −30
        "ronto": "r",  # −27
        "yocto": "y",  # −24
        "zepto": "z",  # −21
        "atto": "a",  # −18
        "femto": "f",  # −15
        "pico": "p",  # −12
        "nano": "n",  # −9
        "micro": "µ",  # −6
        "milli": "m",  # −3
        "centi": "c",  # −2
        "deci": "d",  # −1
        "deca": "da",  # 1
        "hecto": "h",  # 2
        "kilo": "k",  # 3
        "mega": "M",  # 6
        "giga": "G",  # 9
        "tera": "T",  # 12
        "peta": "P",  # 15
        "exa": "E",  # 18
        "zetta": "Z",  # 21
        "yotta": "Y",  # 24
        "ronna": "R",  # 27
        "quetta": "Q",  # 30
    }

    abbreviations = {
        "fg": "fg",  # femtogram
        "pg": "pg",  # picogram
        "ng": "ng",  # nanogram
        "ug": "µg",  # microgram
        "mg": "mg",  # milligram
        "g": "g",  # gram
        "kg": "kg",  # kilogram
        "pm": "pm",  # picometre
        "nm": "nm",  # nanometre
        "um": "µm",  # micrometre
        "mm": "mm",  # millimetre
        "cm": "cm",  # centimetre
        "dm": "dm",  # decimetre
        "m": "m",  # metre
        "km": "km",  # kilometre
        "as": "as",  # attosecond
        "fs": "fs",  # femtosecond
        "ps": "ps",  # picosecond
        "ns": "ns",  # nanosecond
        "us": "µs",  # microsecond
        "ms": "ms",  # millisecond
        "s": "s",  # second
        "fmol": "fmol",  # femtomole
        "pmol": "pmol",  # picomole
        "nmol": "nmol",  # nanomole
        "umol": "µmol",  # micromole
        "mmol": "mmol",  # millimole
        "mol": "mol",  # mole
        "kmol": "kmol",  # kilomole
        "pA": "pA",  # picoampere
        "nA": "nA",  # nanoampere
        "uA": "µA",  # microampere
        "mA": "mA",  # milliampere
        "A": "A",  # ampere
        "kA": "kA",  # kiloampere
        "ul": "µL",  # microlitre
        "ml": "mL",  # millilitre
        "l": "L",  # litre
        "hl": "hL",  # hectolitre
        "uL": "µL",  # microliter
        "mL": "mL",  # milliliter
        "L": "L",  # liter
        "hL": "hL",  # hectoliter
        "mHz": "mHz",  # millihertz
        "Hz": "Hz",  # hertz
        "kHz": "kHz",  # kilohertz
        "MHz": "MHz",  # megahertz
        "GHz": "GHz",  # gigahertz
        "THz": "THz",  # terahertz
        "mN": "mN",  # millinewton
        "N": "N",  # newton
        "kN": "kN",  # kilonewton
        "MN": "MN",  # meganewton
        "Pa": "Pa",  # pascal
        "kPa": "kPa",  # kilopascal
        "MPa": "MPa",  # megapascal
        "GPa": "GPa",  # gigapascal
        "mohm": "mΩ",  # milliohm
        "kohm": "kΩ",  # kilohm
        "Mohm": "MΩ",  # megohm
        "pV": "pV",  # picovolt
        "nV": "nV",  # nanovolt
        "uV": "µV",  # microvolt
        "mV": "mV",  # millivolt
        "V": "V",  # volt
        "kV": "kV",  # kilovolt
        "W": "W",  # watt
        "nW": "nW",  # nanowatt
        "uW": "µW",  # microwatt
        "mW": "mW",  # milliwatt
        "kW": "kW",  # kilowatt
        "MW": "MW",  # megawatt
        "GW": "GW",  # gigawatt
        "J": "J",  # joule
        "uJ": "µJ",  # microjoule
        "mJ": "mJ",  # millijoule
        "kJ": "kJ",  # kilojoule
        "eV": "eV",  # electronvolt
        "meV": "meV",  # millielectronvolt
        "keV": "keV",  # kiloelectronvolt
        "MeV": "MeV",  # megaelectronvolt
        "GeV": "GeV",  # gigaelectronvolt
        "TeV": "TeV",  # teraelectronvolt
        "kWh": "kWh",  # kilowatt hour
        "F": "F",  # farad
        "fF": "fF",  # femtofarad
        "pF": "pF",  # picofarad
        "nF": "nF",  # nanofarad
        "uF": "µF",  # microfarad
        "mF": "mF",  # millifarad
        "H": "H",  # henry
        "fH": "fH",  # femtohenry
        "pH": "pH",  # picohenry
        "nH": "nH",  # nanohenry
        "mH": "mH",  # millihenry
        "uH": "µH",  # microhenry
        "C": "C",  # coulomb
        "nC": "nC",  # nanocoulomb
        "mC": "mC",  # millicoulomb
        "uC": "µC",  # microcoulomb
        "T": "T",  # tesla
        "mT": "mT",  # millitesla
        "uT": "µT",  # microtesla
        "K": "K",  # kelvin
        "dB": "dB",  # decibel
    }


    def __init__(self, unit, unit_font_command=r"\mathrm"):
        self.tex_str, self.power = self._parse_unit(unit, unit_font_command)


    def _parse_unit(self, unit, unit_font_command):
        if not isinstance(unit, str):
            raise TypeError("unit must be a string.")
        if len(unit) == 0:
            raise ValueError("unit must not be empty.")
        
        unit = unit.split(".")
        def _remove_values_from_list(the_list, val):
            return [value for value in the_list if value != val]

        tex_str = ""

        # Count "per" and change power accordingly
        power = (-1)**unit.count("per")
        unit = _remove_values_from_list(unit, "per")

        # Count squared and cubic and change power accordingly
        if "squared" in unit:
            power *= 2 * unit.count("squared")
            unit = _remove_values_from_list(unit, "squared")
        if "cubed" in unit:
            power *= 3 * unit.count("cubed")
            unit = _remove_values_from_list(unit, "cubed")
        if "cubic" in unit:
            power *= 3 * unit.count("cubic")
            unit = _remove_values_from_list(unit, "cubic")

        # Parse prefix and unit
        _prefixes = []
        _units = []
        _abbreviations = []
        _powers = []
        for u in unit:
            if u in self.si_prefixes:
                _prefixes.append(u)
            elif u in self.units:
                _units.append(u)
            elif u in self.abbreviations:
                _abbreviations.append(u)
            else:
                try:
                    _powers.append(float(u))
                except ValueError:
                    raise ValueError(u + " could not be parsed.")

        if len(_units) > 1:
            raise ValueError("Only one unit per ';' allowed.")
        elif len(_prefixes) > 1:
            raise ValueError("Only one prefix per ';' allowed.")
        elif len(_abbreviations) > 1:
            raise ValueError("Only one abbreviation per ';' allowed.")
        elif len(_units) == 1 and len(_abbreviations) == 1:
            raise ValueError("Only one unit or abbreviation per ';' allowed.")
        elif len(_units) == 0 and len(_abbreviations) == 0:
            raise ValueError("No unit was given.")
        elif len(_powers) > 1:
            raise ValueError("Only one power per ';' allowed.")
        
        tex_str = unit_font_command + "{"
        if len(_prefixes) == 1:
            tex_str += self.si_prefixes[_prefixes[0]]
        if len(_abbreviations) == 1:
            tex_str += self.abbreviations[_abbreviations[0]]
        if len(_units) == 1:
            tex_str += self.units[_units[0]]
        tex_str += "}"
        if len(_powers) == 1:
            power *= _powers[0]

        if int(power) == power:
            power = int(power)

        return tex_str, power
