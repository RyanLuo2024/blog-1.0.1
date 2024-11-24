import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List

class Adjustment:
    """Represents adjustment values that are applied to the specified shape."""
    
    @property
    def name(self) -> str:
        """Gets the name of the adjustment."""
        ...
    
    @property
    def value(self) -> int:
        """Gets or sets the raw value of the adjustment.
        
        An adjust value is simply a guide that has a value based formula specified.
        That is, no calculation takes place for an adjust value guide.
        Instead, this guide specifies a parameter value that is used for calculations within the shape guides."""
        ...
    
    @value.setter
    def value(self, value: int):
        ...
    
    ...

class AdjustmentCollection:
    """Represents a read-only collection of :class:`Adjustment` adjust values that are applied to the specified shape."""
    
    def __getitem__(self, index: int) -> aspose.words.model.drawing.Adjustment:
        """Returns an adjustment at the specified index.
        
        :param index: An index into the collection."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of elements contained in the collection."""
        ...
    
    ...

