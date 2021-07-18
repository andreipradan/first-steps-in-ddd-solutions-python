from enum import Enum


class CriminalCase:
    pass


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


class PNCId:
    def __init__(self, value: str):
        self.value = value


class Suspect:
    def __init__(self, offence: CriminalOffence):
        self.offence = offence


class PoliceInvestigation:
    def __init__(self, pnc_id: PNCId, suspect: Suspect):
        self.suspects = []
        if not pnc_id:
            raise ValueError("You must provide a PNC Id")
        if not suspect:
            raise ValueError("You must provide a suspect")
        self.pnc_id = pnc_id
        self.suspects.append(suspect)


class PreChargeDecision:
    pass
