import numpy as np

#suppose a circle has r=1
def guess_pi(n):
    points_circle = total_points = 0

    for i in range(0,n):
        #init point P(x,y)
        y = np.random.uniform(-1,1)
        x = np.random.uniform(-1,1)

        if(x**2 + y**2 <= 1): #check if point P(x,y) is in the circle
            points_circle += 1
        total_points += 1
    return 4*points_circle/total_points

# tol = 1e-5 #minimal error
# for i in range(100,10000):
#     my_pi = guess_pi(i)
#     if(np.abs(np.pi - my_pi) <= tol): 
#         break

my_pi = guess_pi(1000) 
print(np.pi, my_pi)

my_pi = guess_pi(10000) 
print(np.pi, my_pi)

my_pi = guess_pi(100000) 
print(np.pi, my_pi)

my_pi = guess_pi(1000000) 
print(np.pi, my_pi)
