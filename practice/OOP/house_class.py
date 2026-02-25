from dataclasses import dataclass, field
from typing import List
import traceback

LINE_CORRECTOR = 97

@dataclass(frozen=True, order=True)
class House():
    address: str
    floors: int = 1
    flats: int = 1
    
    nearby_objects: List[str] = field(default_factory=list)

house1 = House('Пушкина 12', 5, 40)
house2 = House('Советская 46', 11, 120, ['магазин "Пятерочка"', 'детский сад "Заря"'])
house3 = House('Богатая 1')

print(house1, house2, house3, sep='\n')
print(f'house1 == house2: {house1 == house2}')

try:
    house1.address = None
except Exception as e:
    print(f'\nСтрока {traceback.extract_stack()[-2].lineno - LINE_CORRECTOR} >> house1.address = None >> ОШИБКА: {e}\n')

print(f'house1 > house2: {house1 > house2}')
print(sorted([house1, house2, house3]))