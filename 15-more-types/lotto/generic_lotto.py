import random

from collections.abc import Iterable
from typing import TypeVar, Generic

from tombola import Tombola

T = TypeVar('T')

class LottoBlower(Tombola, Generic[T]):  # <1>

    def __init__(self, items: Iterable[T]) -> None:  # <2>
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None:  # <3>
        self._balls.extend(items)

    def pick(self) -> T:  # <4>
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool:  # <5>
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:  # <6>
        return tuple(self._balls)

"""
1
Generic class declarations thường dùng multiple inheritance, 
Vì ta muốn subclass Generic để xác định formal type parameters để return, kiểu T.

2
The items argument in __init__ is of type Iterable[T], which becomes Iterable[int] 
when an instance is declared as LottoBlower[int].

3
The load method is likewise constrained.

4
The return type of T now becomes int in a LottoBlower[int].

5
No type variable here.

6
Finally, T sets the type of the items in the returned tuple.
"""