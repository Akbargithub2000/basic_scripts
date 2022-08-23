import docx as doc

def Read_Docx(filename):
    doc = doc.Document(filename)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return text

Read_Docx('')