from src.investigation import CriminalOffence
from src.investigation import PoliceInvestigationDetails
from src.investigation import PNCId
from src.investigation import Suspect
from src.preparation import Defendant
from src.preparation import PoliceCaseFile
from src.preparation import TrialPreparationService


class TestTheTrialPreparationService:
    def setup(self):
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        self.pnc_id = PNCId("AN-ID")
        self.police_investigation = PoliceInvestigationDetails(self.pnc_id, suspect)
        self.the_pps = TrialPreparationService()

    def test_should_create_a_criminal_case_when_a_police_case_file_is_accepted(self):
        defendant = Defendant()
        police_case_file = PoliceCaseFile(self.pnc_id, defendant)

        criminal_case = self.the_pps.accept_case_file(police_case_file)

        assert self.pnc_id == criminal_case.pnc_id
        assert police_case_file.defendants == criminal_case.defendants
