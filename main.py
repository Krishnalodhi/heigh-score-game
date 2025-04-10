import random
yes="y"
while yes=="y":
    def game(num):
        with open("heigh.txt") as heigh:
            score=heigh.read()
            if score=="":
                with open("heigh.txt","w") as new:
                    score=new.write(str(num))
                    print("\nnew heigh score is :- ",num)
            elif int(score) > num:
                print("\nbetter luck next time !",num)
            else:
                print("\nyou win :) \nyour new score :- ",num,"\n")
                with open("heigh.txt","w") as new:
                    new.write(str(num))
        yes=input("\nwant to play again y/n :- ")
    num = random.randint(1,99)
    game(num)
