import os

def check_path(path):
    if os.path.exists(path):
        print(f"✅ The path exists: {path}\n")
        

        directory = os.path.dirname(path)
        print(f"📁 Directory: {directory}")
        
        
        filename = os.path.basename(path)
        print(f"📄 Filename: {filename}")
    else:
        print("❌ The path does NOT exist!")


user_path = input("Enter the path to check: ")


check_path(user_path)
