def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List successfully written to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
write_list_to_file("output.txt", my_list)
