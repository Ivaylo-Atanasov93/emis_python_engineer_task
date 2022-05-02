import json


from extractor import Extractor
from bundle_parser import FhirJsonParser
from os import listdir
from sqlalchemy import create_engine


class Worker:
    def __init__(
            self,
            source_files_path,
            credentials,
            export_folder='test/',
            export_as='csv',
    ):
        self.user = credentials['user']
        self.password = credentials['password']
        self.address = credentials['address']
        self.db_name = credentials['db_name']
        self.source_folder = source_files_path
        self.export_folder = export_folder
        self.export_as = export_as
        if export_as != 'csv':
            self.connection = self.__create_connection()
        self.parser = FhirJsonParser()
        self.extractor = Extractor()

    def collect_info(self):
        files = self.__get_files()
        print('Reading from files...')
        for counter, file in enumerate(files):
            file_name = f'{self.source_folder}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                entries_list = json.loads(json_file.read())['entry']
                for entry in entries_list:
                    entry = self.parser.create_entry(**entry["resource"])
                    self.extractor.extract(entry)
        self.extractor.convert_to_data_frames()
        print(f'Exporting data...')
        dataframes = self.extractor.convert_to_data_frames()
        self.__save_tables(dataframes, export_as=self.export_as)

    def __get_files(self):
        return [file for file in listdir(self.source_folder)]

    def __create_connection(self):
        user = self.user
        password = self.password
        address = self.address
        db_name = self.db_name
        connection = create_engine(
            f'postgresql://{user}:{password}@{address}/{db_name}'
        )
        return connection

    def __save_tables(self, data_frames_list: list, export_as="csv",):
        if export_as == "csv":
            print(f'Saving into .csv files...')
            for frame in data_frames_list:
                path = f'{self.export_folder}{frame.name}.csv'
                frame.to_csv(path)
        elif export_as == "postgresql":
            print(f'Saving in the DataBase...')
            for count, frame in enumerate(data_frames_list):
                frame.to_sql(
                    name=frame.name,
                    con=self.connection,
                    if_exists='append',
                )
