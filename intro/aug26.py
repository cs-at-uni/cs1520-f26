import random

DIE_SIDES = 6

def silly_method():
    try:
        print(int(input('Enter a number: ')))
        print('After data conversion')
    except:
        print('Invalid integer')
        print('Try again')

    print('Done')

if __name__=='__main__':
    #silly_method()

    #counts = []

    '''
    for index in range(DIE_SIDES * 2+1):
        counts.append(0)
    '''
    '''
    for _ in range(DIE_SIDES * 2 + 1):
        counts.append(0)
        #print(_)
    '''

    # List comprehension
    counts = [0 for _ in range(DIE_SIDES * 2 + 1)]

    random_rolls = [random.randint(2,DIE_SIDES * 2) for _ in range(1000)]

    print(counts)

    print(eval(input('Enter command: ')))
    