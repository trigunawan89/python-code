x = 'Global x variable'

def test():
    #global x
    y = 'Local y variable'
    x = 'Local x variable'
    print(x +','+y)

if __name__ == '__main__':
    test()
    print(x)
