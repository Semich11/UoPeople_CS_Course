# def function2(param):
#     print (param, param)
#     print (cat)

# def function1(part1, part2):
#     cat = part1 + part2
#     function2(cat)

# chant1 = "See You "
# chant2 = "See Me"
# function1(chant1, chant2)



# def test_function( length, width, height):
#     print ("the area of the box is ", length*width*height)
#     return length*width*height

# l = 12.5
# w = 5
# h = 2
# test_function(l, w, h)

# print ("The area of the box is ", length*width*height)


# def area(l, w):
#     temp = l * w;
#     print("Here is the Temp:::  ", temp)
#     return temp

# l = 4.0
# w = 3.25
# x = area(l, w)
# print("xxxx:   ",   x)
# if ( 0.1 ):
#   print (x)


# n = int(10.)

# print(isinstance(n, float), isinstance(n * 1.0, float))


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        print("Here here")
        result = n * recurse
        print(space, 'returning', result)
        return result

factorial(4)

print(0*1)