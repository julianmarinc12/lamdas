
def run():
    my_list =[1 , "hello" , True , 4.5]
    my_dic ={"firstname":"facundo","lastname":"garcia"}


    super_list = [
        
        {"firstname":"facundo","lastname":"garcia"},
        {"firstname":"julian","lastname":"marin"},
        {"firstname":"facu","lastname":"coral"},
        {"firstname":"ferd","lastname":"perez"}
    ]

    super_dic = {

        "natrurales": [1,2,3,4],
        "integer": [-1,-2,-3,-4],
        "floads": [1.2,12.2,3.2]
    }

    for key, value in super_dic.items():
        print(key," ",value)

    for person in super_list:
        print(person)



if __name__ == "__main__":
    run()