# # # # # def any_lowercase1(s):
# # # # #      for c in s:
# # # # #           if c.islower():
# # # # #                return True
# # # # #           else:
# # # # #                return False


# # # # # 2

# # # # # def any_lowercase2(s):
# # # # #      for c in s:
# # # # #           if 'c'.islower():
# # # # #                return 'True'
# # # # #           else:
# # # # #                return 'False'
# # # #                #Always return true


# # # # # # 3

# # # # # def any_lowercase3(s):
# # # # #      for c in s:
# # # # #           flag = c.islower()
# # # # #      return flag


# # # # # # 4

# # # # # def any_lowercase4(s):
# # # # #      flag = False
# # # # #      for c in s:
# # # # #           flag = flag or c.islower()
# # # # #      return flag

# # # #      #Correct function

# # # # # # 5

# # # # def any_lowercase5(s):
# # # #      for c in s:
# # # #           if not c.islower():
# # # #                return False
# # # #      return True




# # # # # print(any_lowercase1('ha'))
# # # # # print('ha')

# # # # # print(any_lowercase1('HA'))
# # # # # print('HA')


# # # # # print(any_lowercase1('Ha'))
# # # # # print('Ha')

# # # # # print(any_lowercase1('hA'))
# # # # # print('hA')





# # # # # print(any_lowercase2('ha'))
# # # # # print('  ha')

# # # # # print(any_lowercase2('HA'))
# # # # # print('HA')


# # # # # print(any_lowercase2('Ha'))
# # # # # print('Ha')

# # # # # print(any_lowercase2('hA'))
# # # # # print('hA')


# # # # # print(3)
# # # # # print(any_lowercase3('ha'))
# # # # # print('  ha')

# # # # # print(any_lowercase3('HA'))
# # # # # print('HA')


# # # # # print(any_lowercase3('Ha'))
# # # # # print('Ha')

# # # # # print(any_lowercase3('hA'))
# # # # # print('hA')



# # # # # print(4)
# # # # # print(any_lowercase4('ha'))
# # # # # print('  ha')

# # # # # print(any_lowercase4('HA'))
# # # # # print('HA')


# # # # # print(any_lowercase4('Ha'))
# # # # # print('Ha')

# # # # # print(any_lowercase4('hA'))
# # # # # print('hA')



# # # # print(5)
# # # # print(any_lowercase5('ha'))
# # # # print('  ha')

# # # # print(any_lowercase5('HA'))
# # # # print('HA')


# # # # print(any_lowercase5('Ha'))
# # # # print('Ha')

# # # # print(any_lowercase5('hA'))
# # # # print('hA')

# # # name = "christopher"

# # # reversed_name = ""

# # # for char in name:
# # #     print(char)
# # #     reversed_name = char + reversed_name

# # # print("Reversed name:", reversed_name)



# # def subroutine( n ):
# #     while n > 0:
# #         print (n)
# #         n = n - 1

# # subroutine(10)


# while True:

#     while 1 > 0:

#         break

#     print("Got it!")

#     break

# n = 10000
# count = 0
# while n:
#     count = count + 1
#     print('count', count)
#     n = n // 10
#     print("Print: ", n)
# print (count)

index = "Ability is a poor man's wealth".find("W")
print(index)

my_list = [3, 2, 1]
print(my_list.sort())

mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
a=0
total = 0
while a < 3:
    b = 0
    while b < 2:
        total += mylist[a][b]
        b += 1
    a += 1
print(total)


mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2

pi = float(3.14159)
print (pi)


percentage = float ( 60 * 100) / 55
print (percentage)
import timeit

setup_code = "my_list = list(range(1000000)); my_tuple = tuple(my_list)"

list_time = timeit.timeit("for x in my_list: pass", setup=setup_code, number=5)
tuple_time = timeit.timeit("for x in my_tuple: pass", setup=setup_code, number=5)

print("List loop:", list_time)
print("Tuple loop:", tuple_time)

print((2,5))
print(2 ** 3 ** 2)
print(2 ** 9)
n=5
print(n,)



matrix = [
    [2,2,1],
    [1,2,3],
    [1,1,1]
]

total = 0

for sublist in matrix:
    total+=sum(sublist)


print("Total: ", total)

i = 2
def myf(s, n):
    global i
    print(s*i*n)

myf('h1-', 3)


02016402517