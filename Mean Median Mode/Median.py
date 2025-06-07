import numpy as np 

speed = [23, 3, 4, 4, 5, 6, 6, 77, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

x = np.median(speed)
print("Median of speed is: ", x)

#If there are two value in the middle, divide the sum of those two numbers by 2
speed2 = [23, 3, 4, 4, 5, 6, 6, 77, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
x2 = np.median(speed2)
print("Median of speed2 is: ", x2)