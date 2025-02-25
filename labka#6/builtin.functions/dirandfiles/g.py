import os

def delete_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return
        
        
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

file_to_delete = "test"  
delete_file(file_to_delete)
