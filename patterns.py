# Pattern 1: Right-Angled Triangle (Seedha Triangle) ⭐
# Yeh pattern har row mein ek-ek star badhata hai:

# Python
# print("--- Pattern 1 ---")
# for i in range(1, 6):
#     print("*" * i)
# Output:

# Plaintext
# *
# **
# ***
# ****
# *****
# Pattern 2: Inverted Right-Angled Triangle (Ulta Triangle) 🙃
# Yeh pattern shuru mein saare stars dikhata hai aur phir ek-ek kam karta hai:

# Python
# print("--- Pattern 2 ---")
# for i in range(5, 0, -1):
#     print("*" * i)
# Output:

# Plaintext
# *****
# ****
# ***
# **
# *
# Pattern 3: Square Pattern (Chaukona Box) 🔲
# Yeh pattern rows aur columns ki barabar sankhya me stars print karta hai:

# Python
# print("--- Pattern 3 ---")
# for i in range(4):
#     print("* * * * *")
# Output:

# Plaintext
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# Pattern 4: Number Triangle (Numbers ka Triangle) 🔢
# Stars ki jagah yahan numbers print hote hain:

# Python
# print("--- Pattern 4 ---")
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # Nayi line ke liye
# Output:

# Plaintext
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# Pattern 5: Pyramid Pattern (Pyramid Star) 🔺
# Center mein alignment ke sath proper pyramid banane ka code:

# Python
# print("--- Pattern 5 ---")
# for i in range(1, 6):
#     # Spaces aur Stars ko combine karna
#     print(" " * (5 - i) + "* " * i)
# Output:

# Plaintext
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *