users = [
    {"name": "ali", "age": 30, "is_admin": True},
    {"name": "sara", "age": 25, "is_admin": False},
    {"name": "reza", "age": 40, "is_admin": False},
    {"name": "masiha", "age": 21, "is_admin": True},
]
print(users[0]["name"])
print(users)
print()

for user in users:
    print(f"name:{user['name']} , age:{user['age']}")

print()

for user in users:
    if user["is_admin"] == True:
        print(f"Admin found: {user['name']}")
