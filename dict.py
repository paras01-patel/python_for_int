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




# 3. Dictionary mein Data Jodna ya Badalna (Modify karna)
# Aap kisi nayi key ko add kar sakte hain ya purani value ko update kar sakte hain:

# Python
# student = {
#     "name": "Rahul",
#     "score": 85
# }

# # 1. Nayi key-value jodna
# student["city"] = "Indore"

# # 2. Purani value ko update karna
# student["score"] = 90

# print(student)
# # Output: {'name': 'Rahul', 'score': 90, 'city': 'Indore'}
# 4. Dictionary ke Kuch Useful Methods
# .keys(): Sirf saari keys nikalne ke liye.

# .values(): Sirf saari values nikalne ke liye.

# .items(): Saare keys aur values ke pairs nikalne ke liye.

# Python
# car = {
#     "brand": "Hyundai",
#     "model": "i20",
#     "year": 2022
# }

# print(car.keys())    # Output: dict_keys(['brand', 'model', 'year'])
# print(car.values())  # Output: dict_values(['Hyundai', 'i20', 2022])