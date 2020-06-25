import os

class WinLoss:
    def __init__(self):

            Winfile = open('winCount.txt', 'w+')
            Winfile.write("0")
            Winfile.close()


            Lossfile = open('lossCount.txt', 'w+')
            Lossfile.write("0")
            Lossfile.close
        
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


MyWinLoss = WinLoss()
MyWinLoss.addWin()
MyWinLoss.addWin()