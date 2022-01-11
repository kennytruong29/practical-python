# bounce.py
#
# Exercise 1.5
#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
#it bounces back up to 3/5 the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.

initial_height = 100
bounce_height = .60 # 3/5 of the original height each time it bounces back up
bounces = 1
for i in range(1, 10):
    final_height = initial_height * bounce_height
    initial_height = final_height
    bounces = bounces + 1
    print(bounces, round(final_height,4))
