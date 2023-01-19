"""knock knock jokes"""

inter_cow: str = input("do you want an interupitng cow? ")

print("knock knock")

if (inter_cow == "yes"):
    print("who's there?")
    print("Interrupting cow.")
    print("...interupting cow wh-")
    print("MOOO!")
else:
    print("Oh...okay")

if (inter_cow == "your not funny"):
    print("wow... that hurts my feelings")