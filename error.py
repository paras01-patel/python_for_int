# 1. Error Handling Kya Hoti hai?
# Jab aapko lagta hai ki kisi code me error aa sakti hai, toh aap use try block ke andar likhte hain. Agar wahan error aati hai, toh Python seedha except block me chala jata hai aur program band nahi hota.

# Example A: Zero Division Error
# Python
# try:
#     # Yeh code run karne ki koshish karenge
#     num = 10 / 0
#     print("Answer:", num)
# except ZeroDivisionError:
#     # Agar zero se divide karne ki error aayi, toh yeh chalega
#     print("Dhyan dein! Aap kisi bhi number ko 0 se divide nahi kar sakte.")
# Example B: Value Error (Galat Input dena)
# Python
# try:
#     age = int(input("Apni age likhiye: "))
#     print("Aapki age", age, "hai.")
# except ValueError:
#     # Agar user ne number ki jagah koi text likh diya
#     print("Galti! Kripya sirf number enter karein.")