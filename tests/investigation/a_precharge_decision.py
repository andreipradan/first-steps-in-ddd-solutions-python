from src.investigation import CriminalOffence
from src.investigation import OffenceAdvice
from src.investigation import PNCId
from src.investigation import PreChargeDecision
from src.investigation import Suspect


class TestAPreChargeDecision:
    def setup(self):
        pnc_id = PNCId("ANOTHER_PNC_ID")
        self.advice = OffenceAdvice()
        self.suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        self.decision = PreChargeDecision(pnc_id, {self.suspect})

    def test_should_record_alternative_offence_advice_against_suspects(self):
        self.decision.record_alternative_offensive_advice(self.suspect, self.advice)

        assert self.advice == self.decision.get_offence_advice_for(self.suspect)
