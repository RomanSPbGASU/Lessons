def merge_files(new_file_name, *file_names):
    open(new_file_name, "w").close()
    res = open(new_file_name, "at")
    for file_name in file_names:
        with open(file_name) as file:
            res.write(file.read())
        print(file_name, "записан в файл", new_file_name)
    res.close()


if __name__ == "__main__":
    names = "F101.txt", "F123.txt", "F134.txt", "F135.txt"
    merge_files("RES.txt", *names)
