from pydantic import BaseModel

from app.config import Numeric

from .dice_schema import DiceBase, SameDicesBunchBase, DiceResultBase


class RollBase(BaseModel):
    rolled_dices: list[SameDicesBunchBase] | None


class RequestRollDTO(RollBase):
    rolled_dices: list[SameDicesBunchBase] | None = [
        SameDicesBunchBase(dice=DiceBase(dice_face=20), ammount=2)
    ]


class ResponseRollDTO(RollBase):
    rolled_results: list[DiceResultBase]
    rolled_stats: dict[str, Numeric]
