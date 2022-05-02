import pandas as pd


ALLERGY_INTOLERANCE = pd.DataFrame(  # ____________________________________Done
    columns=[
        'AllergyIntoleranceUID',
        'Type',
        'Category',
        'Criticality',
        'Patient',
        'EncounterReference',
        # Reaction -> Reaction
        'RecordedDate',
        'LastOccurance',
        'Note',
        # VerificationStatus -> Coding
        # ClinicalStatus -> Coding
        # Code -> Coding
        # ReactionManifestation -> Coding
    ]
)

CARE_PLAN = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'CarePlanUID',
        'Status',
        'Intent',
        # CategoryCode -> Coding
        'CategoryText',
        'SubjectReference',
        'EncounterReference',
        'PeriodStart',
        'PeriodEnd',
        'CareTeamReference'
        'AddressReference',
        # Activities -> Activities
    ]
)

CARE_TEAM = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'CareTeamUID',
        'Status',
        'SubjectReference',
        'EncounterReference',
        'PeriodStart',
        'PeriodEnd',
        # Participants -> Role
        # ReasonCode -> Coding
        # ManagingOrganization -> Managing Organization
        # Telecom -> Coding
        'Note',
    ]
)

CLAIM = pd.DataFrame(  # __________________________________________________Done
    columns=[
        'ClaimUID',
        'Status',
        # Type -> Coding
        'Use',
        'PatientReference',
        'PatientDisplay',
        'BillablePeriodStart',
        'BillablePeriodEnd',
        'Created',
        'ProviderReference',
        'ProviderDisplay',
        # PriorityCode -> Coding
        # Insurance -> Insurance
        'FacilityReference',
        'FacilityDisplay',
        # Diagnosis -> Diagnosis
        # Item -> Item
        'TotalValue',
        'TotalCurrency',
    ]
)

CONDITION = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'ConditionUID',
        # ClinicalStatusCode -> Coding
        # VerificationStatusCode -> Coding
        # Category -> Coding
        # Coding -> Coding
        'CodeText'
        'Severity',
        'SubjectReference',
        'EncounterReference'
        'OnSetDateTime',
        'AbatementDateTime',
        'RecordedDate',
    ]
)

DEVICE = pd.DataFrame(  # _________________________________________________Done
    columns=[
        'DeviceUID',
        # UdiCarrier -> Udi_Carrier,
        'Status',
        'Manufacturer',
        'ManufactureDate',
        'ExpirationDate',
        'LotNumber',
        'SerialNumber',
        'DeviceName',
        'DeviceNameType',
        # DeviceType -> Coding
        'DeviceTypeText',
        'PatientReference',
    ]
)

DIAGNOSTIC_REPORT = pd.DataFrame(  # ______________________________________Done
    columns=[
        'DiagnosticReportUID',
        'Status',
        # CategoryCodes -> Coding
        # CodeCoding -> Coding
        'PatientReference',
        'EncounterReference',
        'EffectiveDateTime',
        'IssuedDateTime',
        'PerformerReference',
        'PerformerDisplay',
        # PresentedForm -> Form
        'Conclusion',
    ]
)

DOCUMENT_REFERENCE = pd.DataFrame(  # _____________________________________Done
    columns=[
        'DocumentReferenceUID',
        # Identifier -> Identifier
        'Status',
        # DocumentType -> Coding
        # CategoryCoding -> Coding
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

ENCOUNTER = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'EncounterUID',
        'Status',
        'ClassSystem',
        'ClassCode',
        # TypeCode -> Coding
        'SubjectReference',
        'SubjectDisplay',
        'ParticipantType',
        'ParticipantName',
        'ParticipantReference'
        'PeriodStart',
        'PeriodEnd',
        'LocationReference',
        'LocationDisplay',
        'ServiceProviderReference',
        'ServiceProviderDisplay',
    ]
)

