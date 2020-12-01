import os
import csv
import zipfile
import xml.etree.ElementTree as ET
import time

start_time = time.time()
list_of_files = os.listdir(".\zip_folder")

for file in list_of_files:
    with zipfile.ZipFile(os.path.join(".\zip_folder", file), "r") as zipobj:
        for file in zipobj.namelist():
            zipobj.extract(file, ".\zip_folder")
            tree = ET.parse(f"./zip_folder/{file}")
            root = tree.getroot()
            with open("file1.csv", mode="a") as file1:
                file_writer = csv.writer(file1)
                file_writer.writerow([root[0].attrib, root[1].attrib])
            with open("file2.csv", mode="a") as file2:
                file_writer = csv.writer(file2)
                file_writer.writerow([root[0].attrib])
                amount = len(root[2]) - 1
                while amount != -1:
                    file_writer.writerow([root[2][amount].attrib])
                    amount -= 1
            os.remove(f"./zip_folder/{file}")

print("--- %s seconds ---" % (time.time() - start_time))
