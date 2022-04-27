import json
import tabloo
import pandas as pd
from flatten_json import flatten
from os import listdir


class Extractor:
    def __init__(self, path):
        self.folder_path = path
        self.table_names = set()
        self.table_row_names = dict()

    def get_info(self):
        files = self.get_files()
        for file in files:
            file_name = f'{self.folder_path}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                content = json.loads(json_file.read())['entry']
                for json_object in content:
                    flatten_object = flatten(json_object)
                    table_name = flatten_object['resource_resourceType']
                    self.table_names.add(table_name)
                    if table_name not in self.table_row_names.keys():
                        self.table_row_names[table_name] = set()
                    for key in flatten_object.keys():
                        self.table_row_names[table_name].add(key)
        print(f'HERE ARE THE TABLE NAMES: {self.table_names}')
        [print(f'THIS IS A SINGLE KEY: {item}') for item in self.table_row_names.items()]

    def get_files(self):
        return [file for file in listdir(folder_path)]

folder_path = 'sample_files/'
x = Extractor(folder_path)
x.get_info()

