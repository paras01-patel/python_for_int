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