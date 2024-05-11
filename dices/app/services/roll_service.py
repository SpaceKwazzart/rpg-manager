import random

from app.schemas import RequestRollDTO, ResponseRollDTO
from app.config import logger


class RollService:
    def __init__(self) -> None:
        ...

    async def roll_dices(self, rolled_dices: RequestRollDTO) -> ResponseRollDTO:
        rolled_results = []
        total_ammount = 0
        total_result = 0
        max_result = 0
        min_result = float('inf')
        min_face_count = 0
        max_face_count = 0

        for dice_ammount in rolled_dices.rolled_dices:
            logger.debug(rolled_dices)
            dice_face = dice_ammount.dice.dice_face
            ammount = dice_ammount.ammount
            total_ammount += ammount

            for _ in range(ammount):
                result = random.randint(1, dice_face)
                if result == 1:
                    min_face_count += 1
                elif result == dice_face:
                    max_face_count += 1

                total_result += result
                max_result = max(max_result, result)
                min_result = min(min_result, result)
                rolled_results.append(
                    {'dice': {'dice_face': dice_face}, 'result': result}
                )

        return {
            'rolled_results': rolled_results,
            'rolled_stats': {
                'min_face_count': min_face_count,
                'max_face_count': max_face_count,
                'max': max_result,
                'min': min_result,
                'sum': total_result,
                'avg': total_result / total_ammount,
            }
        }
