alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

name = input("What is your name? ").lower()

total = 0
average = 0

a = 0
while a < len(name):
    total += alphabet.index(name[a]) + 1
    a += 1

average = total / len(name)
letter = alphabet[int(average)]

print("The total value of your name is " + str(total))
print("The average value of your name is " + str(average))
print("The letter representing the average value of your name is " + str(letter))