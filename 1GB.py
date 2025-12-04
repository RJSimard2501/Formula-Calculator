import os
import random

def generate_numbers_until_1gb(output_file="numbers.txt", size_limit=1 * 1024 * 1024 * 1024):
    """
    Generates random numbers and writes them to a file until the file size exceeds 1GB.
    
    :param output_file: Name of the output file.
    :param size_limit: Maximum file size in bytes (default: 1GB).
    """
    with open(output_file, "w") as f:
        while True:
            # Generate a random integer and write it to the file
            number = random.randint(0, 10**9)
            f.write(f"{number}\n")
            
            # Check the file size
            if os.path.getsize(output_file) >= size_limit:
                print(f"File size exceeded {size_limit / (1024**3):.2f} GB. Stopping...")
                break

if __name__ == "__main__":
    generate_numbers_until_1gb()
