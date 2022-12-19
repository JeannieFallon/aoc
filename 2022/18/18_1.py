import sys
import fileinput

'''
python 18_1.py input_18.txt
'''

def get_3d_grid(n=25):
    '''Return a 3D array of n^3'''
    return [[[0 for k in range(n)] for j in range(n)] for i in range(n)]


def get_surface_area(grid: list, cubes: list):
    surface_area = 0
    #TODO implement search in 3D for given coords

    return surface_area


def main():
    cubes = []

    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            cubes.append(list(int(i) for i in line.strip().replace(',','')))

    grid = get_3d_grid()
    result = get_surface_area(grid, cubes)

    print(result)
    #assert result == 64
    #print(f'DEMO Success for result: {result}')


if __name__ == "__main__":
    main()
