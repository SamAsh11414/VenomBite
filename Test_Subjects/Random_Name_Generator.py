import random

h1 = int(input ("How many names would you like to be generated?\n Type here: "))

first = ("Coding", "Programing", "Python", "VS Code", "PyCharm", "C++", "C#", "Javascript", )

second = ("God", "Legend", "Leader", "King", "President")


while h1 > 0:
    Fir = random.choice(first)
    Sec = random.choice(second)
    name = (Fir + " " + Sec)
    print("--->" + name)
    h1 = h1 - 1