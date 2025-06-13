#!/usr/bin/env python3
# Author ID: 166335232

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    read_data = f.readlines()
    list_data = [line.strip() for line in read_data]
    f.close()
    return list_data

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    # I use try except to check if file already exist to use append or write(avoid destroyed file by mistake)
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            f = open(file_name, 'a')
            f.write(string_of_lines)
            f.close()
    except FileNotFoundError:
        f = open(file_name, 'w')
        f.write(string_of_lines)
        f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    # same as append_file_string
    f = open(file_name, 'w')
    for string in list_of_lines:
        f.write(str(string) + '\n') #convert to string in case string is not a str type
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    # content = read_file_string(file_name_read)
    # f = open(file_name_write, 'a')
    # f.write(content)
    # f.close()
    content = read_file_list(file_name_read)
    f = open(file_name_write, 'w')
    line_num = 1
    for string in content:
        f.write(str(line_num) + ':' + str(string) + '\n')
        line_num +=1
    f.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))