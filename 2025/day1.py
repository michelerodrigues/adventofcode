


def parse_line(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]

    return lines

def transform_lines_to_numbers(lines):
    numbers = []
    for line in lines:
        if line.startswith("R"):
            numbers.append(int(line[1:]))
        elif line.startswith("L"):
            numbers.append(-int(line[1:]))

    return numbers


def find_password(input_file):
    lines_from_file = parse_line(input_file)
    numbers_list = transform_lines_to_numbers(lines_from_file)
    dial_position = 50
    count_zero = 0

    for number in numbers_list:
        print("Number = ", number)
        dial_position = (dial_position + number) % 100
        print("Added Number to Dial Position = ", dial_position)
        if dial_position < 0:
            dial_position = dial_position + 100
            print("Dial Position < 0 ", dial_position)
        if dial_position == 0:
            count_zero = count_zero + 1
            print("Dial Position == 0 ", dial_position)
        
        
        print("Count Zero = ", count_zero)
        print("--------------------------------")
    return count_zero

def main():
    input_file = "day1_input.txt"
    count_zero = find_password(input_file)
    print("Count Zero = ", count_zero)

if __name__ == "__main__":
    main()