from typing import Protocol, runtime_checkable
from randompick import RandomPicker

@runtime_checkable  # <1>
class LoadableRandomPicker(RandomPicker, Protocol):  # <2>
    def load(self, Iterable) -> None: ...  # <3>

"""
1
If you want the derived protocol to be runtime checkable, you must apply the decorator again—its behavior is not inherited.22

2
Every protocol must explicitly name typing.Protocol as one of its base classes in addition to the protocol we are extending. 
This is different from the way inheritance works in Python.23

3 Back to “regular” object-oriented programming: we only need to declare the method that is new in this derived 
protocol. The pick method declaration is inherited from RandomPicker. 
"""