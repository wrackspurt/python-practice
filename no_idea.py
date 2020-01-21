# No Idea!
"""Task
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the
integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array,
if i ∈ A, you add 1 to your happiness. If i ∈ B, you add -1 to your happiness. Otherwise, your happiness does not
change. Output your final happiness at the end.
Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format:
* The first line contains integers n and m separated by a space.
* The second line contains n integers, the elements of the array.
* The third and fourth lines contain m integers, A and B, respectively.

Constraints:
* 1 <= n <= 10^5
* 1 <= m <= 10^5
* 1 <= Any integer in input <= 10^9

Output Format:
Output a single integer, your total happiness.
"""


if __name__ == '__main__':
    try:
        n, m = (input('please, enter n and m: ').split())
        if int(n) >= 1 and int(m) >= 1:
            array = list(map(int, input('please, enter the elements of the array: ').split()))
            happiness = 0
            if len(array) == int(n):
                a = set(int(i) for i in input('please, enter the elements of set A: ').split())
                b = set(int(i) for i in input('please, enter the elements of set B: ').split())
                if len(a) == int(m) and len(b) == int(m):
                    for i in array:
                        if i in a:
                            happiness += 1
                        elif i in b:
                            happiness -= 1
                else:
                    print('wrong input')
                    exit(0)
            else:
                print('wrong input')
                exit(0)
            print(happiness)
        else:
            print('incorrect input')
    except ValueError:
        print('incorrect input')
