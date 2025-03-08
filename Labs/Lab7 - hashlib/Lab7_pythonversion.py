# my code

import os
import hashlib

def menu():
    while True:
        try:
            print("\n--- File Duplicate Finder ---")
            print("1. Enter directory to search")
            print("2. Exit")

            choice = str(input("Choose an option: "))


            #if the user chose 1 it'll start progra, otherwise it'll break the while loop
            if choice == "1":
                #saves directory user inputs
                directory = input("input directory: ")

                # find duplicates outputs a list full of lists of duplicates 
                # example of what list could look like [[duplicate1, duplicates1] , [duplicate2, duplicate2,duplicate2]]

                #then it'll traverse each set of duplicates and print them out, between each set it'll say "these are duplicates: "
                for set_of_duplicates in find_duplicates(directory):
                    print("these are duplicates: ")
                    for duplicate_file in set_of_duplicates:
                        print(duplicate_file)

            else:
                print('exiting duplicate file finder')
                break

                #allows for keyboard interrupt to leave while loop
        except KeyboardInterrupt:
            break




def find_duplicates(directory):
    dict_of_files= {}
    duplicates = []

    for dirpath, subdir, files in os.walk(directory):
        for file in files:
            # for the current file the for loop is looking at, store file path and checksum
            file_path = os.path.join(dirpath,file)
            file_checksum = get_checksum(file_path)

            #if two files have the same content, they'll have the same checksum. 
            #if the current file has a unique checksum, it'll add a key value pair to the dict_of_files in the format of {file_checksum:[filepath]}
            #if the checksum already exists, then it'll add another filepath to the filepath list.

            if file_checksum in dict_of_files:
                dict_of_files[file_checksum].append(file_path)
            else:
                dict_of_files[file_checksum] = [file_path]

        
    # this will find if there is more than one file path saved per unique checksum and if there is, add it to duplicates
    for file_list in dict_of_files.values():

        if len(file_list) > 1:
            duplicates.append(file_list)

    return duplicates

# I did not write this function.
def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    menu()