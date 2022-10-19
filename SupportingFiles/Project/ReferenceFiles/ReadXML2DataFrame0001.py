import pandas as pd
import xml.etree.ElementTree as ET
import io


def iter_docs(author):
    author_attr = author.attrib
    for doc in author.iter('document'):
        doc_dict = author_attr.copy()
        doc_dict.update(doc.attrib)
        doc_dict['data'] = doc.text
        yield doc_dict

# xml_data = io.StringIO(u'''YOUR XML STRING HERE''')

#etree = ET.parse(xml_data)  # create an ElementTree object
etree = ET.parse("/employee.xml")  # create an ElementTree object

doc_df = pd.DataFrame(list(iter_docs(etree.getroot())))
print(doc_df)