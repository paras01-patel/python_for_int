# # 1. Python Operators (Gana-Gana ya Comparison karne ke liye)
# # Python me alag-alag kaam karne ke liye operators ka use hota hai:

# # A. Arithmetic Operators (Maths karne ke liye)
# # + (Addition - Jodna)

# # - (Subtraction - Ghataana)

# # * (Multiplication - Guna karna)

# # / (Division - Bhaag dena, result decimal me aayega)

# # % (Modulus - Bhaag dene ke baad Remainder / Shesh bachna)

# # Python
# # x = 10
# # y = 3

# # print("Jod (Addition):", x + y)        # 13
# # print("Bhaag (Division):", x / y)      # 3.3333...
# # print("Remainder (Modulus):", x % y)   # 1
# # B. Comparison Operators (Tulna karne ke liye - Result True/False)
# # == (Barabar hai?)

# # != (Barabar nahi hai?)

# # > (Bada hai?)

# # < (Chota hai?)

# # >= (Bada ya barabar hai?)

# # <= (Chota ya barabar hai?)

# # Python
# # my_age = 20
# # required_age = 18

# # # print(my_age >= required_age) # Output: True


# 2. Conditional Statements (If, Elif, Else)
# Jab hume kisi condition ke hisaab se faisla (decision) lena hota hai, tab hum if-elif-else ka use karte hain.

# 💡 Note (Indentation): Python me code block batane ke liye if ke baad 4 spaces (tab) chodna zaroori hota hai.

# Example Code: Grade System
# Python
# marks = 85

# if marks >= 90:
#     print("Grade: A+")
# elif marks >= 75:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# else:
#     print("Grade: Fail / Re-appear")
# 3. Ek Real-Life Mini Project: Water Intake Calculator 💧
# Yeh program check karega ki aapne aaj kitna paani piya hai aur aapko suggestion dega:

# Python
# # User se water intake (liters) pūchhna
# water_drank = float(input("Aaj kitne liters paani piya? "))
# target = 3.5  # Daily goal in Liters

# if water_drank >= target:
#     print("Shabaash! Aapka daily water target pura ho gaya. 🎉")
# elif water_drank >= 2.0:
#     print("Accha hai, par target (3.5L) pura karne ke liye thoda aur paani piyein! 🥛")
# else:
#     print("Dhyan dein! Aapne bahut kam paani piya hai. Abhi 1-2 glass paani piyein. ⚠️