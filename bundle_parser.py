from fhir.resources.patient import Patient
from fhir.resources.documentreference import DocumentReference
from fhir.resources.device import Device
from fhir.resources.careplan import CarePlan
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.imagingstudy import ImagingStudy
from fhir.resources.condition import Condition
from fhir.resources.explanationofbenefit import ExplanationOfBenefit
from fhir.resources.observation import Observation
from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.careteam import CareTeam
from fhir.resources.procedure import Procedure
from fhir.resources.claim import Claim
from fhir.resources.provenance import Provenance
from fhir.resources.medicationadministration import MedicationAdministration
from fhir.resources.encounter import Encounter
from fhir.resources.medication import Medication
from fhir.resources.supplydelivery import SupplyDelivery
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.immunization import Immunization


class FhirJsonParser:
    def __init__(self):
        self.entry_creation = {
            "AllergyIntolerance": AllergyIntolerance,
            "CarePlan": CarePlan,
            "CareTeam": CareTeam,
            "Claim": Claim,
            "Condition": Condition,
            "Device": Device,
            "DiagnosticReport": DiagnosticReport,
            "DocumentReference": DocumentReference,
            "Encounter": Encounter,
            "ExplanationOfBenefit": ExplanationOfBenefit,
            "ImagingStudy": ImagingStudy,
            "Immunization": Immunization,
            "Medication": Medication,
            "MedicationAdministration": MedicationAdministration,
            "MedicationRequest": MedicationRequest,
            "Observation": Observation,
            "Patient": Patient,
            "Procedure": Procedure,
            "Provenance": Provenance,
            "SupplyDelivery": SupplyDelivery,
        }

    def create_entry(self, **entry):
        entry_type = entry['resourceType']
        try:
            return self.entry_creation[entry_type](**entry)
        except KeyError as error:
            print(f'UNKNOWN Type of fhir.resources... Type: {error}')
