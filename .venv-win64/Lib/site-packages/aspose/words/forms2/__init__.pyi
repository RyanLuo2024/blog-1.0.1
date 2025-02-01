import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List

class MorphDataControl(aspose.words.drawing.ole.Forms2OleControl):
    """The MorphDataControl structure is an aggregate of six controls: CheckBox, ComboBox, ListBox, OptionButton, TextBox, and ToggleButton."""
    
    ...

class TextBoxControl(aspose.words.forms2.MorphDataControl):
    """The TextBox control displays text from an organized set of data or user input."""
    
    @property
    def type(self) -> aspose.words.drawing.ole.Forms2OleControlType:
        """Gets type of Forms 2.0 control."""
        ...
    
    @property
    def text(self) -> str:
        """Gets or sets a text of the control."""
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    ...

