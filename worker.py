import json
import pandas as pd

from credentials import user, password, db_name, address
from extractor import Extractor
from bundle_parser import FhirJsonParser
from os import listdir
from sqlalchemy import create_engine
from tables_representations import *


from fhir.resources.supplydelivery import SupplyDelivery

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
        self.connection = self.create_connection()
        self.parser = FhirJsonParser()
        self.extractor = Extractor()

    def collect_info(self):
        files = self.get_files()
        for counter, file in enumerate(files):
            file_name = f'{self.source_folder}{file}'
            with open(file_name, 'r', encoding="utf-8") as json_file:
                entries_list = json.loads(json_file.read())['entry']
                for entry in entries_list:
                    entry = self.parser.create_entry(**entry["resource"])
                    self.extractor.extract(entry)

    def get_files(self):
        return [file for file in listdir(self.source_folder)]

    @staticmethod
    def create_connection():
        connection = create_engine(
            f'postgresql://{user}:{password}@{address}/{db_name}'
        )
        return connection

    def save_tables(self, data_frame: pd.DataFrame, export_as="csv",):
        if export_as == "csv":
            data_frame.to_csv(self.export_folder)  # THIS MUST BE A NAME WITH FILE EXTENTION!  # noqa
        elif export_as == "postgresql":
            data_frame.to_sql(name='', con=self.connection, if_exists='append')  # HERE THE TABLE NAME IS MISING!  # noqa
        else:
            data_frame.to_html()


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
