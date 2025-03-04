def xor_files(file1, file2, output_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(output_file, 'wb') as out:
        while True:
            byte1 = f1.read(1)
            byte2 = f2.read(1)
            if not byte1 or not byte2:
                break
            out.write(bytes([byte1[0] ^ byte2[0]]))

xor_files('1.png', '2.png', 'output')
