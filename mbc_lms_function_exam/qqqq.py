run = True
session = None
FILE_NAME = "membes.txt"
members = []

def save_members():
    with open(FILE_NAME, "w", encoding="utf-8") as f: