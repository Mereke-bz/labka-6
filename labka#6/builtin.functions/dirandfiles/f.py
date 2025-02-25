def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:  
            content = src.read()  
        
        with open(destination_file, 'w') as dest:  
            dest.write(content)  

        print(f"File copied successfully from {source_file} to {destination_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except Exception as e:
        print(f"Error copying file: {e}")

copy_file("pipi", "new.txt")
