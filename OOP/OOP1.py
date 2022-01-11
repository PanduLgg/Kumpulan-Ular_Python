def multiply():
    integer_1 = int(input("enter a whole number: "))
    integer_2 = int(input("enter a whole number: "))
    answer = integer_1 * integer_2
    return ' '.join((str(integer_1), "*", str(integer_2), "=", str(answer)))

print(multiply()) 