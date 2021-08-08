#! bin/bash/python


import os
import argparse
from utilities import url_utilities
import urllib.parse


# We want to parse out words in an html content that we will read in from a text file that we create

def main(database: str, url_list_file: str):
    big_word_list = []
    print("We're going to work with " + database)  # command + D will duplicate line
    print("We're going to scan " + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)

# Edit the run configurations in Run --> edit configurations --> create new Python configuration
# --> set the name, set the location to main.py in this project -->
# specify -i input.txt -db words.db in the parameters.
