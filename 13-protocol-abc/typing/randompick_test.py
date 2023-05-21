import random
from typing import Any, Iterable, TYPE_CHECKING

from randompick import RandomPicker  # <1>

class SimplePicker:  # <2>
    def __init__(self, items: Iterable) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self) -> Any:  # <3>
        return self._items.pop()

def test_isinstance() -> None:  # <4>
    popper: RandomPicker = SimplePicker([1])  # <5>
    assert isinstance(popper, RandomPicker)  # <6>

def test_item_type() -> None:  # <7>
    items = [1, 2]
    popper = SimplePicker(items)
    item = popper.pick()
    assert item in items
    if TYPE_CHECKING:
        reveal_type(item)  # <8>
    assert isinstance(item, int)

"""
1
It’s not necessary to import the static protocol to define a class that implements it. Here I imported RandomPicker only to use it on test_isinstance later.

2
SimplePicker implements RandomPicker—but it does not subclass it. This is static duck typing in action.

3
Any is the default return type, so this annotation is not strictly necessary, but it does make it more clear that we are implementing the RandomPicker protocol as defined in Example 13-18.

4
Don’t forget to add -> None hints to your tests if you want Mypy to look at them.

5
I added a type hint for the popper variable to show that Mypy understands that SimplePicker is consistent-with.

6
This test proves that an instance of SimplePicker is also an instance of RandomPicker. This works because of the @runtime_checkable decorator applied to RandomPicker, and because SimplePicker has a pick method as required.

7
This test invokes the pick method from a SimplePicker, verifies that it returns one of the items given to SimplePicker, and then does static and runtime checks on the returned item.

8
This line generates a note in the Mypy output.
"""