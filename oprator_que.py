Python ke Operators (jaise Arithmetic +, -, *, /, Comparison >, <, Logical and, or, aur Assignment +=) ki practice karne ke liye yahan 5 behtareen coding questions aur unke solutions diye gaye hain:Question 1: Arithmetic Operators (Power aur Area nikalna)Problem: Ek square ki side 12 cm hai. ** (exponent/power) operator ka use karke uska Area ($side^2$) calculate karein.Pythonprint("--- Q1: Square Area using Exponent Operator ---")
side = 12
area = side ** 2  # Power operator (**) ka use

print("Square ki side:", side, "cm")
print("Square ka Area hai:", area, "sq cm 📐")
Question 2: Comparison Operators (Speed Limit Checker)Problem: Ek gaadi ki speed 85 km/h hai aur road ki speed limit 80 km/h hai. Comparison operator (>) ka use karke check karein ki kya gaadi overspeeding kar rahi hai.Pythonprint("\n--- Q2: Speed Limit Comparison ---")
car_speed = 85
speed_limit = 80

is_overspeeding = car_speed > speed_limit

print("Gaadi ki speed:", car_speed)
print("Kya overspeeding ho rahi hai?:", is_overspeeding)