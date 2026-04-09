# # 1. For Loop (Jab aapko pata ho ki kaam kitni baar chalana hai)
# # for loop ka use kisi Sequence (jaise List, String, ya Range) ke har ek item par iterate (jaane) ke liye kiya jata hai.

# # Example A: Range ke sath
# # Python
# # # 1 se 5 tak numbers print karna
# # for i in range(1, 6):
# #     print("Number:", i)
# # Example B: List ke items par loop chalana
# # Python
# # # Diet items ki list par loop chalana
# # diet_items = ["Oats", "Paneer Chilla", "Soya Chunks", "Salad"]

# # for food in diet_items:
# #     print("Aaj khana hai:", food)



# 2. While Loop (Jab tak condition True rahe, tab tak chalega)
# while loop tab tak chalta rehta hai jab tak di gayi condition True hoti hai. Jaise hi condition False hoti hai, loop ruk jata hai.

# Example: Counter chalu rakhna
# Python
# count = 1

# while count <= 3:
#     print("Yeh loop ka round number hai:", count)
#     count = count + 1  # Har baar count badhana zaroori hai, warna infinite loop ban jayega
# 3. Loop Control Statements (Break aur Continue)
# break: Loop ko beech mein hi rokne ke liye use hota hai.

# continue: Current round ko skip karke seedha agle round par jaane ke liye.

# Python
# # 'break' ka example
# for number in range(1, 10):
#     if number == 5:
#         print("Number 5 aa gaya, loop roko!")
#         break
#     print(number)
# 💡 Ek Practical Mini Program: Daily Calorie / Meal Tracker Loop
# Yeh program aapke diet list ke saare items ko ek-ek karke dikhayega aur unhe track karega:

# Python
# # Daily meals ki list
# meals = ["Breakfast: Besan Chilla", "Lunch: Roti & Dal", "Snack: Roasted Chana", "Dinner: Soya Chunks"]

# print("--- Aapka Aaj ka Meal Schedule ---")
# for index, meal in enumerate(meals, start=1):
#     print(f"Meal {index}: {meal}")