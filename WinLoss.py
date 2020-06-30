import os
import requests
import myTkinter

class WinLoss:
    def __init__(self):
        if not os.path.exists('winCount.txt'):
            Winfile = open('winCount.txt', 'w+')
            Winfile.write("0")
            Winfile.close()

        if not os.path.exists('lossCount.txt'):
            Lossfile = open('lossCount.txt', 'w+')
            Lossfile.write("0")
            Lossfile.close()

        if not os.path.exists('steamID64.txt'):
            steamID64 = open('steamID64.txt', 'w+')
            steamID64.write("Delete this line and enter your SteamID64")
            steamID64.close()

        
    def addWin(self):
        Winfile = open('winCount.txt', 'r')
        Wins = Winfile.readlines()
        Winfile.close()
        print(Wins[0])

        NewWins = int(Wins[0]) + 1
        print(NewWins)
        
        NewWinfile = open('winCount.txt', 'w')
        NewWinfile.write(str(NewWins))
        NewWinfile.close()

    def addLoss(self):
        Lossfile = open('lossCount.txt', 'r')
        Losses = Lossfile.readlines()
        Lossfile.close()
        print(Losses[0])

        NewLosses = int(Losses[0]) + 1
        print(NewLosses)

        NewLossfile = open('lossCount.txt', 'w')
        NewLossfile.write(str(NewLosses))
        NewLossfile.close()

myWinLoss = WinLoss()

myTkinter.top.mainloop()