# def calculator (a , b):
#     c = a + b
#     print (c)


# calculator(4,5)

# def Welcome(name):
#     print("Assalamu Alaikum", name)



# Welcome("Turhan")

# def sum (a,b):
#     return a + b

# print(sum(5,6))


# def fun(name):
#     print("Hi",name )


# fun("Turhan")


# def trying (**data):

#     for key, valu in data.items():
#         print(f'Your {key} is {valu}')


# trying(name="Turhan", age=24)


def add_numbers(a,b):
    return a + b

print(add_numbers(5,3))


def greet_user(name = 'Guest'):
     print('Hello', name)

greet_user('Turhan')
greet_user()


def calculate_total(*number):
     print(sum(number))


calculate_total(2, 5, 8, 1)


def user_info(**data):
     for key, valu in data.items():
          print(f"{key}: {valu}")


user_info(name='Turhan', age=23, country='Bangladesh')