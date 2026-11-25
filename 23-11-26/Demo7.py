def demo:
    yeild 10
    yeild 20
    yeild 30
    x=demo()
    print(next(x))
    print(next(x))
    print(next(x))

    forx in demo():
        print(x)
        