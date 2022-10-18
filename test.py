from concurrent.futures import ThreadPoolExecutor
from time import sleep
import time

values = [3,4,5,6,7,8,9,10,11,12,13,14]

def cube(x):
    print(f'Cube of {x}:{x*x*x}')


if __name__ == '__main__':
    result =[]
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=5) as exe:
        # exe.submit(cube,2)

        # Maps the method 'cube' with a list of values.
        result = exe.map(cube,values)

    # for r in result:
    #     print(r)
    print("%s seconds with Thread Pool Executor" % (time.time() - start_time))