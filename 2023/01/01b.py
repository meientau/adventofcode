import fileinput
from rules_b import calc_line

def main():
    sum = 0
    for line in fileinput.input():
        print(f"{sum=}")
        sum += calc_line(line)

    return sum

if __name__ == "__main__":
    sum = main()
    print(f"{sum=}")
