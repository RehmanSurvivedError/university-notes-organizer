
from notes_manager import (
    create_note,
    view_note,
    view_all_notes,
    search_notes,
    delete_note
)


def show_menu() -> int:
    while True:
        print("\t\t\t\t==== Notes Management Menu ====")
        print("1. Create Notes")
        print("2. View Note")
        print("3. View all Notes")
        print("4. Search Notes")
        print("5. Delete Note")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if 1<= choice <= 6:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        

def handle_user_choice(choice: int) -> bool:
    if choice == 1:
        print("Creating a new note...")
        create_note()
        
    elif choice == 2:
        print("Viewing a note...")
        view_note()
    elif choice == 3:
        print("Viewing all notes...")
        view_all_notes()
    elif choice == 4:
        print("Searching notes...")
        search_notes()
    elif choice == 5:
        print("Deleting a note...")
        delete_note()
    elif choice == 6:
        print("Exiting the application. Goodbye!")
        return False
    return True

def main()-> None:
    while True:
        choice = show_menu()
        should_continue = handle_user_choice(choice)
        if not should_continue:
            break


if __name__ == "__main__":
    main()
    

