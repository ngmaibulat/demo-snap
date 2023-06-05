from functools import reduce
from typing import Callable


def compose(*functions):
    return reduce(lambda current, next: lambda x: next(current(x)), functions)


def adder(x: float) -> Callable[[float], float]:
    def fn(y: float) -> float:
        return x + y

    return fn


def tagger(tag: str) -> Callable[[str], str]:
    def fn(content: str) -> str:
        return f"<{tag}>{content}</{tag}>"

    return fn


div = tagger("div")

print(div("Hello World!"))


add_10 = lambda x: x + 10


add_1 = adder(1)
add_10 = adder(10)

result = compose(add_10, add_1, add_10)(1)
print(result)

print(add_10(add_1(1)))
