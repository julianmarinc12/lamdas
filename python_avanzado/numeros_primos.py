def es_primo(num:int)->bool:
    for n in range(2, num):
        if num % n != 0:
            return True
    return False



def run():
    print(es_primo("a"))


if __name__ =="__main__":
    run()
