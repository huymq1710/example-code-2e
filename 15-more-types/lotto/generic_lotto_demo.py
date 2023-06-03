#!/usr/bin/env python3

from typing import TYPE_CHECKING

# tag::LOTTO_USE[]
from generic_lotto import LottoBlower

machine = LottoBlower[int](range(1, 11))  # <1>

first = machine.pick()  # <2>
remain = machine.inspect()  # <3>
# end::LOTTO_USE[]

expected = set(i for i in range(1, 11) if i != first)

assert set(remain) == expected

print('picked:', first)
print('remain:', remain)

if TYPE_CHECKING:
    reveal_type(first)
    # Revealed type is 'builtins.int*'
if TYPE_CHECKING:
    reveal_type(remain)
    # Revealed type is 'builtins.tuple[builtins.int*]'

"""
1
To instantiate a generic class, we give it an actual type parameter, like int here.

2
Mypy will correctly infer that first is an int…

3
… and that remain is a tuple of integers.
"""