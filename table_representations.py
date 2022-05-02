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

MEDICATION = pd.DataFrame(
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

MEDICATION_REQUEST = pd.DataFrame(
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

OBSERVATION = pd.DataFrame(
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

PATIENT = pd.DataFrame(
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

PROCEDURE = pd.DataFrame(
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

PROVENANCE = pd.DataFrame(
    columns=[
        'ProvenanceID',
        'Recorded',
    ]
)

SUPPLY_DELIVERY = pd.DataFrame(
    columns=[
        'SupplyDeliveryUID',
        'Status',
        'PatientReference',
        'SuppliedItemQuantity',
        'SuppliedItemText',
        'OccurrenceDateTime',
    ]
)

EXTENSION = pd.DataFrame(
    columns=[
        'Reference',
        'Url',
        'ValueString',
        'valueDecimal',
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

CONTAINED = pd.DataFrame(
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

NAME = pd.DataFrame(
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
        'ReactionText',
        'Severity',
    ]
)

DOSAGE_INSTRUCTION = pd.DataFrame(
    columns=[
        'Reference',
        'Sequence',
        'Text',
        'AsNeededBoolean',
    ]
)

IDENTIFIER = pd.DataFrame(
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

MANAGING_ORGANIZATION = pd.DataFrame(
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

UDI_CARRIER = pd.DataFrame(
    columns=[
        'Reference',
        'DeviceIdentifier',
        'CarierHRF',
    ]
)

TARGET = pd.DataFrame(
    columns=[
        'Reference',
        'TargetReference',
    ]
)

COMMUNICATION = pd.DataFrame(
    columns=[
        'Reference',
        'LanguageText',
    ]
)

PERFORMER = pd.DataFrame(
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
