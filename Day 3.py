with open("input.txt", "r") as file:
    content = file.read()


def parse(content):
    return content.split("\n")


def proccess_part_1(instructions):
    password: int = 0
    for bank in instructions:
        stored_value: int = 0
        for bat in range(0, len(bank)):
            for i in range(bat + 1, len(bank)):
                try:
                    temp = str(bank[bat] + bank[i])
                    if int(temp) > int(stored_value):
                        stored_value = temp
                except:
                    pass
        password += int(stored_value)
    return password


def proccess_part_2(instructions):
    password: int = 0
    for bank in instructions:
        stored_value: int = 0
        for bat in range(0, len(bank)):
            for i in range(bat + 1, len(bank)):
                try:
                    temp = str(bank[bat] + bank[i])
                    if int(temp) > int(stored_value):
                        stored_value = temp
                except:
                    pass
        password += int(stored_value)
    return password


if __name__ == "__main__":
    instructions = parse(content)
    print("Part 1: " + str(proccess_part_1(instructions)))
    print("Part 2: " + str(proccess_part_2(instructions)))
