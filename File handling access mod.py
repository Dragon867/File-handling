# Define the file path
file_path = "students_data.txt"

# Create a file with initial data for demonstration
def create_initial_file():
    with open(file_path, 'w') as f:
        f.write("Student Name, Grade\n")
        f.write("Alice, A\n")
        f.write("Bob, B\n")
        f.write("Charlie, C\n")
    print("Initial file created with some data.")

# 1. Read Mode - 'r'
def read_file():
    try:
        with open(file_path, 'r') as f:
            print("Reading the file content:")
            print(f.read())  # Read the entire file content
    except FileNotFoundError:
        print("The file does not exist.")
        
# 2. Write Mode - 'w'
def write_file():
    try:
        with open(file_path, 'w') as f:
            f.write("Student Name, Grade\n")
            f.write("David, A\n")
            f.write("Eva, B+\n")
        print("File content has been overwritten with new data.")
    except Exception as e:
        print(f"Error while writing to file: {e}")

# 3. Append Mode - 'a'
def append_file():
    try:
        with open(file_path, 'a') as f:
            f.write("Frank, C+\n")
            f.write("Grace, B\n")
        print("New data has been appended to the file.")
    except Exception as e:
        print(f"Error while appending to file: {e}")

# 4. Read Binary Mode - 'rb'
def read_binary_file():
    try:
        # Create a binary version of the file to demonstrate 'rb'
        with open(file_path, 'rb') as f:
            content = f.read()
            print(f"Binary data read from file: {content}")
    except Exception as e:
        print(f"Error while reading binary file: {e}")

# 5. Write Binary Mode - 'wb'
def write_binary_file():
    try:
        # Create a binary version of the file to demonstrate 'wb'
        with open(file_path, 'wb') as f:
            binary_data = b"Student Name, Grade\nDavid, A\nEva, B+\n"
            f.write(binary_data)
        print("Binary data written to the file.")
    except Exception as e:
        print(f"Error while writing binary file: {e}")

# Activity Workflow
def file_operations_activity():
    # Step 1: Create an initial file with data
    create_initial_file()

    # Step 2: Open the file in different modes
    print("\n--- Read Mode ---")
    read_file()

    print("\n--- Write Mode (Overwrites the file) ---")
    write_file()

    print("\n--- Append Mode ---")
    append_file()

    print("\n--- Read Binary Mode ---")
    read_binary_file()

    print("\n--- Write Binary Mode ---")
    write_binary_file()

# Run the file operations activity
file_operations_activity()
