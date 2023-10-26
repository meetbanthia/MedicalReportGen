import xml.etree.ElementTree as ET

# Provide the full path to the XML file
def getText(filename):
    # Parse the XML file using the provided path
    tree = ET.parse(f"./ecgen-radiology/{filename}")
    root = tree.getroot()

    # Find the "FINDINGS" text within the "AbstractText" element
    fintxt = ''
    for abstract_text in root.iter("AbstractText"):
        if abstract_text.attrib.get("Label") == "INDICATION":
            temp = abstract_text.text
            fintxt = fintxt + temp.strip()
            if fintxt[-1]!='.':
                fintxt = fintxt + '.'
        elif abstract_text.attrib.get("Label") == "FINDINGS":
            temp = abstract_text.text
            fintxt = fintxt + ' ' + temp.strip()
            if fintxt[-1]!='.':
                fintxt = fintxt + '.'
        elif abstract_text.attrib.get("Label") == "IMPRESSION":
            temp = abstract_text.text
            fintxt = fintxt + ' ' + temp.strip()
            if fintxt[-1]!='.':
                fintxt = fintxt + '.'
            break

    return fintxt
