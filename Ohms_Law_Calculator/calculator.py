import math

# Submenu "Ohm"

def ohm_menu():
    while True:
        print("\nCalculate Resistance (Ohm) Menu:")
        print("\n1. Calculate from Voltage and Current")
        print("2. Calculate from Voltage and Watt")
        print("3. Calculate from Watt and Current")
        print("4. Return to main menu")
           
        choice = input("\nChoose an option: ")

        if choice == "1":
            u = float(input("\nEnter Voltage: "))
            i = float(input("Enter Current: "))
            r = round(u * i, 2)
            print("\nThe resistance is: " + str(r) + " Ohm")
            input("Press Enter to continue...") 
        elif choice == "2":
            u = float(input("Enter Voltage: "))
            p = float(input("Enter Watt: "))
            r = round((u * u) / p, 2) 
            print("\nThe resistance is: " + str(r) + " Ohm")
            input("Press Enter to continue...")
        elif choice == "3":
            i = float(input("Enter Current: "))
            p = float(input("Enter Watt: "))
            r = round(p / (i * i), 2) 
            print("\nThe resistance is: " + str(r) + " Ohm")
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# Submenu "Voltage"

def voltage_menu():
    while True:
        print("\nCalculate Voltage (Volts) Menu:")
        print("\n1. Calculate from Ohm and Ampere")
        print("2. Calculate from Ohm and Watt")
        print("3. Calculate from Watt and Ampere")
        print("4. Return to main menu")
           
        choice = input("\nChoose an option: ")

        if choice == "1":
            r = float(input("\nEnter Ohm: "))
            i = float(input("Enter Ampere: "))
            u = round(r * i, 2)
            print("\nThe Voltage is: " + str(u) + " Volts")
            input("Press Enter to continue...") 
        elif choice == "2":
            r = float(input("Enter Ohm: "))
            p = float(input("Enter Watt: "))
            u = round(math.sqrt(u * p), 2) 
            print("\nThe Voltage is: " + str(u) + " Volts")
            input("Press Enter to continue...")
        elif choice == "3":
            i = float(input("Enter Current: "))
            p = float(input("Enter Watt: "))
            u = round(p / i , 2) 
            print("\nThe Voltage is: " + str(u) + " Volts")
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Submenu "Current"

def current_menu():
    while True:
        print("\nCalculate Current (Ampere) Menu:")
        print("\n1. Calculate from Ohm and Volts")
        print("2. Calculate from Ohm and Watt")
        print("3. Calculate from Watt and Volts")
        print("4. Return to main menu")
           
        choice = input("\nChoose an option: ")

        if choice == "1":
            r = float(input("\nEnter Ohm: "))
            u = float(input("Enter Volts: "))
            i = round(u / r, 2)
            print("\nThe Current is: " + str(i) + " Ampere")
            input("Press Enter to continue...") 
        elif choice == "2":
            r = float(input("Enter Ohm: "))
            p = float(input("Enter Watt: "))
            i = round(math.sqrt(p * r), 2) 
            print("\nThe Current is: " + str(i) + " Ampere")
            input("Press Enter to continue...")
        elif choice == "3":
            u = float(input("Enter Voltage: "))
            p = float(input("Enter Watt: "))
            i = round(p / u , 2) 
            print("\nThe Current is: " + str(i) + " Ampere")
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Submenu "Watt"

def watt_menu():
    while True:
        print("\nCalculate Power (Watt) Menu:")
        print("\n1. Calculate from Ampere and Volts")
        print("2. Calculate from Ohm and Volts")
        print("3. Calculate from Ampere and Ohm")
        print("4. Return to main menu")
           
        choice = input("\nChoose an option: ")

        if choice == "1":
            i = float(input("\nEnter Ampere: "))
            u = float(input("Enter Volts: "))
            p = round(u * i, 2)
            print("\nThe Power is: " + str(p) + " Watt")
            input("Press Enter to continue...") 
        elif choice == "2":
            r = float(input("Enter Ohm: "))
            p = float(input("Enter Volts: "))
            p = round((u * u) / r, 2) 
            print("\nThe Power is: " + str(p) + " Watt")
            input("Press Enter to continue...")
        elif choice == "3":
            i = float(input("Enter Ampere: "))
            r = float(input("Enter Ohm: "))
            p = round((i * i) / r , 2) 
            print("\nThe Power is: " + str(p) + " Watt")
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Main menu


def main_menu():
    print("Ohms law:")
    print("1. Calculate Ohm")
    print("2. Calculate Voltage")
    print("3. Calculate Current")
    print("4. Calculate watt")
    print("5. Exit program")

# Create the calculator


calculater = {}

# Main menu loop


while True:
    main_menu()
    choice = input()

    if choice == "1":
        ohm_menu()
    elif choice == "2":
        voltage_menu()
    elif choice == "3":
        current_menu()
    elif choice == "4":
        watt_menu()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
