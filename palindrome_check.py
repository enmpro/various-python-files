word = input()
word_check = ""

for x in range(len(word) - 1, 0 - 1, -1):
    word_check += word[x]

    if word_check == word:
        print("Palindrome")
        break
else:
    print("Not palindrome")

