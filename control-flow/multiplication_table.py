number = int(input("Enter a number to see its multiplication table: "))

for x in range(1, 11):
    z = int(number) * x
    print(f"{number} X {x} = {z}")
