print("enter marks obtained in 5 subject")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validrange = range(0,101)

if avg not in validrange:
    print("invalid input!")
elif avg in range(91,101):
    print("your garde is A1")
elif avg in range(81,91):
    print("your garde is A2")
elif avg in range(71,81):
    print("your garde is B1")
elif avg in range(61,71):
    print("your garde is B2")
elif avg in range(51,61):
    print("your garde is c1")
elif avg in range(41,51):
    print("your garde is C2")
elif avg in range(31, 41):
    print("your garde is D")
elif avg in range(21,31):
    print("your garde is E1")
elif avg in range(0,21):
    print("your garde is E2")
