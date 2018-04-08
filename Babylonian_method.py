import random

def sqrt(value):
    value = prevans = float(value)
    try:
        sqrtans = float(random.randint(0,10000000000000000000000000000000000000000000000000000)%value-1+value)
    except:
        sqrtans = 0
    print('Random number is: ', sqrtans)
    print('You are finding the square root of: ', value)
    print('According to the Babylonian Method, each number calculated is your new guess at finding the correct answer:')  
    while sqrtans != prevans:
        prevans = sqrtans
        sqrtans = (sqrtans + (value / sqrtans)) / 2.0
        print (sqrtans)
        if sqrtans < 0:
            return 'Cannot Compute Imaginary Numbers'
            
    print('The square root of your answer is: ')
    return sqrtans

if __name__ == '__main__':
    print(sqrt(144))
        
    
