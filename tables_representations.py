import pandas as pd


ALLERGY_INTOLERANCE = pd.DataFrame(
    columns=[
        'AllergyIntoleranceUID',
        'Type',
        'Category',
        'Criticality',
        'Patient',
        'EncounterReference',
        'RecordedDate',
    ]
)

CARE_PLAN = pd.DataFrame(
    columns=[
        'CarePlanUID',
        'Status',
        'Intent',
        'CategoryText',
        'SubjectReference',
        'EncounterReference',
        'PeriodStart',
        'PeriodEnd',
        'CareTeamReference'
        'AddressReference',
    ]
)

CARE_TEAM = pd.DataFrame(
    columns=[
        'CareTeamUID',
        'Status',
        'SubjectReference',
        'EncounterReference',
        'PeriodStart',
        'PeriodEnd',
        'Note',
    ]
)

CLAIM = pd.DataFrame(
    columns=[
        'ClaimUID',
        'Status',
        'Use',
        'PatientReference',
        'PatientDisplay',
        'BillablePeriodStart',
        'BillablePeriodEnd',
        'Created',
        'ProviderReference',
        'ProviderDisplay',
        'FacilityReference',
        'FacilityDisplay',
        'TotalValue',
        'TotalCurrency',
    ]
)

CONDITION = pd.DataFrame(
    columns=[
        'ConditionUID',
        'CodeText'
        'Severity',
        'SubjectReference',
        'EncounterReference'
        'OnSetDateTime',
        'AbatementDateTime',
        'RecordedDate',
    ]
)

DEVICE = pd.DataFrame(
    columns=[
        'DeviceUID',
        'Status',
        'Manufacturer',
        'ManufactureDate',
        'ExpirationDate',
        'LotNumber',
        'SerialNumber',
        'DeviceName',
        'DeviceNameType',
        'DeviceTypeText',
        'PatientReference',
    ]
)

DIAGNOSTIC_REPORT = pd.DataFrame(  # ______________________________________Done
    columns=[
        'DiagnosticReportUID',
        'Status',
        'PatientReference',
        'EncounterReference',
        'EffectiveDateTime',
        'IssuedDateTime',
        'Conclusion',
    ]
)

DOCUMENT_REFERENCE = pd.DataFrame(
    columns=[
        'DocumentReferenceUID',
        'Status',
        'SubjectReference',
        'Date',
        'AuthorReference',
        'AuthorDisplay',
        'CustodianReference',
        'CustodianDisplay',
        'EncounterReference',
        'ContentAttachmentType'
        'ContentAttachmentData',
        'FormatDisplay',
        'ContentType',
        'ContentData',
        'ContextEncounter',
        'ContextPeriodStart',
        'ContextPeriodEnd',
    ]
)

ENCOUNTER = pd.DataFrame(
    columns=[
        'EncounterUID',
        'Status',
        'SubjectReference',
        'SubjectDisplay',
        'ParticipantType',
        'ParticipantName',
        'ParticipantReference',
        'PeriodStart',
        'PeriodEnd',
        'LocationReference',
        'LocationDisplay',
        'ServiceProviderReference',
        'ServiceProviderDisplay',
    ]
)

EXPLANATION_OF_BENEFIT = pd.DataFrame(
    columns=[
        'ExplanationOfBenefitUID',
        'Status',
        'Use',
        'PatientReference',
        'BillablePeriodStart',
        'BillablePeriodEnd',
        'CreatedDate',
        'InsurerDisplay',
        'ProviderReference',
        'ReferralReference',
        'FacilityReference',
        'FacilityDisplay',
        'ClaimReference',
        'OutcomeStatus',
        'CareTeamProviderReference',
        'CareTeamRoleDisplay',
        'TotalText',
        'TotalAmountValue',
        'TotalCurrency',
        'PaymentAmountValue',
        'PaymentCurrency',
    ]
)

IMAGING_STUDY = pd.DataFrame(
    columns=[
        'ImagingStudyUID',
        'Status',
        'SubjectReference',
        'EncounterReference',
        'Started',
        'NumberOfSeries',
        'NumberOfInstances',
        'LocationReference',
        'LocationDisplay',
    ]
)

IMMUNIZATION = pd.DataFrame(
    columns=[
        'ImmunizationUID',
        'Status',
        'VaccineCodeText',
        'PatientReference',
        'EncounterReference',
        'OccurrenceDateTime',
        'PrimarySource',
        'LocationReference',
        'LocationDisplay',
    ]
)

MEDICATION = pd.DataFrame(  # _____________________________________________Done
    columns=[
        'MedicationUID',
        'CodeText'
        'Status',
    ]
)

ITEM = pd.DataFrame(
    columns=[
        'Reference',
        'Sequence',
        'DiagnosticSequence'
        'productOrServiceText',
        'ServicePeriodStart',
        'ServicePeriodEnd',
        'EncounterReference',
    ]
)

MEDICATION_ADMINISTRATION = pd.DataFrame(
    columns=[
        'MedicationAdministrationUID',
        'Status',
        'SubjectReference',
        'ContextReference',
        'EffectiveDateTime',
        'ReasonReference',
    ]
)

MEDICATION_REQUEST = pd.DataFrame(  # _____________________________________Done
    columns=[
        'MedicationRequestUID',
        'Status',
        'Intent',
        'SubjectReference',
        'EncounterReference',
        'AuthoredOn',
        'RequesterReference',
        'RequesterDisplay',
        'ReasonReference',
    ]
)

