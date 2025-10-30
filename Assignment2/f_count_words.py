try:
    with open("sample.txt", 'r') as file:
        text = file.read()
        words = text.split() 
        print(f"Total number of words: {len(words)}")
except FileNotFoundError:
    print(f"Error: File {'sample.txt'} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
