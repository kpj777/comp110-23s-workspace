""" for loop practice"""

xs:list[int] = (1, 2, 3)

i: int = 0
while i < len(xs):
    element: int = xs[i]
    print(element)
    i += 1


for element in xs:
    ##creates the variable element for you
    print(element)

names: list[str] = ["amy", "carl", "joe"]

for idx in range(0,3):
    print(f"{idx}:{names[idx]}")






