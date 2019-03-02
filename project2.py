# Project #2 - Master Yoda says..
# - Write a program, using functions, that asks the user for a long string containing multiple words.
# - Print back to the user the same string, except with the words in backwards order.
print("Master Yoda says...")
ask = input("Why do you love Jedi? Describe yourself in at least 10 words: ")

a = ask

answer = " ".join(a.split()[::-1])
print("\n")
print("User's answer is: ", answer)
