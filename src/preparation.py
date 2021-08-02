from src.investigation import PNCId


class Defendant:
    pass


class CriminalCase:
    def __init__(self, pnc_id: PNCId, defendants: set[Defendant]):
        self.pnc_id = pnc_id
        self.defendants = defendants


class PoliceCaseFile:
    def __init__(self, pnc_id: PNCId, defendant: Defendant):
        self.pnc_id = pnc_id
        self.defendants = {defendant}
