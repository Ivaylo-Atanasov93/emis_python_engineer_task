import pandas as pd

from tables_representations import *

class Extractor:
    def __init__(self):
        self.EXTRACT_FUNCTIONS_MAPPER = {
            "AllergyIntolerance": self.__extract_allergy_intolerance,
            "CarePlan": self.__extract_care_plan,
            "CareTeam": self.__extract_care_team,
            "Claim": self.__extract_claim,
            "Condition": self.__extract_condition,
            "Device": self.__extract_device,
            "DiagnosticReport": self.__extract_diagnostic_report,
            "DocumentReference": self.__extract_document_reference,
            "Encounter": self.__extract_encounter,
            "ExplanationOfBenefit": self.__extract_explanation_of_benefit,
            "ImagingStudy": self.__extract_imaging_study,
            "Immunization": self.__extract_immunization,
            "Medication": self.__extract_medication,
            "MedicationAdministration": self.__extract_medication_administration,  # noqa
            "MedicationRequest": self.__extract_medication_request,
            "Observation": self.__extract_observation,
            "Patient": self.__extract_patient,
            "Procedure": self.__extract_procedure,
            "Provenance": self.__extract_provenance,
            "SupplyDelivery": self.__extract_supply_delivery,
        }
        self.allergy_intolerance_cols = {
            'uid': [],
            'type': [],
            'category': [],
            'criticality': [],
            'patient': [],
            'encounter': [],
            'recorded': [],
        }
        self.care_plan_cols = {
            'uid': [],
            'status': [],
            'intent': [],
            'category_text': [],
            'subject': [],
            'encounter': [],
            'period_start': [],
            'period_end': [],
            'care_team': [],
            'address_reference': [],
        }
        self.care_team_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'period_start': [],
            'period_end': [],
            'note': [],
        }
        self.claim_cols = {
            'uid': [],
            'status': [],
            'use': [],
            'patient_ref': [],
            'patient_dis': [],
            'bill_period_start': [],
            'bill_period_end': [],
            'created': [],
            'provider_ref': [],
            'provider_dis': [],
            'facility_ref': [],
            'facility_dis': [],
            'total_value': [],
            'total_currency': [],
        }
        self.condition_cols = {
            'uid': [],
            'code_text': [],
            'severity': [],
            'subject': [],
            'encounter': [],
            'on_set_time': [],
            'abatement_date': [],
            'recorded': [],
        }
        self.device_cols = {
            'uid': [],
            'status': [],
            'manufacturer': [],
            'manufacture_date': [],
            'expiration_date': [],
            'lot_number': [],
            'serial_number': [],
            'device_name': [],
            'name_type': [],
            'type_text': [],
            'patient': [],
        }
        self.diagn_report_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'effective': [],
            'issued': [],
            'performer_ref': [],
            'performer_dis': [],
            'conclusion': [],
        }
        self.document_ref_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'date': [],
            'author_ref': [],
            'author_dis': [],
            'custodian_ref': [],
            'custodian_dis': [],
            'encounter': [],
            'content_attach_type': [],
            'content_attach_data': [],
            'period_start': [],
            'period_end': [],
        }
        self.encounter_cols = {
            'uid': [],
            'status': [],
            'subject_ref': [],
            'subject_dis': [],
            'participant_type': [],
            'participant_name': [],
            'participant_ref': [],
            'period_start': [],
            'period_end': [],
            'location_ref': [],
            'location_dis': [],
            'provider_ref': [],
            'provider_dis': [],
        }
        self.explanation_of_ben_cols = {
            'uid': [],
            'status': [],
            'use': [],
            'patient': [],
            'period_start': [],
            'period_end': [],
            'created': [],
            'insurer': [],
            'provider': [],
            'referral': [],
            'facility_ref': [],
            'facility_dis': [],
            'claim': [],
            'outcome': [],
            'care_team_prov_ref': [],
            'care_team_role_dis': [],
            'total_text': [],
            'total_value': [],
            'total_currency': [],
            'payment_amount': [],
            'payment_currency': [],
        }
        self.imaging_study_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'started': [],
            'num_of_series': [],
            'num_of_instances': [],
            'location_ref': [],
            'location_dis': [],
        }
        self.immunization_cols = {
            'uid': [],
            'status': [],
            'vaccine_code_text': [],
            'patient': [],
            'encounter': [],
            'occurrence': [],
            'primary_source': [],
            'location_ref': [],
            'location_dis': [],
        }
        self.medication_cols = {
            'uid': [],
            'code_text': [],
            'status': [],
        }
        self.med_admin_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'context': [],
            'effective_date': [],
            'reason': [],
        }
        self.med_request_cols = {
            'uid': [],
            'status': [],
            'intent': [],
            'subject': [],
            'encounter': [],
            'authored_on': [],
            'requester_ref': [],
            'requester_dis': [],
            'reason': [],

        }
        self.observation_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'effective_date': [],
            'issued': [],
            'quant_value': [],
            'quant_unit': [],
            'quant_system': [],
            'quant_code': [],
        }
        self.patient_cols = {
            'uid': [],
            'status': [],
            'div': [],
            'gender': [],
            'date_of_birth': [],
            'deceased': [],
            'marital_status': [],
            'multiple_birth': [],
            'general_practitioner': [],
            'managing_organization': [],
        }
        self.procedure_cols = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'period_start': [],
            'period_end': [],
            'location_ref': [],
            'location_dis': [],
        }
        self.provenance_cols = {
            'uid': [],
            'recorded': [],
        }
        self.supply_delivery_cols = {
            'uid': [],
            'status': [],
            'patient': [],
            'item_quantity': [],
            'item_text': [],
            'occurrence': [],
        }
        self.contained_cols = {
            'reference': [],
            'resource_type': [],
            'resource_id': [],
            'status': [],
            'intent': [],
            'subject': [],
            'requester': [],
            'performer': [],
            'payor': [],
        }
        self.item_cols = {
            'reference': [],
            'sequence': [],
            'diagnostic_seq': [],
            'prod_or_serv_text': [],
            'period_start': [],
            'period_end': [],
            'encounter': [],
        }
        self.address_cols = {
            'reference': [],
            'latitude': [],
            'longitude': [],
            'line': [],
            'city': [],
            'state': [],
            'post_code': [],
            'country': [],
        }
        self.agents_cols = {
            'reference': [],
            'type': [],
            'agent_ref': [],
            'agent_dis': [],
            'on_behalf_of_ref': [],
            'on_behalf_of_dis': [],
        }
        self.coding_cols = {
            'reference': [],
            'type': [],
            'system': [],
            'code': [],
            'display': [],
        }
        self.extension_cols = {
            'reference': [],
            'url': [],
            'string': [],
            'decimal': [],
        }
        self.insurance_cols = {
            'reference': [],
            'sequence': [],
            'focal': [],
            'coverage_ref': [],
            'coverage_dis': [],
        }
        self.name_cols = {
            'reference': [],
            'use': [],
            'family': [],
            'given': [],
            'prefix': [],
        }
        self.telecom_cols = {
            'reference': [],
            'system': [],
            'value': [],
            'use': [],
        }
        self.activities_cols = {
            'reference': [],
            'detail': [],
            'status': [],
            'location': [],
        }
        self.dosage_instruction_cols = {
            'reference': [],
            'sequence': [],
            'text': [],
            'as_needed': [],
        }
        self.participant_cols = {
            'reference': [],
            'role_text': [],
            'member_ref': [],
            'member_dis': [],
        }
        self.diagnosis_cols = {
            'reference': [],
            'sequence': [],
            'diagnostic_ref': [],
        }
        self.form_cols = {
            'reference': [],
            'content_type': [],
            'data': [],
        }
        self.identifier_cols = {
            'reference': [],
            'system': [],
            'value': [],
        }
        self.managing_organ_cols = {
            'reference': [],
            'organization_ref': [],
            'organization_dis': [],
        }
        self.performer_cols = {
            'reference': [],
            'performer_ref': [],
            'performer_dis': [],
        }
        self.reaction_cols = {
            'reference': [],
            'reaction_text': [],
            'severity': [],
        }
        self.udi_carrier_cols = {
            'reference': [],
            'device_identifier': [],
            'carrier_hrf': [],
        }
        self.communication_cols = {
            'reference': [],
            'language': [],
        }
        self.target_cols = {
            'reference': [],
            'target_ref': [],
        }

    def extract(self, fhir_object):
        resource_type = fhir_object.resource_type
        self.EXTRACT_FUNCTIONS_MAPPER[resource_type](fhir_object)

    def convert_to_data_frames(self):
        final_data_frames = list()
        info_template_pairs = self.__get_info_template_pairs()
        for info, template, name in info_template_pairs:
            headers = list(template.columns)
            keys = list(info.keys())
            new_data_frame = pd.DataFrame()
            for index, header in enumerate(headers):
                if info[keys[index]]:
                    new_data_frame[header] = info[keys[index]]
            template = pd.concat(
                [template, new_data_frame],
                ignore_index=True,
                axis=0,
            )
            # template.reset_index()
            template.name = name
            final_data_frames.append(template)
        return final_data_frames

    def __extract_allergy_intolerance(self, fhir_object):
        uid = fhir_object.id
        intolerance_type = fhir_object.type
        intolerance_category = fhir_object.category[0]
        criticality = fhir_object.criticality
        patient = fhir_object.patient.reference
        encounter = None
        if fhir_object.encounter:
            encounter = fhir_object.encounter.reference
        recorded_date = fhir_object.recordedDate
        self.allergy_intolerance_cols['uid'].append(uid)
        self.allergy_intolerance_cols['type'].append(intolerance_type)
        self.allergy_intolerance_cols['category'].append(intolerance_category)
        self.allergy_intolerance_cols['criticality'].append(criticality)
        self.allergy_intolerance_cols['patient'].append(patient)
        self.allergy_intolerance_cols['encounter'].append(encounter)
        self.allergy_intolerance_cols['recorded'].append(recorded_date)
        if fhir_object.reaction:
            self.__get_reaction(fhir_object.reaction, uid, )
        self.__get_coding_object(
            fhir_object.clinicalStatus.coding,
            uid,
            'AllergyIntoleranceClinicalStatus',
        )
        self.__get_coding_object(
            fhir_object.verificationStatus.coding,
            uid,
            'AllergyIntoleranceVerificationStatus'
        )
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'AllergyIntoleranceCode',
        )

    def __extract_care_plan(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        intent = fhir_object.intent
        category_text = fhir_object.category[0].text
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        start_period = fhir_object.period.start
        end_period = fhir_object.period.end
        care_team_reference = fhir_object.careTeam[0].reference
        address_reference = None
        if fhir_object.addresses:
            address_reference = fhir_object.addresses[0].reference
        self.care_plan_cols['uid'].append(uid)
        self.care_plan_cols['status'].append(status)
        self.care_plan_cols['intent'].append(intent)
        self.care_plan_cols['category_text'].append(category_text)
        self.care_plan_cols['subject'].append(subject_reference)
        self.care_plan_cols['encounter'].append(encounter_reference)
        self.care_plan_cols['period_start'].append(start_period)
        self.care_plan_cols['period_end'].append(end_period)
        self.care_plan_cols['care_team'].append(care_team_reference)
        self.care_plan_cols['address_reference'].append(address_reference)
        if fhir_object.activity:
            self.__get_activities(fhir_object.activity, uid, )
        for concept in fhir_object.category:
            self.__get_coding_object(concept.coding, uid, 'DiagnosticReport', )

    def __extract_care_team(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        start_period = fhir_object.period.start
        end_period = fhir_object.period.end
        note = fhir_object.note
        self.care_team_cols['uid'].append(uid)
        self.care_team_cols['status'].append(status)
        self.care_team_cols['subject'].append(subject_reference)
        self.care_team_cols['encounter'].append(encounter_reference)
        self.care_team_cols['period_start'].append(start_period)
        self.care_team_cols['period_end'].append(end_period)
        self.care_team_cols['note'].append(note)
        self.__get_participants(fhir_object.participant, uid)
        if fhir_object.reasonCode:
            self.__get_coding_object(
                fhir_object.reasonCode[0].coding,
                uid,
                'CareTeamReason',
            )
        if fhir_object.managingOrganization:
            self.__get_managing_organization(
                fhir_object.managingOrganization,
                uid
            )
        if fhir_object.telecom:
            self.__get_telecom(
                fhir_object.telecom,
                uid,
            )

    def __extract_claim(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        use = fhir_object.use
        patient_reference = fhir_object.patient.reference
        patient_display = fhir_object.patient.display
        billable_period_start = fhir_object.billablePeriod.start
        billable_period_end = fhir_object.billablePeriod.end
        created = fhir_object.created
        provider_reference = fhir_object.provider.reference
        provider_display = fhir_object.provider.display
        total_value = fhir_object.total.value
        currency = fhir_object.total.currency
        facility_reference = None
        facility_display = None
        if fhir_object.facility:
            facility_reference = fhir_object.facility.reference
            facility_display = fhir_object.facility.display
        if fhir_object.diagnosis:
            self.__get_claim_diagnosis(
                fhir_object.diagnosis,
                uid,
            )
        self.claim_cols['uid'].append(uid)
        self.claim_cols['status'].append(status)
        self.claim_cols['use'].append(use)
        self.claim_cols['patient_ref'].append(patient_reference)
        self.claim_cols['patient_dis'].append(patient_display)
        self.claim_cols['bill_period_start'].append(billable_period_start)
        self.claim_cols['bill_period_end'].append(billable_period_end)
        self.claim_cols['created'].append(created)
        self.claim_cols['provider_ref'].append(provider_reference)
        self.claim_cols['provider_dis'].append(provider_display)
        self.claim_cols['facility_ref'].append(facility_reference)
        self.claim_cols['facility_dis'].append(facility_display)
        self.claim_cols['total_value'].append(total_value)
        self.claim_cols['total_currency'].append(currency)
        self.__get_claim_items(fhir_object.item, uid, )
        self.__get_insurance(fhir_object.insurance, uid, )
        self.__get_coding_object(fhir_object.type.coding, uid, 'Claim')
        self.__get_coding_object(fhir_object.priority.coding, uid, 'ClaimPriority')  # noqa

    def __extract_condition(self, fhir_object):
        uid = fhir_object.id
        code_text = fhir_object.code.text
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        severity = fhir_object.severity
        on_set_date_time = fhir_object.onsetDateTime
        abatement_date_time = fhir_object.abatementDateTime
        recorded_date = fhir_object.recordedDate
        self.condition_cols['uid'].append(uid)
        self.condition_cols['code_text'].append(code_text)
        self.condition_cols['severity'].append(severity)
        self.condition_cols['subject'].append(subject_reference)
        self.condition_cols['encounter'].append(encounter_reference)
        self.condition_cols['on_set_time'].append(on_set_date_time)
        self.condition_cols['abatement_date'].append(abatement_date_time)
        self.condition_cols['recorded'].append(recorded_date)
        self.__get_coding_object(
            fhir_object.clinicalStatus.coding,
            uid,
            'ConditionClinicalStatus',
        )
        self.__get_coding_object(
            fhir_object.verificationStatus.coding,
            uid,
            'ConditionVerificationStatus'
        )
        self.__get_coding_object(fhir_object.code.coding, uid, 'ConditionCode')
        for category in fhir_object.category:
            self.__get_coding_object(category.coding, uid, 'ConditionCategory')

    def __extract_device(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        manufacturer = fhir_object.manufacturer
        manufacture_date = fhir_object.manufactureDate
        expiration_date = fhir_object.expirationDate
        lot_number = fhir_object.lotNumber
        serial_number = fhir_object.serialNumber
        device_type_text = fhir_object.type.text
        patient_reference = fhir_object.patient.reference
        device_name = None
        device_name_type = None
        if fhir_object.deviceName:
            device_name = fhir_object.deviceName[0].name
            device_name_type = fhir_object.deviceName[0].type
        self.device_cols['uid'].append(uid)
        self.device_cols['status'].append(status)
        self.device_cols['manufacturer'].append(manufacturer)
        self.device_cols['manufacture_date'].append(manufacture_date)
        self.device_cols['expiration_date'].append(expiration_date)
        self.device_cols['lot_number'].append(lot_number)
        self.device_cols['serial_number'].append(serial_number)
        self.device_cols['device_name'].append(device_name)
        self.device_cols['name_type'].append(device_name_type)
        self.device_cols['type_text'].append(device_type_text)
        self.device_cols['patient'].append(patient_reference)
        self.__get_coding_object(fhir_object.type.coding, uid, 'DeviceType')
        self.__get_udi_carrier(fhir_object.udiCarrier, uid)

    def __extract_diagnostic_report(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        effective_date_time = fhir_object.effectiveDateTime
        issued = fhir_object.issued
        conclusion = fhir_object.conclusion
        self.diagn_report_cols['uid'].append(uid)
        self.diagn_report_cols['status'].append(status)
        self.diagn_report_cols['subject'].append(subject_reference)
        self.diagn_report_cols['encounter'].append(encounter_reference)
        self.diagn_report_cols['effective'].append(effective_date_time)
        self.diagn_report_cols['issued'].append(issued)
        self.diagn_report_cols['conclusion'].append(conclusion)
        if fhir_object.presentedForm:
            self.__get_presented_form(
                fhir_object.presentedForm,
                uid,
            )
        self.__get_performer(
            fhir_object.performer,
            uid,
        )
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'DiagnosticReportCode'
        )
        for category in fhir_object.category:
            self.__get_coding_object(
                category.coding,
                uid,
                'DiagnosticReportCategory',
            )

    def __extract_document_reference(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        date = fhir_object.date
        author_reference = fhir_object.author[0].reference
        author_display = fhir_object.author[0].display
        custodian_reference = fhir_object.custodian.reference
        custodian_display = fhir_object.custodian.display
        encounter_reference = fhir_object.context.encounter[0].reference
        content_type = fhir_object.content[0].attachment.contentType
        data = fhir_object.content[0].attachment.data
        context_start_date = fhir_object.context.period.start
        context_end_date = fhir_object.context.period.end
        self.document_ref_cols['uid'].append(uid)
        self.document_ref_cols['status'].append(status)
        self.document_ref_cols['subject'].append(subject_reference)
        self.document_ref_cols['date'].append(date)
        self.document_ref_cols['author_ref'].append(author_reference)
        self.document_ref_cols['author_dis'].append(author_display)
        self.document_ref_cols['custodian_ref'].append(custodian_reference)
        self.document_ref_cols['custodian_dis'].append(custodian_display)
        self.document_ref_cols['encounter'].append(encounter_reference)
        self.document_ref_cols['content_attach_type'].append(content_type)
        self.document_ref_cols['content_attach_data'].append(data)
        self.document_ref_cols['period_start'].append(context_start_date)
        self.document_ref_cols['period_end'].append(context_end_date)
        self.__get_coding_object(
            fhir_object.type.coding,
            uid,
            'DocumentReferenceType',
        )
        self.__get_identifier(
            fhir_object.identifier,
            uid,
        )
        for category in fhir_object.category:
            self.__get_coding_object(
                category.coding,
                uid,
                'DocumentReferenceCategory',
            )

    def __extract_encounter(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        subject_display = fhir_object.subject.display
        participant_type = fhir_object.participant[0].type[0].text
        participant_name = fhir_object.participant[0].individual.display
        participant_reference = fhir_object.participant[0].individual.reference
        start_period = fhir_object.period.start
        end_period = fhir_object.period.end
        location_reference = fhir_object.location[0].location.reference
        location_display = fhir_object.location[0].location.display
        provider_reference = fhir_object.serviceProvider.reference
        provider_display = fhir_object.serviceProvider.display
        self.encounter_cols['uid'].append(uid)
        self.encounter_cols['status'].append(status)
        self.encounter_cols['subject_ref'].append(subject_reference)
        self.encounter_cols['subject_dis'].append(subject_display)
        self.encounter_cols['participant_type'].append(participant_type)
        self.encounter_cols['participant_name'].append(participant_name)
        self.encounter_cols['participant_ref'].append(participant_reference)
        self.encounter_cols['period_start'].append(start_period)
        self.encounter_cols['period_end'].append(end_period)
        self.encounter_cols['location_ref'].append(location_reference)
        self.encounter_cols['location_dis'].append(location_display)
        self.encounter_cols['provider_ref'].append(provider_reference)
        self.encounter_cols['provider_dis'].append(provider_display)
        for obj_type in fhir_object.type:
            self.__get_coding_object(obj_type.coding, uid, 'EncounterType')

    def __extract_explanation_of_benefit(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        use = fhir_object.use
        patient = fhir_object.patient.reference
        bill_period_start = fhir_object.billablePeriod.start
        bill_period_end = fhir_object.billablePeriod.end
        created = fhir_object.created
        insurer_display = fhir_object.insurer.display
        provider_reference = fhir_object.provider.reference
        referral = fhir_object.referral.reference
        facility_reference = fhir_object.facility.reference
        facility_display = fhir_object.facility.display
        claim = fhir_object.claim.reference
        outcome = fhir_object.outcome
        total = fhir_object.total[0].category.text
        total_value = fhir_object.total[0].amount.value
        total_currency = fhir_object.total[0].amount.currency
        payment_value = fhir_object.payment.amount.value
        payment_currency = fhir_object.payment.amount.currency
        self.explanation_of_ben_cols['uid'].append(uid)
        self.explanation_of_ben_cols['status'].append(status)
        self.explanation_of_ben_cols['use'].append(use)
        self.explanation_of_ben_cols['patient'].append(patient)
        self.explanation_of_ben_cols['period_start'].append(bill_period_start)
        self.explanation_of_ben_cols['period_end'].append(bill_period_end)
        self.explanation_of_ben_cols['created'].append(created)
        self.explanation_of_ben_cols['insurer'].append(insurer_display)
        self.explanation_of_ben_cols['provider'].append(provider_reference)
        self.explanation_of_ben_cols['referral'].append(referral)
        self.explanation_of_ben_cols['facility_ref'].append(facility_reference)
        self.explanation_of_ben_cols['facility_dis'].append(facility_display)
        self.explanation_of_ben_cols['claim'].append(claim)
        self.explanation_of_ben_cols['outcome'].append(outcome)
        self.explanation_of_ben_cols['total_text'].append(total)
        self.explanation_of_ben_cols['total_value'].append(total_value)
        self.explanation_of_ben_cols['total_currency'].append(total_currency)
        self.explanation_of_ben_cols['payment_amount'].append(payment_value)
        self.explanation_of_ben_cols['payment_currency'].append(payment_currency)  # noqa
        self.__get_coding_object(
            fhir_object.type.coding,
            uid,
            'ExplanationOfBenType',
        )
        self.__get_identifier(
            fhir_object.identifier,
            uid,
        )

    def __extract_imaging_study(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter = fhir_object.subject.reference
        started = fhir_object.started
        number_of_series = fhir_object.numberOfSeries
        number_of_instances = fhir_object.numberOfInstances
        location_reference = fhir_object.location.reference
        location_display = fhir_object.location.display
        self.imaging_study_cols['uid'].append(uid)
        self.imaging_study_cols['status'].append(status)
        self.imaging_study_cols['subject'].append(subject_reference)
        self.imaging_study_cols['encounter'].append(encounter)
        self.imaging_study_cols['started'].append(started)
        self.imaging_study_cols['num_of_series'].append(number_of_series)
        self.imaging_study_cols['num_of_instances'].append(number_of_instances)
        self.imaging_study_cols['location_ref'].append(location_reference)
        self.imaging_study_cols['location_dis'].append(location_display)
        for code in fhir_object.procedureCode:
            self.__get_coding_object(code.coding, uid, 'ImagingStudyProcedureCode')  # noqa
        self.__get_identifier(fhir_object.identifier, uid)

    def __extract_immunization(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        vaccine_code_text = fhir_object.vaccineCode.text
        patient_reference = fhir_object.patient.reference
        encounter = fhir_object.encounter.reference
        occurrence_date_time = fhir_object.occurrenceDateTime
        primary_source = fhir_object.primarySource
        location_reference = fhir_object.location.reference
        location_display = fhir_object.location.display
        self.immunization_cols['uid'].append(uid)
        self.immunization_cols['status'].append(status)
        self.immunization_cols['vaccine_code_text'].append(vaccine_code_text)
        self.immunization_cols['patient'].append(patient_reference)
        self.immunization_cols['encounter'].append(encounter)
        self.immunization_cols['occurrence'].append(occurrence_date_time)
        self.immunization_cols['primary_source'].append(primary_source)
        self.immunization_cols['location_ref'].append(location_reference)
        self.immunization_cols['location_dis'].append(location_display)
        self.__get_coding_object(
            fhir_object.vaccineCode.coding,
            uid,
            'ImmunizationVaccineCode',
        )

    def __extract_medication(self, fhir_object):
        uid = fhir_object.id
        medication_code_text = fhir_object.code.text
        status = fhir_object.status
        self.medication_cols['uid'].append(uid)
        self.medication_cols['code_text'].append(medication_code_text)
        self.medication_cols['status'].append(status)
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'MedicationCode',
        )

    def __extract_medication_administration(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        context = fhir_object.context.reference
        effective_date_time = fhir_object.effectiveDateTime
        reason_value = None
        if fhir_object.reasonReference:
            reason_value = fhir_object.reasonReference[0].reference
        self.med_admin_cols['uid'].append(uid)
        self.med_admin_cols['status'].append(status)
        self.med_admin_cols['subject'].append(subject_reference)
        self.med_admin_cols['context'].append(context)
        self.med_admin_cols['effective_date'].append(effective_date_time)
        self.med_admin_cols['reason'].append(reason_value)
        self.__get_coding_object(
            fhir_object.medicationCodeableConcept.coding,
            uid,
            'MedicationAdministrationCode',
        )

    def __extract_medication_request(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        intent = fhir_object.intent
        subject_reference = fhir_object.subject.reference
        encounter = fhir_object.encounter.reference
        authored_on = fhir_object.authoredOn
        requester_reference = fhir_object.requester.reference
        requester_display = fhir_object.requester.display
        reason_reference = None
        if fhir_object.reasonReference:
            reason_reference = fhir_object.reasonReference[0].reference
        self.med_request_cols['uid'].append(uid)
        self.med_request_cols['status'].append(status)
        self.med_request_cols['intent'].append(intent)
        self.med_request_cols['subject'].append(subject_reference)
        self.med_request_cols['encounter'].append(encounter)
        self.med_request_cols['authored_on'].append(authored_on)
        self.med_request_cols['requester_ref'].append(requester_reference)
        self.med_request_cols['requester_dis'].append(requester_display)
        self.med_request_cols['reason'].append(reason_reference)
        if fhir_object.dosageInstruction:
            self.__get_dosage_instruction(
                fhir_object.dosageInstruction,
                uid
            )
        if fhir_object.medicationCodeableConcept:
            self.__get_coding_object(
                fhir_object.medicationCodeableConcept.coding,
                uid,
                'MedicationRequestCode'
            )

    def __extract_observation(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter = fhir_object.encounter.reference
        effective_date_time = fhir_object.effectiveDateTime
        issued = fhir_object.issued
        value_quantity_value = None
        value_quantity_unit = None
        value_quantity_system = None
        value_quantity_code = None
        if fhir_object.valueQuantity:
            value_quantity_value = fhir_object.valueQuantity.value
            value_quantity_unit = fhir_object.valueQuantity.unit
            value_quantity_system = fhir_object.valueQuantity.system
            value_quantity_code = fhir_object.valueQuantity.code
        self.observation_cols['uid'].append(uid)
        self.observation_cols['status'].append(status)
        self.observation_cols['subject'].append(subject_reference)
        self.observation_cols['encounter'].append(encounter)
        self.observation_cols['effective_date'].append(effective_date_time)
        self.observation_cols['issued'].append(issued)
        self.observation_cols['quant_value'].append(value_quantity_value)
        self.observation_cols['quant_unit'].append(value_quantity_unit)
        self.observation_cols['quant_system'].append(value_quantity_system)
        self.observation_cols['quant_code'].append(value_quantity_code)
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'ObservationCode'
        )
        for category in fhir_object.category:
            self.__get_coding_object(
                category.coding,
                uid,
                'ObservationCategory'
            )

    def __extract_patient(self, fhir_object):
        uid = fhir_object.id
        text_status = fhir_object.text.status
        text_div = fhir_object.text.div
        gender = fhir_object.gender
        date_of_birth = fhir_object.birthDate
        deceased_date = fhir_object.deceasedDateTime
        marital_status_text = fhir_object.maritalStatus.text
        multiple_birth = fhir_object.multipleBirthBoolean
        general_practitioner = fhir_object.generalPractitioner
        managing_organization = fhir_object.managingOrganization
        self.patient_cols['uid'].append(uid)
        self.patient_cols['status'].append(text_status)
        self.patient_cols['div'].append(text_div)
        self.patient_cols['gender'].append(gender)
        self.patient_cols['date_of_birth'].append(date_of_birth)
        self.patient_cols['deceased'].append(deceased_date)
        self.patient_cols['marital_status'].append(marital_status_text)
        self.patient_cols['multiple_birth'].append(multiple_birth)
        self.patient_cols['general_practitioner'].append(general_practitioner)
        self.patient_cols['managing_organization'].append(managing_organization)  # noqa
        self.__get_coding_object(
            fhir_object.maritalStatus.coding,
            uid,
            'PatientMaritalStatus'
        )
        self.__get_address(
            fhir_object.address,
            uid
        )
        self.__get_extension(
            fhir_object.extension,
            uid,
        )
        self.__get_identifier(
            fhir_object.identifier,
            uid,
        )
        self.__get_names(
            fhir_object.name,
            uid
        )
        self.__get_telecom(
            fhir_object.telecom,
            uid,
        )

    def __extract_procedure(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.subject.reference
        performed_period_start = fhir_object.performedPeriod.start
        performed_period_end = fhir_object.performedPeriod.end
        location_reference = fhir_object.location.reference
        location_display = fhir_object.location.display
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'ProcedureCode'
        )
        self.procedure_cols['uid'].append(uid)
        self.procedure_cols['status'].append(status)
        self.procedure_cols['subject'].append(subject_reference)
        self.procedure_cols['encounter'].append(encounter_reference)
        self.procedure_cols['period_start'].append(performed_period_start)
        self.procedure_cols['period_end'].append(performed_period_end)
        self.procedure_cols['location_ref'].append(location_reference)
        self.procedure_cols['location_dis'].append(location_display)

    def __extract_provenance(self, fhir_object):
        uid = fhir_object.id
        recorded = fhir_object.recorded
        self.__get_target_references(
            fhir_object.target,
            uid
        )
        self.__get_agents(
            fhir_object.agent,
            uid,
        )
        self.provenance_cols['uid'].append(uid)
        self.provenance_cols['recorded'].append(recorded)

    def __extract_supply_delivery(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        patient_reference = fhir_object.patient.reference
        supplied_item_quantity = fhir_object.suppliedItem.quantity.value
        supplied_item_text = fhir_object.suppliedItem.itemCodeableConcept.text
        occurrence_date_time = fhir_object.occurrenceDateTime
        self.supply_delivery_cols['uid'].append(uid)
        self.supply_delivery_cols['status'].append(status)
        self.supply_delivery_cols['patient'].append(patient_reference)
        self.supply_delivery_cols['item_quantity'].append(supplied_item_quantity)  # noqa
        self.supply_delivery_cols['item_text'].append(supplied_item_text)
        self.supply_delivery_cols['occurrence'].append(occurrence_date_time)
        self.__get_coding_object(
            fhir_object.suppliedItem.itemCodeableConcept.coding,
            uid,
            'SuppliedItemCoding'
        )
        self.__get_coding_object(
            fhir_object.type.coding,
            uid,
            'SupplyDeliveryType',
        )

    def __get_coding_object(self, coding_objects_list, reference, code_type):
        for coding in coding_objects_list:
            system = coding.system
            code = coding.code
            display = coding.display
            self.coding_cols['reference'].append(reference)
            self.coding_cols['type'].append(code_type)
            self.coding_cols['system'].append(system)
            self.coding_cols['code'].append(code)
            self.coding_cols['display'].append(display)

    def __get_reaction(self, reaction_list, reference):
        for reaction in reaction_list:
            reaction_text = reaction.manifestation[0].text
            severity = reaction.severity
            self.__get_coding_object(
                reaction.manifestation[0].coding,
                reference,
                'Reaction',
            )
            self.reaction_cols['reference'].append(reference)
            self.reaction_cols['reaction_text'].append(reaction_text)
            self.reaction_cols['severity'].append(severity)

    def __get_activities(self, activities, reference):
        for activity in activities:
            detail_text = activity.detail.code.text
            status = activity.detail.status
            location = activity.detail.location.display
            self.__get_coding_object(
                activity.detail.code.coding,
                reference,
                'Activity'
            )
            self.activities_cols['reference'].append(reference)
            self.activities_cols['detail'].append(detail_text)
            self.activities_cols['status'].append(status)
            self.activities_cols['location'].append(location)

    def __get_participants(self, participants, reference):
        for participant in participants:
            role_text = participant.role[0].text
            member_reference = participant.member.reference
            member_display = participant.member.display
            self.participant_cols['reference'].append(reference)
            self.participant_cols['role_text'].append(role_text)
            self.participant_cols['member_ref'].append(member_reference)
            self.participant_cols['member_dis'].append(member_display)
            self.__get_coding_object(
                participant.role[0].coding,
                reference,
                'Participant'
            )

    def __get_telecom(self, telecom_list, reference):
        for telecom in telecom_list:
            system = telecom.system
            value = telecom.value
            use = telecom.use
            self.telecom_cols['reference'].append(reference)
            self.telecom_cols['system'].append(system)
            self.telecom_cols['value'].append(value)
            self.telecom_cols['use'].append(use)

    def __get_insurance(self, insurance_list, reference):
        for insurance in insurance_list:
            sequence = insurance.sequence
            focal = insurance.focal
            coverage_reference = insurance.coverage.reference
            coverage_display = insurance.coverage.display
            self.insurance_cols['reference'].append(reference)
            self.insurance_cols['sequence'].append(sequence)
            self.insurance_cols['focal'].append(focal)
            self.insurance_cols['coverage_ref'].append(coverage_reference)
            self.insurance_cols['coverage_dis'].append(coverage_display)

    def __get_items(self, items_list, reference):
        for item in items_list:
            sequence = item.sequence
            diagnosis_sequence = None
            if item.diagnosisSequence:
                diagnosis_sequence = item.diagnosisSequence[0]
            product_or_service_text = None
            if item.productOrService:
                product_or_service_text = item.productOrService.text
            start_period = None
            end_period = None
            if item.servicePeriod:
                start_period = item.servicePeriod.start
                end_period = item.servicePeriod.end
            encounter_reference = None
            if item.encounter:
                encounter_reference = item.encounter[0].reference
            self.item_cols['reference'].append(reference)
            self.item_cols['sequence'].append(sequence)
            self.item_cols['diagnostic_seq'].append(diagnosis_sequence)
            self.item_cols['prod_or_serv_text'].append(product_or_service_text)
            self.item_cols['period_start'].append(start_period)
            self.item_cols['period_end'].append(end_period)
            self.item_cols['encounter'].append(encounter_reference)
            self.__get_coding_object(
                item.locationCodeableConcept.coding,
                reference,
                'Item'
            )
            self.__get_coding_object(
                item.productOfService.coding,
                reference,
                'Item'
            )
            for code in item.category:
                self.__get_coding_object(code.coding, reference, 'ItemType')

    def __get_claim_items(self, claim_items_list, reference):
        for item in claim_items_list:
            sequence = item.sequence
            product_or_service_text = item.productOrService.text
            diagnosis_sequence = None
            if item.diagnosisSequence:
                diagnosis_sequence = item.diagnosisSequence[0]
            start_period = None
            end_period = None
            encounter_reference = None
            if item.encounter:
                encounter_reference = item.encounter[0].reference
            self.__get_coding_object(
                item.productOrService.coding,
                reference,
                'Item'
            )
            self.item_cols['reference'].append(reference)
            self.item_cols['sequence'].append(sequence)
            self.item_cols['diagnostic_seq'].append(diagnosis_sequence)
            self.item_cols['prod_or_serv_text'].append(product_or_service_text)
            self.item_cols['period_start'].append(start_period)
            self.item_cols['period_end'].append(end_period)
            self.item_cols['encounter'].append(encounter_reference)

    def __get_extension(self, extensions, reference):
        for extension in extensions:
            url = extension.url
            value_string = extension.valueString
            value_decimal = extension.valueDecimal
            if extension.valueCoding:
                self.__get_coding_object(
                    extension.valueCoding,
                    reference,
                    'PatientExtension'
                )
            self.extension_cols['reference'].append(reference)
            self.extension_cols['url'].append(url)
            self.extension_cols['string'].append(value_string)
            self.extension_cols['decimal'].append(value_decimal)

    def __get_contained(self, contained_list, reference):
        for element in contained_list:
            resource_type = element.resource_type
            resource_id = element.id
            status = element.status
            intent = element.intent
            subject = element.subject.reference
            requester = element.requester.reference
            payor = None
            if element.payor:
                payor = element.payor[0].display
            self.contained_cols['reference'].append(reference)
            self.contained_cols['respurce_type'].append(resource_type)
            self.contained_cols['resource_id'].append(resource_id)
            self.contained_cols['status'].append(status)
            self.contained_cols['intent'].append(intent)
            self.contained_cols['subject'].append(subject)
            self.contained_cols['requester'].append(requester)
            self.contained_cols['payor'].append(payor)
            self.__get_performer(element.performer, reference)

    def __get_udi_carrier(self, carriers_list, reference):
        for carrier in carriers_list:
            device_identifier = carrier.deviceIdentifier
            carrier_hrf = carrier.carrierHRF
            self.udi_carrier_cols['reference'].append(reference)
            self.udi_carrier_cols['device_identifier'].append(device_identifier)  # noqa
            self.udi_carrier_cols['carrier_hrf'].append(carrier_hrf)

    def __get_dosage_instruction(self, instructions, reference):
        for instruction in instructions:
            sequence = instruction.sequence
            text = instruction.text
            as_needed = instruction.asNeededBoolean
            self.dosage_instruction_cols['reference'].append(reference)
            self.dosage_instruction_cols['sequence'].append(sequence)
            self.dosage_instruction_cols['text'].append(text)
            self.dosage_instruction_cols['as_needed'].append(as_needed)

    def __get_presented_form(self, forms_list, reference):
        for form in forms_list:
            content_type = form.contentType
            data = form.data
            self.form_cols['reference'].append(reference)
            self.form_cols['content_type'].append(content_type)
            self.form_cols['data'].append(data)

    def __get_performer(self, performers_list, reference):
        for performer in performers_list:
            performer_reference = performer.reference
            performer_display = performer.display
            self.performer_cols['reference'].append(reference)
            self.performer_cols['performer_ref'].append(performer_reference)
            self.performer_cols['performer_dis'].append(performer_display)

    def __get_claim_diagnosis(self, diagnosis_list, reference):
        for diagnosis in diagnosis_list:
            sequence = diagnosis.sequence
            diagnose_reference = diagnosis.diagnosisReference.reference
            if diagnosis.type:
                for d in diagnosis.type:
                    self.__get_coding_object(d.coding, reference, 'DiagnosisType')  # noqa
            self.diagnosis_cols['reference'].append(reference)
            self.diagnosis_cols['sequence'].append(sequence)
            self.diagnosis_cols['diagnostic_ref'].append(diagnose_reference)

    def __get_managing_organization(self, organizations, reference):
        for organization in organizations:
            organization_reference = organization.reference
            organization_display = organization.display
            self.managing_organ_cols['reference'].append(reference)
            self.managing_organ_cols['organization_ref'].append(organization_reference)  # noqa
            self.managing_organ_cols['organization_dis'].append(organization_display)  # noqa

    def __get_identifier(self, identifiers_list, reference):
        for identifier in identifiers_list:
            system = identifier.system
            value = identifier.value
            if identifier.type:
                self.__get_coding_object(
                    identifier.type.coding,
                    reference,
                    'IdentifierType'
                )
            self.identifier_cols['reference'].append(reference)
            self.identifier_cols['system'].append(system)
            self.identifier_cols['value'].append(value)

    def __get_names(self, names_list, reference):
        for name in names_list:
            use = name.use
            family = name.family
            given = name.given
            if given:
                given = ' '.join(x.strip() for x in given)
            prefix = name.prefix
            if prefix:
                prefix = ' '.join([y.strip() for y in prefix])
            self.name_cols['reference'].append(reference)
            self.name_cols['use'].append(use)
            self.name_cols['family'].append(family)
            self.name_cols['given'].append(given)
            self.name_cols['prefix'].append(prefix)

    def __get_address(self, address_list, reference):
        for address in address_list:
            latitude = address.extension[0].extension[0].valueDecimal
            longitude = address.extension[0].extension[1].valueDecimal
            line = address.line
            city = address.city
            state = address.state
            country = address.country
            self.address_cols['reference'].append(reference)
            self.address_cols['latitude'].append(latitude)
            self.address_cols['longitude'].append(longitude)
            self.address_cols['line'].append(line)
            self.address_cols['city'].append(city)
            self.address_cols['state'].append(state)
            self.address_cols['country'].append(country)

    def __get_communication(self, communication_list, reference):
        for element in communication_list:
            language_text = element.text
            self.communication_cols['reference'].append(reference)
            self.communication_cols['language'].append(language_text)
            self.__get_coding_object(
                element.coding,
                reference,
                'PatientCommunication',
            )

    def __get_target_references(self, target_list, reference):
        for target in target_list:
            target_reference = target.reference
            self.target_cols['reference'].append(reference)
            self.target_cols['target_ref'].append(target_reference)

    def __get_agents(self, agents_list, reference):
        for agent in agents_list:
            agent_text = agent.type.text
            who_reference = agent.who.reference
            who_display = agent.who.display
            on_behalf_of_reference = agent.onBehalfOf.reference
            on_behalf_of_display = agent.onBehalfOf.display
            self.agents_cols['reference'].append(reference)
            self.agents_cols['type'].append(agent_text)
            self.agents_cols['agent_ref'].append(who_reference)
            self.agents_cols['agent_dis'].append(who_display)
            self.agents_cols['on_behalf_of_ref'].append(on_behalf_of_reference)
            self.agents_cols['on_behalf_of_dis'].append(on_behalf_of_display)
            self.__get_coding_object(
                agent.type.coding,
                reference,
                'AgentType',
            )

    def __get_info_template_pairs(self):
        info_tuples_list = [
            (self.allergy_intolerance_cols, ALLERGY_INTOLERANCE, 'allergyIntolerance'),  # noqa
            (self.care_plan_cols, CARE_PLAN, 'carePlans'),
            (self.care_team_cols, CARE_TEAM, 'careTeams'),
            (self.claim_cols, CLAIM, 'claims'),
            (self.condition_cols, CONDITION, 'conditions'),
            (self.device_cols, DEVICE, 'devices'),
            (self.diagn_report_cols, DIAGNOSTIC_REPORT, 'diagnosticReports'),
            (self.document_ref_cols, DOCUMENT_REFERENCE, 'documentReferences'),
            (self.encounter_cols, ENCOUNTER, 'encounters'),
            (self.explanation_of_ben_cols, EXPLANATION_OF_BENEFIT, 'explanationsOfBenefit'),  # noqa
            (self.imaging_study_cols, IMAGING_STUDY, 'imagingStudies'),
            (self.immunization_cols, IMMUNIZATION, 'immunizations'),
            (self.medication_cols, MEDICATION, 'medications'),
            (self.item_cols, ITEM, 'items'),
            (self.med_admin_cols, MEDICATION_ADMINISTRATION, 'medicationAdministrations'),
            (self.med_request_cols, MEDICATION_REQUEST, 'medicationRequests'),
            (self.observation_cols, OBSERVATION, 'observations'),
            (self.patient_cols, PATIENT, 'patients'),
            (self.procedure_cols, PROCEDURE, 'procedures'),
            (self.provenance_cols, PROVENANCE, 'provenance'),
            (self.supply_delivery_cols, SUPPLY_DELIVERY, 'supplyDeliveries'),
            (self.extension_cols, EXTENSION, 'extensions'),
            (self.diagnosis_cols, DIAGNOSIS, 'diagnosis'),
            (self.insurance_cols, INSURANCE, 'insurances'),
            (self.agents_cols, AGENT, 'agents'),
            (self.coding_cols, CODE, 'codes'),
            (self.activities_cols, ACTIVITIES, 'activities'),
            (self.address_cols, ADDRESS, 'addresses'),
            (self.contained_cols, CONTAINED, 'contained'),
            (self.name_cols, NAME, 'names'),
            (self.reaction_cols, REACTION, 'reactions'),
            (self.dosage_instruction_cols, DOSAGE_INSTRUCTION, 'dosageInstructions'),  # noqa
            (self.identifier_cols, IDENTIFIER, 'identifiers'),
            (self.telecom_cols, TELECOM, 'telecoms'),
            (self.managing_organ_cols, MANAGING_ORGANIZATION, 'managingOrganizations'),  # noqa
            (self.form_cols, FORM, 'forms'),
            (self.udi_carrier_cols, UDI_CARRIER, 'udiCarriers'),
            (self.target_cols, TARGET, 'targets'),
            (self.communication_cols, COMMUNICATION, 'communications'),
            (self.performer_cols, PERFORMER, 'performers'),
            (self.participant_cols, PARTICIPANT, 'participants'),
        ]
        return info_tuples_list
