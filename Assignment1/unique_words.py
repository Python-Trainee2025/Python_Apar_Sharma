userInput = input("Enter the sentence/paragraph: ")
input_list = userInput.split()
lowercase_list = [word.lower() for word in input_list]
print("count:", len(set(lowercase_list)))