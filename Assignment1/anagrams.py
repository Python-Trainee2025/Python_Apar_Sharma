userInput = input("Enter two words (separate it by space): ")
(word1, word2) = userInput.split()
if sorted(word1) == sorted (word2):
    print("They are anagrams!!")
else:
    print("They aren't anagrams!!")