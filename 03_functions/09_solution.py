def even_generation(limit):
    for  i in range (2, limit +1, 2):
        yield i





for num in even_generation(10):
    print(num)        