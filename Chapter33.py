def one_way(my_list, number):
    while number !=0:
        if number > 0:
            elem = my_list.pop(0)
            my_list.append(elem)
            number -= 1
        else:
            elem = my_list.pop(-1)
            my_list.insert(0, elem)
            number += 1
    return my_list




def main():
    my_list = input("Input elements of list with 'SPACE': ").split()
    num = int(input('Input with size of moving: '))
    new_list = one_way(my_list, num)
    print(new_list)

main()