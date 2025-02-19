email = input("email: ")
index = email.index("@")

username = email[:index]
mail = email[index + 1:]

print(f"Your username is {username} and your email provider is {mail}")