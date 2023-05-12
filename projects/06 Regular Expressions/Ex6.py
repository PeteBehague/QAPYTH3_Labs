#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces.
    postcode = re.sub(r"[ \t\n]", "", postcode)
    
    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub(r"(\d[A-Z][A-Z]$)", r" \1", postcode)
    
    # Print the reformatted postcode.
    print (postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = 0   # TODO (b) Replace this line with a call to re.match().
    m = re.match(r"$[A-Z](2)[0-9][1,2][A-Z][0,1] [0-9][A-Z](2)", postcode)
    if m:
        valid = valid + 1
    else:
        invalid = invalid + 1

        

infile.close()

# TODO (b) Print the valid and invalid totals.