EXPLANATION_OF_BENEFIT = pd.DataFrame(  # _________________________________Done
    columns=[
        'ExplanationOfBenefitUID',
        # Identifier -> Identifier
        'Status',
        # TypeCoding -> Coding
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

IMAGING_STUDY = pd.DataFrame(  # __________________________________________Done
    columns=[
        'ImagingStudyUID',
        # Identifier, -> Identifier
        'Status',
        'SubjectReference',
        'EncounterReference',
        'Started',
        'NumberOfSeries',
        'NumberOfInstances',
        # ProcedureCode -> Coding
        'LocationReference',
        'LocationDisplay',
    ]
)

IMMUNIZATION = pd.DataFrame(  # ___________________________________________Done
    columns=[
        'ImunizationUID',
        'Status',
        # VaccineCode  -> Coding
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
        # Code     -> Coding
        'CodeText'
        'Status',
    ]
)

ITEM = pd.DataFrame(
    columns=[
        'Reference',
        'Sequence',
        'DiagnosticSequence'
        # CategoryCoding -> Coding
        'productOrServiceText',
        #ProductOfServiceCode -> Coding
        'ServicePeriodStart',
        'ServicePeriodEnd',
        # LocationCodableConcept -> Coding
        'EncounterReference',
    ]
)

MEDICATION_ADMINISTRATION = pd.DataFrame(  # ______________________________Done
    columns=[
        'MedicationAdministrationUID',
        'Status',
        # MedicationCodeableConceptCode -> Coding
        'SubjectReference',
        'ContextReference',
        'EffectiveDateTime',
        'ReasonReference',
        'DosageValue',
        'DosageRateQuantity'
    ]
)

MEDICATION_REQUEST = pd.DataFrame(  # _____________________________________Done
    columns=[
        'MedicationRequestUID',
        'Status',
        'Intent',
        # MedicationCodeableConceptCode -> Coding
        'SubjectReference',
        'EncounterReference',
        'AuthoredOn',
        'RequesterReference',
        'RequesterDisplay',
        'ReasonReference',
        #dosageInstruction -> DosageInstruction
    ]
)

OBSERVATION = pd.DataFrame(  # ____________________________________________Done
    columns=[
        'ObservationUID',
        'Status',
        # Category -> Coding
        # Code     -> Coding
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
        # Extensions -> Extensions
        # Identifier -> Identifier
        # Names -> Names
        # Telecom -> Coding
        'Gender',
        'DateOfBirth',
        'Deceased',
        # Address -> Address,
        'MartialStatusText'
        # MaritalStatus -> Coding,
        'MultipleBirth',
        # Communication -> Communication
        'GeneralPractitioner',
        'ManagingOrganisation'
    ]
)

PROCEDURE = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'ProcedureUID',
        'Status',
        # Code -> Coding
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
        # TargetReferences -> Target
        'Recorded',
        # Agent -> Agent
    ]
)

SUPPLY_DELIVERY = pd.DataFrame(  # ________________________________________Done
    columns=[
        'SupplyDeliveryUID',
        'Status',
        'PatientReference',
        # Type -> Coding,
        'SuppliedItemQuantity',
        'SuppliedItemText',
        # SuppliedItemCode
        'OccuranceDateTime',
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

EXTENSION = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'Reference',
        'Url',
        'ValueString',
        'valueDecimal',
        'ValueAddressCity',
        'ValueAddressState',
        'ValueAddressCountry',
        # ValueCoding -> Coding
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
        # Extension -> Extension
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
        'Beneficiary',
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

ROLES = pd.DataFrame(  # ______________________________________________NOT Done
    columns=[
        'Reference',
        # Coding -> Coding
        'RoleText',
        'MemberReference',
        'MemberDisplay',
    ]
)

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

COMMUNICATION = pd.DataFrame(  # __________________________________________Done
    columns=[
        'Reference',
        'LanguageText',
        # Coding -> Coding  # _____________________________________________Done
    ]
)

PERFORMER = pd.DataFrame(  # ______________________________________________Done
    columns=[
        'Reference',
        'PerformerReference',
        'PerformerDisplay',
    ]
)