import numpy as np
import matplotlib as mpl
import csv

def dataEntry():
    species = input("Enter a species\n")
    name = input("Enter Specimen Name\n")
    locality = input("Enter Specimen Locality\n")
    price = input("Enter a Specimen price\n")
    date = input("Enter a Specimen purchase date (MM/DD/YY)\n")

    data_dict = [{'Species': species, 'Name': name, 'Locality': locality, 'Price': price, 'Date': date}]

    fields = ['Species', 'Name', 'Locality', 'Price', 'Date']

    with open('garnets.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=",")

        writer.writerows(data_dict)

def visualization():
     print()
    #placeholder

def info():
     print()
    #placeholder

def menu(option):
        match option:
            case "1":
                dataEntry()
            case "2":
                visualization()
            case "3":
                info()
            case _:
                  print("Error: Selection must be from list")

if __name__ == '__main__':
    option = input("Select an option\n1: Data Entry\n2: Visualization\n3. Info\n")
    menu(option)