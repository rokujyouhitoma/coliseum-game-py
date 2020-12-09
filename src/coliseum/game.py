import typing


class Game:
    pass


class ConbatScheduler:
    pass


class CombatRule:
    pass


class Combat:
    rule: CombatRule
    scheduler: ConbatScheduler


class Actor:
    pass


class Fighter(Actor):
    pass


class ActionRequest:
    actor: Actor


class ActionResult:
    request: ActionRequest


class CombatTurnRequest:
    pass


class CombatTurnResult:
    action_results: typing.List[ActionResult]
