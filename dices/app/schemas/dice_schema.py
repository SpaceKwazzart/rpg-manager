from pydantic import BaseModel


class DiceBase(BaseModel):
    dice_face: int | None = 6


class DiceResultBase(BaseModel):
    dice: DiceBase
    result: int


class SameDicesBunchBase(BaseModel):
    dice: DiceBase
    ammount: int
