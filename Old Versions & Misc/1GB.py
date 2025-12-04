#Imports
import os
import random

#Main
def main(output_file="numbers.txt", size_limit=1 * 1024 * 1024 * 1024):
    print("Starting ...")

    #Open output_file to write to
    with open(output_file, "w") as f:
        while True:
            #Set OpCount
            OpCount = 0
            
            #Generate a random number and write it to the file 100 times
            while OpCount <= 100:
                number = random.randint(10**9, 11**9)
                f.write(f"{number}\n")
                OpCount += 1

            #Check the file size
            if os.path.getsize(output_file) >= size_limit:
                print(f"File size exceeded {size_limit / (1024**3):.2f} GB. Stopping...")
                break

#Program Start
main()
