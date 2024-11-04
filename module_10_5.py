import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    lin_time = time.time() - start_time
    print(f'Линейный: {lin_time}')

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    mult_time = time.time() - start_time
    print(f'Многопроцессный: {mult_time}')
