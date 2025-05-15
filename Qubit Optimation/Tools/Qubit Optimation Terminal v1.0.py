# Qubit Optimation Terminal v1.0
# Sourceduty.com

import numpy as np
import matplotlib.pyplot as plt

def display_menu():
    print("\n----------------------------------------")
    print(" Qubit Optimation Terminal v1.0 ")
    print("----------------------------------------\n")
    print("This program allows you to explore the balance and trade-offs between quantum parameters.")
    print("Use the menu below to modify variables, weights, and view optimation results.\n")
    print("----------------------------------------")
    print(" Main Menu ")
    print("----------------------------------------")
    print("1. Adjust Fidelity")
    print("2. Adjust Decoherence")
    print("3. Adjust Entanglement")
    print("4. Adjust Weights")
    print("5. Optimate and Display Results")
    print("6. Help")
    print("7. Exit")
    print("----------------------------------------\n")

def display_help():
    print("\n----------------------------------------")
    print(" Help Menu ")
    print("----------------------------------------\n")
    print("This optimation model allows you to explore the balance between Fidelity, Decoherence, and Entanglement.")
    print("You can adjust their values and assign weights to see how they contribute to the final qubit performance.")
    print("----------------------------------------\n")

def adjust_value(parameter_name, current_value):
    while True:
        try:
            new_value = float(input(f"Enter new value for {parameter_name} (0-1): "))
            if 0 <= new_value <= 1:
                return new_value
            else:
                print("Invalid input. Please enter a value between 0 and 1.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def adjust_weight(parameter_name, current_weight):
    while True:
        try:
            new_weight = int(input(f"Enter new weight for {parameter_name} (1-100): "))
            if 1 <= new_weight <= 100:
                return new_weight
            else:
                print("Invalid input. Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def optimate_qubit(fidelity, decoherence, entanglement, weight_f, weight_d, weight_e):
    total_weight = weight_f + weight_d + weight_e
    norm_f = weight_f / total_weight
    norm_d = weight_d / total_weight
    norm_e = weight_e / total_weight
    
    outcome = (fidelity * norm_f) + ((1 - decoherence) * norm_d) + (entanglement * norm_e)
    
    labels = ['Fidelity', '1 - Decoherence', 'Entanglement']
    values = [fidelity * norm_f, (1 - decoherence) * norm_d, entanglement * norm_e]
    
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['blue', 'red', 'green'])
    plt.title("Qubit Optimation Visualization")
    plt.xlabel("Quantum Parameters")
    plt.ylabel("Weighted Contribution")
    plt.show()
    
    print("\n----------------------------------------")
    print(" Optimation Results ")
    print("----------------------------------------\n")
    print(f"Fidelity: {fidelity:.2f}, Weight: {weight_f}")
    print(f"Decoherence: {decoherence:.2f}, Weight: {weight_d}")
    print(f"Entanglement: {entanglement:.2f}, Weight: {weight_e}")
    print(f"Final Optimation Score: {outcome:.2f}")
    print("----------------------------------------\n")

def main():
    fidelity = 0.9
    decoherence = 0.1
    entanglement = 0.7
    weight_f = 40
    weight_d = 30
    weight_e = 30
    
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            fidelity = adjust_value("Fidelity", fidelity)
        elif choice == "2":
            decoherence = adjust_value("Decoherence", decoherence)
        elif choice == "3":
            entanglement = adjust_value("Entanglement", entanglement)
        elif choice == "4":
            weight_f = adjust_weight("Fidelity", weight_f)
            weight_d = adjust_weight("Decoherence", weight_d)
            weight_e = adjust_weight("Entanglement", weight_e)
        elif choice == "5":
            optimate_qubit(fidelity, decoherence, entanglement, weight_f, weight_d, weight_e)
        elif choice == "6":
            display_help()
        elif choice == "7":
            print("Exiting the program.\n")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
