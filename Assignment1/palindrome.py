userInput = input("Enter two words (separate it by space): ")
(word1, word2) = userInput.split()
if word1 == word2[::-1]:
    print("They are palindrome!!")
else:
    print("They aren't palindrome!!")