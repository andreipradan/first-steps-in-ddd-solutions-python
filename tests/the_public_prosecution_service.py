from src.investigation import CriminalOffence
from src.investigation import PoliceInvestigation
from src.investigation import PNCId
from src.investigation import Suspect
from src.justice_app import PublicProsecutionService
from src.preparation import Defendant
from src.preparation import PoliceCaseFile


class TestThePublicProsecutionService:
    def setup(self):
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        self.pnc_id = PNCId("AN-ID")
        self.police_investigation = PoliceInvestigation(self.pnc_id, suspect)
        self.the_pps = PublicProsecutionService()

    def test_should_create_a_pre_charge_decision_case_when_receiving_a_pcd_request(
        self,
    ):
        pcd_case = self.the_pps.receive_request_for_pre_charge_decision(
            self.police_investigation
        )

        assert self.pnc_id == pcd_case.pnc_id
        assert self.police_investigation.suspects == pcd_case.get_suspects()

    def test_should_create_a_criminal_case_when_a_police_case_file_is_accepted(self):
        defendant = Defendant()
        police_case_file = PoliceCaseFile(self.pnc_id, defendant)

        criminal_case = self.the_pps.accept_case_file(police_case_file)

        assert self.pnc_id == criminal_case.pnc_id
        assert police_case_file.defendants == criminal_case.defendants
