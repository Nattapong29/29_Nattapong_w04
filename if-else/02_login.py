#username = "admin"
#password = "1234678"
user_input = str(input("Enter your User : "))
pass_input = complex(input("Enter your Password"))
print(type(pass_input))
if user_input == "admin"and pass_input == complex("1234678"):
    print("Login Success !!!")
else:
    print("Invalid username or password")