def u_chars(filename):
    char_count = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char_count[char] == 1:
                    print(char, end='')

u_chars('file.txt')