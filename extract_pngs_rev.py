import sys
import os.path

f = open(sys.argv[1], "rb")

data = f.read()
f.close()

png_data = []

start_signature = [0x89, 0x50, 0x4e, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
end_signature = [0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82]

start_pos = 7

end_pos = 7

read_mode = False

num_files = 0

for byte in data[::-1]:
    if (read_mode == False):
        if (end_pos == -1):
            read_mode = True
            end_pos = 7
        elif (byte == end_signature[end_pos]):
            png_data.append(byte)
            end_pos -= 1
        elif (end_pos != 0):
            end_pos = 7
            png_data = []
    else:
        if (start_pos == -1):
            read_mode = False
            start_pos = 7
            while (os.path.isfile("images/image" + str(num_files) + ".png")):
                num_files += 1
            f = open("images/image" + str(num_files) + ".png", "wb")
            for info in png_data[::-1]:
                f.write(info.to_bytes(1, 'big'))
            f.close()
            png_data = []
            num_files += 1
            continue
        png_data.append(byte)
        if (byte == start_signature[start_pos]):
            start_pos -= 1
        elif (start_pos != 7):
            start_pos = 7


    

    

