from scipy import stats


#The Mode value is the value that appears the most number of times:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)