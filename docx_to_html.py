
from spire.doc import *
from spire.doc.common import *
import sys
a = sys.argv[1]
b = sys.argv[1]
# 创建一个 Document 对象
document = Document()
# 加载一个 Word DOCX 文档
document.LoadFromFile(a)
# 或加载一个 Word DOC 文档
# document.LoadFromFile("测试.doc")
 
# 设置是否在 HTML 中嵌入图片
document.HtmlExportOptions.ImageEmbedded = True
 
# 设置是否将表单字段导出为纯文本在 HTML 中显示
document.HtmlExportOptions.IsTextInputFormFieldAsText = True
 
# 设置是否在 HTML 中导出页眉和页脚
document.HtmlExportOptions.HasHeadersFooters = False


# 将 Word 文档保存为 HTML 文件
document.SaveToFile(b, FileFormat.Html)
 
document.Close()
