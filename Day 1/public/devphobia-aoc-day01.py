def increment_counter(list, w_size, counter=0):
    '''
    Calculates number of increments by
    comparing the current window's first
    number to it's sucessor's last number.

    Example:

    window_a = a + b + c
    window_b = b + c + d

    window_b > window_a if d > a
    '''
    for i in range(len(list)):
        if i <= (len(list) - 1  - w_size) and list[i+w_size] > list[i]: counter += 1
    return counter

depths = [int(depth) for depth in open("input.txt", "r").readlines()]

print(increment_counter(depths, 1), increment_counter(depths, 3))
