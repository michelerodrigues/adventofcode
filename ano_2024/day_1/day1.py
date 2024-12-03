import os

def load_file(file_path):
    # definir duas listas vazias onde serão inseridos os location_id de cada coluna do arquivo
    locations_1 = []
    locations_2 = []

    if not file_path:
        print(f"File: {file_path}")

        print("Error: File path empty or None.")
        return locations_1, locations_2

    # open() https://www.w3schools.com/python/ref_func_open.asp
    try:
        with open(file_path, 'r', encoding='utf-8') as location_file:
            for line in location_file:
                print(f"Line: {repr(line)}")
                col = line.strip().split()
                 
                if(len(col) == 2):
                    try:
                        locations_1.append(int(col[0]))
                        locations_2.append(int(col[1]))
                    except:
                            print("Error during number convertion")
                else:
                    print("No data to append")


    except FileNotFoundError:
        print("File not found")
    except Exception as e:
         print("Error loading file: ", e)

    return locations_1, locations_2


def order_lists(loc1, loc2):
    try:
        loc1.sort()
        loc2.sort()
    except Exception as e:
        print("Can't sort lists ", e)

    return loc1, loc2


def calculate_distance_apart(loc1, loc2):
    distances = []
    for index, item in enumerate(loc1):
        sub = abs(loc1[index] - loc2[index])
        distances.append(sub)

    return distances


def sum_distances(distances):
    sum_distances = 0
    for dist in distances:
        sum_distances = sum_distances + dist

    return sum_distances


def main():
    file_path = os.path.abspath('day_1/input-day1.txt')

    if not file_path:
        print("File path empty or None.")
        return
    
    locations_1, locations_2 = load_file(file_path)
    locations_1, locations_2 = order_lists(locations_1, locations_2)
    distances = calculate_distance_apart(locations_1, locations_2)
    final_result = sum_distances(distances)

    print("The total distance between the lists is ", final_result)


if __name__ == "__main__":
    main()