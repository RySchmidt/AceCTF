import hashlib
import os

# Function to calculate the checksum of a file using sha256
def calculate_checksum(file_path, algorithm='sha256'):
    hash_algo = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

# Function to find the file with matching checksum
def find_matching_file(target_checksum, folder_path, algorithm='sha256'):
    # Debugging: Check if the folder path is correct
    print(f"Looking in folder: {folder_path}")

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return

    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        print(filename)
        file_path = os.path.join(folder_path, filename)
        
        # Skip if it's not a file
        if os.path.isfile(file_path):
            # Calculate the checksum of the current file using sha256
            file_checksum = calculate_checksum(file_path, algorithm)
            
            # Check if it matches the target checksum
            if file_checksum == target_checksum:
                print(f'Matching file found: {filename}')
                return filename

    print('No matching file found.')
    return None

# Example usage
target_checksum = '48bb0b2c17079a325c1b3996b4ce50ab01d3aa2faa24a840f520d17e30e73646'  # Enter the target checksum here
folder_path = './files'

# Call the function
find_matching_file(target_checksum, folder_path)
