import tabloo
import pandas as pd

from os import listdir

folder_path = 'sample_files/'
file_names = [file for file in listdir(folder_path)]
print(f'THOSE ARE ALL THE FILES: {file_names}')

for counter, file in enumerate(file_names):
    file_name = f'{folder_path}{file}'
    with open(file_name, 'r', encoding="utf-8") as json_file:
        content = pd.read_json(json_file)
        content = content['entry']
        for entry in content:
            entry = pd.json_normalize(entry)
            # tabloo.show(entry)
            print(f'This is the file: {entry["resource.resourceType"]}')
        # for x in content['entry']:
        #     info = x['resource']['resourceType']
        #     categories.add(info)


# import json
# from os import listdir
#
# folder_path = 'sample_files/'
# file_names = [file for file in listdir(folder_path)]
# print(f'THOSE ARE ALL THE FILES: {file_names}')
# categories = set()
# sub_categories_set = set()
# categories_dict = {
#     'ExplanationOfBenefit': False,
#     'Claim': False,
#     'Encounter': False,
#     'Observation': False,
#     'Patient': False,
#     'Immunization': False,
#     'MedicationRequest': False,
#     'Provenance': False,
#     'MedicationAdministration': False,
#     'CarePlan': False,
#     'DiagnosticReport': False,
#     'Device': False,
#     'ImagingStudy': False,
#     'SupplyDelivery': False,
#     'Medication': False,
#     'Procedure': False,
#     'Condition': False,
#     'AllergyIntolerance': False,
#     'CareTeam': False,
#     'DocumentReference': False,
# }
#
# for counter, file in enumerate(file_names):
#     file_name = f'{folder_path}{file}'
#     with open(file_name, 'r', encoding="utf-8") as json_file:
#         content = json.loads(json_file.read())
#     for x in content['entry']:
#         info = x['resource']['resourceType']
#         categories.add(info)
# print(f'THOSE ARE ALL THE DIFFERENT CATEGORIES WE HAVE: {len(categories)}')
# [print(f'CATEGORY: {category}') for category in categories]
#
# for counter, file in enumerate(file_names):
#     file_name = f'{folder_path}{file}'
#     with open(file_name, 'r', encoding="utf-8") as json_file:
#         content = json.loads(json_file.read())
#
#     for x in content['entry']:
#         info = x['resource']['resourceType']
#         if not categories_dict[info]:
#             x["resource"]['resourceType'] = x["resource"]['resourceType'].zfill(30).replace('0', ' ' )
#             [sub_categories_set.add(y) for y in x["resource"].keys()]
#             print(f'THIS IS THE RESOURCE AS TEXT: {x["resource"]["resourceType"]}: {x["resource"].keys()}')
#             categories_dict[info] = True
#     print()
#
# [print(f'KEY: {key}') for key in sub_categories_set]
# print(f'LENGTH: {len(sub_categories_set)}')
# MAIN_PATIENT_KEYS = ['resourceType', 'type', 'entry']

# # resourceType = Bundle
# # type = transaction
#
# #
# # import json
# #
# # from types import SimpleNamespace
# #
# # file_name = 'sample_files/test_4.json'
# #
# # with open(file_name, 'r') as json_file:
# #     content = json.loads(json_file.read())
# #
# # patient = json.dumps(content)
# # final_patient = json.loads(patient, object_hook=lambda d: SimpleNamespace(**d))
# #
# # # print(f'THOSE ARE THE PATIENT KEYS: {content["entry"]}')
# # print(f'THIS IS THE PATIENT OBJECT: {final_patient} TYPE: {type(final_patient)}')
# #
# # MAIN_PATIENT_KEYS = ['resourceType', 'type', 'entry']
# #
# # # resourceType = Bundle
# # # type = transaction
# # # entry = list length = 308
