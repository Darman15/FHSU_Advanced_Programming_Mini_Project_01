def fibonacci_generator(top_num):
    a = 0
    b = 1
    while a <= top_num:
        yield a
        c = a  
        a = b
        b = c + b

# enter the top number to go to in param
fibanacci_list = []
fibanacci_list = fibonacci_generator(377)
# printing to make sure I 'made' a generator object
print(fibanacci_list)

for num in fibanacci_list:
    print(num)