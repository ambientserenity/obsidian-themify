from Parser import file_to_rules

if __name__ == '__main__':
    for s in file_to_rules("test.css"):
        print(s)
        print("----")
        pass