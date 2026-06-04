# Python mein functions ke baad, agla sabse important topic hai Lists aur Methods (Data ko organize aur manage karna).

# Jab aapke paas bohot saara data ho (jaise students ke naam, daily ka weight record, ya shopping items), toh hum unhein alag-alag variables me rakhne ki jagah ek List me store karte hain.

# 1. List Kya Hoti hai?
# List ek aisi container hoti hai jisme aap multiple values ko square brackets [ ] ke andar store kar sakte hain. Isme numbers, text, ya dono ek sath aa sakte hain.

# Python
# # Ek simple list
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print(fruits)
# 2. List ke Indexing aur Slicing (Data nikalna)
# List ke har item ka ek number hota hai jise Index kehte hain. Python me indexing 0 se shuru hoti hai.

# Python
# colors = ["Red", "Green", "Blue", "Yellow"]

# print(colors[0])  # Output: Red (Pehla item)
# print(colors[2])  # Output: Blue (Teesra item)
# print(colors[-1]) # Output: Yellow (Sabse aakhri item)
# 3. List ke Kuch Main Methods (Operations karne ke liye)
# Python list ke sath kuch built-in functions aate hain jo data ko badalne me madad karte hain:

# A. .append() — Naya item aakhri me jodna
# Python
# diet = ["Oats", "Paneer"]
# diet.append("Soya Chunks")

# print(diet)  # Output: ['Oats', 'Paneer', 'Soya Chunks']
# B. .insert() — Kisi specific position par item dalna
# Python
# numbers = [10, 20, 30]
# numbers.insert(1, 15)  # Index 1 par 15 daal do

# print(numbers)  # Output: [10, 15, 20, 30]