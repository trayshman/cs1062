# regex1_demo.py
# Author: Christine F. Reilly
# Demonstration of regular expressions (Part 1)

import re # Import the regular expressions module

# Function to find lines in a file that are the From: lines in an email message.
# Parameter: sting - name of the file
def email_lines(fname):
    fhand = open(fname) # Open the input file

    # Iterate through the lines in the file
    for line in fhand:
        line = line.strip() # remove leading and trailing whitespace

        # Search for lines that are the From: lines in an email message
        if re.search('^From:\s[a-zA-Z0-9]\S*@\S*[a-zA-Z]$', line):
            print(line)



    fhand.close()
# end of email_lines function

# Function to extract all email addresses in a file.
# Parameter: sting - name of the file
def all_emails(fname):
    fhand = open(fname) # Open the input file

    # Iterate through the lines in the file
    for line in fhand:
        line = line.strip() # remove leading and trailing whitespace

        # Extract all email addresses from the line
        emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)

        # Print the extracted email addresses
        for e in emails:
            print(e)


    fhand.close()
# end of all_emails function

# Function to extract the year from the date line that is part of the email header.
# Parameter: sting - name of the file
def print_years(fname):
    fhand = open(fname) # Open the input file

    # Iterate through the lines in the file
    for line in fhand:
        line = line.strip() # remove leading and trailing whitespace

        # Search for lines that are the Date: lines in an email message
        # Print the year part of the date
        years = re.findall('^Date:\s*[a-zA-Z]+,\s*[0-9]+\s*[a-zA-Z]+\s([0-9][0-9][0-9][0-9])', line)
        for y in years:
            print(y)
# end of print_years function

# Main part of program

file_name = 'mbox-regex.txt'

email_lines(file_name)

all_emails(file_name)

print_years(file_name)
