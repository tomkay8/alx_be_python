number = int(input("Enter the size of the pattern: "))

row = number

i = 1
while i <= row:
    j = 1
    for j in range(number):
        print("*", end = "")
    print()
    i+=1
    
