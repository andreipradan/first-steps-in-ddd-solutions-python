from src.justice_app import CriminalOffence
from src.justice_app import PreChargeDecision
from src.justice_app import Suspect


class TestAPreChargeDecision:
    def test_should_record_alternative_offence_advice_against_suspects(self):
        suspect = Suspect(CriminalOffence.CUTTING_AWAY_BUOYS_ETC)
        decision = PreChargeDecision()
        advice = OffenceAdvice()

        decision.record_alternative_offensive_advice(suspect, advice)

        assert advice == decision.get_offence_advice_for(suspect)
