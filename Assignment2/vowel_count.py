text = input("Enter a word or sentence: ")
vowels = 'aeiou'
count = 0
for char in text.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels in the input: {count}")
