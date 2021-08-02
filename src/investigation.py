from enum import Enum


class CriminalOffence(Enum):
    # List from https://www.cps.gov.uk/sites/default/files/
    # documents/publications/annex_1a_table_of_offences_scheme_c.pdf
    DANGEROUS_DRIVING = "Dangerous driving"
    ENDANGERING_AN_AIRCRAFT = "Endangering an aircraft"
    FALSE_ACCOUNTING = "False accounting"
    IMPERSONATING_CUSTOMS_OFFICER = "Impersonating Customs officer"
    KEEPING_A_DISORDERLY_HOUSE = "Keeping a disorderly house"
    CORRUPTION_IN_PUBLIC_OFFICE = "Corruption in public office"
    CUTTING_AWAY_BUOYS_ETC = "Cutting away buoys etc"
    FALSE_EVIDENCE_BEFORE_EUROPEAN_COURT = "False evidence before European Court"
    FIRING_ON_REVENUE_VESSEL = "Firing on Revenue vessel"
    FRAUDULENT_EVASION_OF_AGRICULTURAL_LEVY = "Fraudulent evasion of agricultural levy"
    OBSTRUCTING_ENGINE_OR_CARRIAGE_ON_RAILWAY = (
        "Obstructing engine or carriage on railway"
    )


class OffenceAdvice:
    pass


class Suspect:
    def __init__(self, offence: CriminalOffence):
        self.offence = offence


class PNCId:
    def __init__(self, value: str):
        self.value = value


class PoliceInvestigation:
    def __init__(self, pnc_id: PNCId, suspect: Suspect):
        if not pnc_id:
            raise ValueError("You must provide a PNC Id")
        if not suspect:
            raise ValueError("You must provide a suspect")
        self.pnc_id = pnc_id
        self.suspects = {suspect}


class PreChargeDecision:
    def __init__(self, pnc_id: PNCId, suspects: set[Suspect]):
        self.offence_advice = {suspect: None for suspect in suspects}
        self.pnc_id = pnc_id

    def get_offence_advice_for(self, suspect: Suspect):
        return self.offence_advice.get(suspect)

    def get_suspects(self):
        return self.offence_advice.keys()

    def record_alternative_offensive_advice(
        self, suspect: Suspect, advice: OffenceAdvice
    ):
        self.offence_advice[suspect] = advice
