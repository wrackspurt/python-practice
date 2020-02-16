# collections.Counter()
"""Task
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired
size.

Your task is to compute how much money Raghu earned.

Input Format
* The first line contains X, the number of shoes.
* The second line contains the space separated list of all the shoe sizes in the shop.
* The third line contains N, the number of customers.
* The next  lines contain the space separated values of the shoe size desired by the customer and xi, the price of the
shoe.

Constraints
* 0 < X < 10^3
* 0 < N <= 10^3
* 20 < xi < 100
* 2 < shoe size < 20

Output Format
Print the amount of money earned by Raghu.
"""


from collections import Counter

if __name__ == '__main__':
    try:
        x = int(input('enter the number of shoes: '))
        sizes = Counter(
            list(map(int, input('enter the space separated list of all the shoe sizes in the shop: ').split())))
        income = 0
        for _ in range(int(input('enter the number of customers: '))):
            customer_size, *price = input('enter the size and the price of the shoe: ').split()
            if sizes[int(customer_size)]:
                income += int(price[0])
                sizes[int(customer_size)] -= 1
        print(income)
    except ValueError:
        print('wrong input')

