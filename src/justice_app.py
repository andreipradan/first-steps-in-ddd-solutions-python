from src.investigation import PNCId
from src.investigation import PoliceInvestigation
from src.investigation import Suspect


class CriminalCase:
    def __init__(self, pnc_id: PNCId, suspects: set[Suspect]):
        self.pnc_id = pnc_id
        self.suspects = suspects


class PublicProsecutionService:
    def receive_request_for_pre_charge_decision(
        self, police_investigation: PoliceInvestigation
    ):
        return CriminalCase(police_investigation.pnc_id, police_investigation.suspects)
