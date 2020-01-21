# Set Mutations (solution 2)


if __name__ == '__main__':
    try:
        m = int(input('please, enter the number of elements in set A: '))
        a = set(int(i) for i in input('please, enter the elements of set A: ').split())
        if len(a) == m:
            for _ in range(int(input('please, enter the number of other sets: '))):
                operation, *length = input('please, enter the operation name and the length of the set: ').split()
                try:
                    getattr(a, operation)(set(map(int, input('please, enter the elements of the set: ').split())))
                except AttributeError:
                    print('something went wrong')
                    exit(-1)
        else:
            print('incorrect input')
            exit(-1)
        print(sum(a))
    except ValueError:
        print('wrong input')
