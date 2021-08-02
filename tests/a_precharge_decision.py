from src.justice_app import CriminalOffence
from src.justice_app import OffenceAdvice
from src.justice_app import PreChargeDecision
from src.justice_app import Suspect


class TestAPreChargeDecision:
    def setup(self):
        self.advice = OffenceAdvice()
        self.decision = PreChargeDecision()
        self.suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)

    def test_should_record_alternative_offence_advice_against_suspects(self):
        self.decision.record_alternative_offensive_advice(self.suspect, self.advice)

        assert self.advice == self.decision.get_offence_advice_for(self.suspect)
