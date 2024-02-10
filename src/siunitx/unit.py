"""Parsing of units.

"""


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
        if "square" in unit:
            power *= 2 * unit.count("squared")
            unit = _remove_values_from_list(unit, "squared")
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
