# ascii_art.py

def print_jirojiro_art():
    try:
        with open("jirojiro.txt", "r") as art_file:
            art = art_file.read()
        print(art)
    except FileNotFoundError:
        print("jirojiro.txt not found. Make sure the file is in the same directory as your script.")
