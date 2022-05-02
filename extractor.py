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
        reaction_text = fhir_object.reaction
        recorded_date = fhir_object.recordedDate
        code_text = fhir_object.code.text
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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        if fhir_object.activity:
            self.__get_activities(fhir_object.activity, uid, )
        for concept in fhir_object.category:
            self.__get_coding_object(concept.coding, uid, 'DiagnosticReport', )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_care_team(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        start_period = fhir_object.period.start
        end_period = fhir_object.period.end
        note = fhir_object.note
        self.__get_participants(fhir_object.participant, uid, )
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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        self.__get_claim_item(fhir_object.item, uid, )
        self.__get_insurance(fhir_object.insurance, uid, )
        self.__get_coding_object(fhir_object.type.coding, uid, 'Claim')
        self.__get_coding_object(fhir_object.priority.coding, uid, 'ClaimPriority')
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_condition(self, fhir_object):
        uid = fhir_object.id
        code_text = fhir_object.code.text
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        severity = fhir_object.severity
        on_set_date_time = fhir_object.onsetDateTime
        abatementDateTime = fhir_object.abatementDateTime
        recorded_date = fhir_object.recordedDate
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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        self.__get_coding_object(fhir_object.type.coding, uid, 'DeviceType')
        self.__get_udi_carrier(fhir_object.udiCarrier, uid)
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_diagnostic_report(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        encounter_reference = fhir_object.encounter.reference
        effective_date_time = fhir_object.effectiveDateTime
        issued = fhir_object.issued
        conclusion = fhir_object.conclusion
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
            self.__get_coding_object(category.coding, uid, 'DiagnosticReportCategory')
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        for type in fhir_object.type:
            self.__get_coding_object(type.coding, uid, 'EncounterType')
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_explanation_of_benefit(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        use = fhir_object.use
        patient = fhir_object.patient
        billable_period_start = fhir_object.billablePeriod.start
        billable_period_end = fhir_object.billablePeriod.end
        created = fhir_object.created
        insurer_display = fhir_object.insurer.display
        provider_reference = fhir_object.provider.reference
        referral = fhir_object.referral.reference
        facility_reference = fhir_object.facility.reference
        facility_display = fhir_object.facility.display
        claim = fhir_object.claim.reference
        outcome = fhir_object.outcome
        total = fhir_object.total[0].category.text
        total_amount_value = fhir_object.total[0].amount.value
        total_amount_currency = fhir_object.total[0].amount.currency
        payment_amount_value = fhir_object.payment.amount.value
        payment_amount_currency = fhir_object.payment.amount.currency
        self.__get_coding_object(
            fhir_object.type.coding,
            uid,
            'ExplanationOfBenType',
        )
        self.__get_identifier(
            fhir_object.identifier,
            uid,
        )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        for code in fhir_object.procedureCode:
            self.__get_coding_object(code.coding, uid, 'ImagingStudyProcedureCode')
        self.__get_identifier(fhir_object.identifier, uid)
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        self.__get_coding_object(
            fhir_object.vaccineCode.coding,
            uid,
            'ImmunizationVaccineCode',
        )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_medication(self, fhir_object):
        uid = fhir_object.id
        medication_code_text = fhir_object.code.text
        status = fhir_object.status
        self.__get_coding_object(
            fhir_object.code.coding,
            uid,
            'MedicationCode',
        )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __extract_medication_administration(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        subject_reference = fhir_object.subject.reference
        context = fhir_object.context.reference
        effective_date_time = fhir_object.effectiveDateTime
        reason_value = None
        if fhir_object.reasonReference:
            reason_value = fhir_object.reasonReference[0].reference
        self.__get_coding_object(
            fhir_object.medicationCodeableConcept.coding,
            uid,
            'MedicationAdministrationCode',
        )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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

    def __extract_supply_delivery(self, fhir_object):
        uid = fhir_object.id
        status = fhir_object.status
        patient_reference = fhir_object.patient.reference
        supplied_item_quantity = fhir_object.suppliedItem.quantity.value
        supplied_item_text = fhir_object.suppliedItem.itemCodeableConcept.text
        occurrence_date_time = fhir_object.occurrenceDateTime
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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_reaction(self, reaction_list, reference):
        for reaction in reaction_list:
            reaction_text = reaction.manifestation[0].text
            severity = reaction.severity
            self.__get_coding_object(
                reaction.manifestation[0].coding,
                reference,
                'Reaction',
            )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_participants(self, participants, reference):
        for participant in participants:
            role_text = participant.role[0].text
            member_reference = participant.member.reference
            member_display = participant.member.display
            self.__get_coding_object(
                participant.role[0].coding,
                reference,
                'Participant'
            )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_telecom(self, telecom_list, reference):
        for telecom in telecom_list:
            system = telecom.system
            value = telecom.value
            use = telecom.use
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_insurance(self, insurance_list, reference):
        for insurance in insurance_list:
            sequence = insurance.sequence
            focal = insurance.focal
            coverage_reference = insurance.coverage.reference
            coverage_display = insurance.coverage.display
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_items(self, items_list, reference):
        for item in items_list:
            sequence = item.sequence
            if item.diagnosisSequence:
                diagnosis_sequence = item.diagnosisSequence[0]
            if item.productOrService:
                product_of_service_text = item.productOrService.text
            if item.servicePeriod:
                service_period_start = item.servicePeriod.start
            service_period_end = item.servicePeriod.end
            encounter_reference = item.encounter[0].reference
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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_claim_item(self, claim_items_list, reference):
        for item in claim_items_list:
            sequence = item.sequence
            product_or_service_text = item.productOrService.text
            if item.diagnosisSequence:
                diagnosis_sequence = item.diagnosisSequence[0]
            if item.encounter:
                encounter_reference = item.encounter[0].reference
            self.__get_coding_object(
                item.productOrService.coding,
                reference,
                'Item'
            )
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
            self.__get_performer(element.performer, reference)
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_udi_carrier(self, carriers_list, reference):
        for carrier in carriers_list:
            device_identifier = carrier.deviceIdentifier
            carrier_hrf = carrier.carrierHRF
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_dosage_instruction(self, instructions, reference):
        for instruction in instructions:
            sequence = instruction.sequence
            text = instruction.text
            as_needed = instruction.asNeededBoolean
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_presented_form(self, forms_list, reference):
        for form in forms_list:
            content_type = form.contentType
            data = form.data
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_performer(self, performers_list, reference):
        for performer in performers_list:
            performer_reference = performer.reference
            performer_display = performer.display
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_claim_diagnosis(self, diagnosis_list, reference):
        for diagnosis in diagnosis_list:
            sequence = diagnosis.sequence
            diagnose_reference = diagnosis.diagnosisReference.reference
            if diagnosis.type:
                for d in diagnosis.type:
                    self.__get_coding_object(d.coding, reference, 'DiagnosisType')
        # TODO MIND THIS PIECE OF SHIT
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_managing_organization(self, organizations, reference):
        for organization in organizations:
            organization_reference = organization.reference
            organization_display = organization.display
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

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
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_address(self, address_list, reference):
        for address in address_list:
            latitude = address.extension[0].extension[0].valueDecimal
            longitude = address.extension[0].extension[1].valueDecimal
            line = address.line
            city = address.city
            state = address.state
            country = address.country
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_communication(self, communication_list, reference):
        for element in communication_list:
            language_text = element.text
            self.__get_coding_object(
                element.coding,
                reference,
                'PatientCommunication',
            )

    def __get_target_references(self, target_list, reference):
        for target in target_list:
            target_reference = target.reference
        # TODO GET THOSE ELEMENTS INTO THE CODING DATA FRAME

    def __get_agents(self, agents_list, reference):
        for agent in agents_list:
            agent_text = agent.type.text
            who_reference = agent.who.reference
            who_display = agent.who.display
            on_behalf_of_reference = agent.onBehalfOf.reference
            on_behalf_of_display = agent.onBehalfOf.display
            self.__get_coding_object(
                agent.type.coding,
                reference,
                'AgentType',
            )

