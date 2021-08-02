from src.investigation import CriminalOffence
from src.investigation import PoliceInvestigation
from src.investigation import PNCId
from src.investigation import Suspect
from src.justice_app import PublicProsecutionService


class TestThePublicProsecutionService:
    def setup(self):
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        self.pnc_id = PNCId("AN-ID")
        self.police_investigation = PoliceInvestigation(self.pnc_id, suspect)
        self.the_pps = PublicProsecutionService()

    def test_should_create_a_case_when_receiving_a_pcd_request(self):

        police_case = self.the_pps.receive_request_for_pre_charge_decision(
            self.police_investigation
        )

        assert self.pnc_id == police_case.pnc_id
        assert self.police_investigation.suspects == police_case.suspects
