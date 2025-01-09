def generate_info_files():
    # Prompt the user for the name of the text file
    file_name = input().strip()

    try:
        # Open and read the file
        with open(file_name, "r") as file:
            photo_file_names = file.readlines()

        # Check if the file is empty
        # if not photo_file_names:
        #     print("Error: The file is empty.")
        #     return

        # Process each photo file name and replace "_photo.jpg" with "_info.txt"
        info_file_names = []
        for photo_name in photo_file_names:
            photo_name = photo_name.strip()
            if photo_name.endswith("_photo.jpg"):
                info_file_name = photo_name.replace("_photo.jpg", "_info.txt")
                info_file_names.append(info_file_name)

        # Output the modified file names
        for info_name in info_file_names:
            print(info_name)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

generate_info_files()
