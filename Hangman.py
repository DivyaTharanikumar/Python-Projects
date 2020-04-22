x=1
f = open('C:\\Users\\srifo\\OneDrive\\Desktop\\words.txt', 'r')
lines = f.readlines()
f.close()

while True:
    for line in lines:
        word = line
        if(x==0):
            print("Congratulations! You won the game!")
            next_game=input("Next Game:Y or N")
            if(next_game=='N'):
             break
        g=0
        ln = len(word)
        x = ln - 1
        str = '*'
        str = str * x
        chars = list(str)
        print(chars)

        while(g<=10 and x!=0):
            l=input("Guess a letter")
            g=g+1
            s = chars.count('*')
            for i in range(ln-1):
                 if l==word[i]:
                       chars[i]=l
                       x=x-1
                       print("\n number of letters to guess",x)
                       print("\n Blanks Updated after your guess:", chars)
            if(chars.count('*')==s):
               print("Sorry incorrect gueesing!Try again!")
        if(g>10):
             print("Oops!Game Over")
             next_game = input("Next Game:Y or N")
             if (next_game == 'N'):
                 break