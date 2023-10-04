data_type = ["B","KB","MB","GB"]

def make_readable(size):
    count = 0
    while(size>=1024):
        size = size/1024
        count += 1
    file_size = f"{size} {data_type[count]}"
    return file_size
    
