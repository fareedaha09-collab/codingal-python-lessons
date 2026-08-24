print("#*30  ")
print("welcome to ride builder")
print("#*30 ")

print("step1: pick your vehicle")
print("  1- bike")
print("  2- car")
print()

choice = int(input("Enter 1 or 2:  "))
print()


if choice == 1:
    print("step 2: pick your bike type")
    print("1 - scooty")
    print("2 - mountain bike")
    print()

    bike_type = int(input("enter 1 or 2:  "))
    print()

    if bike_type ==1:
        print("you picked  : scooty")
        print("top speed   : 80km/h")
        print("best for   :  city roads")
    else: 
        print("you picked  : mountain bike")
        print("top speed   : 40km/h")
        print("best for   :  off-roads trails")
elif choice == 2:
    print("step 2: pick your car type")
    print("1 - sedan")
    print("2 - SUV")
    print()

    car_type = int(input("enter 1 or 2: "))
    print()

    if car_type == 1:
        print("you picked   :sedan")
        print("seats    : 5 passengers")
        print("best for  : family trips")
    else:
        print("you picked   :SUV")
        print("seats    : 7 passengers")
        print("best for  : off-road adventures")

else:
    print("that was not a valid choice")
    print("please enter 1 for bike or 2 for car")

print()
print("")
print("your custom ride is ready!")
print("enjoy the journey!")
print()