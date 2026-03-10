# # 1. Variables aur Different Data Types ka Code
# # Python mein variable banane ke liye koi data type likhne ki zaroorat nahi padti, Python khud samajh jata hai ki value kis type ki hai.

# # Python
# # # 1. Integer (Poore numbers / Whole numbers)
# # age = 22
# # weight = 84  # Aapka weight

# # # 2. Float (Decimal numbers / Point wale numbers)
# # height_feet = 5.9
# # temperature = 36.6

# # # 3. String (Text / Words)
# # name = "Priya"
# # city = "Indore"

# # # 4. Boolean (True ya False)
# # is_fitness_goal = True
# # is_raining = False

# # # Print karke values dekhna
# # print("Naam:", name)
# # print("Vajan:", weight, "kg")
# # print("Height:", height_feet, "feet")
# # print("Kya fitness goal hai?", is_fitness_goal)
# # 2. Variables ke sath Calculation ka Code
# # Aap variables ke upar maths ke operations (+, -, *, /) bhi kar sakte hain:

# # Python
# # # Do numbers ka sum ya calculation
# # item1_price = 450
# # item2_price = 300

# # total_price = item1_price + item2_price
# # discount = 50

# # final_price = total_price - discount

# # print("Total Bill:", total_price)
# # print("Discount ke baad final price:", final_price)

# 3. List aur Dictionary Variables (Advanced)
# Jab aapko ek sath kayi saari values store karni ho, toh List ya Dictionary ka use hota hai:

# List (Multiple items ko order mein rakhna):
# Python
# # Diet items ki list
# diet_food = ["Oats", "Paneer", "Besan Chilla", "Soya Chunks", "Salad"]

# print("Pehla food item:", diet_food[0])  # Output: Oats
# print("Dusra food item:", diet_food[1])  # Output: Paneer

# # List mein naya item jodna
# diet_food.append("Fruits")
# print("Updated Diet List:", diet_food)
# Dictionary (Key-Value pair mein data store karna):
# Python
# # Apni profile ki details ek dictionary mein store karna
# user_profile = {
#     "name": "Priya",
#     "weight": 84,
#     "height": "5.9 ft",
#     "goal": "Weight Loss",
#     "is_veg": True
# }

# # Kisi specific value ko access karna
# print("User ka goal hai:", user_profile["goal"])
# print("User ka weight hai:", user_profile["weight"], "kg")
# 4. Ek Chota sa Complete Program (User Input ke sath)
# Yeh program user se unka naam aur weight lega aur ek chota message print karega:

# Python
# # User se input lena
# user_name = input("Apna naam likhiye: ")
# user_weight = float(input("Apna weight (kg mein) likhiye: "))

# print("---")
# print("Hello,", user_name)
# print("Aapka current weight", user_weight, "kg hai.")

# if user_weight > 70:
#     print(
#         "Suggstion: Aapko apne weight loss aur healthy diet par dhyan dena"
#         " chahiye!"
#     )
# else:
#     print("Aapka weight bilkul fit range mein hai.")