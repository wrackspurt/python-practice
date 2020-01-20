# Set Mutations (solution 3)


if __name__ == '__main__':
    try:
        m = int(input('please, enter the number of elements in set A: '))
        a = set(int(i) for i in input('please, enter the elements of set A: ').split())
        n = int(input('please, enter the number of other sets: '))
        if len(a) == m:
            for _ in range(n):
                operation, *length = input('please, enter the operation name and the length of the set: ').split()
                if operation in ['update', 'intersection_update', 'difference_update', 'symmetric_difference_update']:
                    new_set = set(map(int, input('please, enter the elements of the set: ').split()))
                    if operation == 'update':
                        a.update(new_set)
                    elif operation == 'intersection_update':
                        a.intersection_update(new_set)
                    elif operation == 'difference_update':
                        a.difference_update(new_set)
                    elif operation == 'symmetric_difference_update':
                        a.symmetric_difference_update(new_set)
                else:
                    print('wrong operation')
                    exit(-1)
        print(sum(a))
    except ValueError:
        print('wrong input')
