import sys

f = open(sys.argv[1], "rb")

data = f.read()
f.close()

png_data = []

start_signature = [0x89, 0x50, 0x4e, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
end_signature = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]

start_pos = 0

end_pos = 0

read_mode = False

num_files = 0

for byte in data:
    if (read_mode == False):
        if (start_pos == 8):
            read_mode = True
            start_pos = 0
        elif (byte == start_signature[start_pos]):
            png_data.append(byte)
            start_pos += 1
        elif (start_pos != 0):
            start_pos = 0
            png_data = []
    else:
        if (end_pos == 8):
            read_mode = False
            end_pos = 0
            f = open("images/image" + str(num_files) + ".png", "wb")
            for info in png_data:
                f.write(info.to_bytes(1, 'big'))
            f.close()
            png_data = []
            num_files += 1
            continue
        png_data.append(byte)
        if (byte == end_signature[end_pos]):
            end_pos += 1
        elif (end_pos != 0):
            end_pos = 0


    

    

