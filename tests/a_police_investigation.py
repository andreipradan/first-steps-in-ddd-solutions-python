import pytest

from src.justice_app import CriminalOffence
from src.justice_app import PNCId
from src.justice_app import PoliceInvestigation
from src.justice_app import Suspect


class TestAPoliceInvestigation:
    def setup(self):
        self.pnc_id = PNCId("1234-ESDT")
        self.suspect = Suspect(CriminalOffence.FALSE_ACCOUNTING)
        self.an_investigation = PoliceInvestigation(self.pnc_id, self.suspect)

    def test_must_have_a_police_national_computer_id(self):
        assert self.an_investigation.pnc_id is not None

    def test_cannot_be_created_with_an_empty_police_national_computer_id(self):
        with pytest.raises(ValueError) as error:
            PoliceInvestigation(None, self.suspect)
        assert "You must provide a PNC Id" in error.value.args

    def test_cannot_be_created_with_no_suspect(self):
        with pytest.raises(ValueError) as error:
            PoliceInvestigation(self.pnc_id, None)
        assert "You must provide a suspect" in error.value.args
