import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class BasicTextShaperCache:
    
    def __init__(self, factory: aspose.words.shaping.ITextShaperFactory):
        ...
    
    ...

class Cluster:
    
    def __init__(self, codepoints: List[int], glyphs: List[aspose.words.shaping.Glyph]):
        ...
    
    @overload
    @staticmethod
    def get_string(clusters: List[aspose.words.shaping.Cluster]) -> str:
        ...
    
    @overload
    def get_string(self) -> str:
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        ...
    
    def deep_clone(self) -> aspose.words.shaping.Cluster:
        ...
    
    @property
    def codepoints(self) -> List[int]:
        ...
    
    @property
    def codepoints_length(self) -> int:
        ...
    
    @property
    def glyphs(self) -> List[aspose.words.shaping.Glyph]:
        ...
    
    ...

class Glyph:
    
    def __init__(self, glyph_index: int, advance: int, advance_offset: int, ascender_offset: int):
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        ...
    
    def clone(self) -> aspose.words.shaping.Glyph:
        ...
    
    @property
    def glyph_index(self) -> int:
        ...
    
    @property
    def advance(self) -> int:
        ...
    
    @advance.setter
    def advance(self, value: int):
        ...
    
    @property
    def advance_offset(self) -> int:
        ...
    
    @property
    def ascender_offset(self) -> int:
        ...
    
    ...

class ITextShaper:
    
    def shape_text(self, runs: List[str], direction: aspose.words.shaping.Direction, script: aspose.words.shaping.UnicodeScript, enabled_font_features: List[aspose.words.shaping.FontFeature], variations: List[aspose.words.shaping.VariationAxisCoordinate]) -> List[List[aspose.words.shaping.Cluster]]:
        ...
    
    ...

class ITextShaperFactory:
    
    @overload
    def get_text_shaper(self, font_path: str, face_index: int) -> aspose.words.shaping.ITextShaper:
        ...
    
    @overload
    def get_text_shaper(self, font_id: str, font_blob: bytes, face_index: int) -> aspose.words.shaping.ITextShaper:
        ...
    
    ...

class VariationAxisCoordinate:
    
    def __init__(self):
        ...
    
    @property
    def axis(self) -> aspose.words.shaping.VariationAxis:
        ...
    
    @axis.setter
    def axis(self, value: aspose.words.shaping.VariationAxis):
        ...
    
    @property
    def coordinate(self) -> float:
        ...
    
    @coordinate.setter
    def coordinate(self, value: float):
        ...
    
    ...

class Direction(Enum):
    
    DEFAULT: int
    
    LTR: int
    
    RTL: int
    
    TTB: int
    
    BTT: int
    

class FontFeature(Enum):
    
    GLYPH_COMPOSITION_DECOMPOSITION: int
    
    STANDARD_LIGATURES: int
    
    REQUIRED_LIGATURES: int
    
    CONTEXTUAL_LIGATURES: int
    
    DISCRETIONARY_LIGATURES: int
    
    HISTORICAL_LIGATURES: int
    
    PROPORTIONAL_FIGURES: int
    
    TABULAR_FIGURES: int
    
    LINING_FIGURES: int
    
    OLDSTYLE_FIGURES: int
    
    VERTICAL_ALTERNATES: int
    
    VERTICAL_ALTERNATES_AND_ROTATION: int
    
    STYLISTIC_SET01: int
    
    STYLISTIC_SET02: int
    
    STYLISTIC_SET03: int
    
    STYLISTIC_SET04: int
    
    STYLISTIC_SET05: int
    
    STYLISTIC_SET06: int
    
    STYLISTIC_SET07: int
    
    STYLISTIC_SET08: int
    
    STYLISTIC_SET09: int
    
    STYLISTIC_SET10: int
    
    STYLISTIC_SET11: int
    
    STYLISTIC_SET12: int
    
    STYLISTIC_SET13: int
    
    STYLISTIC_SET14: int
    
    STYLISTIC_SET15: int
    
    STYLISTIC_SET16: int
    
    STYLISTIC_SET17: int
    
    STYLISTIC_SET18: int
    
    STYLISTIC_SET19: int
    
    STYLISTIC_SET20: int
    
    KERNING: int
    

class ScriptShapingLevel(Enum):
    
    NONE: int
    
    UNKNOWN: int
    
    MINIMUM: int
    
    FULL: int
    

