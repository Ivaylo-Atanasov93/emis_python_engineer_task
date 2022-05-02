# FHIR.json parser

Many thanks to https://github.com/nazrulworld/fhir.resources

The target of this project is to parse raw FHIR Patient messages into a tabular format.

Installation:

I will assume that you already have Python and pip installed on your device

 - run "git clone git@github.com:Ivaylo-Atanasov93/emis_python_engineer_task.git"
 - run "pip install -r requirements.txt"

Project structure:
    
    Currently the project is set to read the raw data from JSON files that you will find in the 'sample_files/' folder.
    The credentials for the data base should be stored in a credentials.py file in the working directory of the project (You will not find this file in the project as it is parf from the .gitignore file).
      - The credentials are saved as variables, the names of which you can find in the main.py file as imports.
 
How the project works:
  
    In the main.py file you will find initialized Worker class that takes as attributes:
        - path to the source folder from where it`s going to take the information
        - path to the output folder where you would like to save your .csv files if you wish to save the results as files
        - export_as variable that states the export type, currently there are two methods: saving as .csv files or saving in postgresql data base.
        
    After the class is initialized all you need to do is to call the collect_info() function and wait four your data to be transformed.
    
Architecture:

     The project contains 4 different files, and each of them stores a single class.
        - bundle_parser.py : This file takes care for the different resource types that the bundle contains. It contains a  class that uses a bunch of data classes from the fhir.resources package which are implemented with pydantic.
        - table_representations.py contains 20 main resource type dataframe templates and 21 subtype templates.
        - extractor.py : This one is "the heavy lifter" in the project. Contains implementation for translation for all the resource types I found in the data folder of the task repository. Uses pandas to create table represenations and then concatenates the collected information with the templates from the table_representations.py file.
        - worker.py takes care of the iteration of the files and the saving functionality.



P.S Docker is not yet configured as I never worked with it and I had some issues with it.
        
      
        
