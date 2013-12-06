csvcat
======

This is a small utility to check csv files on the command line.
```
 Usage:
    -c column numbers in this format "[4-7],[9-10],11,24
    -r row numbers in this format "[4-7],[9-10],11,24
    -d delimiter (default ,)
    -q quote char (default ")
 Example:
    csvcat.py -c "[4-7],[9-10]" -r "[1-4],6" test.csv
```
