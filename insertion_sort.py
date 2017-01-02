number_list = [3, 7, 4, 9, 5, 2, 6, 1]


def insertion_sort(num_list):
    sorted_list = list()
    sorted_list.append(num_list[0])

    for i in range(1, len(num_list)):
        x = num_list[i]
        j = i - 1
        while j >= 0 and num_list[j] > x:
            num_list[j + 1] = num_list[j]
            j = j - 1

        num_list[j + 1] = x
        print(num_list)


def main():
    insertion_sort(number_list)

if __name__ == '__main__':
    main()