OBSERVATION = pd.DataFrame(  # ____________________________________________Done
    columns=[
        'ObservationUID',
        'Status',
        'SubjectReference',
        'EncounterReference',
        'EffectiveDateTime',
        'Issued',
        'ValueQuantityValue',
        'ValueQuantityUnit',
        'ValueQuantitySystem',
        'ValueQuantityCode',
    ]
)

PATIENT = pd.DataFrame(  # ________________________________________________Done
    columns=[
        'PatientUID',
        'TextStatus',
        'TextDiv',
        'Gender',
        'DateOfBirth',
        'Deceased',
        'MartialStatusText'
        'MultipleBirth',
        'GeneralPractitioner',
        'ManagingOrganisation'
    ]
)

PROCEDURE = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'ProcedureUID',
        'Status',
        'SubjectReference',
        'EncounterReference',
        'PerformedPeriodStart',
        'PerformedPeriodEnd',
        'LocationReference',
        'LocationDisplay',
    ]
)

PROVENANCE = pd.DataFrame(  # _____________________________________________Done
    columns=[
        'ProvenanceID',
        'Recorded',
    ]
)

SUPPLY_DELIVERY = pd.DataFrame(  # ________________________________________Done
    columns=[
        'SupplyDeliveryUID',
        'Status',
        'PatientReference',
        'SuppliedItemQuantity',
        'SuppliedItemText',
        'OccurrenceDateTime',
    ]
)

NUMBER_OF_INSTANCES = pd.DataFrame(  # ____________________________________Done
    columns=[
        'Reference',
        'InstanceUID',
        'SopClassSystem',
        'SopClassCode',
        'Number',
        'Title',
    ]
)

EXTENSION = pd.DataFrame(
    columns=[
        'Reference',
        'Url',
        'ValueString',
        'valueDecimal',
        'ValueAddressCity',
        'ValueAddressState',
        'ValueAddressCountry',
    ]
)

DIAGNOSIS = pd.DataFrame(
    columns=[
        'Reference',
        'Sequence',
        'DiagnosisReference',
    ]
)

INSURANCE = pd.DataFrame(
    columns=[
        'Reference',
        'Sequence',
        'Focal',
        'CoverageReference',
        'CoverageDisplay',
    ]
)

AGENT = pd.DataFrame(
    columns=[
        'Reference',
        'TypeText',
        'AgentsWhoReference',
        'AgentsWhoDisplay',
        'AgentsOnBehalfOfReference',
        'AgentsOnBehalvOfDisplay',
    ]
)

CODE = pd.DataFrame(
    columns=[
        'Reference',
        'Type'
        'System',
        'Code',
        'Display',
    ]
)

ACTIVITIES = pd.DataFrame(
    columns=[
        'Reference',
        'DetailText',
        'Status',
        'LocationDisplay',
    ]
)

ADDRESS = pd.DataFrame(
    columns=[
        'Reference',
        'Line',
        'City',
        'State',
        'PostalCode',
        'Country',
    ]
)

CONTAINED = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'Reference',
        'ResourceType',
        'ResourceID',
        'Status',
        'Intent',
        'Subject',
        'Requester',
        'Performer',
        'Payor',
    ]
)

NAME = pd.DataFrame(  # ___________________________________________________Done
    columns=[
        'Reference',
        'Use',
        'Family',
        'Given',
        'Prefix',
    ]
)

REACTION = pd.DataFrame(
    columns=[
        'Reference',
        # Manifestation -> Coding
        'ReactionText',
        'Severity',
    ]
)

DOSAGE_INSTRUCTION = pd.DataFrame(  # _____________________________________Done
    columns=[
        'Reference',
        'Sequence',
        'Text',
        'AsNeededBoolean',
    ]
)

IDENTIFIER = pd.DataFrame(  # _____________________________________________Done
    columns=[
        'Reference',
        'System',
        'Value',
    ]
)

TELECOM = pd.DataFrame(
    columns=[
        'Reference',
        'System',
        'Value',
        'Use',
    ]
)

MANAGING_ORGANIZATION = pd.DataFrame(  # __________________________________Done
    columns=[
        'Reference',
        'ManagingOrganizationReference',
        'ManagingOrganizationDisplay',
    ]
)

FORM = pd.DataFrame(
    columns=[
        'Reference',
        'ContentType',
        'Data',
    ]
)

# ROLES = pd.DataFrame(  # ______________________________________________NOT Done
#     columns=[
#         'Reference',
#         # Coding -> Coding
#         'RoleText',
#         'MemberReference',
#         'MemberDisplay',
#     ]
# )

CATEGORY = pd.DataFrame(  # _______________________________________________Done
    columns=[
        'Reference',
        'Category',
    ]
)

UDI_CARRIER = pd.DataFrame(
    columns=[
        'Reference',
        'DeviceIdentifier',
        'CarierHRF',
    ]
)

TARGET = pd.DataFrame(  # _________________________________________________Done
    columns=[
        'Reference',
        'TargetReference',
    ]
)

REASON_REFERENCE = pd.DataFrame(  # _______________________________________Done
    columns=[
        'Reference',
        'ReasonReference',
    ]
)

COMMUNICATION = pd.DataFrame(
    columns=[
        'Reference',
        'LanguageText',
    ]
)

PERFORMER = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'Reference',
        'PerformerReference',
        'PerformerDisplay',
    ]
)

PARTICIPANT = pd.DataFrame(
    columns=[
        'Reference',
        'RoleText',
        'MemberReference',
        'MemberDisplay',
    ]
)