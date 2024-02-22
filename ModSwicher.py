import os
import shutil
from dotenv import load_dotenv
load_dotenv()


MODFOLDER = os.getenv("MODFOLDER")
AUTOMATEDMODSSTORAGE = os.getenv("AUTOMATEDMODSSTORAGE")




def main():
    print("Select wich mods you would like to play with:")
    #get a list of all posible mods
    listOfMods = []
    indexOfMOD = 0
    for file in os.listdir(AUTOMATEDMODSSTORAGE):

        file_path = os.path.join(AUTOMATEDMODSSTORAGE, file)
        listOfMods.append(file_path)
        print(indexOfMOD, " : ", file)
        indexOfMOD += 1

    #get the user input
    userInput = input("Enter the number of the mod you would like to play with: ")
    if userInput.isdigit() and int(userInput) < len(listOfMods):
        chosenMod = listOfMods[int(userInput)]
    else:
        print(userInput, " is a invalid argument. ")
        main()
 
     
    
    


    #check if the mod is already in the mods folder
    if compareTwofoldersForeSamecontent(chosenMod, MODFOLDER):
        print("The mod is already in the mods folder. Program will exit.")
        print("Enjoy playing with the mods!")
        exit()

    #delete all files in the mods folder afther asking permison
    print("Can I delete the following files: ", os.listdir(MODFOLDER))
    
    if input("If I can press enter if not press any other key: ") =="":

        deleteAllFilesInMODSFOLDER()
    else:
         exit

    #copy the mod to the mods folder
    print("Debug: starting to copy")
    copyModToModsFolder(chosenMod)
        





    





        
def deleteAllFilesInMODSFOLDER():
    # Delete all files in the mods folder
    for file in os.listdir(MODFOLDER):
        file_path = os.path.join(MODFOLDER, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception as e:
            print(e)
            print("Fail to delete " + file_path)


def compareTwofoldersForeSamecontent(folder1, folder2):
    # Compare two folders for same content
    # Return True if same, False if not
    # Get the file list of both folders
    folder1Files = os.listdir(folder1)
    folder2Files = os.listdir(folder2)

    # Check if the two folders have the same amount of files
    if len(folder1Files) != len(folder2Files):
        return False

    # Check if the two folders have the same files
    for file in folder1Files:
        if file not in folder2Files:
            return False

    # Check if the two folders have the same files
    for file in folder2Files:
        if file not in folder1Files:
            return False

    # If all the checks are passed, return True
    return True

def copyModToModsFolder(modfolder_path):
    #copy all mods in modfolder_path to the mods folder
    for file in os.listdir(modfolder_path):
        file_path = os.path.join(modfolder_path, file)
        try:
            if os.path.isfile(file_path):
                shutil.copy(file_path, MODFOLDER)

        except Exception as e:
            print(e)
            print("Fail to copy " + file_path)
    
    





main()