                  # control flow and loops

# if statements

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
print("This line will always execute.")

# if else statements

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print("This line will always execute.")

# if elif else statements

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
print("This line will always execute.")


# match case

status = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")


# for loop

for i in range(5):
    print("Iteration:", i)
    print(i)

for i in range(1, 6):
    print("5 *", i, "=", 5 * i)

# while loop

count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# break statement

for i in range(5):
    if i == 3:
        break
    print(i)

# continue statement

for i in range(5):
    if i == 2:
        continue
    print(i) 

# pass statement

for i in range(5):
    if i == 3:
        pass  
    print(i)  