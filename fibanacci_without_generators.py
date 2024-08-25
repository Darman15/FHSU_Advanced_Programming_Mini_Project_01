def fibonacci_up_to_n(top_num):
    sequence = []
    a = 0
    b = 1   
    while a <= top_num:
        sequence.append(a)
        c = a
        a = b
        b = c + a
    return sequence

# enter number we want to go up to in
result = fibonacci_up_to_n(377)
print(result)
