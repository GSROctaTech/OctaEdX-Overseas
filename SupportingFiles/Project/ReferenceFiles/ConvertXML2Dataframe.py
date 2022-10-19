import pandas as pd
import xml.etree.ElementTree as et


def parse_XML(xml_file, df_cols):
    """Parse the input XML file and store the result in a pandas
    DataFrame with the given columns.

    The first element of df_cols is supposed to be the identifier
    variable, which is an attribute of each node element in the
    XML data; other features will be parsed from the text content
    of each sub-element.
    """

    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    rows = []

    for node in xroot:
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]:
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else:
                res.append(None)
        rows.append({df_cols[i]: res[i]
                     for i, _ in enumerate(df_cols)})

    out_df = pd.DataFrame(rows, columns=df_cols)

    return out_df


df = parse_XML("E:/GSReddy/PythonProjects/SampleData/employee.xml",
               ['id','name','email','password','token','livelng','livelat','livelocation'])

xtree = et.parse("E:/GSReddy/PythonProjects/SampleData/employee.xml")
xroot = xtree.getroot()
print(xroot)
print(df)

for node in xroot:
    s_id = node.attrib.get("id")
    s_name = node.attrib.get("name")
    s_mail = node.find("email")
    s_pwd = node.find("password")
    s_token = node.find("token")
    s_livelng = node.find("livelng").text
    s_livelat = node.find("livelat").text
    s_liveloc = node.find("livelocation")

print(s_id)
