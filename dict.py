#     1. Dictionary Kya Hoti hai?
# Dictionary ko curly braces { } ke andar banaya jata hai. Isme har element ek Key aur ek Value ke pair mein hota hai (key: value).

# Python
# # Ek user profile ki dictionary
# user_profile = {
#     "name": "Priya",
#     "weight": 84,
#     "height": "5.9 ft",
#     "goal": "Weight Loss",
#     "is_veg": True
# }

# print(user_profile)
# 2. Dictionary se Data Kaise Access Karein?
# List ki tarah isme index numbers (0, 1, 2) ki zaroorat nahi padti. Aap seedha Key ka naam likh kar uski value nikal sakte hain:

# Python
# user_profile = {
#     "name": "Priya",
#     "weight": 84,
#     "goal": "Weight Loss"
# }

# # Key ke zariye value nikalna
# print(user_profile["name"])  # Output: Priya
# print(user_profile["goal"])  # Output: Weight Loss