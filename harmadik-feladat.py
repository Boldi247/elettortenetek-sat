def decrementEach(file_path, times=4):
    print("Attempting to decrement each element...")
    with open(file_path, 'r') as file:
        lines = [line.strip().split() for line in file]

    numbers = [[int(num) for num in line] for line in lines]

    for step in range(times):
        for row in numbers:
            for i in range(len(row)):
                if row[i] != 0:
                    row[i] -= 1
        for row in numbers:
            print(' '.join(str(num) for num in row))
        if step < times - 1:
            print()    
    return None

if __name__ == '__main__':
    decrementEach("harmadik-feladat.txt", times=4)
