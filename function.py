# # # # 1. Variables aur Basic Print
# # # naam = "Priya"
# # # vajan = 84
# # # height = 5.9

# # # print("--- User Profile ---")
# # # print("Naam:", naam)
# # # print("Vajan:", vajan, "kg")
# # # print("Height:", height, "feet")


# # # # 2. If-Else Condition (Weight Check)
# # # print("\n--- Weight Status ---")
# # # if vajan > 70:
# # #     print("Sujhav: Aapko weight loss diet aur cardio plan par dhyan dena chahiye.")
# # # else:
# # #     print("Sujhav: Aapka weight normal range me hai.")


# # # # 3. For Loop (Diet Items Print Karna)
# # # print("\n--- Daily Diet Items ---")
# # # diet_list = ["Oats", "Besan Chilla", "Paneer", "Soya Chunks", "Salad"]

# # # for index, item in enumerate(diet_list, start=1):
# # #     print(f"Item {index}: {item}")


# # # # 4. Function (Calculation ke liye)
# # # def add_numbers(a, b):
# # #     return a + b


# # # total = add_numbers(40, 44)
# # # print("\n--- Function Output ---")
# # # print("Total Calculation (40 + 44):", total)



# # 1. Built-in Functions (Pre-defined functions)
# # Yeh wo functions hote hain jo Python mein pehle se hi bane-banaye aate hain. Inhe use karne ke liye hamein koi code likh kar define nahi karna padta, bas seedha call karna hota hai.

# # Examples:

# # print() — Screen par kuch dikhane ke liye.

# # len() — Kisi list ya string ki lambai (length) pata karne ke liye.

# # type() — Variable ka data type check karne ke liye.

# # sum() — Numbers ka jod nikalne ke liye.

# # Code Example:

# # Python
# # naam = "Priya"
# # vajan_list = [70, 75, 84]

# # print("Naam ki lambai:", len(naam))      # Output: 5
# # print("Total vajan:", sum(vajan_list))    # Output: 229
# # print("Data type:", type(vajan_list))     # Output: <class 'list'>
# # 2. User-Defined Functions (Custom functions)
# # Yeh wo functions hote hain jo programmer (hum khud) apni zaroorat ke hisaab se banate hain. Inhe banane ke liye def keyword ka use hota hai.

# # Code Example:

# # Python
# # # Ek custom function banana jo greeting de
# # def welcome_message(user_name):
# #     print("Welcome,", user_name, "!")

# # # Function ko call karna
# # welcome_message("Priya")
# # 🔹 User-Defined Functions ke bhi kuch khaas types hote hain:
# # Bina Argument aur Bina Return value ke (Simple Function):

# # Python
# # def say_hello():
# #     print("Hello!")

# # say_hello()
# # Argument ke sath (Inputs ke sath):

# # Python
# # def multiply(a, b):
# #     print(a * b)

# # multiply(5, 4)  # Output: 20
# # Return value ke sath (Result wapas dene wala):

# # Python
# # def square(number):
# #     return number * number

# # result = square(6)
# # print(result)  # Output: 36
# # Lambda Functions (Anonymous / One-line functions):
# # Aise functions jinka koi naam nahi hota aur yeh ek hi line me likhe jaate hain (lambda keyword use karke):

# # Python
# # # Ek line me square nikalne ka function
# # find_square = lambda x: x * x

# # print(find_square(5))  # Output: 25


# 1. No Arguments, No Return Value (Na input, na output)
# Yeh sabse simple function hota hai. Isme na toh hum andar koi value bhejte hain, aur na hi yeh kuch return karta hai. Yeh bas apna kaam karke chupchap print kar deta hai.

# Python
# def print_banner():
#     print("-------------------")
#     print("  PYTHON PROGRAM   ")
#     print("-------------------")

# # Function ko chalana
# print_banner()
# 2. With Arguments, No Return Value (Input hai, par return nahi)
# Is type ke function mein hum andar kuch values (inputs) bhejte hain (arguments), wo unpe kaam karta hai, par koi value wapas (return) nahi deta—bas wahi print ya display kar deta hai.

# Python
# def greet_user(name):
#     print("Hello,", name, "! Kaise hain aap?")

# # Input bhejna
# greet_user("Priya")






# 3. With Arguments and Return Value (Input bhi hai, aur output bhi wapas milta hai)
# Yeh sabse zyada use hone wala type hai. Isme hum function ko data dete hain, wo andar calculation karta hai, aur return keyword ka use karke final result humein wapas deta hai taaki hum use kisi variable me store kar sakein.

# Python
# def multiply_numbers(a, b):
#     result = a * b
#     return result  # Result wapas bhej raha hai

# # Wapas aaye hue result ko variable me save karna
# ans = multiply_numbers(5, 4)
# print("Calculation ka answer:", ans)  # Output: 20
# 4. Lambda Functions / Anonymous Functions (Ek line ka chota function)
# Aise functions jinka koi naam nahi hota (anonymous), aur unhein poore def syntax ki jagah sirf ek hi line mein likh diya jaata hai. Inme lambda keyword ka use hota hai.

# Python
# # Ek line me square (varg) nikalne ka function
# find_square = lambda x: x * x

# print(find_square(6))  # Output: 36