#Imports
import os
import shutil

#Generate the 1GB file
def generateFile(fileName):
    
    #Open output_file to write to
    with open(fileName, "w") as f:

        #Set OpCount & Size Limit
        sizeLimit = 1 *(1024 ** 3)
        OpCount = 0

        #Print 100 times   
        while True:
            while OpCount <= 100:
                spam = "_" * 10000
                f.write(f"{spam}\n")
                print(f"{OpCount}\n")
                OpCount += 1

            #Check the file size
            if os.path.getsize(fileName) >= sizeLimit:
                print("File size exceeded 1GB. Stopping...")
                break
                
#Copy file x amout of times
def copyFile(fileNumber, fileName):

    #Set fileCount & fileName
    fileCount = 1
    
    #Copy file until count is reached
    print("Starting...")
    while fileCount <= fileNumber:
        copyName = f"{os.path.splitext(fileName)[0]}_copy{i}{os.path.splitext(fileName)[1]}"
        shutil.copy(fileName, copyName)
        fileCount += 1

    #End
    print(f"{fileCount} files were created using up over {fileCount}GB of space!")
    

#Main
def main():

    #Prompt for number of Gigs to eat
    fileNumber = int(input("How many copies do you want to create? "))
    fileName = "output_file.txt"
    print("Starting...")
    
    #Generate the 1GB file
    generateFile(fileName)
    
    #Copy the file
    copyFile(fileNumber, fileName)

#Start
main()
