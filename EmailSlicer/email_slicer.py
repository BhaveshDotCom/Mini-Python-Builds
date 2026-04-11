email = input("Enter your email...\t")

index = email.index("@")
Username = email[:index]
domain = email[index+1:]

print("--------------------")
print("Username: ", Username)
print("Domain: ", domain)
print("--------------------")