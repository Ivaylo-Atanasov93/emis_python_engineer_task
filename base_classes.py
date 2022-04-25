class Patient:
    def __init__(
            self,
            patient_id,
            meta,
            text,
            extension,
            identifier,
            name,
            telecom,
            gender,
            birth_date,
            deceased_date_time,
            address,
            marital_status,
            multiple_birth,
            communication,
    ):
        self.patient_id = patient_id
        self.meta = meta
        self.text = text
        self.extension = extension
        self.identifier = identifier
        self.name = name
        self.telecom = telecom
        self.gender = gender
        self.birth_date = birth_date
        self.deceased_date_time = deceased_date_time
        self.address = address
        self.marital_status = marital_status
        self.multiple_birth = multiple_birth
        self.communication = communication


class Encounter:
    def __init__(
            self,
            enc_id,
            meta,
            identifier,
            status,
            enc_class,
            enc_type,
            subject,
            participant,
            period,
            location,
            service_provider,
    ):
        self.enc_id = enc_id
        self.meta = meta
        self.identifier = identifier
        self.status = status
        self.enc_class = enc_class
        self.type = enc_type
        self.subject = subject
        self.participant = participant
        self.period = period
        self.location = location
        self.service_provider = service_provider


class Condition:
    def __init__(
            self,
            condition_id,
            meta,
            clinical_status,
            verification_status,
            category,
            code,
            subject,
            encounter,
            onset_date_time,
            recorded_date,
    ):
        self.condition_id = condition_id
        self.meta = meta
        self.clinical_status = clinical_status
        self.verification_status = verification_status
        self.category = category
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.onset_date_time = onset_date_time
        self.recorded_date = recorded_date


class DiagnosticReport:
    def __init__(
            self,
            diagnostic_report_id,
            meta,
            status,
            category,
            code,
            subject,
            encounter,
            effective_date_time,
            issued,
            performer,
            presented_form,
    ):
        self.diagnostic_report_id = diagnostic_report_id
        self.meta = meta
        self.status = status
        self.category = category
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.effective_date_time = effective_date_time
        self.issued = issued
        self.performer = performer
        self.presented_form = presented_form


class DocumentReference:
    def __init__(
            self,
            document_reference_id,
            meta,
            identifier,
            status,
            type,
            subject,
            participant,
            period,
            location,
            service_provider,
    ):
        self.document_reference_id = document_reference_id
        self.meta = meta
        self.identifier = identifier
        self.status = status
        self.type = type
        self.subject = subject
        self.participant = participant
        self.period = period
        self.location = location
        self.service_provider = service_provider


class Claim:
    def __init__(
            self,
            claim_id,
            status,
            type,
            use,
            patient,
            billable_period,
            created,
            provider,
            priority,
            facility,
            diagnosis,
            insurance,
            item,
            total,
    ):
        self.claim_id = claim_id
        self.status = status
        self.type = type
        self.use = use
        self.patient = patient
        self.billable_period = billable_period
        self.created = created
        self.provider = provider
        self.priority = priority
        self.facility = facility
        self.fiagnosis = diagnosis
        self.insurance = insurance
        self.item = item
        self.total = total

class ExplanationOfBenefit:
    def __init__(
            self,
            explanation_id,
            contained,
            identifier,
            status,
            explanation_type,
            use,
            patient,
            billable_period,
            created,
            insurer,
            provider,
            referral,
            facility,
            claim,
            outcome,
            care_team,
            diagnosis,
            insurance,
            item,
            total,
            payment,
    ):
        self.explanation_id = explanation_id
        self.contained = contained
        self.identifier = identifier
        self.status = status
        self.type = explanation_type
        self.use = use
        self.patient = patient
        self.billable_period = billable_period
        self.created = created
        self.insurer = insurer
        self.provider = provider
        self.referral = referral
        self.facility = facility
        self.claim = claim
        self.outcome = outcome
        self.care_team = care_team
        self.diagnosis = diagnosis
        self.insurance = insurance
        self.item = item
        self.total = total
        self.payment = payment


class Observation:
    def __init__(
            self,
            observation_id,
            meta,
            status,
            category,
            code,
            subject,
            encounter,
            effective_date_time,
            issued,
            value_quantity,
    ):
        self.observation_id = observation_id
        self.meta = meta
        self.status = status
        self.category = category
        self.code = code
        self.subject = subject,
        self.encounter = encounter
        self.effective_date_time = effective_date_time
        self.issued = issued
        self.value_quantity = value_quantity


