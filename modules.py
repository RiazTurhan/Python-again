# f = open('data.txt', 'w')
# f.write('"My name is Turhan"')
# f.close()


# y = open('data.txt', 'r')
# print(y.read())

# x = open('data.txt', 'a')
# x.write("Learning Python File Handling")
# x.close


with open('notes.txt', 'w') as file:
    for i in range(3):
        line = input(f"Enter line {i+1}: ")
        file.write(line + '\n')


with open('notes.txt', 'r') as file:
    line = file.readlines()
    for i in line:
        print(i.strip())

        