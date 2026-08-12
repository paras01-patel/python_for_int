Question 1: Voting Eligibility (Vot dene ki yogyata)
Python
print("--- Q1: Voting Eligibility ---")
age = int(input("Apni age enter karein: "))

if age >= 18:
    print("Aap vote de sakte hain! 🎉")
else:
    print("Aap abhi chote hain, vote nahi de sakte. ❌")
Question 2: Even or Odd Number (Sam ya Visham sankhya)
Python
print("\n--- Q2: Even or Odd Number ---")
num = 14  # Aap yahan koi bhi number badal kar check kar sakti hain

if num % 2 == 0:
    print(num, "ek Even (Sam) number hai.")
else:
    print(num, "ek Odd (Visham) number hai.")
    
    
    
Question 3: Largest of Two Numbers (Do numbers me bada kaun?)
Python
print("\n--- Q3: Largest of Two Numbers ---")
num1 = 45
num2 = 60

if num1 > num2:
    print("Pehla number bada hai:", num1)
elif num2 > num1:
    print("Dusra number bada hai:", num2)
else:
    print("Dono numbers barabar hain!")
Question 4: Pass / Fail Exam Checker
Python
print("\n--- Q4: Pass / Fail Exam Checker ---")
marks = 72  # Student ke marks

if marks >= 40:
    print("Pass ho gaye! 🎉 (Aapke marks hain:", marks, ")")
else:
    print("Fail / Re-appear ❌ (Aur mehnat ki zaroorat hai)")
    
    
Question 5: Fitness Weight Category
Python
print("\n--- Q5: Fitness Weight Category ---")
weight = 84  # Kg me weight

if weight < 70:
    print("Aapka weight normal range me hai.")
elif weight <= 85:
    print("Aapko thoda weight management aur cardio par dhyan dena chahiye. 👍")
else:
    print("Strict diet aur daily 10k steps ka target follow karein! 💧")
    
    
    
Question 6: Positive, Negative, or Zero (Number check)
Problem: Ek variable me number lijiye aur check kijiye ki wo Positive hai, Negative hai, ya Zero ke barabar hai.

Python
print("--- Q6: Positive/Negative/Zero ---")
num = -8

if num > 0:
    print(num, "ek Positive number hai.")
elif num < 0:
    print(num, "ek Negative number hai.")
else:
    print("Yeh number Zero (0) hai.")
Question 7: Leap Year Checker (Leap varsh ki jaanch)
Problem: Ek saal (year) variable lijiye aur pata kijiye ki wo Leap Year hai ya nahi.

Hint: Jo saal 4 se divide ho aur 100 se na ho, ya 400 se poora divide ho, wo leap year hota hai.

Python
print("\n--- Q7: Leap Year Checker ---")
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "ek Leap Year hai! 📅")
else:
    print(year, "Leap Year nahi hai.  ")


Question 8: Greatest of Three Numbers (Teen numbers me sabse bada kaun?)
Problem: Teen alag-alag variables me numbers lijiye (jaise a = 25, b = 40, c = 30) aur pata lagaiye ki sabse bada number kaun sa hai.

Python
print("\n--- Q8: Greatest of Three Numbers ---")
a = 25
b = 40
c = 30

if a >= b and a >= c:
    print("Sabse bada number hai:", a)
elif b >= a and b >= c:
    print("Sabse bada number hai:", b)
else:
    print("Sabse bada number hai:", c)
    
    
Question 9: School Grade Calculator (Grades nikalna)
Problem: Student ke score ke hisaab se grade print karein:

Score >= 90: Grade A+

Score >= 75: Grade A

Score >= 60: Grade B

Baaki sabke liye: Grade C

Python
print("\n--- Q9: School Grade Calculator ---")
score = 82

if score >= 90:
    print("Grade: A+ 🎉")
elif score >= 75:
    print("Grade: A 👍")
elif score >= 60:
    print("Grade: B 🙂")
else:
    print("Grade: C (Aur mehnat karein) ⚠️")
Question 10: Hydration Status Checker (Paani peene ka target)
Problem: Aaj kitna paani piya (liters me) uska variable lijiye (jaise 3.0). Target 3.5L hai:

Agar 3.5 ya usse zyada hai: "Target pura! 🎉"

Agar 2.0 se 3.4 ke beech hai: "Thoda aur paani piyein! 💧"

Agar 2.0 se kam hai: "Bahut kam paani piya, abhi glass piyein! ⚠️"

Python
print("\n--- Q10: Hydration Status Checker ---")
water_drunk = 3.0
target = 3.5

if water_drunk >= target:
    print("Shabaash! Aapka daily water target pura ho gaya. 🎉")
elif water_drunk >= 2.0:
    print("Accha hai, par target (3.5L) tak pahunchne ke liye thoda aur paani piyein! 💧")
else:
    print("Dhyan dein! Aapne bahut kam paani piya hai. Abhi 1-2 glass paani piyein.