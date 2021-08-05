from src.investigation import CriminalOffence
from src.investigation import PNCId
from src.investigation import PoliceInvestigationDetails
from src.investigation import PreChargeDecisionService
from src.investigation import Suspect


class TestThePreChargeDecisionService:
    def setup(self):
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        self.pnc_id = PNCId("AN-ID")
        self.decision_service = PreChargeDecisionService()
        self.investigation_details = PoliceInvestigationDetails(self.pnc_id, suspect)

    def test_should_create_a_pre_charge_decision_case_when_receiving_a_pcd_request(
        self,
    ):
        pcd_case = self.decision_service.receive_request_for_pre_charge_decision(
            self.investigation_details
        )

        assert self.pnc_id == pcd_case.pnc_id
        assert self.investigation_details.suspects == pcd_case.get_suspects()
