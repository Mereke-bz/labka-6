def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()  
            return len(lines)  
    except FileNotFoundError:
        print("❌ Error: File not found!")
        return None

file_path = input("Enter the file path: ")

num_lines = count_lines(file_path)
if num_lines is not None:
    print(f"📄 The file contains {num_lines} lines.")
