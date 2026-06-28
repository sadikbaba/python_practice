with open("read_and_write_file.txt") as file_object:
    content = file_object
    for line in content:
        print(line.rstrip())
