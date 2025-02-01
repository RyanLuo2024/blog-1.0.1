import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class AiModel:
    """Represents information about a Generative Language Model."""
    
    @staticmethod
    def create(model_type: aspose.words.ai.AiModelType) -> aspose.words.ai.AiModel:
        """Creates a new instance of :class:`AiModel` class."""
        ...
    
    def with_api_key(self, api_key: str) -> aspose.words.ai.AiModel:
        """Sets a specified API key to the model."""
        ...
    
    def as_open_ai_model(self) -> aspose.words.ai.OpenAiModel:
        """Cast AiModel to :class:`OpenAiModel`."""
        ...
    
    def as_google_ai_model(self) -> aspose.words.ai.GoogleAiModel:
        """Cast AiModel to :class:`GoogleAiModel`."""
        ...
    
    ...

class GoogleAiModel(aspose.words.ai.AiModel):
    """An abstract class representing the integration with Google’s AI models within the Aspose.Words."""
    
    ...

class IAiModelText:
    """The common interface for AI models designed to generate a variety of text-based content."""
    
    @overload
    def summarize(self, doc: aspose.words.Document, options: aspose.words.ai.SummarizeOptions) -> aspose.words.Document:
        """Generates a summary of the specified document, with options to adjust the length of the summary.
        This operation leverages the connected AI model for content processing.
        
        :param doc: The document to be summarized.
        :param options: Optional settings to control the summary length and other parameters.
        :returns: A summarized version of the document's content."""
        ...
    
    @overload
    def summarize(self, docs: List[aspose.words.Document], options: aspose.words.ai.SummarizeOptions) -> aspose.words.Document:
        """Generates summaries for an array of documents, with options to control the summary length and other settings.
        This method utilizes the connected AI model for processing each document in the array.
        
        :param docs: An array of documents to be summarized.
        :param options: Optional settings to control the summary length and other parameters
        :returns: A summarized version of the document's content."""
        ...
    
    ...

class OpenAiModel(aspose.words.ai.AiModel):
    """An abstract class representing the integration with OpenAI's large language models within the Aspose.Words."""
    
    def with_organization(self, organization_id: str) -> aspose.words.ai.OpenAiModel:
        """Sets a specified Organization to the model."""
        ...
    
    def with_project(self, project_id: str) -> aspose.words.ai.OpenAiModel:
        """Sets a specified Project to the model."""
        ...
    
    ...

class SummarizeOptions:
    """Allows to specify various options for summarizing document content."""
    
    def __init__(self):
        """Initializes a new instances of :class:`SummarizeOptions` class."""
        ...
    
    @property
    def summary_length(self) -> aspose.words.ai.SummaryLength:
        """Allows to specify summary length.
        Default value is :attr:`SummaryLength.MEDIUM`."""
        ...
    
    @summary_length.setter
    def summary_length(self, value: aspose.words.ai.SummaryLength):
        ...
    
    ...

class AiModelType(Enum):
    """Represents the types of :class:`AiModel` that can be integrated into the document processing workflow.
    
    This enumeration is used to define which large language model (LLM) should be utilized for tasks
    such as summarization, translation, and content generation."""
    
    """GPT-4o generative model type."""
    GPT_4O: int
    
    """GPT-4o mini generative model type."""
    GPT_4O_MINI: int
    
    """GPT-4 Turbo generative model type."""
    GPT_4_TURBO: int
    
    """GPT-3.5 Turbo generative model type."""
    GPT_35_TURBO: int
    
    """Gemini 1.5 Flash generative model type."""
    GEMINI_15_FLASH: int
    
    """Gemini 1.5 Flash-8B generative model type."""
    GEMINI_15_FLASH_8B: int
    
    """Gemini 1.5 Pro generative model type."""
    GEMINI_15_PRO: int
    

class SummaryLength(Enum):
    """Enumerates possible lengths of summary."""
    
    """Try to generate 1-2 sentences."""
    VERY_SHORT: int
    
    """Try to generate 3-4 sentences."""
    SHORT: int
    
    """Try to generate 5-6 sentences."""
    MEDIUM: int
    
    """Try to generate 7-10 sentences."""
    LONG: int
    
    """Try to generate 11-20 sentences."""
    VERY_LONG: int
    

