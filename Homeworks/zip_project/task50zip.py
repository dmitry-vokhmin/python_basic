import random, string
import os
import xml.etree.ElementTree as gfg
import uuid
from zipfile import ZipFile

def random_unique_str():
    return uuid.uuid1()

def random_number():
    return random.randint(1, 100)

def random_string():
    return "".join(random.choice(string.ascii_letters) for i in range(random.randint(10, 40)))


def generate_xml():
    root = gfg.Element("root")

    unique_str = str(random_unique_str())
    var_id = gfg.Element(f"var name='id' value='{unique_str}'")
    root.append(var_id)

    var_level = gfg.Element(f"var name='level' value='{random_number()}'")
    root.append(var_level)

    objects = gfg.Element("objects")
    root.append(objects)

    amount = random.randint(1, 10)
    while amount:
        object_name = gfg.SubElement(objects, f"object name={random_string()}")
        amount -= 1

    tree = gfg.ElementTree(root)

    with open(f"{unique_str}.xml", "wb") as files:
        tree.write(files)

    return f"{unique_str}.xml"


if __name__ == '__main__':
    zip_amount = 50
    while zip_amount:
        with ZipFile(f"{zip_amount}.zip", "w") as zipobj:
            xml_amount = 100
            while xml_amount:
                xml_file = generate_xml()
                zipobj.write(xml_file)
                os.remove(xml_file)
                xml_amount -= 1
        zip_amount -= 1