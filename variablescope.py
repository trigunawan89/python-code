x = 'Global x'

def test():
    #global x
    y = 'Local y'
    x = 'Local x'
    print(x +','+y)

if __name__ == '__main__':
    test()
    print(x)
