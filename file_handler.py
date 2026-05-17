
import os
from typing import Optional,List

NOTES_FOLDER = "notes"

def create_notes_folder() -> None:
    if not os.path.exists(NOTES_FOLDER):
        os.makedirs(NOTES_FOLDER)

def save_note(title: str, content: str) -> None:
    if title and content is not None:
        create_notes_folder()
        file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

        with open(file_path, 'w',encoding='utf-8') as file:
            file.write(content)



def read_note(title: str) -> Optional[str]:

    file_path = os.path.join(NOTES_FOLDER, f"{title}.txt")

    if not os.path.exists((file_path)):
        return None
    
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        return content

def get_all_notes() -> List:

    create_notes_folder()
    notes = []

    for filename in os.listdir(NOTES_FOLDER):
        if filename.endswith('.txt'):
            note_name = filename.replace('.txt','')
            notes.append(note_name)
    return notes


def remove_note(title: str) -> Optional[bool]:
    file_path = os.path.join(
            NOTES_FOLDER,
            f"{title}.txt"
        )

    if not os.path.exists(file_path):
            return False

    os.remove(file_path)

    return True