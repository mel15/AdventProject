def main():
    print("Day 3!")
    total_value = 0
    with open("input.txt", "r") as file:
        content = file.read()
        len_cont = len(content)
        for i in range(len_cont):
            first_4 = content[i:i + 4]
            if first_4 == "mul(":
                num1, end_index = GetNumber(i + 4, len_cont, content)
                if num1 is None:
                    continue
                if end_index + 1 < len_cont and content[end_index:end_index + 1] == ",":
                    num2, end_index2 = GetNumber(end_index + 1, len_cont, content)
                    if num2 is None:
                        continue
                    if end_index2 + 1 < len_cont and content[end_index2:end_index2 + 1] == ")":
                        total_value = total_value + num1 * num2
        print(total_value)


def GetNumber(i, len_cont, content):
    if i + 3 < len_cont:
        if num := IsNumber(content[i:i + 3]):
            return num, i + 3
    if i + 2 < len_cont:
        if num := IsNumber(content[i:i + 2]):
            return num, i + 2
    if i + 1 < len_cont:
        if num := IsNumber(content[i:i + 1]):
            return num, i + 1
    return None, None


def IsNumber(try_num):
    try:
        return int(try_num)
    except:
        return None


if __name__ == "__main__":
    main()
