import random
# import string



R = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','.','?']


while True:
    print("1. Encode\n0. Decode\n99. Exit")
    choice = input("# > ")


    if choice=="1":
        a = input("$ > ")
        x = a.split(" ")
        out = []
        for b in x:
            if len(b)<3:
                en = b[::-1]
            else:
                en = b[1:]+b[0]
                for i in range(3):
                    r1 = random.choice(R)
                    r2 = random.choice(R)
                    en = r1 + en + r2
            out.append(en)
        out = " ".join(out)
        print(out)


    elif choice == "0":
        a = input("$ > ")
        x = a.split(" ")
        out = []
        for b in x:
            if len(b)<3:
                en = b[::-1]
            else:
                en = b[1:]+b[0]
                en = b[-4]+b[3:-4]
            out.append(en)
        out = " ".join(out)

        print(out)


    elif choice == "99":
        exit()


    else:
        print("Wrong Input!!!")





