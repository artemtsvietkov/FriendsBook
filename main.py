# Mina vänner-boken
# Artem Tsvietkov TEINF22
# 2024-09-03

class Friend:
    def __init__(self, first_name: str, last_name: str, age: int, phone: str, hobby: str) -> None: 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.hobby = hobby
    
    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Phone: {self.phone}, Hobby: {self.hobby}"  #Retrnerar 

    
def create_friend(friend_book: list):  #Tar in all input i form av list 
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    hobby = input("Enter hobby: ")
    
    new_friend = Friend(first_name, last_name, age, phone, hobby)
    friend_book.append(new_friend)
    print("Friend added successfully!\n")
    

def main():
    friend_book = []
    while True: #Körs så länge användaren väljer 3
        print("Friend-book's menu:")
        print("1. Add a new friend")
        print("2. Print all friends")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_friend(friend_book)
        elif choice == "2":
            if friend_book:
                for friend in friend_book:
                    print(friend)
                print()
            else:
                print("Friend book is empty.\n")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()