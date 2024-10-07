import random

def generate_numbers(filename, count):
    with open(filename, 'w') as file:
        for _ in range(count):
            file.write(str(random.randint(1, 100)) + "\n")
            
def count_numbers(filename):
    count = 0
    
    with open(filename, "r") as file:
        for line in file:
            num = int(line.strip())
            if num  % 2 != 0 and num ** 2 % 2 != 0:
                count += 1
    return count

