### Task: List all the files in list of foloders that user provide 

# Multipe folders and those can have multiple files

# os.listdir(FS)  ==> It will list al the files under the FS
 
import os

folders = input("Enter all FS name wih spaces:  ").split()     #### storing all FS names dynamically into a list


for folder in folders:
    print("\n")

    try:
        files = os.listdir(folder)                             #### for nth folder, listing the files and saving in a list called files


    except FileNotFoundError:
        print("The" + folder + "is not a valid folder")
        continue

    print("Contents under " + folder + " is:")
    print("=======================================")

    for file in files:
        print(file)
