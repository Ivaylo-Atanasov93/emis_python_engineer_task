import json
import pandas as pd

from credentials import user, password, db_name, address
from extractor import Extractor
from bundle_parser import FhirJsonParser
from os import listdir
from sqlalchemy import create_engine


class Worker:
    def __init__(
            self,
            source_files_path,
            export_folder=None,
            export_as='csv',
    ):
        self.source_folder = source_files_path
        self.export_folder = export_folder
        self.export_as = export_as
        if export_as != 'csv':
            self.connection = self.create_connection()
        self.parser = FhirJsonParser()
        self.extractor = Extractor()

    def collect_info(self):
        files = self.get_files()
        print('Reading from files...')
        for counter, file in enumerate(files):
            # if counter == 2:
            #     break
            file_name = f'{self.source_folder}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                entries_list = json.loads(json_file.read())['entry']
                for entry in entries_list:
                    entry = self.parser.create_entry(**entry["resource"])
                    self.extractor.extract(entry)
        self.extractor.convert_to_data_frames()
        print(f'Exporting data...')
        dataframes = self.extractor.convert_to_data_frames()
        self.save_tables(dataframes, export_as=self.export_as)

    def get_files(self):
        return [file for file in listdir(self.source_folder)]

    @staticmethod
    def create_connection():
        connection = create_engine(
            f'postgresql://{user}:{password}@{address}/{db_name}'
        )
        return connection

    def save_tables(self, data_frames_list: list, export_as="csv",):
        if export_as == "csv":
            print(f'Saving into .csv files...')
            for frame in data_frames_list:
                path = f'{self.export_folder}{frame.name}.csv'
                frame.to_csv(path)
        elif export_as == "postgresql":
            print(f'Saving in the DataBase...')
            for count, frame in enumerate(data_frames_list):
                print(f'THIS THE {count}th table, Name: {frame.name}')
                frame.to_sql(
                    name=frame.name,
                    con=self.connection,
                    if_exists='append',
                )




raw_information_json_files_path = 'sample_files/'
export_folder = 'output/'  # If we initialise the instance of the class without
# this variable, and we leave the default export_to variable (as a .csv)
# the script will print the values and they will NOT be saved anywhere.
export_as_type = 'postgresql'  # DEFAULT = csv
x = Worker(
    raw_information_json_files_path,
    export_folder,
    export_as_type,
)
x.collect_info()
