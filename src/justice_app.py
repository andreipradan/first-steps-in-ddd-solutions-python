from src.investigation import PoliceInvestigationDetails
from src.investigation import PreChargeDecisionCase
from src.preparation import CriminalCase
from src.preparation import PoliceCaseFile


class PublicProsecutionService:
    def accept_case_file(self, police_case_file: PoliceCaseFile):
        return CriminalCase(police_case_file.pnc_id, police_case_file.defendants)

    def receive_request_for_pre_charge_decision(
        self, police_investigation: PoliceInvestigationDetails
    ):
        return PreChargeDecisionCase(
            police_investigation.pnc_id, police_investigation.suspects
        )
