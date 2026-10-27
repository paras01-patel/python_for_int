# Python ke Operators (jaise Arithmetic +, -, *, /, Comparison >, <, Logical and, or, aur Assignment +=) ki practice karne ke liye yahan 5 behtareen coding questions aur unke solutions diye gaye hain:Question 1: Arithmetic Operators (Power aur Area nikalna)Problem: Ek square ki side 12 cm hai. ** (exponent/power) operator ka use karke uska Area ($side^2$) calculate karein.Pythonprint("--- Q1: Square Area using Exponent Operator ---")
# side = 12
# area = side ** 2  # Power operator (**) ka use

# print("Square ki side:", side, "cm")
# print("Square ka Area hai:", area, "sq cm 📐")
# Question 2: Comparison Operators (Speed Limit Checker)Problem: Ek gaadi ki speed 85 km/h hai aur road ki speed limit 80 km/h hai. Comparison operator (>) ka use karke check karein ki kya gaadi overspeeding kar rahi hai.Pythonprint("\n--- Q2: Speed Limit Comparison ---")
# car_speed = 85
# speed_limit = 80

# is_overspeeding = car_speed > speed_limit

# print("Gaadi ki speed:", car_speed)
# print("Kya overspeeding ho rahi hai?:", is_overspeeding)


# Question 3: Logical Operators (and & or)
# Problem: Ek club me entry ke liye age 18 ya usse zyada honi chahiye aur paas me ID card hona chahiye (has_id = True). Logical and operator ka use karke check karein ki entry milegi ya nahi.

# Python
# print("\n--- Q3: Club Entry using Logical Operators ---")
# age = 20
# has_id = True

# # 'and' tabhi True dega jab dono conditions sahi hongi
# can_enter = (age >= 18) and has_id

# print("Kya entry milti hai?:", can_enter)
# Question 4: Assignment Operators (+= aur -=)
# Problem: Aapke paas shuru me 5000 rs the. Pehle 1200 rs shopping me jode (+=) aur phir 500 rs ka bill pay karke kam kiye (-=). Final balance nikalein.

# Python
# print("\n--- Q4: Wallet Balance using Assignment Operators ---")
# wallet = 5000
# print("Shuru ka balance:", wallet)

# wallet += 1200  # Paise aana (Addition assignment)
# print("1200 milne ke baad:", wallet)

# wallet -= 500   # Paise kharch hona (Subtraction assignment)
# print("500 kharch karne ke baad final balance:", wallet, "rs")

# Question 5: Modulus Operator (% - Remainder nikalna)
# Problem: Aapke paas 45 chocolates hain aur unhein 4 doston me barabar baantna hai. Pata karein ki baantne ke baad kitni chocolates bachengi (Remainder).

# Python
# print("\n--- Q5: Chocolates Remainder using Modulus ---")
# total_chocolates = 45
# friends = 4

# # Modulus operator (%) remainder deta hai
# leftover_chocolates = total_chocolates % friends

# print("Kul chocolates:", total_chocolates)
# print("Dost:", friends)
# print("Baantne ke baad bachi hui chocolates (Remainder):", leftover_chocolates, "🍫")

# Question 6: Floor Division Operator (//)
# Problem: Aapne aaj ke din mein total 14,250 steps chale hain. // (floor division) operator ka use karke pata lagayein ki aapne kitne poore thousands (hazaaron) ke milestones cross kiye hain.

# Python
# print("--- Q6: Floor Division Operator ---")
# steps = 14250
# # 1000 se divide karke integer quotient nikalna
# thousands_milestone = steps // 1000

# print("Total steps:", steps)
# print("Poore thousand milestones cross kiye:", thousands_milestone, "hazaar 👟")


# Question 7: Membership Operator (in)
# Problem: Aapki allowed diet list hai: ["Oats", "Paneer", "Soya Chunks", "Fruits"]. Check karein ki kya "Paneer" is list mein maujood hai ya nahi (in operator ka use karke).

# Python
# print("\n--- Q7: Membership Operator (`in`) ---")
# diet_list = ["Oats", "Paneer", "Soya Chunks", "Fruits"]
# food_item = "Paneer"

# is_allowed = food_item in diet_list

# print("Kya diet list me", food_item, "shamil hai?:", is_allowed)


# Python
# print("\n--- Q8: Compound Assignment (`*=`) ---")
# water_target = 3.0
# print("Normal target:", water_target, "liters")

# # Workout day multiplier
# water_target *= 1.5  

# print("Workout day par updated water target:", water_target, "liters")