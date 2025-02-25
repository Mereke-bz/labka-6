import string

def generate_text_files():
    for letter in string.ascii_uppercase:  
        filename = f"{letter}.txt"
        with open(filename, "w") as file:
            file.write(f"This is file {filename}\n")  
    print("26 text files (A.txt to Z.txt) have been created successfully.")


generate_text_files()
