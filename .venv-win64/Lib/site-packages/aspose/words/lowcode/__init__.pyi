import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class Converter:
    """Represents a group of methods intended to convert a variety of different types of documents using a single line of code.
    
    The specified input and output files or streams, along with the desired save format,
    are used to convert the given input document of the one format into the output document
    of the other specified format.
    
    The convert functionality supports over 35+ different file formats.
    
    The :meth:`Converter.convert_to_images` group of methods are designed to transform documents into images,
    with each page being converted into a separate image file. These methods also convert PDF documents directly to fixed-page formats
    without loading them into the document model, which enhances both performance and accuracy.
    
    With :attr:`aspose.words.saving.ImageSaveOptions.page_set`, you can specify a particular set of pages to convert into images."""
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str) -> None:
        """Converts the given input document into the output document using specified input output file names and its extensions.
        
        :param input_file: The input file name.
        :param output_file: The output file name."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str, save_format: aspose.words.SaveFormat) -> None:
        """Converts the given input document into the output document using specified input output file names and the final document format.
        
        :param input_file: The input file name.
        :param output_file: The output file name.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into the output document using specified input output file names and save options.
        
        :param input_file: The input file name.
        :param output_file: The output file name.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, load_options: aspose.words.loading.LoadOptions, output_file: str, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into the output document using specified input output file names its load/save options.
        
        :param input_file: The input file name.
        :param load_options: The input document load options.
        :param output_file: The output file name.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input streams.
        :param output_stream: The output stream.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input streams.
        :param load_options: The input document load options.
        :param output_stream: The output stream.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str) -> None:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension""""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str, save_format: aspose.words.SaveFormat) -> None:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_format: Save format. Only image save formats are allowed."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_options: Image save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, load_options: aspose.words.loading.LoadOptions, output_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param load_options: The input document load options.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_options: Image save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the input file pages to images.
        
        :param input_file: The input file name.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the input stream pages to images.
        
        :param input_stream: The input stream.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the input stream pages to images.
        
        :param input_stream: The input stream.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the input stream pages to images.
        
        :param input_stream: The input stream.
        :param load_options: The input document load options.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(doc: aspose.words.Document, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the document pages to images.
        
        :param doc: The input document.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(doc: aspose.words.Document, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the document pages to images.
        
        :param doc: The input document.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the enduser."""
        ...
    
    ...

class Merger:
    """Represents a group of methods intended to merge a variety of different types of documents into a single output document.
    
    The specified input and output files or streams, along with the desired merge and save options,
    are used to merge the given input documents into a single output document.
    
    The merging functionality supports over 35 different file formats."""
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str]) -> None:
        """Merges the given input documents into a single output document using specified input and output file names.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        
        By default :attr:`MergeFormatMode.KEEP_SOURCE_FORMATTING` is used."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], save_format: aspose.words.SaveFormat, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and the final document format.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_format: The save format.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and save options.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], load_options: List[aspose.words.loading.LoadOptions], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and save options.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param load_options: Load options for the input files.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(input_files: List[str], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_files: The input file names.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(input_files: List[str], load_options: List[aspose.words.loading.LoadOptions], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_files: The input file names.
        :param load_options: Load options for the input files.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: List[io.BytesIO], save_format: aspose.words.SaveFormat) -> None:
        """Merges the given input documents into a single output document using specified input output streams and the final document format.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: List[io.BytesIO], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output streams and save options.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(input_streams: List[io.BytesIO], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_streams: The input streams.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @staticmethod
    def merge_docs(input_documents: List[aspose.words.Document], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_documents: The input documents.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    ...

class MergeFormatMode(Enum):
    """Specifies how formatting is merged when combining multiple documents."""
    
    """Combine the formatting of the merged documents.
    
    By using this option, Aspose.Words adapts the formatting of the first document to match the structure and
    appearance of the second document, but keeps some of the original formatting intact.
    This option is useful when you want to maintain the overall look and feel of the destination document
    but still retain certain formatting aspects from the original document.
    
    This option does not have any affect when the input and the output formats are PDF."""
    MERGE_FORMATTING: int
    
    """Means that the source document will retain its original formatting,
    such as font styles, sizes, colors, indents, and any other formatting elements applied to its content.
    
    By using this option, you ensure that the copied content appears as it did in the original source,
    regardless of the formatting settings of the first document in merge queue.
    
    This option does not have any affect when the input and the output formats are PDF."""
    KEEP_SOURCE_FORMATTING: int
    
    """Preserve the layout of the original documents in the final document.
    
    In general, it looks like you print out the original documents and manually adhere them together using glue."""
    KEEP_SOURCE_LAYOUT: int
    

