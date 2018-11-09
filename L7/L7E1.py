def merge_files(new_file_name, *file_names):
    res = open(new_file_name, )
    for file_name in file_names:
        with open(file_name) as file:



if __name__ == "__main__":
    file_names = ["F101.txt", "F123.txt", "F134.txt", "F135.txt"]
    merge_files("RES.txt", file_names)
