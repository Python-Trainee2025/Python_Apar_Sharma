emp_dictionary = {
    "e1": {"name": "Ram", "phoneNum": "9863727373"},
    "e2": {"name": "Suman", "phoneNum": "9863783783"},
    "e3": {"name": "Sudip", "phoneNum": "9863727460"},
    "e4": {"name": "Chiran", "phoneNum": "986378937"}
}

name = input("Enter the name: ").lower()
details = list(emp_dictionary.values())

flag = 1
for i,d in enumerate(details):
    if d["name"].lower() == name:
        print(f"phone number of {name} is: {d['phoneNum']}")
        flag = 0
    
if flag:
    print("Name not found in the directory!!!")
