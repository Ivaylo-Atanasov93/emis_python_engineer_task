import json
import tabloo
import pandas as pd

from credentials import user, password
from sqlalchemy import create_engine
from flatten_json import flatten
from os import listdir


class Extractor:
    def __init__(self, path):
        self.folder_path = path
        self.table_names = set()
        self.table_row_names = dict()
        self.engine = self.get_engine()
        self.table_names_dict = dict()

    def get_info(self):
        files = self.get_files()
        for file in files:
            file_name = f'{self.folder_path}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                content = json.loads(json_file.read())['entry']
                self.linked_list = dict()
                for json_object in content:
                    flatten_object = flatten(json_object)
                    table_name = flatten_object['resource_resourceType']
                    if table_name not in self.table_names_dict.keys():
                        self.table_names_dict[table_name] = []
                    self.table_names_dict[table_name].append(
                        flatten_object
                    )
            self.save_object()
        #             table_name = flatten_object['resource_resourceType']
        #             self.table_names.add(table_name)
        #             if table_name not in self.table_row_names.keys():
        #                 self.table_row_names[table_name] = set()
        #             for key in flatten_object.keys():
        #                 self.table_row_names[table_name].add(key)
        # print(f'HERE ARE THE TABLE NAMES: {self.table_names}')
        # [print(f'THIS IS A SINGLE KEY: {item}') for item in self.table_row_names.items()]

    @staticmethod
    def get_files():
        return [file for file in listdir(folder_path)]

    @staticmethod
    def get_engine():
        return create_engine(
            f'postgresql://{user}:{password}@'
            f'localhost:5432/emis_data_engineer_role'
        )

    def save_object(self):
        for key, value in self.table_names_dict.items():
            table_name = key.lower()
            if table_name == 'encounter':
                print(f'THIS IS THE OBJECT I AM APPENDING NOW: {value}')
            df = pd.DataFrame(value)
            df.to_sql(table_name, self.engine, if_exists='append')


folder_path = 'sample_files/'
x = Extractor(folder_path)
x.get_info()

