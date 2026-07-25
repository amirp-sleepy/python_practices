#! python
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import os, shutil, re

def main():
    files_list = search()
    if len(files_list) == 0:
        print("There is no file with American date at working dircetory!")
    else:
        change_name(files_list)
        print("done!")


def search():
    
    american_date = re.compile(r"""
                    ^(.*?)                              #anything before date g1
                    (0?[1-9]|1[0-2])-                   #month g2
                    (0?[1-9]|[12]\d|3[01])-             #days g3
                    ((?:19|20)\d\d)                     #year g4
                    (.*)$                               #anything after date g5
                    """, re.VERBOSE) 

    files = []
    for i in os.listdir("."):
        match_file = american_date.search(i)
        #ignore another files
        if match_file == None:
            continue
        files += [match_file]

    return files

def change_name(files):
    file_name = ""
    new_name = ""

    beforePart = ""
    monthPart = ""
    dayPart = ""
    yearPart = ""
    afterPart = ""

    for match_item in files:

        beforePart = match_item.group(1)
        monthPart = match_item.group(2)
        dayPart = match_item.group(3)
        yearPart = match_item.group(4)
        afterPart = match_item.group(5)
        
        file_name = match_item.group()
        
        new_name = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
        
        working_dir = os.path.abspath(".")
        file_name = os.path.join(working_dir, file_name)
        new_name = os.path.join(working_dir, new_name)      

        shutil.move(file_name, new_name)

main()
    