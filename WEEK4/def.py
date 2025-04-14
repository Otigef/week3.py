def modify_content(content):
    """
    Modify the content as needed.
    For demonstration, we'll convert the text to uppercase.
    """
    return content.upper()

def main():
    # Prompt the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Open and read the contents of the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the contents
        modified_content = modify_content(content)

        # Define the output filename
        output_filename = 'modified_' + input_filename

        # Write the modified contents to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
