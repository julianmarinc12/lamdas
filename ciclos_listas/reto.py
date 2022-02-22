
from re import S


def run():
    Squares = [ i for i in range(1,9999) if i%4==0 and i%6==0 and i%9==0 ]

    print(Squares)


if __name__ =="__main__":
    run()