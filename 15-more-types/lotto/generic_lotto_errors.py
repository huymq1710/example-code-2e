from generic_lotto import LottoBlower

machine = LottoBlower[int]([1, .2])
## error: List item 1 has incompatible type "float";  # <1>
##        expected "int"

machine = LottoBlower[int](range(1, 11))

machine.load('ABC')
## error: Argument 1 to "load" of "LottoBlower"  # <2>
##        has incompatible type "str";
##        expected "Iterable[int]"
## note:  Following member(s) of "str" have conflicts:
## note:      Expected:
## note:          def __iter__(self) -> Iterator[int]
## note:      Got:
## note:          def __iter__(self) -> Iterator[str]

"""
1
Upon instantiation of LottoBlower[int], Mypy flags the float.

2
When calling .load('ABC'), Mypy explains why a str won’t do: str.__iter__ returns an Iterator[str], 
but LottoBlower[int] requires an Iterator[int].
"""