import typing


class Game:
    pass


class Combat:
    pass


class Actor:
    pass


class ActionRequest:
    actor: Actor


class ActionResult:
    request: ActionRequest


class CombatTurnRequest:
    actors: typing.List[Actor]


class CombatTurnResult:
    action_results: typing.List[ActionResult]
