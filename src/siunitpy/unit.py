"""Parsing of units.

"""


class _unit():
    """
    This class is used to parse units.

    """
    units = {
# SI base units
        "ampere": r"\text{A}",
        "candela": r"\text{cd}",
        "kelvin": r"\text{K}",
        "kilogram": r"\text{kg}",
        "metre": r"\text{m}",
        "mole": r"\text{mol}",
        "second": r"\text{s}",
# SI derived units
        "becquerel": r"\text{Bq}",
        "degreeCelsius": r"\text{◦C}",
        "coulomb": r"\text{C}",
        "farad": r"\text{F}",
        "gray": r"\text{Gy}",
        "hertz": r"\text{Hz}",
        "henry": r"\text{H}",
        "joule": r"\text{J}",
        "lumen": r"\text{lm}",
        "katal": r"\text{kat}",
        "lux": r"\text{lx}",
        "ohm": r"\text{Ω}",
        "pascal": r"\text{Pa}",
        "radian": r"\text{rad}",
        "siemens": r"\text{S}",
        "sievert": r"\text{Sv}",
        "steradian": r"\text{sr}",
        "tesla": r"\text{T}",
        "volt": r"\text{V}",
        "watt": r"\text{W}",
        "weber": r"\text{Wb}",
# Non-SI units accepted for use with the SI
        "astronomicalunit": r"\text{au}",
        "bel": r"\text{B}",
        "dalton": r"\text{Da}",
        "day": r"\text{d}",
        "decibel": r"\text{dB}",
        "degree": r"\text{◦}",
        "electronvolt": r"\text{eV}",
        "hectare": r"\text{ha}",
        "hour": r"\text{h}",
        "litre": r"\text{L}",
        "liter": r"\text{L}",
        "arcminute": r"^\prime",
        "minute": r"\text{min}",
        "arcsecond": r"^{\prime\prime}",
        "neper": r"\text{Np}",
        "tonne": r"\text{t}",
    }

    si_prefixes = {
        "quecto": r"\text{q}",  # −30
        "ronto": r"\text{r}",  # −27
        "yocto": r"\text{y}",  # −24
        "zepto": r"\text{z}",  # −21
        "atto": r"\text{a}",  # −18
        "femto": r"\text{f}",  # −15
        "pico": r"\text{p}",  # −12
        "nano": r"\text{n}",  # −9
        "micro": r"\text{µ}",  # −6
        "milli": r"\text{m}",  # −3
        "centi": r"\text{c}",  # −2
        "deci": r"\text{d}",  # −1
        "deca": r"\text{da}",  # 1
        "hecto": r"\text{h}",  # 2
        "kilo": r"\text{k}",  # 3
        "mega": r"\text{M}",  # 6
        "giga": r"\text{G}",  # 9
        "tera": r"\text{T}",  # 12
        "peta": r"\text{P}",  # 15
        "exa": r"\text{E}",  # 18
        "zetta": r"\text{Z}",  # 21
        "yotta": r"\text{Y}",  # 24
        "ronna": r"\text{R}",  # 27
        "quetta": r"\text{Q}",  # 30
    }

    abbreviations = {
        "fg": r"\text{fg}",  # femtogram
        "pg": r"\text{pg}",  # picogram
        "ng": r"\text{ng}",  # nanogram
        "ug": r"\text{µg}",  # microgram
        "mg": r"\text{mg}",  # milligram
        "g": r"\text{g}",  # gram
        "kg": r"\text{kg}",  # kilogram
        "pm": r"\text{pm}",  # picometre
        "nm": r"\text{nm}",  # nanometre
        "um": r"\text{µm}",  # micrometre
        "mm": r"\text{mm}",  # millimetre
        "cm": r"\text{cm}",  # centimetre
        "dm": r"\text{dm}",  # decimetre
        "m": r"\text{m}",  # metre
        "km": r"\text{km}",  # kilometre
        "as": r"\text{as}",  # attosecond
        "fs": r"\text{fs}",  # femtosecond
        "ps": r"\text{ps}",  # picosecond
        "ns": r"\text{ns}",  # nanosecond
        "us": r"\text{µs}",  # microsecond
        "ms": r"\text{ms}",  # millisecond
        "s": r"\text{s}",  # second
        "fmol": r"\text{fmol}",  # femtomole
        "pmol": r"\text{pmol}",  # picomole
        "nmol": r"\text{nmol}",  # nanomole
        "umol": r"\text{µmol}",  # micromole
        "mmol": r"\text{mmol}",  # millimole
        "mol": r"\text{mol}",  # mole
        "kmol": r"\text{kmol}",  # kilomole
        "pA": r"\text{pA}",  # picoampere
        "nA": r"\text{nA}",  # nanoampere
        "uA": r"\text{µA}",  # microampere
        "mA": r"\text{mA}",  # milliampere
        "A": r"\text{A}",  # ampere
        "kA": r"\text{kA}",  # kiloampere
        "ul": r"\text{µL}",  # microlitre
        "ml": r"\text{mL}",  # millilitre
        "l": r"\text{L}",  # litre
        "hl": r"\text{hL}",  # hectolitre
        "uL": r"\text{µL}",  # microliter
        "mL": r"\text{mL}",  # milliliter
        "L": r"\text{L}",  # liter
        "hL": r"\text{hL}",  # hectoliter
        "mHz": r"\text{mHz}",  # millihertz
        "Hz": r"\text{Hz}",  # hertz
        "kHz": r"\text{kHz}",  # kilohertz
        "MHz": r"\text{MHz}",  # megahertz
        "GHz": r"\text{GHz}",  # gigahertz
        "THz": r"\text{THz}",  # terahertz
        "mN": r"\text{mN}",  # millinewton
        "N": r"\text{N}",  # newton
        "kN": r"\text{kN}",  # kilonewton
        "MN": r"\text{MN}",  # meganewton
        "Pa": r"\text{Pa}",  # pascal
        "kPa": r"\text{kPa}",  # kilopascal
        "MPa": r"\text{MPa}",  # megapascal
        "GPa": r"\text{GPa}",  # gigapascal
        "mohm": r"\text{mΩ}",  # milliohm
        "kohm": r"\text{kΩ}",  # kilohm
        "Mohm": r"\text{MΩ}",  # megohm
        "pV": r"\text{pV}",  # picovolt
        "nV": r"\text{nV}",  # nanovolt
        "uV": r"\text{µV}",  # microvolt
        "mV": r"\text{mV}",  # millivolt
        "V": r"\text{V}",  # volt
        "kV": r"\text{kV}",  # kilovolt
        "W": r"\text{W}",  # watt
        "nW": r"\text{nW}",  # nanowatt
        "uW": r"\text{µW}",  # microwatt
        "mW": r"\text{mW}",  # milliwatt
        "kW": r"\text{kW}",  # kilowatt
        "MW": r"\text{MW}",  # megawatt
        "GW": r"\text{GW}",  # gigawatt
        "J": r"\text{J}",  # joule
        "uJ": r"\text{µJ}",  # microjoule
        "mJ": r"\text{mJ}",  # millijoule
        "kJ": r"\text{kJ}",  # kilojoule
        "eV": r"\text{eV}",  # electronvolt
        "meV": r"\text{meV}",  # millielectronvolt
        "keV": r"\text{keV}",  # kiloelectronvolt
        "MeV": r"\text{MeV}",  # megaelectronvolt
        "GeV": r"\text{GeV}",  # gigaelectronvolt
        "TeV": r"\text{TeV}",  # teraelectronvolt
        "kWh": r"\text{kWh}",  # kilowatt hour
        "F": r"\text{F}",  # farad
        "fF": r"\text{fF}",  # femtofarad
        "pF": r"\text{pF}",  # picofarad
        "nF": r"\text{nF}",  # nanofarad
        "uF": r"\text{µF}",  # microfarad
        "mF": r"\text{mF}",  # millifarad
        "H": r"\text{H}",  # henry
        "fH": r"\text{fH}",  # femtohenry
        "pH": r"\text{pH}",  # picohenry
        "nH": r"\text{nH}",  # nanohenry
        "mH": r"\text{mH}",  # millihenry
        "uH": r"\text{µH}",  # microhenry
        "C": r"\text{C}",  # coulomb
        "nC": r"\text{nC}",  # nanocoulomb
        "mC": r"\text{mC}",  # millicoulomb
        "uC": r"\text{µC}",  # microcoulomb
        "T": r"\text{T}",  # tesla
        "mT": r"\text{mT}",  # millitesla
        "uT": r"\text{µT}",  # microtesla
        "K": r"\text{K}",  # kelvin
        "dB": r"\text{dB}",  # decibel
    }


    def __init__(self, unit):
        self.tex_str, self.power = self._parse_unit(unit)


    def _parse_unit(self, unit):
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
                    _powers.append(int(u))
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
        
        if len(_prefixes) == 1:
            tex_str = self.si_prefixes[_prefixes[0]]
        if len(_abbreviations) == 1:
            tex_str += self.abbreviations[_abbreviations[0]]
        if len(_units) == 1:
            tex_str += self.units[_units[0]]
        if len(_powers) == 1:
            power *= _powers[0]

        return tex_str, power