class Procedure:
    def __init__(
            self,
            procedure_id,
            meta,
            status,
            code,
            subject,
            encounter,
            performed_period,
            location,
    ):
        self.procedure_id = procedure_id
        self.meta = meta
        self.status = status
        self.code = code
        self.subject = subject
        self.encounter = encounter
        self.performed_period = performed_period
        self.location = location


class Immunization:
    def __init__(
            self,
            immunization_id,
            meta,
            status,
            vaccine_code,
            patient,
            encounter,
            performed_period,
            location,
    ):
        self.immunization_id = immunization_id
        self.meta = meta
        self.status = status
        self.vaccine_code = vaccine_code
        self.patient = patient
        self.encounter = encounter
        self.performed_period = performed_period
        self.location = location


class MedicationRequest:
    def __init__(
            self,
            medication_request_id,
            meta,
            status,
            subject,
            encounter,
            period,
            participant,
            reason_code,
            managing_organization,
    ):
        self.medication_request_id = medication_request_id
        self.meta = meta
        self.status = status
        self.subject = subject
        self.encounter = encounter
        self.period = period
        self.participant = participant
        self.reason_code = reason_code
        self.managing_organization = managing_organization


class CareTeam:
    def __init__(
            self,
            care_team_id,
            meta,
            status,
            subject,
            encounter,
            period,
            participant,
            reason_code,
            managing_organisation,
    ):
        self.care_team_id = care_team_id
        self.meta = meta
        self.status = status
        self.subject = subject
        self.encounter = encounter
        self.period = period
        self.participant = participant
        self.reason_code = reason_code
        self.managing_organisation = managing_organisation


class ImagingStudy:
    def __init__(
            self,
            imaging_study_id,
            identifier,
            status,
            subject,
            encounter,
            started,
            number_of_series,
            number_of_instances,
            procedure_code,
            location,
            series,
    ):
        self.imaging_study_id = imaging_study_id
        self.identifier = identifier
        self.status = status
        self.subject = subject
        self.encounter = encounter
        self.started = started
        self.number_of_series = number_of_series
        self.number_of_instances = number_of_instances
        self.procedure_code = procedure_code
        self.location = location
        self.series = series


class Medication:
    def __init__(
            self,
            medication_id,
            meta,
            code,
            status,
    ):
        self.medication_id = medication_id
        self.meta = meta
        self.code = code
        self.status = status


class MedicationAdministration:
    def __init__(
            self,
            medication_administration_id,
            status,
            medication_codeable_concept,
            subject,
            context,
            effective_date_time,
            reason_reference,
    ):
        self.medication_administration_id = medication_administration_id
        self.status = status
        self.medication_codeable_concept = medication_codeable_concept
        self.subject = subject
        self.context = context
        self.effective_date_time = effective_date_time
        self.reason_reference = reason_reference


class Provenance:
    def __init__(
            self,
            provenance_id,
            meta,
            target,
            recorded,
            agent,
    ):
        self.provenance_id = provenance_id
        self.meta = meta
        self.target = target
        self.recorded = recorded
        self.agent = agent


class AllergyIntolerance:
    def __init__(
            self,
            allergy_intolerance_id,
            meta,
            clinical_status,
            verification_status,
            allgergy_type,
            category,
            criticality,
            code,
            patient,
            recorded_date,
    ):
        self.allergy_intolerance_id = allergy_intolerance_id
        self.meta = meta
        self.clinical_status = clinical_status
        self.verification_status = verification_status
        self.allergy_type = allgergy_type
        self.category = category
        self.criticality = criticality
        self.code = code
        self.patient = patient
        self.recorded_date = recorded_date


class Device:
    def __init__(
            self,
            device_id,
            meta,
            udi_carrier,
            distinct_identifier,
            manufacture_date,
            expiration_date,
            lot_number,
            serial_number,
            device_name,
            device_type,
            patient,
    ):
        self.device_id = device_id
        self.meta = meta
        self.udi_carrier = udi_carrier
        self.distinct_identifier = distinct_identifier
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date
        self.lot_number = lot_number
        self.serial_number = serial_number
        self.device_name = device_name
        self.device_type = device_type
        self.patient = patient


class SupplyDelivery:
    def __init__(
            self,
            supply_delivery_id,
            status,
            patient,
            supply_delivery_type,
            supplied_item,
            occurrence_date_time,
    ):
        self.supply_delivery_id = supply_delivery_id
        self.status = status
        self.patient = patient
        self.supply_delivery_id = supply_delivery_id
        self.supply_delivery_type = supply_delivery_type
        self.supplied_item = supplied_item
        self.occurrence_date_time = occurrence_date_time


