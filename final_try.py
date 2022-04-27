import json

from credentials import user, password
from os import listdir
from sqlalchemy import create_engine
from table_maker_core.extent_table import ExtentTable
from table_maker_core.table_maker import TableMaker


class Extractor:
    def __init__(self, path):
        self.folder_path = path
        self.table_names = set()
        self.connection = self.create_connection()
        self.tables_list = []

    def collect_info(self):
        files = self.get_files()
        for counter, file in enumerate(files):
            if counter == 2:
                break
            file_name = f'{self.folder_path}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                self.tables_list.append(json.loads(json_file.read())['entry'])
        print(f'The info has been collected...')

    def save_info(self):
        for item in self.tables_list:
            # break
            extent_table = ExtentTable()
            table_maker = TableMaker(extent_table)
            table_maker.convert_json_objects_to_tables(
                item,
                item[0]['resource']['id']
            )
            export_directory = 'output'
            table_maker.save_tables(
                directory=export_directory,
            )

    @staticmethod
    def get_files():
        return [file for file in listdir(folder_path)]

    @staticmethod
    def create_connection():
        connection = create_engine(
            f'postgresql://{user}:{password}@'
            'localhost:5432/emis_data_engineer_role'
        )
        return connection


folder_path = 'sample_files/'
x = Extractor(folder_path)
x.collect_info()
x.save_info()