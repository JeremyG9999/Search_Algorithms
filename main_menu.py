import os
import time
from scripts.binary_search import Binary_Search
from scripts.linear_search import Linear_Search
from scripts.binary_recursive import Binary_Recursive

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a choice:\n")
            print("1. Binary Search")
            print("2. Linear Search")
            print("3. Binary Recursive Search")
            print("4. Clear Terminal")
            print("5. Exit")
            option = input("Select a menu option: ")
            if option == "1":
                self.cls()
                Binary_Search.main()
            elif option == "2":
                self.cls()
                Linear_Search.main()
            elif option == "3":
                self.cls()
                Binary_Recursive.main()
            elif option == "4":
                self.cls()
            elif option == "5":
                break
            else:
                print("Invalid input")

    def cls(self):
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    Menu().main_menu()
