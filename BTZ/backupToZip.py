#! python
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os, zipfile

def back_to_zipfile(folder, path):

    zip_name = choose_name(folder, path)
    

    backup_zip = zipfile.ZipFile(zip_name, "w")
    create_zip(backup_zip, folder)
    print("\rdone!")


#choose name for backup file
def choose_name(folder, path):
    folder_name = os.path.basename(os.path.normpath(folder))
    folder_name = os.path.join(path, folder_name)
    zipfile_name = ""
    
    for number in range(1, 10000):
        if not os.path.exists(folder_name + f"_{number}.zip"):
            zipfile_name = folder_name + f"_{number}.zip"
            break
    return zipfile_name

#create backup file
def create_zip(backup_file, folder):
    
    for corrent_folder, sub_folders, sub_files in os.walk(folder):
        print(f"Adding files in {corrent_folder}...")
        backup_file.write(corrent_folder, compress_type= zipfile.ZIP_DEFLATED)

        #adding files
        for filename in sub_files:

            #skip backup zip files
            new_base = os.path.basename(folder) + "_"
            if filename.startswith(new_base) and filename.endswith(".zip"):
                continue

            backup_file.write(os.path.join(corrent_folder, filename), compress_type= zipfile.ZIP_DEFLATED)

    backup_file.close()

def main():
    folder = input("Inter the address of folder you want to backup: ")
    if folder == "" or folder.isspace():
        print("you should Inter an address!")
        return
    
    path = input("Inter the backup path or press Enter key(defult : working directory): ")

    if path == "" or path.isspace():
        back_to_zipfile(folder, ".")
    else:
        back_to_zipfile(folder, path)

main()