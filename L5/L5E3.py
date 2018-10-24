if __name__ == "__main__":
    print("Исходный список: \n")
    names = ["Сергей", "Ольга", "Юрий", "Сергей", "Александр"]
    for name in names:
        print(name)
    print("\nОтсортированный список:\n")
    names = (lambda l: sorted(list(set(l)), key= lambda x: len(x)))(names)
    for name in names:
        print(name)
