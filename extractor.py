class Extractor:
    def __init__(self):
        self.extract_functions_mapper = {
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
            "MedicationAdministration": self.__extract_medication_administration,
            "MedicationRequest": self.__extract_medication_request,
            "Observation": self.__extract_observation,
            "Patient": self.__extract_patient,
            "Procedure": self.__extract_procedure,
            "Provenance": self.__extract_provenance,
            "SupplyDelivery": self.__extract_supply_delivery,
        }
        self.ALLERGY_INTOLERANCE_COLS = {
            'uid': [],
            'type': [],
            'category': [],
            'criticality': [],
            'patient': [],
            'encounter': [],
            'recorded': [],
        }
        self.CARE_PLAN_COLS = {
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
        self.CARE_TEAM_COLS = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'period_start': [],
            'period_end': [],
            'note': [],
        }
        self.CLAIM_COLS = {
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
        self.CONDITION_COLS = {
            'uid': [],
            'code_text': [],
            'severity': [],
            'subject': [],
            'encounter': [],
            'on_set_time': [],
            'abatement_date': [],
            'recorded': [],
        }
        self.DEVICE_COLS = {
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
        self.DIAGN_REPORT_COLS = {
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
        self.DOCUMENT_REF_COLS = {
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
        self.ENCOUNTER_COLS = {
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
        self.EXPLANATION_OF_BEN_COLS = {
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
        self.IMAGING_STUDY_COLS = {
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
        self.IMMUNIZATION_COLS = {
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
        self.MEDICATION_COLS = {
            'uid': [],
            'code_text': [],
            'status': [],
        }
        self.MED_ADMIN_COLS = {
            'uid': [],
            'status': [],
            'subject': [],
            'context': [],
            'effective_date': [],
            'reason': [],
        }
        self.MED_REQUEST_COLS = {
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
        self.OBSERVATION_COLS = {
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
        self.PATIENT_COLS = {
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
        self.PROCEDURE_COLS = {
            'uid': [],
            'status': [],
            'subject': [],
            'encounter': [],
            'period_start': [],
            'period_end': [],
            'location_ref': [],
            'location_dis': [],
        }
        self.PROVENANCE_COLS = {
            'uid': [],
            'recorded': [],
        }
        self.SUPPLY_DELIVERY_COLS = {
            'uid': [],
            'status': [],
            'patient': [],
            'item_quantity': [],
            'item_text': [],
            'occurrence': [],
        }
        self.CONTAINED_COLS = {
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
        self.ITEM_COLS = {
            'reference': [],
            'sequence': [],
            'diagnostic_seq': [],
            'prod_or_serv_text': [],
            'period_start': [],
            'period_end': [],
            'encounter': [],
        }
        self.ADDRESS_COLS = {
            'reference': [],
            'latitude': [],
            'longitude': [],
            'line': [],
            'city': [],
            'state': [],
            'post_code': [],
            'country': [],
        }
        self.AGENTS_COLS = {
            'reference': [],
            'type': [],
            'agent_ref': [],
            'agent_dis': [],
            'on_behalf_of_ref': [],
            'on_behalf_of_dis': [],
        }
        self.CODING_COLS = {
            'reference': [],
            'type': [],
            'system': [],
            'code': [],
            'display': [],
        }
        self.EXTENSION_COLS = {
            'reference': [],
            'url': [],
            'string': [],
            'decimal': [],
            'address': [],
        }
        self.INSURANCE_COLS = {
            'reference': [],
            'sequence': [],
            'focal': [],
            'coverage_ref': [],
            'coverage_dis': [],
        }
        self.NAME_COLS = {
            'reference': [],
            'use': [],
            'family': [],
            'given': [],
            'prefix': [],
        }
        self.TELECOM_COLS = {
            'reference': [],
            'system': [],
            'value': [],
            'use': [],
        }
        self.ACTIVITIES_COLS = {
            'reference': [],
            'detail': [],
            'status': [],
            'location': [],
        }
        self.DOSAGE_INSTRUCTION_COLS = {
            'reference': [],
            'sequence': [],
            'text': [],
            'as_needed': [],
        }
        self.PARTICIPANT_COLS = {
            'reference': [],
            'role_text': [],
            'member_ref': [],
            'member_dis': [],
        }
        self.DIAGNOSIS_COLS = {
            'reference': [],
            'sequence': [],
            'diagnostic_ref': [],
        }
        self.FORM_COLS = {
            'reference': [],
            'content_type': [],
            'data': [],
        }
        self.IDENTIFIER_COLS = {
            'reference': [],
            'system': [],
            'value': [],
        }
        self.MAN_ORGAN_COLS = {
            'reference': [],
            'organization_ref': [],
            'organization_dis': [],
        }
        self.PERFORMER_COLS = {
            'reference': [],
            'performer_ref': [],
            'performer_dis': [],
        }
        self.REACTION_COLS = {
            'reference': [],
            'reaction_text': [],
            'severity': [],
        }
        self.UDI_CARRIER_COLS = {
            'reference': [],
            'device_identifier': [],
            'carrier_hrf': [],
        }
        self.COMMUNICATION_COLS = {
            'reference': [],
            'language': [],
        }
        self.TARGET_COLS = {
            'reference': [],
            'target_ref': [],
        }

    def extract(self, fhir_object):
        resource_type = fhir_object.resource_type
        self.extract_functions_mapper[resource_type](fhir_object)

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
        self.ALLERGY_INTOLERANCE_COLS['uid'].append(uid)
        self.ALLERGY_INTOLERANCE_COLS['type'].append(intolerance_type)
        self.ALLERGY_INTOLERANCE_COLS['category'].append(intolerance_category)
        self.ALLERGY_INTOLERANCE_COLS['criticality'].append(criticality)
        self.ALLERGY_INTOLERANCE_COLS['patient'].append(patient)
        self.ALLERGY_INTOLERANCE_COLS['encounter'].append(encounter)
        self.ALLERGY_INTOLERANCE_COLS['recorded'].append(recorded_date)
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
        self.CARE_PLAN_COLS['uid'].append(uid)
        self.CARE_PLAN_COLS['status'].append(status)
        self.CARE_PLAN_COLS['intent'].append(intent)
        self.CARE_PLAN_COLS['category_text'].append(category_text)
        self.CARE_PLAN_COLS['subject'].append(subject_reference)
        self.CARE_PLAN_COLS['encounter'].append(encounter_reference)
        self.CARE_PLAN_COLS['period_start'].append(start_period)
        self.CARE_PLAN_COLS['period_end'].append(end_period)
        self.CARE_PLAN_COLS['care_team'].append(care_team_reference)
        self.CARE_PLAN_COLS['address_reference'].append(address_reference)
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
        self.CARE_TEAM_COLS['uid'].append(uid)
        self.CARE_TEAM_COLS['status'].append(status)
        self.CARE_TEAM_COLS['subject'].append(subject_reference)
        self.CARE_TEAM_COLS['encounter'].append(encounter_reference)
        self.CARE_TEAM_COLS['period_start'].append(start_period)
        self.CARE_TEAM_COLS['period_end'].append(end_period)
        self.CARE_TEAM_COLS['note'].append(note)
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
        self.CLAIM_COLS['uid'].append(uid)
        self.CLAIM_COLS['status'].append(status)
        self.CLAIM_COLS['use'].append(use)
        self.CLAIM_COLS['patient_ref'].append(patient_reference)
        self.CLAIM_COLS['patient_dis'].append(patient_display)
        self.CLAIM_COLS['bill_period_start'].append(billable_period_start)
        self.CLAIM_COLS['bill_period_end'].append(billable_period_end)
        self.CLAIM_COLS['created'].append(created)
        self.CLAIM_COLS['provider_ref'].append(provider_reference)
        self.CLAIM_COLS['provider_dis'].append(provider_display)
        self.CLAIM_COLS['facility_ref'].append(facility_reference)
        self.CLAIM_COLS['facility_dis'].append(facility_display)
        self.CLAIM_COLS['total_value'].append(total_value)
        self.CLAIM_COLS['total_currency'].append(currency)
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
        self.CONDITION_COLS['uid'].append(uid)
        self.CONDITION_COLS['code_text'].append(code_text)
        self.CONDITION_COLS['severity'].append(severity)
        self.CONDITION_COLS['subject'].append(subject_reference)
        self.CONDITION_COLS['encounter'].append(encounter_reference)
        self.CONDITION_COLS['on_set_time'].append(on_set_date_time)
        self.CONDITION_COLS['abatement_date'].append(abatement_date_time)
        self.CONDITION_COLS['recorded'].append(recorded_date)
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
        self.DEVICE_COLS['uid'].append(uid)
        self.DEVICE_COLS['status'].append(status)
        self.DEVICE_COLS['manufacturer'].append(manufacturer)
        self.DEVICE_COLS['manufacture_date'].append(manufacture_date)
        self.DEVICE_COLS['expiration_date'].append(expiration_date)
        self.DEVICE_COLS['lot_number'].append(lot_number)
        self.DEVICE_COLS['serial_number'].append(serial_number)
        self.DEVICE_COLS['device_name'].append(device_name)
        self.DEVICE_COLS['name_type'].append(device_name_type)
        self.DEVICE_COLS['type_text'].append(device_type_text)
        self.DEVICE_COLS['patient'].append(patient_reference)
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
        self.DIAGN_REPORT_COLS['uid'].append(uid)
        self.DIAGN_REPORT_COLS['status'].append(status)
        self.DIAGN_REPORT_COLS['subject'].append(subject_reference)
        self.DIAGN_REPORT_COLS['encounter'].append(encounter_reference)
        self.DIAGN_REPORT_COLS['effective'].append(effective_date_time)
        self.DIAGN_REPORT_COLS['issued'].append(issued)
        self.DIAGN_REPORT_COLS['conclusion'].append(conclusion)
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
        self.DOCUMENT_REF_COLS['uid'].append(uid)
        self.DOCUMENT_REF_COLS['status'].append(status)
        self.DOCUMENT_REF_COLS['subject'].append(subject_reference)
        self.DOCUMENT_REF_COLS['date'].append(date)
        self.DOCUMENT_REF_COLS['author_ref'].append(author_reference)
        self.DOCUMENT_REF_COLS['author_dis'].append(author_display)
        self.DOCUMENT_REF_COLS['custodian_ref'].append(custodian_reference)
        self.DOCUMENT_REF_COLS['custodian_dis'].append(custodian_display)
        self.DOCUMENT_REF_COLS['encounter'].append(encounter_reference)
        self.DOCUMENT_REF_COLS['content_attach_type'].append(content_type)
        self.DOCUMENT_REF_COLS['content_attach_data'].append(data)
        self.DOCUMENT_REF_COLS['period_start'].append(context_start_date)
        self.DOCUMENT_REF_COLS['period_end'].append(context_end_date)
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
        self.ENCOUNTER_COLS['uid'].append(uid)
        self.ENCOUNTER_COLS['status'].append(status)
        self.ENCOUNTER_COLS['subject_ref'].append(subject_reference)
        self.ENCOUNTER_COLS['subject_dis'].append(subject_display)
        self.ENCOUNTER_COLS['participant_type'].append(participant_type)
        self.ENCOUNTER_COLS['participant_name'].append(participant_name)
        self.ENCOUNTER_COLS['participant_ref'].append(participant_reference)
        self.ENCOUNTER_COLS['period_start'].append(start_period)
        self.ENCOUNTER_COLS['period_end'].append(end_period)
        self.ENCOUNTER_COLS['location_ref'].append(location_reference)
        self.ENCOUNTER_COLS['location_dis'].append(location_display)
        self.ENCOUNTER_COLS['provider_ref'].append(provider_reference)
        self.ENCOUNTER_COLS['provider_dis'].append(provider_display)
        for obj_type in fhir_object.type:
            self.__get_coding_object(obj_type.coding, uid, 'EncounterType')

    def __extract_explanation_of_benefit(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        use = fhir_object.use
        patient = fhir_object.patient
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
        self.EXPLANATION_OF_BEN_COLS['uid'].append(uid)
        self.EXPLANATION_OF_BEN_COLS['status'].append(status)
        self.EXPLANATION_OF_BEN_COLS['use'].append(use)
        self.EXPLANATION_OF_BEN_COLS['patient'].append(patient)
        self.EXPLANATION_OF_BEN_COLS['period_start'].append(bill_period_start)
        self.EXPLANATION_OF_BEN_COLS['period_end'].append(bill_period_end)
        self.EXPLANATION_OF_BEN_COLS['created'].append(created)
        self.EXPLANATION_OF_BEN_COLS['insurer'].append(insurer_display)
        self.EXPLANATION_OF_BEN_COLS['provider'].append(provider_reference)
        self.EXPLANATION_OF_BEN_COLS['referral'].append(referral)
        self.EXPLANATION_OF_BEN_COLS['facility_ref'].append(facility_reference)
        self.EXPLANATION_OF_BEN_COLS['facility_dis'].append(facility_display)
        self.EXPLANATION_OF_BEN_COLS['claim'].append(claim)
        self.EXPLANATION_OF_BEN_COLS['outcome'].append(outcome)
        self.EXPLANATION_OF_BEN_COLS['total_text'].append(total)
        self.EXPLANATION_OF_BEN_COLS['total_value'].append(total_value)
        self.EXPLANATION_OF_BEN_COLS['total_currency'].append(total_currency)
        self.EXPLANATION_OF_BEN_COLS['payment_amount'].append(payment_value)
        self.EXPLANATION_OF_BEN_COLS['payment_currency'].append(payment_currency)
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
        self.IMAGING_STUDY_COLS['uid'].append(uid)
        self.IMAGING_STUDY_COLS['status'].append(status)
        self.IMAGING_STUDY_COLS['subject'].append(subject_reference)
        self.IMAGING_STUDY_COLS['encounter'].append(encounter)
        self.IMAGING_STUDY_COLS['started'].append(started)
        self.IMAGING_STUDY_COLS['num_of_series'].append(number_of_series)
        self.IMAGING_STUDY_COLS['num_of_instances'].append(number_of_instances)
        self.IMAGING_STUDY_COLS['location_ref'].append(location_reference)
        self.IMAGING_STUDY_COLS['location_dis'].append(location_display)
        for code in fhir_object.procedureCode:
            self.__get_coding_object(code.coding, uid, 'ImagingStudyProcedureCode')
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
        self.IMMUNIZATION_COLS['uid'].append(uid)
        self.IMMUNIZATION_COLS['status'].append(status)
        self.IMMUNIZATION_COLS['vaccine_code_text'].append(vaccine_code_text)
        self.IMMUNIZATION_COLS['patient'].append(patient_reference)
        self.IMMUNIZATION_COLS['encounter'].append(encounter)
        self.IMMUNIZATION_COLS['occurrence'].append(occurrence_date_time)
        self.IMMUNIZATION_COLS['primary_source'].append(primary_source)
        self.IMMUNIZATION_COLS['location_ref'].append(location_reference)
        self.IMMUNIZATION_COLS['location_dis'].append(location_display)
        self.__get_coding_object(
            fhir_object.vaccineCode.coding,
            uid,
            'ImmunizationVaccineCode',
        )

    def __extract_medication(self, fhir_object):
        uid = fhir_object.id
        medication_code_text = fhir_object.code.text
        status = fhir_object.status
        self.MEDICATION_COLS['uid'].append(uid)
        self.MEDICATION_COLS['code_text'].append(medication_code_text)
        self.MEDICATION_COLS['status'].append(status)
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
        self.MED_ADMIN_COLS['uid'].append(uid)
        self.MED_ADMIN_COLS['status'].append(status)
        self.MED_ADMIN_COLS['subject'].append(subject_reference)
        self.MED_ADMIN_COLS['context'].append(context)
        self.MED_ADMIN_COLS['effective_date'].append(effective_date_time)
        self.MED_ADMIN_COLS['reason'].append(reason_value)
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
        self.MED_REQUEST_COLS['uid'].append(uid)
        self.MED_REQUEST_COLS['status'].append(status)
        self.MED_REQUEST_COLS['intent'].append(intent)
        self.MED_REQUEST_COLS['subject'].append(subject_reference)
        self.MED_REQUEST_COLS['encounter'].append(encounter)
        self.MED_REQUEST_COLS['authored_on'].append(authored_on)
        self.MED_REQUEST_COLS['requester_ref'].append(requester_reference)
        self.MED_REQUEST_COLS['requester_dis'].append(requester_display)
        self.MED_REQUEST_COLS['reason'].append(reason_reference)
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
        self.OBSERVATION_COLS['uid'].append(uid)
        self.OBSERVATION_COLS['status'].append(status)
        self.OBSERVATION_COLS['subject'].append(subject_reference)
        self.OBSERVATION_COLS['encounter'].append(encounter)
        self.OBSERVATION_COLS['effective_date'].append(effective_date_time)
        self.OBSERVATION_COLS['issued'].append(issued)
        self.OBSERVATION_COLS['quant_value'].append(value_quantity_value)
        self.OBSERVATION_COLS['quant_unit'].append(value_quantity_unit)
        self.OBSERVATION_COLS['quant_system'].append(value_quantity_system)
        self.OBSERVATION_COLS['quant_code'].append(value_quantity_code)
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
        self.PATIENT_COLS['uid'].append(uid)
        self.PATIENT_COLS['status'].append(text_status)
        self.PATIENT_COLS['div'].append(text_div)
        self.PATIENT_COLS['gender'].append(gender)
        self.PATIENT_COLS['date_of_birth'].append(date_of_birth)
        self.PATIENT_COLS['deceased'].append(deceased_date)
        self.PATIENT_COLS['marital_status'].append(marital_status_text)
        self.PATIENT_COLS['multiple_birth'].append(multiple_birth)
        self.PATIENT_COLS['general_practitioner'].append(general_practitioner)
        self.PATIENT_COLS['managing_organization'].append(managing_organization)  # noqa
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
        self.PROCEDURE_COLS['uid'].append(uid)
        self.PROCEDURE_COLS['status'].append(status)
        self.PROCEDURE_COLS['subject'].append(subject_reference)
        self.PROCEDURE_COLS['encounter'].append(encounter_reference)
        self.PROCEDURE_COLS['period_start'].append(performed_period_start)
        self.PROCEDURE_COLS['period_end'].append(performed_period_end)
        self.PROCEDURE_COLS['location_ref'].append(location_reference)
        self.PROCEDURE_COLS['location_dis'].append(location_display)

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
        self.PROVENANCE_COLS['uid'].append(uid)
        self.PROVENANCE_COLS['recorded'].append(recorded)

    def __extract_supply_delivery(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        patient_reference = fhir_object.patient.reference
        supplied_item_quantity = fhir_object.suppliedItem.quantity.value
        supplied_item_text = fhir_object.suppliedItem.itemCodeableConcept.text
        occurrence_date_time = fhir_object.occurrenceDateTime
        self.SUPPLY_DELIVERY_COLS['uid'].append(uid)
        self.SUPPLY_DELIVERY_COLS['status'].append(status)
        self.SUPPLY_DELIVERY_COLS['patient'].append(patient_reference)
        self.SUPPLY_DELIVERY_COLS['item_quantity'].append(supplied_item_quantity)  # noqa
        self.SUPPLY_DELIVERY_COLS['item_text'].append(supplied_item_text)
        self.SUPPLY_DELIVERY_COLS['occurrence'].append(occurrence_date_time)
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
            self.CODING_COLS['reference'].append(reference)
            self.CODING_COLS['type'].append(code_type)
            self.CODING_COLS['system'].append(system)
            self.CODING_COLS['code'].append(code)
            self.CODING_COLS['display'].append(display)

    def __get_reaction(self, reaction_list, reference):
        for reaction in reaction_list:
            reaction_text = reaction.manifestation[0].text
            severity = reaction.severity
            self.__get_coding_object(
                reaction.manifestation[0].coding,
                reference,
                'Reaction',
            )
            self.REACTION_COLS['reference'].append(reference)
            self.REACTION_COLS['reaction_text'].append(reaction_text)
            self.REACTION_COLS['severity'].append(severity)

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
            self.ACTIVITIES_COLS['reference'].append(reference)
            self.ACTIVITIES_COLS['detail'].append(detail_text)
            self.ACTIVITIES_COLS['status'].append(status)
            self.ACTIVITIES_COLS['location'].append(location)

    def __get_participants(self, participants, reference):
        for participant in participants:
            role_text = participant.role[0].text
            member_reference = participant.member.reference
            member_display = participant.member.display
            self.PARTICIPANT_COLS['reference'].append(reference)
            self.PARTICIPANT_COLS['role_text'].append(role_text)
            self.PARTICIPANT_COLS['member_ref'].append(member_reference)
            self.PARTICIPANT_COLS['member_dis'].append(member_display)
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
            self.TELECOM_COLS['reference'].append(reference)
            self.TELECOM_COLS['system'].append(system)
            self.TELECOM_COLS['value'].append(value)
            self.TELECOM_COLS['use'].append(use)

    def __get_insurance(self, insurance_list, reference):
        for insurance in insurance_list:
            sequence = insurance.sequence
            focal = insurance.focal
            coverage_reference = insurance.coverage.reference
            coverage_display = insurance.coverage.display
            self.INSURANCE_COLS['reference'].append(reference)
            self.INSURANCE_COLS['sequence'].append(sequence)
            self.INSURANCE_COLS['focal'].append(focal)
            self.INSURANCE_COLS['coverage_ref'].append(coverage_reference)
            self.INSURANCE_COLS['coverage_dis'].append(coverage_display)

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
            self.ITEM_COLS['reference'].append(reference)
            self.ITEM_COLS['sequence'].append(sequence)
            self.ITEM_COLS['diagnostic_seq'].append(diagnosis_sequence)
            self.ITEM_COLS['prod_or_serv_text'].append(product_or_service_text)
            self.ITEM_COLS['period_start'].append(start_period)
            self.ITEM_COLS['period_end'].append(end_period)
            self.ITEM_COLS['encounter'].append(encounter_reference)
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
            self.ITEM_COLS['reference'].append(reference)
            self.ITEM_COLS['sequence'].append(sequence)
            self.ITEM_COLS['diagnostic_seq'].append(diagnosis_sequence)
            self.ITEM_COLS['prod_or_serv_text'].append(product_or_service_text)
            self.ITEM_COLS['period_start'].append(start_period)
            self.ITEM_COLS['period_end'].append(end_period)
            self.ITEM_COLS['encounter'].append(encounter_reference)

    def __get_extension(self, extensions, reference):
        for extension in extensions:
            url = extension.url
            value_string = extension.valueString
            value_decimal = extension.valueDecimal
            value_address = extension.valueAddress
            if extension.valueCoding:
                self.__get_coding_object(
                    extension.valueCoding,
                    reference,
                    'PatientExtension'
                )
            self.EXTENSION_COLS['reference'].append(reference)
            self.EXTENSION_COLS['url'].append(url)
            self.EXTENSION_COLS['string'].append(value_string)
            self.EXTENSION_COLS['decimal'].append(value_decimal)
            self.EXTENSION_COLS['address'].append(value_address)

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
            self.CONTAINED_COLS['reference'].append(reference)
            self.CONTAINED_COLS['respurce_type'].append(resource_type)
            self.CONTAINED_COLS['resource_id'].append(resource_id)
            self.CONTAINED_COLS['status'].append(status)
            self.CONTAINED_COLS['intent'].append(intent)
            self.CONTAINED_COLS['subject'].append(subject)
            self.CONTAINED_COLS['requester'].append(requester)
            self.CONTAINED_COLS['payor'].append(payor)
            self.__get_performer(element.performer, reference)

    def __get_udi_carrier(self, carriers_list, reference):
        for carrier in carriers_list:
            device_identifier = carrier.deviceIdentifier
            carrier_hrf = carrier.carrierHRF
            self.UDI_CARRIER_COLS['reference'].append(reference)
            self.UDI_CARRIER_COLS['device_identifier'].append(device_identifier)
            self.UDI_CARRIER_COLS['carrier_hrf'].append(carrier_hrf)

    def __get_dosage_instruction(self, instructions, reference):
        for instruction in instructions:
            sequence = instruction.sequence
            text = instruction.text
            as_needed = instruction.asNeededBoolean
            self.DOSAGE_INSTRUCTION_COLS['reference'].append(reference)
            self.DOSAGE_INSTRUCTION_COLS['sequence'].append(sequence)
            self.DOSAGE_INSTRUCTION_COLS['text'].append(text)
            self.DOSAGE_INSTRUCTION_COLS['as_needed'].append(as_needed)

    def __get_presented_form(self, forms_list, reference):
        for form in forms_list:
            content_type = form.contentType
            data = form.data
            self.FORM_COLS['reference'].append(reference)
            self.FORM_COLS['content_type'].append(content_type)
            self.FORM_COLS['data'].append(data)

    def __get_performer(self, performers_list, reference):
        for performer in performers_list:
            performer_reference = performer.reference
            performer_display = performer.display
            self.PERFORMER_COLS['reference'].append(reference)
            self.PERFORMER_COLS['performer_ref'].append(performer_reference)
            self.PERFORMER_COLS['performer_dis'].append(performer_display)

    def __get_claim_diagnosis(self, diagnosis_list, reference):
        for diagnosis in diagnosis_list:
            sequence = diagnosis.sequence
            diagnose_reference = diagnosis.diagnosisReference.reference
            if diagnosis.type:
                for d in diagnosis.type:
                    self.__get_coding_object(d.coding, reference, 'DiagnosisType')
            self.DIAGNOSIS_COLS['reference'].append(reference)
            self.DIAGNOSIS_COLS['sequence'].append(sequence)
            self.DIAGNOSIS_COLS['diagnostic_ref'].append(diagnose_reference)

    def __get_managing_organization(self, organizations, reference):
        for organization in organizations:
            organization_reference = organization.reference
            organization_display = organization.display
            self.MAN_ORGAN_COLS['reference'].append(reference)
            self.MAN_ORGAN_COLS['organization_ref'].append(organization_reference)
            self.MAN_ORGAN_COLS['organization_dis'].append(organization_display)

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
            self.IDENTIFIER_COLS['reference'].append(reference)
            self.IDENTIFIER_COLS['system'].append(system)
            self.IDENTIFIER_COLS['value'].append(value)

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
            self.NAME_COLS['reference'].append(reference)
            self.NAME_COLS['use'].append(use)
            self.NAME_COLS['family'].append(family)
            self.NAME_COLS['given'].append(given)
            self.NAME_COLS['prefix'].append(prefix)

    def __get_address(self, address_list, reference):
        for address in address_list:
            latitude = address.extension[0].extension[0].valueDecimal
            longitude = address.extension[0].extension[1].valueDecimal
            line = address.line
            city = address.city
            state = address.state
            country = address.country
            self.ADDRESS_COLS['reference'].append(reference)
            self.ADDRESS_COLS['latitude'].append(latitude)
            self.ADDRESS_COLS['longitude'].append(longitude)
            self.ADDRESS_COLS['line'].append(line)
            self.ADDRESS_COLS['city'].append(city)
            self.ADDRESS_COLS['state'].append(state)
            self.ADDRESS_COLS['country'].append(country)

    def __get_communication(self, communication_list, reference):
        for element in communication_list:
            language_text = element.text
            self.COMMUNICATION_COLS['reference'].append(reference)
            self.COMMUNICATION_COLS['language'].append(language_text)
            self.__get_coding_object(
                element.coding,
                reference,
                'PatientCommunication',
            )

    def __get_target_references(self, target_list, reference):
        for target in target_list:
            target_reference = target.reference
            self.TARGET_COLS['reference'].append(reference)
            self.TARGET_COLS['target_ref'].append(target_reference)

    def __get_agents(self, agents_list, reference):
        for agent in agents_list:
            agent_text = agent.type.text
            who_reference = agent.who.reference
            who_display = agent.who.display
            on_behalf_of_reference = agent.onBehalfOf.reference
            on_behalf_of_display = agent.onBehalfOf.display
            self.AGENTS_COLS['reference'].append(reference)
            self.AGENTS_COLS['type'].append(agent_text)
            self.AGENTS_COLS['agent_ref'].append(who_reference)
            self.AGENTS_COLS['agent_dis'].append(who_display)
            self.AGENTS_COLS['on_behalf_of_ref'].append(on_behalf_of_reference)
            self.AGENTS_COLS['on_behalf_of_dis'].append(on_behalf_of_display)
            self.__get_coding_object(
                agent.type.coding,
                reference,
                'AgentType',
            )

