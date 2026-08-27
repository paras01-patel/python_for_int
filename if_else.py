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
    print("Dhyan dein! Aapne bahut kam paani piya hai. Abhi 1-2 glass paani piyein.)
          
          
Yahan agle 5 aur naye aur thode advanced if-else coding questions aur unke solutions diye gaye hain, jisme aapke fitness targets se juda hua ek sawaal bhi hai:

Question 11: Shopping Discount Calculator (Chhoot nikalna)
Problem: Total bill amount ke hisaab se discount calculate karein:

Agar bill 5000 se zyada hai: 20% discount 🎉

Agar bill 2000 se 5000 ke beech hai: 10% discount 👍

Agar 2000 se kam hai: Koi discount nahi ❌

Python
print("--- Q11: Shopping Discount Calculator ---")
bill_amount = 3500

if bill_amount > 5000:
    print("Badhai ho! Aapko 20% ka bada discount mila hai. 🎉")
elif bill_amount >= 2000:
    print("Accha hai! Aapko 10% ka discount mila hai. 👍")
else:
    print("Is bill par koi discount nahi hai. 2000 se upar ki kharidari par discount milega!")
Question 12: Triangle Validity Checker (Triangle ban sakta hai ya nahi?)
Problem: Teen sides (a, b, c) di gayi hain. Check karein ki kya ye ek valid triangle bana sakti hain.

Hint: Kisi bhi do sides ka sum teesri side se bada hona chahiye (a + b > c aur b + c > a aur a + c > b).

Python
print("\n--- Q12: Triangle Validity Checker ---")
a, b, c = 10, 12, 15

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Yeh teeno sides milkar ek valid triangle bana sakti hain! 📐")
else:
    print("Yeh triangle nahi ban sakta. ❌")
    
    
Question 13: Daily Step Count Target (Aapke fitness plan se juda!)
Problem: Aaj ke total steps ke liye variable lijiye (jaise 8500). Target 10,000 steps ka hai:

Agar steps >= 10,000: "Awesome! Daily step goal achieved! 🎯"

Agar steps >= 7,000: "Good job! Bas thodi si aur walking bachi hai. 👟"

Agar steps < 7,000: "Shaam ko thoda aur walk karein, target pura karna hai! 🚶‍♀️"

Python
print("\n--- Q13: Daily Step Count Target ---")
steps_walked = 8500

if steps_walked >= 10000:
    print("Awesome! Aapka 10k steps ka daily goal pura ho gaya! 🎯")
elif steps_walked >= 7000:
    print("Good job! Aap target ke bahut kareeb hain, thoda sa aur walk karein. 👟")
else:
    print("Aapke steps abhi kam hain. Chaliye, thodi der evening walk par chalte hain!")
    
    
Question 14: Simple Calculator (Basic Operations)
Problem: Do numbers (num1 = 20, num2 = 5) aur ek operator string ('+', '-', '*', '/') lijiye aur if-elif use karke calculation kariye.

Python
print("\n--- Q14: Simple Calculator ---")
num1 = 20
num2 = 5
operator = "*"

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    print("Result:", num1 / num2)
else:
    print("Galat operator chuna hai! Kripya +, -, *, ya / use karein.")
    
    
    
Question 15: Password Strength Checker (Password kitna mazboot hai?)
Problem: Ek password string ki lambai (len()) check karein:

Agar lambai 8 ya usse zyada hai: "Strong password! 🔒"

Agar lambai 5 se 7 ke beech hai: "Moderate password. Isko aur secure banayein. ⚠️"

Agar lambai 5 se kam hai: "Weak password! Kam se kam 8 characters use karein. ❌"

Python
print("\n--- Q15: Password Strength Checker ---")
password = "Priya@123"

if len(password) >= 8:
    print("Strong password! 🔒")
elif len(password) >= 5:
    print("Moderate password. Thoda aur lamba karein toh aur accha hoga. ⚠️")
else:
    print("Weak password! Kripya kam se kam 8 characters ka password banayein. ❌")
    
Question 16: Age Group Category (Umra ke hisaab se category)
Problem: User ki age ke hisaab se check karein ki wo kis group mein aati hai:

Age < 13: Child (Bacha)

Age 13 se 19: Teenager

Age 20 se 59: Adult

Age 60 ya usse zyada: Senior Citizen

Python
print("--- Q16: Age Group Category ---")
age = 28

if age < 13:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
elif age <= 59:
    print("Category: Adult 👍")
else:
    print("Category: Senior Citizen 🧓")
Question 17: BMI Calculator & Health Category (Aapke fitness plan se juda!)
Problem: BMI (Body Mass Index) calculate karein. Formula: weight / (height_m * height_m).

Agar BMI < 18.5: Underweight

Agar BMI 18.5 se 24.9: Normal weight 🎉

Agar BMI 25 se 29.9: Overweight ⚠️

Agar BMI 30 ya zyada: Obese

Python
print("\n--- Q17: BMI Calculator ---")
weight = 84  # kg mein
height_m = 1.75  # meters mein (approx 5'9")

bmi = weight / (height_m * height_m)
print("Aapka BMI aaya hai:", round(bmi, 2))

if bmi < 18.5:
    print("Status: Underweight")
elif bmi <= 24.9:
    print("Status: Normal Weight 🎉")
elif bmi <= 29.9:
    print("Status: Overweight. Thoda cardio aur diet par dhyan dein! 👟")
else:
    print("Status: Obese. Strict fitness plan follow karne ki zaroorat hai! 💧")
    
Question 18: Weekday vs Weekend Activity Planner
Problem: Din ka naam (day = "Saturday") lijiye aur check kariye ki wo weekday hai ya weekend:

Saturday ya Sunday: "Weekend hai! Relax karein ya long walk par jayein. 🌳"

Baaki din: "Weekday hai! Office/Study aur workout ka schedule follow karein. 💻"

Python
print("\n--- Q18: Weekday vs Weekend Planner ---")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(day, "-> Weekend hai! Relax karein ya long walk par jayein. 🌳")
else:
    print(day, "-> Weekday hai! Office/Study aur workout ka schedule follow karein. 💻")
    
Question 19: Temperature Advisory (Mausam ke hisaab se salah)
Problem: Temperature (temp = 32) ke hisaab se message print karein:

Temp > 35: "Bahut garmi hai! Hydrated rahein aur khoob paani piyein. ☀️"

Temp 20 se 35 ke beech: "Mausam bahut accha hai! Workout ke liye perfect. 🌤️"

Temp < 20: "Thand hai! Garam kapde pehnein. 🧥"

Python
print("\n--- Q19: Temperature Advisory ---")
temp = 32

if temp > 35:
    print("Bahut garmi hai! Hydrated rahein aur khoob paani piyein. ☀️")
elif temp >= 20:
    print("Mausam bahut accha hai! Walk aur workout ke liye perfect. 🌤️")
else:
    print("Thand hai! Garam kapde pehnein aur sehat ka dhyan rakhein. 🧥")
