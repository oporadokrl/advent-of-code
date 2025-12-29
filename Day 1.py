with open("input.txt", "r") as file:
    content = (file.read()).split("\n")

actual_number = 50
password = 0


def part_1(password, actual_number):
    for move in content:
        for _ in range(int(move[1:])):
            if str(move[0]) == "R":
                actual_number += 1
            else:
                actual_number -= 1
            if actual_number == -1 or actual_number == 100:
                actual_number %= 100
        if actual_number == 0:
            password += 1
    return password


def part_2(password, actual_number):
    for move in content:
        for _ in range(int(move[1:])):
            if str(move[0]) == "R":
                actual_number += 1
            else:
                actual_number -= 1
            if actual_number == -1 or actual_number == 100:
                actual_number %= 100
            if actual_number == 0:
                password += 1
    return password


if __name__ == "__main__":
    print("password for part 1: " + str(part_1(password, actual_number)))
    print("password for part 2: " + str(part_2(password, actual_number)))
