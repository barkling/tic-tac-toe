def menu():
    print("-"*17)
    print("-"*4+"模式1：pvp"+"-"*4)
    print("-"*4+"模式2：pve"+"-"*4)
    print("-"*4+"模式3：eve"+"-"*4)
    print("-"*17)
    model=input(">>>>> 请选择你要游玩的模式：")
    if(model not in["1","2","3"]):
        menu()
    return model

if __name__ == '__main__':
    menu()