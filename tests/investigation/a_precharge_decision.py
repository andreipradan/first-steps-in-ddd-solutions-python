from src.investigation import CriminalOffence
from src.investigation import OffenceAdvice
from src.investigation import PreChargeDecision
from src.investigation import Suspect


class TestAPreChargeDecision:
    def setup(self):
        self.advice = OffenceAdvice()
        self.decision = PreChargeDecision()
        self.suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)

    def test_should_record_alternative_offence_advice_against_suspects(self):
        self.decision.record_alternative_offensive_advice(self.suspect, self.advice)

        assert self.advice == self.decision.get_offence_advice_for(self.suspect)
