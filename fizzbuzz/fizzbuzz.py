#""" This is my fizzbuzz program """
count = int(input('Gimme the top number: '))

def fizzbuzz(max_number):
    # """ this is the fizzbuzz algorithm applied to the value x """
    for x in range(1,max_number):
        if x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        elif x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        else:
            print(x)

fizzbuzz(count)
