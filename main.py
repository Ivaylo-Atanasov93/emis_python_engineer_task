from worker import Worker
from credentials import password, user, address, db_name


if __name__ == '__main__':
    raw_information_json_files_path = 'sample_files/'  # This is a path to the
    # folder that contains the files that we`re going to transform.
    db_credentials = {
        'user': user,
        'password': password,
        'address': address,
        'db_name': db_name,
    }
    output_folder = 'output/'
    export_as_type = 'postgresql'  # DEFAULT = csv
    x = Worker(
        raw_information_json_files_path,
        credentials=db_credentials,
        export_folder=output_folder,
        export_as=export_as_type,
    )
    x.collect_info()
