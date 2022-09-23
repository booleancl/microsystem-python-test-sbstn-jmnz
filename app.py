import random
import time

def read_file(name):
    file_name = "signs/" + name + ".txt"
    file = open(file_name, "r")
    for line in file:
        print(line)
    time.sleep(3)

def lucky_color():
    colors = ["Azul", "Violeta", "Morado", "Lila", "Rosa", "Amarillo"]
    random_color = random.choice(colors)
    print("Tu Color de la Suerte es: ", random_color)
    time.sleep(3)

def print_menu():
    print("###############################")
    print("Selecciona el número correspondiente a tu signo")
    print(1, "Acuario")
    print(2, "Aries")
    print(3, "Cancer")
    print(4, "Capricornio")
    print(5, "Geminis")
    print(6, "Leo")
    print(7, "Libra")
    print(8, "Piscis")
    print(9, "Sagitario")
    print(10, "Escorpión")
    print(11, "Tauro")
    print(12, "Virgo")
    print(13, "Color de la suerte")
    print(0, "Salir")
    print("###############################")
        
user_input = ""

print("Bienvenido al Horóscopo")

while user_input != "0":
    print_menu()
    user_input = input()
    if user_input == "1":
        read_file("aquarius")
    elif user_input == "2":
        read_file("aries")
    elif user_input == "3":
        read_file("cancer")
    elif user_input == "4":
        read_file("capricornus")
    elif user_input == "5":
        read_file("gemini")
    elif user_input == "6":
        read_file("leo")
    elif user_input == "7":
        read_file("libra")
    elif user_input == "8":
        read_file("pisces")
    elif user_input == "9":
        read_file("sagittarius")
    elif user_input == "10":
        read_file("scorpio")
    elif user_input == "11":
        read_file("taurus")
    elif user_input == "12":
        read_file("virgo")
    elif user_input == "13":
        lucky_color()
    elif user_input == "0":
        print("Chau chau")
        exit()
    else:
        print("Opción incorrecta")