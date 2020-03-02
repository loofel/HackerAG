
def calculate(i,x,y):
    if (i=="+"):
        return x+y
    elif (i=="-"):
        return x-y
    elif (i=="*"):
        return x*y
    elif (i=="/"):
        return x/y
    elif (i=="^"):
        return x**y

def convert(type, temp_input):
    if type == "A":
        return temp_input + 273.15
    elif type == "B":
        return temp_input * 9/5 + 32
    elif type == "C":
        return temp_input - 273.15
    elif type == "D":
        return (temp_input - 273.15) * 9/5 + 32
    elif type == "E":
        return 5/9 * (temp_input - 32)
    elif type == "F":
        return (temp_input + 459.67) * 5/9
    else:
        return "Fehler! Gib einer der Buchstaben ein, die gefordert sind!"


greet = "Wähle 1. für den Taschenrechner! \nWähle 2. für den Temperaturumrechner! \nWähle 3. zum Schließen!\n"
calc_greet = "******Willkommen beim Taschenrechner!******\nWähle '+' für Addition!\nWähle '-' für Subtraktion!\nWähle '*' für Multiplikation!\nWähle '/' für Division!\nWähle '^' für die Potenz!\nDrücke '.' für 'Zurück'!\n"
conv_greet = """
*******Willkommen beim Tempetaturumrechner!*******
        Wähle, was du umrechnen willst!

        A = "von Celsius nach Kelvin"
        B = "von Celsius nach Fahrenheit"
        C = "von Kelvin nach Celsius"
        D = "von Kelvin nach Fahrenheit"
        E = "von Fahrenheit nach Celsius"
        F = "von Fahrenheit nach Kelvin"
        Tippe "." für 'Zurück'!
"""

user_input = input(greet)
while True:
    if user_input == "1":
        calc_operation = input(calc_greet)
        if calc_operation == ".":
            user_input = "."
        else:
            input_number1 = float(input("Gib deine 1. Zahl ein: "))
            input_number2 = float(input("Gib deine 2. Zahl ein: "))
            print(calculate(calc_operation,input_number1,input_number2))
        
    elif user_input == "2":
        conv_type = input(conv_greet).upper()
        if conv_type == ".":
            user_input = "."
        else:
            conv_temp = float(input("Gib deine zu umrechnende Temperatur ein: "))
            print(convert(conv_type, conv_temp))
    elif user_input == "3":
        break
    elif user_input == ".":
        user_input = input(greet)
    else:
        user_input = input("***Gib einer der vorgegebenen Zahlen ein!***")



