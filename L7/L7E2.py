class IOList(list):

    def read(self, file_name):
        self.clear()
        with open(file_name) as file:
            for line in file.readlines():
                self.append(list(map(lambda item: int(item), line.split(" "))))

    def write(self, file_name):
        with open(file_name, "w") as file:
            file.writelines(str(self))

    def __str__(self):
        res = ""
        for line in self:
            res += " ".join((str(num) for num in line)) + "\n"
        return res


def write_files():
    with open("arr_1.txt", "w") as arr_1:
        arr_1.write("0 1 2 3 4")
    with open("arr_2.txt", "w") as arr_2:
        arr_2.write("5 6 0 7 1")


if __name__ == "__main__":
    write_files()
    first_name = "arr_1.txt"
    second_name = "arr_2.txt"
    res_name = "res.txt"
    first_arr = IOList()
    first_arr.read(first_name)
    print("Перый массив считан из файла", first_name)
    print(first_arr, end="")
    second_arr = IOList()
    second_arr.read(second_name)
    print("Второй массив считан из файла", second_name)
    print(second_arr, end="")
    res_arr = IOList()
    terms = [*first_arr, *second_arr]
    sums = list(map(lambda a, b: a + b, *terms))
    diffs = list(map(lambda a, b: a - b, *terms))
    prods = list(map(lambda a, b: a * b, *terms))
    res_arr.extend([sums, diffs, prods])
    print("Результирующий массив")
    print(res_arr)
    res_arr.write(res_name)
    print("Результирующий массив записан в файл", res_name, end="\n")
    res_arr.read(res_name)
    print("Результирующий массив считан из файла", res_name)
    print(res_arr)
