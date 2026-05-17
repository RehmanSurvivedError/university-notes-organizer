from file_handler import(
    save_note,
    read_note,
    get_all_notes,
    remove_note
)


def create_note() -> None:
    title = input("Enter the title of the note: ").strip()
    content = input("Enter the content of the note:").strip()

    save_note(title, content)
    print("Note created successfully!")


def view_note() -> None:

    title = input("Enter the title of the note you want to view: ").strip()
    content = read_note(title)

    if not content:
        print("Note not found.")
    else:
        print("====Note found====")
        print(f"Title: {title}")
        print(f"Content: {content}")

def view_all_notes() -> None:

    notes = get_all_notes()

    if not notes:
        print("No notes found.")

    else:
        print("====All Notes====")
        
        for title, content in enumerate(notes, start=1):
            print(f"{title} : {content}")

def search_notes() -> None:

    keyword = input("Enter the keyword to search for: ").strip()

    notes = get_all_notes()

    matching_notes = [note for note in notes if keyword in note['title'] or keyword in note['content']]

    if not matching_notes:
        print("No notes found.")

def delete_note() -> None:

    title = input("Enter the title of the note you want to delete: ").strip()

    success = remove_note(title)

    if success:
        print("Note deleted successfully!")
    print("No note found with the given title.")


