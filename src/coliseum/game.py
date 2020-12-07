import typing


class Game:
    pass


class ConbatScheduler:
    pass


class CombatRule:
    pass


class Combat:
    rule: CombatRule


class Fighter:
    pass


class ActionRequest:
    pass


class ActionResult:
    pass


class CombatTurnRequest:
    pass


class CombatTurnResult:
    action_results: typing.List[ActionResult]