class UnicodeScript(Enum):
    
    ADLAM: int
    
    CAUCASIAN_ALBANIAN: int
    
    AHOM: int
    
    ARABIC: int
    
    IMPERIAL_ARAMAIC: int
    
    ARMENIAN: int
    
    AVESTAN: int
    
    BALINESE: int
    
    BAMUM: int
    
    BASSA_VAH: int
    
    BATAK: int
    
    BENGALI: int
    
    BHAIKSUKI: int
    
    BOPOMOFO: int
    
    BRAHMI: int
    
    BRAILLE: int
    
    BUGINESE: int
    
    BUHID: int
    
    CHAKMA: int
    
    CANADIAN_ABORIGINAL: int
    
    CARIAN: int
    
    CHAM: int
    
    CHEROKEE: int
    
    CHORASMIAN: int
    
    COPTIC: int
    
    CYPRIOT: int
    
    CYRILLIC: int
    
    DEVANAGARI: int
    
    DIVES_AKURU: int
    
    DOGRA: int
    
    DESERET: int
    
    DUPLOYAN: int
    
    EGYPTIAN_HIEROGLYPHS: int
    
    ELBASAN: int
    
    ELYMAIC: int
    
    ETHIOPIC: int
    
    GEORGIAN: int
    
    GLAGOLITIC: int
    
    GUNJALA_GONDI: int
    
    MASARAM_GONDI: int
    
    GOTHIC: int
    
    GRANTHA: int
    
    GREEK: int
    
    GUJARATI: int
    
    GURMUKHI: int
    
    HANGUL: int
    
    HAN: int
    
    HANUNOO: int
    
    HATRAN: int
    
    HEBREW: int
    
    HIRAGANA: int
    
    ANATOLIAN_HIEROGLYPHS: int
    
    PAHAWH_HMONG: int
    
    NYIAKENG_PUACHUE_HMONG: int
    
    KATAKANA_OR_HIRAGANA: int
    
    OLD_HUNGARIAN: int
    
    OLD_ITALIC: int
    
    JAVANESE: int
    
    KAYAH_LI: int
    
    KATAKANA: int
    
    KHAROSHTHI: int
    
    KHMER: int
    
    KHOJKI: int
    
    KHITAN_SMALL_SCRIPT: int
    
    KANNADA: int
    
    KAITHI: int
    
    TAI_THAM: int
    
    LAO: int
    
    LATIN: int
    
    LEPCHA: int
    
    LIMBU: int
    
    LINEAR_A: int
    
    LINEAR_B: int
    
    LISU: int
    
    LYCIAN: int
    
    LYDIAN: int
    
    MAHAJANI: int
    
    MAKASAR: int
    
    MANDAIC: int
    
    MANICHAEAN: int
    
    MARCHEN: int
    
    MEDEFAIDRIN: int
    
    MENDE_KIKAKUI: int
    
    MEROITIC_CURSIVE: int
    
    MEROITIC_HIEROGLYPHS: int
    
    MALAYALAM: int
    
    MODI: int
    
    MONGOLIAN: int
    
    MRO: int
    
    MEETEI_MAYEK: int
    
    MULTANI: int
    
    MYANMAR: int
    
    NANDINAGARI: int
    
    OLD_NORTH_ARABIAN: int
    
    NABATAEAN: int
    
    NEWA: int
    
    NKO: int
    
    NUSHU: int
    
    OGHAM: int
    
    OL_CHIKI: int
    
    OLD_TURKIC: int
    
    ORIYA: int
    
    OSAGE: int
    
    OSMANYA: int
    
    PALMYRENE: int
    
    PAU_CIN_HAU: int
    
    OLD_PERMIC: int
    
    PHAGS_PA: int
    
    INSCRIPTIONAL_PAHLAVI: int
    
    PSALTER_PAHLAVI: int
    
    PHOENICIAN: int
    
    MIAO: int
    
    INSCRIPTIONAL_PARTHIAN: int
    
    REJANG: int
    
    HANIFI_ROHINGYA: int
    
    RUNIC: int
    
    SAMARITAN: int
    
    OLD_SOUTH_ARABIAN: int
    
    SAURASHTRA: int
    
    SIGN_WRITING: int
    
    SHAVIAN: int
    
    SHARADA: int
    
    SIDDHAM: int
    
    KHUDAWADI: int
    
    SINHALA: int
    
    SOGDIAN: int
    
    OLD_SOGDIAN: int
    
    SORA_SOMPENG: int
    
    SOYOMBO: int
    
    SUNDANESE: int
    
    SYLOTI_NAGRI: int
    
    SYRIAC: int
    
    TAGBANWA: int
    
    TAKRI: int
    
    TAI_LE: int
    
    NEW_TAI_LUE: int
    
    TAMIL: int
    
    TANGUT: int
    
    TAI_VIET: int
    
    TELUGU: int
    
    TIFINAGH: int
    
    TAGALOG: int
    
    THAANA: int
    
    THAI: int
    
    TIBETAN: int
    
    TIRHUTA: int
    
    UGARITIC: int
    
    VAI: int
    
    WARANG_CITI: int
    
    WANCHO: int
    
    OLD_PERSIAN: int
    
    CUNEIFORM: int
    
    YEZIDI: int
    
    YI: int
    
    ZANABAZAR_SQUARE: int
    
    INHERITED: int
    
    COMMON: int
    
    UNKNOWN: int
    

class VariationAxis(Enum):
    
    ITALIC: int
    
    OPTICAL_SIZE: int
    
    SLANT: int
    
    WEIGHT: int
    
    WIDTH: int
    

