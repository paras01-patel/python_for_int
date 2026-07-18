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




# Pattern 6: Inverted Number Triangle (Ulta Number Triangle) 🔄
# Har row mein numbers kam hote jaate hain:

# Python
# print("--- Pattern 6 ---")
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# Output:

# Plaintext
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
# Pattern 7: Repeated Number Row Triangle (Same number repeat hona) 🔢
# Jis row ka number hota hai, wahi utni baar print hota hai:

# Python
# print("--- Pattern 7 ---")
# for i in range(1, 6):
#     print(str(i) * i)
# Output:

# Plaintext
# 1
# 22
# 333
# 4444
# 55555



# Pattern 8: Floyd's Triangle (Continuous Numbers) 📈
# Isme numbers lagataar aage badhte hain, row ke khatam hone par bhi rukte nahi:

# Python
# print("--- Pattern 8 ---")
# num = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()
# Output:

# Plaintext
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# Pattern 9: Diamond Pattern (Heere jaisa aakar) 💎
# Pyramid aur ulta pyramid ko mila kar ek khoobsurat diamond banta hai:

# Python
# print("--- Pattern 9 ---")
# # Upar ka hissa (Pyramid)
# for i in range(1, 4):
#     print(" " * (3 - i) + "* " * i)

# # Neeche ka hissa (Ulta Pyramid)
# for i in range(2, 0, -1):
#     print(" " * (3 - i) + "* " * i)
# Output:

# Plaintext
#   * 
#  * * 
# * * * 
#  * * 
#   * 
# Pattern 10: Alphabet Triangle (A, B, C characters ka triangle) 🔤
# Numbers ki jagah English alphabets (chr() function ki madad se) print karna:

# Python
# print("--- Pattern 10 ---")
# for i in range(1, 6):
#     for j in range(65, 65 + i):  # 65 ASCII value hai 'A' ki
#         print(chr(j), end=" ")
#     print()
# Output:

# Plaintext
# A 
# A B 
# A B C 
# A B C D 
# A B C D E




# Yahan agle 5 aur naye patterns hain jo aapke nested loops aur logic ko aur strong karenge:

# Pattern 11: Right-Aligned Star Triangle (Right side jhuka hua triangle) 📐
# Isme stars ko right side align karne ke liye pehle spaces print kiye jaate hain:

# Python
# print("--- Pattern 11 ---")
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * i)
# Output:

# Plaintext
#     *
#    **
#   ***
#  ****
# *****
# Pattern 12: Binary Number Triangle (0 aur 1 ka triangle) 💻
# Isme row aur column ke sum ke hisaab se 1 ya 0 print hota hai:

# Python
# print("--- Pattern 12 ---")
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         if (i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
# Output:

# Plaintext
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1



# Pattern 13: Hollow Square Pattern (Khali dibba) 🔲
# Isme sirf border par stars hote hain aur beech mein khali jagah (space) hoti hai:

# Python
# print("--- Pattern 13 ---")
# for i in range(4):
#     for j in range(4):
#         # Agar pehli row, aakhri row, pehla column ya aakhri column ho
#         if i == 0 or i == 3 or j == 0 or j == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:

# Plaintext
# * * * * 
# *     * 
# *     * 
# * * * * 
# Pattern 14: Repeated Row Number Pattern (Har row me same number) 🔢
# Har row me wahi number print hota hai jo row ka number hota hai:

# Python
# print("--- Pattern 14 ---")
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# Output:

# Plaintext
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# Pattern 15: Inverted Right-Aligned Triangle (Ulta right-aligned triangle) 📉
# Stars dheere-dheere kam hote hain aur right side aligned rehte hain:

# Python
# print("--- Pattern 15 ---")
# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * i)
# Output:

# Plaintext
# *****
#  ****
#   ***
#    **
#     *



# Pattern 16: X-Star Pattern (Cross ya X ka aakar) ✖️
# Isme diagonal lines par stars print hote hain:

# Python
# print("--- Pattern 16 ---")
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == i or j == (n - 1 - i):
#             print("*", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# Output:

# Plaintext
# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 
# Pattern 17: Palindrome Number Triangle (Center numbers aage aur peeche chalte hain) 🔄
# Isme numbers pehle badhte hain aur fir wapas ghante hain:

# Python
# print("--- Pattern 17 ---")
# for i in range(1, 5):
#     # Spaces dena
#     print("  " * (4 - i), end="")
#     # Badhte hue numbers
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     # Ghatte hue numbers
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
#     print()
# Output:

# Plaintext
#       1 
#     1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1



# Pattern 18: Plus (+) Sign Pattern ➕
# Isme beech ki row aur column mein stars milkar plus ka sign banate hain:

# Python
# print("--- Pattern 18 ---")
# n = 5
# mid = n // 2
# for i in range(n):
#     for j in range(n):
#         if i == mid or j == mid:
#             print("*", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
# Output:

# Plaintext
#     *     
#     *     
# * * * * * 
#     *     
#     *


