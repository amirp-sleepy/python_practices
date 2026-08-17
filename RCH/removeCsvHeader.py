#! python3
# This program remove the header from all CSV files in 
# current working directory.

import os, csv

def main():
    for file in os.listdir():
        if file.endswith(".csv"):
            print(f"\r\033[KRemoving header of {file} ...", end="")

            csvFile = open(f"./{file}")
            csvReader = csv.reader(csvFile)

            outFile = open("tempFile.csv", "w", newline="")
            outWriter = csv.writer(outFile)
            
            for row in csvReader:
                if csvReader.line_num == 1:
                    continue
                outWriter.writerow(row)

            outFile.close()
            csvFile.close()
            
            os.replace("tempFile.csv", f"{file}")
            
    print("\nDone!")

main()

