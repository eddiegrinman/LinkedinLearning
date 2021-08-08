#! bin/bash/python



import os
import argparse


def main(database: str, url_list_file: str):
    print("We're going to work with " + database)  # command + D will duplicate line
    print("We're going to scan " + url_list_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)

# Edit the run configurations in Run --> edit configurations --> create new Pythin configuration
# --> set the name, set the location to main.py in this project -->
# specify -i input.txt -db words.db in the parameters.
