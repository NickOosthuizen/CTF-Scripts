import sys

# add in null bytes between characters and change chars to decimal values
# converting to decimal values as "rb" interprets bytes as decimal values
def preprocess_string(search_string):
    if (len(search_string) == 0):
        return None
    win_string = []
    for char in search_string:
        win_string.append(ord(char))
        win_string.append(0x00)
    win_string.pop()
    return win_string


def string_search(search_string, search_data):
    win_string = preprocess_string(search_string)

    if (win_string is None):
        print("Empty String inputted")
        return
    
    offset = 0x00
    position = 0
    null_flag = False
    read_mode = False
    current_string = []
    string_len = len(win_string)

    for byte in search_data:
        if read_mode == False:
            if (byte == win_string[position]):
                if (byte != 0x00):
                    current_string.append(byte)
                position += 1
                if (position == string_len):
                    read_mode = True
                    position = 0
            else:
                current_string = []
                position = 0 
        else:
            # if two null bytes are encountered in a row, the string is complete
            if (byte == 0x00):
                if (null_flag == True):
                    read_mode = False
                    null_flag = False
                    output_string(current_string, offset)
                    current_string = []
                else: 
                    null_flag = True
            else:
                current_string.append(byte)
                null_flag = False
            
        offset += 1


def output_string(bytes_array, offset):
    char_array = []
    for byte in bytes_array:
        char_array.append(chr(byte))

    # to get the proper offset have to factor in nullbytes
    offset = offset - 2 * len(char_array)
    
    print(''.join(char_array) + " (Offset: " + hex(offset) + ")")


def main():
    input = sys.argv[2]
    f = open(sys.argv[1], "rb")

    if (f.mode != "rb"):
        print("There was a problem opening the file")
        return
    
    data = f.read()
    f.close()

    string_search(input, data)


if __name__=="__main__":
    main()

