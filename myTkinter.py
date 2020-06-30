import tkinter

def connectAPI():
    userID = steamID64.get()


def reset():
    Winfile = open('winCount.txt', 'w+')
    Winfile.write("0")
    Winfile.close()

    Lossfile = open('lossCount.txt', 'w+')
    Lossfile.write("0")
    Lossfile.close

# Beginning of Tkinter code
top = tkinter.Tk()
steamID64 = tkinter.Entry()
connect_button = tkinter.Button(top, text="CONNECT", command = connectAPI )

b = tkinter.Button( top,
                    text = "RESET",
                    fg="red",
                    command = reset
                  )

tkinter.Label(text = "Enter your SteamID64").pack()

steamID64.pack()
connect_button.pack()
b.pack()

