import json
import os

list_of_files = os.listdir("D:/test")
my_dict = {
    8697: ["Если это единственный ключ, значит повторений нет :("]
}
result = {}

for files in list_of_files:
    with open(os.path.join("D:/test/", files), 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for products in data["products"]:
            if products["id"] in my_dict:
                my_dict[products["id"]].append(data["name"])
            else:
                my_dict[products["id"]] = [data["name"]]
        for key, value in my_dict.items():
            if len(value) > 1:
                result[key] = value
print(result)
