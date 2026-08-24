currentavg= 38
totalnumbers = 40
correctNum = 56
wrongNum = 36

currentsum = currentavg * totalnumbers
#print(currentsum)
diff = correctNum - wrongNum
correctsum = currentsum + diff
correctavg = correctsum /   totalnumbers
print(f"correct Avg : {correctavg}")
