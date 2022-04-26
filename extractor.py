import json
import tabloo
import pandas as pd
from flatten_json import flatten
from os import listdir


class Extractor:
    def __init__(self, path):
        self.folder_path = path

    def get_info(self):
        files = self.get_files()
        for file in files:
            file_name = f'{self.folder_path}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                content = json.loads(json_file.read())['entry']
                for json_object in content:
                    flatten_object = flatten(json_object)
                    print(flatten_object)

    def get_files(self):
        return [file for file in listdir(folder_path)]

folder_path = 'sample_files/'
x = Extractor(folder_path)
x.get_info()

