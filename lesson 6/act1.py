print("smart school day by planner")
print("answer 3 quick questions and i will plan your day!\n")
day = input("what day is it? (monday to suday):").strip().capitalize()
weather = input(what's the weather?(sunny/rainy / cloudy):  ").strip().lower()     
homework = input ("homework done? (yes / no): ").strip().lower()

print()
print(f"your plan for {day}")
print("-" * 35)

if day in ("saturday", "sunday"):
    print("day type  :Weekend- enjoy your free time!")
elif day =="Monday":
    print("day type  : first day of the weeek. Pack your weekly planner.")
elif day == "friday":
    print("dqy type  : last school day . Return library books today.")
elif day in ("tuesday",  "wednesday", "thursday"):
    print("day type  : regular school day. Stay focused!")
else:
    print("day type : day not recognised. please check the spelling.")

if weather== "sunny" and "homework" == "yes":
    print("after school: head to the park - great weather and homework is done!")

if  weather == "rainy" or weather =="cloudy":
print("weather tip : pack your umbrella - it may get wet outside.")