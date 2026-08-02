from typing import Optional, List, Dict, Union


# Optional
def get_name(name: Optional[str]) -> str:
    if name is None:
        return "No name provided"
    return name


# List
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)


# Dict
def get_student() -> Dict[str, int]:
    return {"age": 20, "marks": 95}


# Uniongit statu
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2


print(get_name("Gour"))
print(get_name(None))

print(sum_numbers([1, 2, 3, 4, 5]))

print(get_student())

print(square(5))
print(square(2.5))