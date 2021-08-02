from src.justice_app import CriminalOffence
from src.justice_app import PoliceInvestigation
from src.justice_app import PNCId
from src.justice_app import Suspect


class TestThePublicProsecutionService:
    def setup(self):
        self.the_pps = PublicProsecutionService()

    def test_should_create_a_case_when_receiving_a_pcd_request(self):
        pnc_id = PNCId("AN-ID")
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        police_investigation = PoliceInvestigation(pnc_id, suspect)

        police_case = self.the_pps.receive_request_for_pre_charge_decision(
            police_investigation
        )

        assert pnc_id == police_case.pnc_id
        assert police_investigation.suspects == police_case.suspects
