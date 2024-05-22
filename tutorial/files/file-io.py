# file-io.py, files and file io operations

'''
The main basic functions for reading and writing files are:
 - open() - open a file
 - read() - read a file
 - write() - write a file
 - close() - close a file

 These are from the built-in Python file object, which is returned by the open() function, and is located in the io module.
'''

# Open a file with exclusive creation flag (x)
def create_file(filename):
    """
    This function creates a file with the given filename. If the file already exists, it does not overwrite it.

    :param filename: The name of the file to create.
    """
    try:
        with open(filename, 'x') as file:
            print("File created")
    except FileExistsError:
        print("File already exists and cannot be overwritten. FileExistsError exception raised.")

# Usage
filename = input("Enter the filename to create (x flag, exclusive create, will not truncate): ")
create_file(filename)

# Open a file with read flag (r)
def read_file(filename):
    """
    This function reads the contents of a file with the given filename.

    :param filename: The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            print("File contents:")
            print(file.read())
    except FileNotFoundError:
        print("File not found. FileNotFoundError exception raised.")

# Usage
filename = input("Enter the filename to read (r flag): ")
read_file(filename)


'''
open() function flags:
- r - read, which is the default mode.  It opens the file for reading.
- w - write. It will create a new file or overwrite (truncate) an existing file.
- x - exclusive creation. If the file already exists, the operation will fail.
- a - append. It will open the file for writing at the end of the file.  If the file does not exist, it will create a new file.
- t - text mode. This is the default mode. It opens the file in text mode.
- b - binary mode. It opens the file in binary mode.
- + - read and write. It will open the file for reading and writing.
'''
