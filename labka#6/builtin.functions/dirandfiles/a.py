import os

def check_access(path):
    print(f"\n🔍 Checking access for: {path}\n")

    if os.path.exists(path):
        print("✅ Path exists")
        
        if os.access(path, os.R_OK):
            print("📖 Readable ✅")
        else:
            print("📖 Readable ❌")

        if os.access(path, os.W_OK):
            print("✏️ Writable ✅")
        else:
            print("✏️ Writable ❌")

        if os.access(path, os.X_OK):
            print("🚀 Executable ✅")
        else:
            print("🚀 Executable ❌")

    else:
        print("❌ Path does NOT exist")

user_path = input("Enter the path to check: ")

check_access(user_path)
