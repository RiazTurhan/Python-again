age = input("what's your age: ")
age = int(age)
if age >= 18:
    print("You are an adult.")
elif age < 12:
    print("You are a child.")
else:
    print("You are a teenager.")


def person(name , age):
    if name == "Alice" and age >= 18:
        return "Hello Alice, you are an adult."
    else:
        return "Sorry, you are not Alice or not an adult."

print(person('Alice', 29))
print(person('Hamid', 29))


age = 18
Male = True

if age >= 18 and Male:
    print("You are an adult male.")
else:
    print ("You are either an adult female or a minor.")