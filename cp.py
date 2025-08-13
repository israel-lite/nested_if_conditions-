values = [False, True]

print("Truth Table: NOT")
print("A  | NOT A")
print("-----------")
for A in values:
    print(f"{int(A)}  |   {int(not A)}")
print()

print("Truth Table: AND")
print("A  B | A AND B")
print("----------------")
for A in values:
    for B in values:
        print(f"{int(A)}  {int(B)} |    {int(A and B)}")
print()

print("Truth Table: OR")
print("A  B | A OR B")
print("---------------")
for A in values:
    for B in values:
        print(f"{int(A)}  {int(B)} |   {int(A or B)}")
print()

print("Truth Table: XOR")
print("A  B | A XOR B")
print("----------------")
for A in values:
    for B in values:
        xor = (A and not B) or (not A and B)
        print(f"{int(A)}  {int(B)} |    {int(xor)}")
