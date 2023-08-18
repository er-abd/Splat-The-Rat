from tkinter import (
    Tk,
    Canvas,
    Button,
    Entry,
    PhotoImage,
    NW,
    CENTER,
    END,
    Radiobutton,
    StringVar,
    messagebox,
)
import json
from random import randint as rand

# This game was developed by: Abdullah Alabdullah
# Completed on 25/11/2022
# All images in this game are taken from the following websites: pixabay.com, unsplash.com, shutterstock.com
# Default Screen resolution is 1920x1080.


# default screen resolution is 1920x1080.
width = 1920
height = 1080


def removeDefaultText(event, entry):
    """This function removes the defualt from the Entry box in the navigation window"""
    playerNameField.delete(0, END)


def updateChoosenVehicle(index):
    """This function changes the vehicle displayed in the game responding to user customization in the settings window"""
    global choosenVehicleIndex
    choosenVehicleIndex = index


def updateChoosenTime(length):
    """This function changes the length of the game responding to user customization in the settings window"""
    global gameTime
    gameTime = length


def updateChoosenBack(back):
    """This function changes the background color of the game responding to user customization in the settings window"""
    global backCol
    backCol = back


def keysWindowStart():
    """This function opens a new window which shows how the game operates i.e. keys used in the game."""
    global keysWindow
    # if the keysWindow does not exist, create it then distroy the navCanvas (where we came from).
    if not boardCanvas.winfo_exists():
        keysWindow = Canvas(window, width=width, height=height, bg=backCol)
    navCanvas.destroy()
    keysWindowImage = keysWindow.create_image(1600, 780, image=keysBackImage)

    # navigation buttons
    mainWindowBtn = Button(
        window,
        command=navWindowStart,
        text="👈  Back",
        background=backCol,
        foreground="#880808",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    # this places the button on the screen.
    boardWindow = keysWindow.create_window(175, 50, window=mainWindowBtn, anchor=CENTER)

    # Movement keys
    # create a text on the keys Window.
    keysWindow.create_text(
        350,
        200,
        anchor=NW,
        font="System 33 bold",
        text="Up:-   ⬆ or  w",
        fill="#880808",
    )
    keysWindow.create_text(
        350,
        270,
        anchor=NW,
        font="System 33 bold",
        text="Right:-   ➡️ or  w",
        fill="#880808",
    )
    keysWindow.create_text(
        350,
        340,
        anchor=NW,
        font="System 33 bold",
        text="Down:-   ⬇️ or  w",
        fill="#880808",
    )
    keysWindow.create_text(
        350,
        410,
        anchor=NW,
        font="System 33 bold",
        text="Left:-   ⬅️ or  w",
        fill="#880808",
    )

    # Other keys
    keysWindow.create_text(
        950,
        200,
        anchor=NW,
        font="System 33 bold",
        text="Pause & Restart:- Escape",
        fill="#880808",
    )
    keysWindow.create_text(
        950,
        270,
        anchor=NW,
        font="System 33 bold",
        text="Boss-Key:- Alt+b",
        fill="#880808",
    )
    keysWindow.create_text(
        950,
        340,
        anchor=NW,
        font="System 33 bold",
        text="Increase Speed:- Control-f",
        fill="#880808",
    )
    keysWindow.create_text(
        950,
        410,
        anchor=NW,
        font="System 33 bold",
        text="Extra Time:- Control-t",
        fill="#880808",
    )

    #pack any changes
    keysWindow.pack()


def settingsWindowStart():
    """This function opens a window that allows the user to customise the game by changing the vehicel, game lendth or background coulor."""
    global settingsWindow
    if not settingsWindow.winfo_exists():
        settingsWindow = Canvas(window, width=width, height=height, bg=backCol)
    navCanvas.destroy()
    endGameWindow.destroy()
    # create an image on the settings window.
    settingsWindowImage = settingsWindow.create_image(250, 400, image=settingsImage)

    # Change Used Vehicle
    settingsWindow.create_text(
        750,
        30,
        anchor=NW,
        font="System 38 bold",
        text="How do you want to kill the rats?",
        fill="#880808",
    )
    # this variable groups all the buttons that change the used vehicle.
    z = StringVar()
    tunkBtn = Radiobutton(
        window,
        image=vehicles[0],
        selectcolor="#880808",
        command=lambda: updateChoosenVehicle(0),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=z,
        width=200,
        value="a",
    )
    tunkBtnPlace = settingsWindow.create_window(900, 230, window=tunkBtn, anchor=CENTER)

    motorBtn = Radiobutton(
        window,
        image=vehicles[1],
        selectcolor="#880808",
        command=lambda: updateChoosenVehicle(1),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=z,
        width=200,
        value="b",
    )
    motorBtnPlace = settingsWindow.create_window(
        1200, 230, window=motorBtn, anchor=CENTER
    )

    eagleBtn = Radiobutton(
        window,
        image=vehicles[2],
        selectcolor="#880808",
        command=lambda: updateChoosenVehicle(2),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=z,
        width=200,
        value="C",
    )
    eagleBtnPlace = settingsWindow.create_window(
        1500, 230, window=eagleBtn, anchor=CENTER
    )

    # Change Game Timing
    settingsWindow.create_text(
        750,
        380,
        anchor=NW,
        font="System 38 bold",
        text="How many minutes do you want to play?",
        fill="#880808",
    )
    y = StringVar()
    oneMinBtn = Radiobutton(
        window,
        image=times[0],
        selectcolor="#880808",
        command=lambda: updateChoosenTime(60),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=y,
        height=200,
        width=200,
        value="q",
    )
    oneMinBtnPlace = settingsWindow.create_window(
        1050, 580, window=oneMinBtn, anchor=CENTER
    )

    twoMunBtn = Radiobutton(
        window,
        image=times[1],
        selectcolor="#880808",
        command=lambda: updateChoosenTime(120),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=y,
        height=200,
        width=200,
        value="w",
    )
    twoMunBtnPlace = settingsWindow.create_window(
        1350, 580, window=twoMunBtn, anchor=CENTER
    )

    # Change Background Color
    settingsWindow.create_text(
        750,
        700,
        anchor=NW,
        font="System 38 bold",
        text="Change background Colour...",
        fill="#880808",
    )
    r = StringVar()
    color1Btn = Radiobutton(
        window,
        image=colors[0],
        selectcolor="#880808",
        command=lambda: updateChoosenBack("#dfe4ea"),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=r,
        height=200,
        width=200,
        value="j",
    )
    color1BtnPlace = settingsWindow.create_window(
        900, 880, window=color1Btn, anchor=CENTER
    )

    color2Btn = Radiobutton(
        window,
        image=colors[1],
        selectcolor="#880808",
        command=lambda: updateChoosenBack("#dff9fb"),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=r,
        height=200,
        width=200,
        value="k",
    )
    color2BtnPlace = settingsWindow.create_window(
        1200, 880, window=color2Btn, anchor=CENTER
    )

    color3Btn = Radiobutton(
        window,
        image=colors[2],
        selectcolor="#880808",
        command=lambda: updateChoosenBack("#9AECDB"),
        bg=backCol,
        cursor="hand2",
        borderwidth=1,
        indicatoron=0,
        variable=r,
        height=200,
        width=200,
        value="l",
    )
    color3BtnPlace = settingsWindow.create_window(
        1500, 880, window=color3Btn, anchor=CENTER
    )

    # Navigation Buttons
    # when the button is pressed, the command = navWindowStart (open navigation window) will be executed.
    mainWindowBtn2 = Button(
        window,
        command=navWindowStart,
        text="     Main 🕹️",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    navWindowButton = settingsWindow.create_window(
        300, 700, window=mainWindowBtn2, anchor=CENTER
    )

    # quit is a built-in fucntion and used to close the game.
    exitBtn = Button(
        window,
        command=quit,
        text="Exit 🔒",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    exit = settingsWindow.create_window(300, 800, window=exitBtn, anchor=CENTER)
    settingsWindow.pack()


def leaderboardWindowStart():
    """This function opens a window that displays the leaderboard containing the scores of top 10 players."""
    global boardCanvas
    if not boardCanvas.winfo_exists():
        boardCanvas = Canvas(window, width=width, height=height, bg=backCol)
    navCanvas.destroy()
    endGameWindow.destroy()
    boardWindowImage = boardCanvas.create_image(1500, 500, image=boardImage)

    # navigation buttons (as above).
    mainWindowBtn = Button(
        window,
        command=navWindowStart,
        text="     Main 🕹️",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    boardWindow = boardCanvas.create_window(
        1100, 850, window=mainWindowBtn, anchor=CENTER
    )

    exitBtn = Button(
        window,
        command=quit,
        text="Exit 🔒",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    exit = boardCanvas.create_window(1100, 950, window=exitBtn, anchor=CENTER)

    # open the named json file, store it in "f", load f to "data".
    f = open("leaderboard.json")
    data = json.load(f)

    count = 0
    count2 = 0
    # for each user in the data (the stored file), increment count by 1 to count the total number of users in the file.
    for i in data["users"]:
        count += 1
    
    # x,y coords to display the names on the board.
    xx = 200
    yy = 200
    zz = 500

    # create an empty list that can be used to store the scores then sort the list.
    storage = []

    # we only want to display the top 10 scores.
    while count > 0 and count2 < 10:
        # add 50 space between every two names.
        yy += 50
        # {data['users'][count-1]['name']} means: in the file (stored in data), for every user starting from the last one (accounted for by count -1), print their name.
        boardCanvas.create_text(
            xx,
            yy,
            anchor=NW,
            font="System 38 bold",
            text=f"{count2 + 1}.  {data['users'][count-1]['name']}",
            fill="#880808",
        )
        # append the score of that specific user to the empty list "storage" then move up the list (using count -1).
        # count2 += 1 to stop when 10 names are on the screen.
        storage.append(data["users"][count - 1]["score"])
        count -= 1
        count2 += 1
    # sort the list of scores in asscending order.
    sortedList = sorted(storage, reverse=True)

    # set count2=0 to use it again for the scores.
    count2 = 0
    yy = 200
    # count the number of users.
    for i in data["users"]:
        count += 1
    # exactly the same as we did with the names.
    while count > 0 and count2 < 10:
        yy += 50
        boardCanvas.create_text(
            zz,
            yy,
            anchor=NW,
            font="System 38 bold",
            text=sortedList[count2],
            fill="#880808",
        )
        count -= 1
        count2 += 1
    boardCanvas.pack()


def gameWindowStart(name):
    """This function opens a window where the game runs and sets up the game."""
    global gameCanvas, userName

    userName = name
    # save names to json file
    f = open("leaderboard.json")
    data = json.load(f)
    # check if the user played the game before (thier name is in the file).
    for i in data["users"]:
        if i["name"] == userName:
            used = True
            # ask ten user if they want to reset their score.
            if (
                messagebox.askyesno(
                    "Reset Score",
                    "You have played the game before, do you want to reset your score?",
                )
                == True
            ):
                # if the user wants to rest teh score
                count = 0
                # loop through teh file and find that name of the user then store its location in "index"
                for i in data["users"]:
                    if i["name"] == userName:
                        index = count
                    count += 1
                # set the score of the user loacted at "index" to 0.
                data["users"][index]["score"] = 0

                # write the above to the file.
                with open("leaderboard.json", "w") as f:
                    json.dump(data, f, indent=4)
            elif (
                messagebox.askyesno(
                    "Reset Score",
                    "You have played the game before, do you want to reset your score?",
                )
                == False
            ):
                pass
        else:
            used = False
    # if the user is new, append their name to teh file with score=0.
    if not used:
        data["users"].append({"name": userName, "score": 0})
        # serialize the file
        savedData = json.dumps(data, indent=4)
        # write to the file
        with open("leaderboard.json", "w") as board:
            board.write(savedData)
        f.close()
    if not gameCanvas.winfo_exists():
        """This function"""
        gameCanvas = Canvas(window, width=width, height=height, bg=backCol)
    navCanvas.destroy()
    if endGameWindow.winfo_exists():
        endGameWindow.destroy()
    gameCanvas.pack()
    newGame()
    setGamePanel()
    setWindowBackground()
    drawLanes()
    updateLevel()
    drawVehicle()
    placeRat()
    moveRat()
    placeAnimal()
    moveAnimal()
    # show the welcome image when you first run the game.
    babyImage(0)
    updateTime()


def navWindowStart():
    """This function is the main window where users can decide what they want to do, e.g. play the game, chnage settings, learn about keys, see the leaderboard or close the game."""
    global navCanvas, playerNameField
    if not navCanvas.winfo_exists():
        navCanvas = Canvas(window, width=width, height=height, bg=backCol)
        if endGameWindow.winfo_exists():
            endGameWindow.destroy()
        if gameCanvas.winfo_exists():
            gameCanvas.destroy()
        if boardCanvas.winfo_exists():
            boardCanvas.destroy()
        if settingsWindow.winfo_exists():
            settingsWindow.destroy()
        if keysWindow.winfo_exists():
            keysWindow.destroy()
    navWindowImage = navCanvas.create_image(500, 500, image=welcomeImage)

    welcomeTitle = navCanvas.create_text(
        1000, 50, anchor=NW, font="System 90 bold", text="Splat  The  Rat", fill="red"
    )

    # ask the user to input their name if they want to.
    playerNameField = Entry(
        window,
        width=17,
        background=backCol,
        foreground="#636e72",
        font="System 28 bold",
    )
    defaultText = "Your Name"
    # diplaye the defult text in the field.
    playerNameField.insert(0, defaultText)
    # when click on the field with lmb, clear the box to allow for user input. 
    playerNameField.bind(
        "<Button-1>", lambda event: removeDefaultText(event, playerNameField)
    )
    playerNamePlace = navCanvas.create_window(
        1300, 350, window=playerNameField, anchor=CENTER
    )

    playGameBtn = Button(
        window,
        command=lambda: gameWindowStart(playerNameField.get()),
        text="Play 🎮",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    playGame = navCanvas.create_window(1300, 450, window=playGameBtn, anchor=CENTER)

    settingsWindowBtn = Button(
        window,
        command=settingsWindowStart,
        text="Settings ⚙️",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    settingsWindowButton = navCanvas.create_window(
        1300, 550, window=settingsWindowBtn, anchor=CENTER
    )

    keysWindowBtn = Button(
        window,
        command=keysWindowStart,
        text="Keys ⌨️",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    keysWindowBtnPlace = navCanvas.create_window(
        1300, 650, window=keysWindowBtn, anchor=CENTER
    )

    boardWindowBtn = Button(
        window,
        command=leaderboardWindowStart,
        text="Leaderboard 🎩",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    boardWindow = navCanvas.create_window(
        1300, 750, window=boardWindowBtn, anchor=CENTER
    )

    exitBtn = Button(
        window,
        command=quit,
        text="Exit 🔒",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    exit = navCanvas.create_window(1300, 850, window=exitBtn, anchor=CENTER)

    navCanvas.pack()


def updateTime():
    """This function simply updates the timer every 1s (1000ms) as long as the game is not paused and finishs the game when time=0."""
    global timerText, timeUp
    if gamePaused == 0:
        timerText = timerText - 1
        gameCanvas.itemconfig(timerCanvas, text=f"Time Left:     {timerText}  ⏳")
    if timerText == 0:
        timeUp = 1
        endGameWindowStart()
    window.after(1000, updateTime)


def pauseGame():
    """This function is called from the function that repons to the pause key event. It simply inverts the value of gamePaused everytime the function is called."""
    global gamePaused, pauseImage
    # negate the boolean values 0 and 1 whenever the pause button is pressed.
    gamePaused ^= 1
    if gamePaused == 1:
        pauseImage = gameCanvas.create_image(950, 500, image=gamePausedImage)
    if gamePaused == 0:
        gameCanvas.delete(pauseImage)


def endGameWindowStart():
    """This function is called when the game ends. Here, player can see their scores and navigate to the main window or see the leaderboard."""
    global endGameWindow, userScore
    # make an endGame window if it is not already
    if not endGameWindow.winfo_exists():
        endGameWindow = Canvas(window, width=width, height=height, bg=backCol)
    # distroy the original window after endGameWindow is created
    if endGameWindow.winfo_exists():
        gameCanvas.destroy()
    # set endGame Window images
    gameOver1 = endGameWindow.create_image(250, 270, image=endGameImages[0])
    gameOver2 = endGameWindow.create_image(1580, 820, image=endGameImages[1])
    # Texts
    # if the reason for gameOver is score=0 show the following
    if scoreZero == 1:
        endGameWindow.create_text(
            450,
            330,
            anchor=NW,
            font="System 40 bold",
            text="Next time don't kill innocent animals  🐱",
            fill="#880808",
        )
        endGameWindow.create_text(
            450,
            430,
            anchor=NW,
            font="System 40 bold",
            text=f"Your final score:  {userScore} ⚔️",
            fill="#880808",
        )
    # if the reason for gameOver is time=0 show the following
    if timeUp == 1:
        endGameWindow.create_text(
            450,
            330,
            anchor=NW,
            font="System 40 bold",
            text="Time Up           ⏳",
            fill="#880808",
        )
        endGameWindow.create_text(
            450,
            430,
            anchor=NW,
            font="System 40 bold",
            text="Well Done         🤞",
            fill="#880808",
        )
        endGameWindow.create_text(
            450,
            530,
            anchor=NW,
            font="System 40 bold",
            text=f"Your final score:  {userScore} ⚔️",
            fill="#880808",
        )
    
    # naviagtion buttons
    mainWindowBtn = Button(
        window,
        command=navWindowStart,
        text="     Main 🕹️",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    boardWindow = endGameWindow.create_window(
        1000, 750, window=mainWindowBtn, anchor=CENTER
    )

    boardWindowBtn1 = Button(
        window,
        command=leaderboardWindowStart,
        text="Leaderboard 🎩",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    boardWindow = endGameWindow.create_window(
        1000, 850, window=boardWindowBtn1, anchor=CENTER
    )

    exitBtn = Button(
        window,
        command=quit,
        text="Exit 🔒",
        background=backCol,
        foreground="red",
        font="System 25 bold",
        anchor=CENTER,
        width=15,
        cursor="hand2",
    )
    exit = endGameWindow.create_window(1000, 950, window=exitBtn, anchor=CENTER)

    finalScore = userScore

    f = open("leaderboard.json")
    data = json.load(f)
    # get the location of the username in the file.
    count = 0
    for i in data["users"]:
        if i["name"] == userName:
            index = count
        count += 1
    # store the user score in the appropriate place.
    data["users"][index]["score"] = finalScore
    
    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)
    # pack any changes
    endGameWindow.pack()


def checkScore():
    """This function checks if the score is  <= 0 so the game can be ended."""
    global userScore, scoreZero
    # end the game if score is less than 0
    if userScore <= 0:
        userScore = 0
        scoreZero = 1
        endGameWindowStart()


def fastVehicle(event):
    """This function responds the cheat code that makes the vehicle faster by increasing its speed."""
    global fastVehicleAllow, vehicleSpeed
    if fastVehicleAllow > 0:
        fastVehicleAllow = fastVehicleAllow - 1
        vehicleSpeed = vehicleSpeed + 5


def extraTime(event):
    """This function responds to the extra time cheat code by increasing the length of the game."""
    global extraTimeAllow, timerText
    if extraTimeAllow > 0:
        extraTimeAllow = extraTimeAllow - 1
        timerText = timerText + 10
        gameCanvas.itemconfig(timerCanvas, text=f"Time Left:     {timerText}  ⏳")


def bossHere(event):
    """This function pauses the game and shows an image when the display boss key is prressed."""
    global bossKeyOn, gamePaused, window, bossStateImage
    # negate the boolean 0 and 1
    bossKeyOn ^= 1
    # pause game
    gamePaused ^= 1
    if bossKeyOn == 1:
        # change the window title.
        window.title("Course Enrolement")
        bossStateImage = gameCanvas.create_image(x, y, image=bossImage)
    if bossKeyOn == 0:
        # show the original title.
        window.title("Splat The Rat")
        gameCanvas.delete(bossStateImage)


def pauseEvent(event):
    """This function triggers when the pausekey is pressed."""
    pauseGame()


def moveN(event):
    """This function triggers when the user presses any of the move up keys."""
    vehicle_coords = gameCanvas.coords(vehicle)
    # only move when the game is not paused
    if gamePaused == 0:
        if vehicle_coords[1] > 90:
            gameCanvas.move(vehicle, 0, -vehicleSpeed)


def moveS(event):
    """This function triggers when the user presses any of the move down keys."""
    vehicle_coords = gameCanvas.coords(vehicle)
    # only move when the game is not paused
    if gamePaused == 0:
        if vehicle_coords[1] < 930:
            gameCanvas.move(vehicle, 0, vehicleSpeed)


def moveW(event):
    """This function triggers when the user presses any of the move to the left keys."""
    vehicle_coords = gameCanvas.coords(vehicle)
    # only move when the game is not paused
    if gamePaused == 0:
        if vehicle_coords[0] > 720:
            gameCanvas.move(vehicle, -vehicleSpeed, 0)


def moveE(event):
    """This function triggers when the user presses any of the move to the right keys."""
    vehicle_coords = gameCanvas.coords(vehicle)
    # only move when the game is not paused
    if gamePaused == 0:
        if vehicle_coords[0] < 1820:
            gameCanvas.move(vehicle, vehicleSpeed, 0)


def updateLevel():
    """This function updates the level corresponding to change in the score."""
    global mov_speed, animal_live, userScore
    if userScore <= 100:
        level = 1
        gameCanvas.itemconfig(levelCanvas, text="Your Level:   ⚡")
        mov_speed = 2
        animal_live = 5
    elif 100 < userScore <= 200:
        level = 2
        gameCanvas.itemconfig(levelCanvas, text="Your Level:   ⚡ ⚡")
        mov_speed = 4
        animal_live = 10
    elif 200 < userScore <= 350:
        level = 3
        gameCanvas.itemconfig(levelCanvas, text="Your Level:   ⚡ ⚡ ⚡")
        mov_speed = 5
        animal_live = 10
    elif userScore > 350:
        userScore = 8
        gameCanvas.itemconfig(levelCanvas, text="Your Level:   ⚡ ⚡ ⚡ ⚡")
        mov_speed = 6
        animal_live = 15


def newGame():
    """This function sets up a new game by re-initializing some variables."""
    global userScore, scoreZero, timeUp

    f = open("leaderboard.json")
    data = json.load(f)


    count = 0
    # if the user has played the game before, get their old score.
    for i in data["users"]:
        if i["name"] == userName:
            index = count
        count += 1
    userScore = data["users"][index]["score"]

    scoreZero = 0
    timeUp = 0


def blood(type):
    """This function shows blood on the screen after an animal is killed."""
    # display the blood where the animal/rat was killed.
    if type == 1:
        rat_coords = gameCanvas.coords(rat)
        choosen_blood = bloods[0]
        blood = gameCanvas.create_image(0, 0, image=choosen_blood)
        bloodX = rat_coords[0]
        bloodY = rat_coords[1]
        gameCanvas.move(blood, bloodX, bloodY)
        # cleare the blood after 2s.
        window.after(2000, gameCanvas.delete, blood)
    elif type == 2:
        animal_coords = gameCanvas.coords(animal)
        choosen_blood = bloods[0]
        blood = gameCanvas.create_image(0, 0, image=choosen_blood)
        bloodX = animal_coords[0]
        bloodY = animal_coords[1]
        gameCanvas.move(blood, bloodX, bloodY)
        window.after(2000, gameCanvas.delete, blood)


# the function will check if the vehicle is overlapping with the rat.
def overlapping(i, j):
    """This function checks when the vehicle collides with a rat or an animal."""
    # determine if the coordinates of the two objects are overlapping.
    if i[0] < j[2] and i[2] > j[0] and i[1] < j[3] and i[3] > j[1]:
        # return True if they are overlapping.
        return True
    return False


def drawVehicle():
    """This function draws the vehicle and called when the game starts."""
    global vehicle
    choosenVehicle = vehicles[choosenVehicleIndex]
    vehicle = gameCanvas.create_image(x + 330, 800, image=choosenVehicle)


def moveAnimal():
    """This function moves the animal when the game is not paued or the bosskey is not on."""
    global userScore, killedAnimlas
    killedAnimlas = False
    # get rat coords
    animal_coords = gameCanvas.coords(animal)
    t = gameCanvas.create_rectangle(gameCanvas.bbox(animal), outline="")
    animal_4_coords = gameCanvas.coords(t)
    # get vehicle coords
    # convert (x,y) coords to (x0, y0, x1, y1) which will be used for checking overlapping.
    v = gameCanvas.create_rectangle(gameCanvas.bbox(vehicle), outline="")
    vehicle_4_coords = gameCanvas.coords(v)
    if animal_coords[1] > 1030:
        gameCanvas.delete(animal)
        placeAnimal()
    elif overlapping(animal_4_coords, vehicle_4_coords):
        gameCanvas.delete(baby_image)
        userScore = userScore - animal_live
        gameCanvas.itemconfig(
            scoreCanvas, text=f"Your Score:        {userScore}    ↘️", fill="#880808"
        )
        updateLevel()
        blood(2)
        checkScore()
        babyImage(rand(5, 7))
        gameCanvas.delete(animal)
        placeAnimal()
        messageNum = rand(1, 4)
        choosenMessage = negMessages[messageNum]
        gameCanvas.itemconfig(comCanvas, text=choosenMessage, fill="#880808")
    else:
        # only move when the game is not paused
        if gamePaused == 0:
            gameCanvas.move(animal, 0, mov_speed)
    if "gameOver" not in locals():
        # 10 is the speed
        window.after(10, moveAnimal)


# This function will remove the first rat after it has left the gameCanvas and make a new one.``
def moveRat():
    """This function moves the animal when the game is not paued or the bosskey is not on."""
    global userScore
    # get rat coords
    rat_coords = gameCanvas.coords(rat)
    q = gameCanvas.create_rectangle(gameCanvas.bbox(rat), outline="")
    rat_4_coords = gameCanvas.coords(q)
    # get vehicle coords
    s = gameCanvas.create_rectangle(gameCanvas.bbox(vehicle), outline="")
    vehicle_4_coords = gameCanvas.coords(s)
    if rat_coords[1] > 1030:
        gameCanvas.delete(rat)
        placeRat()
    elif overlapping(rat_4_coords, vehicle_4_coords):
        gameCanvas.delete(baby_image)
        userScore = userScore + 10
        gameCanvas.itemconfig(
            scoreCanvas, text=f"Your Score:        {userScore}    ↗️", fill="#4cd137"
        )
        updateLevel()
        blood(1)
        babyImage(rand(1, 3))
        gameCanvas.itemconfig(baby_image, image=babyImages[rand(1, 3)])
        gameCanvas.delete(rat)
        placeRat()
        messageNum = rand(1, 4)
        choosenMessage = posMessages[messageNum]
        gameCanvas.itemconfig(comCanvas, text=choosenMessage, fill="#4cd137")
    else:
        # only move when the game is not paused
        if gamePaused == 0:
            gameCanvas.move(rat, 0, mov_speed)
    if "gameOver" not in locals():
        window.after(10, moveRat)  # speed


def placeAnimal():
    """This function places an animal at ramdom x coordinates when the game starts."""
    global animal, animalX
    animalNum = rand(0, 2)
    choosen_animal = animals[animalNum]
    animalX = rand(720, 1840)
    # create it at (0,0) then move it to the desired location.
    animal = gameCanvas.create_image(0, 0, image=choosen_animal)
    gameCanvas.move(animal, animalX, 0)


def placeRat():
    """This function places a rat at ramdom x coordinates when the game starts."""
    global rat, ratX
    ratNum = rand(0, 3)
    choosen_rat = rats[ratNum]
    ratX = rand(720, 1840)
    rat = gameCanvas.create_image(0, 0, image=choosen_rat)
    gameCanvas.move(rat, ratX, 0)


def babyImage(b):
    """This function displayes an image on the screen in respond to user gaining/loosing points."""
    global baby_image
    choosen_baby_image = babyImages[b]
    baby_image = gameCanvas.create_image(300, 340, image=choosen_baby_image)


def setGamePanel():
    """This function sets the texts and images of the left hand side of the game where we display the score, level, messages, and title."""
    global titleCanvas, titleText, timerCanvas, timerText, levelCanvas, levelText, scoreCanvas, scoreText, comText, comCanvas, userScore
    # -------------------------- SET GAME WINDOW TITLE
    titleText = "Splat The Rat"
    titleCanvas = gameCanvas.create_text(
        140, 25, anchor=NW, font="System 40 bold", text=titleText, fill="#880808"
    )

    # -------------------------- SET GAME WINDOW TIMER
    timerText = gameTime
    timerCanvas = gameCanvas.create_text(
        40,
        670,
        anchor=NW,
        font="System 29 bold",
        text=f"Time Left:     {timerText}  ⏳",
        fill="#18dcff",
    )

    # -------------------------- SET GAME WINDOW LEVEL
    levelText = "Your Level:   ⚡"
    levelCanvas = gameCanvas.create_text(
        40, 760, anchor=NW, font="System 29 bold", text=levelText, fill="#18dcff"
    )

    # -------------------------- SET GAME WINDOW SCORE
    scoreText = f"Your Score:        {userScore}"
    scoreCanvas = gameCanvas.create_text(
        40, 850, anchor=NW, font="System 29 bold", text=scoreText, fill="black"
    )

    # -------------------------- SET GAME WINDOW COMMUNICATION BOX
    comText = "Messages:..................."
    comCanvas = gameCanvas.create_text(
        40, 940, anchor=NW, font="System 29 bold", text=comText, fill="black"
    )


def drawLanes():
    """This function drwas the lanes on the game screen."""
    # store the balls
    line_balls = []
    # store the colours
    c = ["red", "yellow"]

    # the left most line
    space = lane_ball_size
    for i in range(41):
        # covers the width
        x = width // 3 + lane_ball_size
        # only civer the top half
        y = space
        space = space + (height // 45)
        # this is just to store the location of the ball
        xy = (x, y, x + lane_ball_size, y + lane_ball_size)
        # xy is the first 4 parameters that specify the coordinates
        new_line_ball = gameCanvas.create_oval(xy, fill=c[0])
        line_balls.append(new_line_ball)
    line_balls.clear()

    # the 2nd line
    space = lane_ball_size
    for i in range(41):
        # covers the width
        x = 1066
        # only civer the top half
        y = space
        space = space + (height // 45)
        # this is just to store the location of the ball
        xy = (x, y, x + lane_ball_size, y + lane_ball_size)
        # xy is the first 4 parameters that specify the coordinates
        new_line_ball = gameCanvas.create_oval(xy, fill=c[1])
        line_balls.append(new_line_ball)
    line_balls.clear()

    # the 2nd line
    space = lane_ball_size
    for i in range(41):
        # covers the width
        x = 1492
        # only civer the top half
        y = space
        space = space + (height // 45)
        # this is just to store the location of the ball
        xy = (x, y, x + lane_ball_size, y + lane_ball_size)
        # xy is the first 4 parameters that specify the coordinates
        new_line_ball = gameCanvas.create_oval(xy, fill=c[1])
        line_balls.append(new_line_ball)
    line_balls.clear()

    # the right most line
    space = lane_ball_size
    for i in range(41):
        # covers the width
        x = width - (lane_ball_size * 4) + lane_ball_size
        # only civer the top half
        y = space
        space = space + (height // 45)
        # this is just to store the location of the ball
        xy = (x, y, x + lane_ball_size, y + lane_ball_size)
        # xy is the first 4 parameters that specify the coordinates
        new_line_ball = gameCanvas.create_oval(xy, fill=c[0])
        line_balls.append(new_line_ball)


def setWindowBackground():
    """This function sets the bakground of the game window."""
    # store the balls
    balls = []
    # store the colours
    c = ["#2ed573", "#1e90ff", "#ff4757"]
    # we want 800 balls
    for i in range(200):
        # covers the width
        x = rand(ball_size, width // 3)
        # only civer the top half
        y = rand(ball_size, height - ball_size)
        # fill colour
        fill = rand(0, 2)
        # this is just to store the location of the ball
        xy = (x, y, x + ball_size, y + ball_size)
        # xy is the first 4 parameters that specify the coordinates
        new_ball = gameCanvas.create_oval(xy, fill=c[fill])
        balls.append(new_ball)


def setWindowDimensions(w, h):
    """This function sets the window dimensions of the game."""
    window = Tk()
    window.title("Splat The Rat")
    # get then store the computer's screen size
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate the center
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    # window size
    window.geometry("%dx%d+%d+%d" % (w, h, x, y))
    # -------------------------- WINDOW ICONS
    return window


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# -------------------------- SET DEFAULT VARIABLES WHEN STARTING THE GAME
gamePaused = 0
bossKeyOn = 0
scoreZero = 0
timeUp = 0
defaultVehicleSpeed = 10
choosenVehicleIndex = 0
vehicleSpeed = defaultVehicleSpeed
mov_speed = 2
gameTime = 60
extraTimeAllow = 2
fastVehicleAllow = 3
backCol = "#dfe4ea"
userScore = 0


# -------------------------- DIMENSSIONS OF MAIN WINDOW CANVAS
x = width / 2
y = height / 2
window = setWindowDimensions(width, height)
gameCanvas = Canvas(window, width=width, height=height, background=backCol)

# -------------------------- SET DIMENSSIONS OF THE BALLS
ball_size = 3
lane_ball_size = 15

# -------------------------- VEHICLE KEY BINDS
window.bind("<Up>", moveN)
window.bind("<Down>", moveS)
window.bind("<Left>", moveW)
window.bind("<Right>", moveE)
window.bind("<w>", moveN)
window.bind("<s>", moveS)
window.bind("<a>", moveW)
window.bind("<d>", moveE)

# -------------------------- OTHER KEY BINDS
window.bind("<Escape>", pauseEvent)
window.bind("<Control-b>", bossHere)
window.bind("<Control-t>", extraTime)
window.bind("<Control-f>", fastVehicle)


# -------------------------- SETTINGS WINDOW IMAGE
settingsImage = PhotoImage(file="images/settings.png").subsample(3)
settingsWindow = Canvas(window, width=width, height=height, bg=backCol)

# -------------------------- WELCOME WINDOW IMAGE
welcomeImage = PhotoImage(file="images/welcome.png").subsample(2)
navCanvas = Canvas(window, width=width, height=height, bg=backCol)

# -------------------------- LEADERBOARD WINDOW IMAGE
boardImage = PhotoImage(file="images/board.png").subsample(2)
boardCanvas = Canvas(window, width=width, height=height, bg=backCol)

# -------------------------- KEYS WINDOW IMAGE
keysBackImage = PhotoImage(file="images/keysBack.png").subsample(1)
keysWindow = Canvas(window, width=width, height=height, bg=backCol)

# -------------------------- End GAME
endGameImages = [
    PhotoImage(file="images/endGame1.png").subsample(1),
    PhotoImage(file="images/endGame2.png").subsample(1),
]
endGameWindow = Canvas(window, width=width, height=height, bg=backCol)

# -------------------------- PAUSE IMAGE
gamePausedImage = PhotoImage(file="images/pause.png").subsample(2)

# -------------------------- BOSS KEY IMAGE
bossImage = PhotoImage(file="images/boss.png")

# -------------------------- MESSAGEBOX ICON
messageboxIcon = PhotoImage(file="images/boss.png")

# -------------------------- VEHICLES
vehicles = [
    PhotoImage(file="images/vehicle1.png").subsample(3),
    PhotoImage(file="images/vehicle2.png").subsample(7),
    PhotoImage(file="images/vehicle3.png").subsample(7),
]

# -------------------------- RATS
rats = [
    PhotoImage(file="images/rat1.png").subsample(7),
    PhotoImage(file="images/rat2.png").subsample(5),
    PhotoImage(file="images/rat3.png").subsample(5),
    PhotoImage(file="images/rat4.png").subsample(7),
]

# -------------------------- ANIMLAS
animals = [
    PhotoImage(file="images/cat.png").subsample(4),
    PhotoImage(file="images/dog.png").subsample(3),
    PhotoImage(file="images/goat.png").subsample(3),
]

# -------------------------- BLOOD
bloods = [PhotoImage(file="images/blood.png").subsample(5)]
# -------------------------- NUMBERED BALLS
times = [
    PhotoImage(file="images/time1.png").subsample(1),
    PhotoImage(file="images/time2.png").subsample(2),
]
# -------------------------- BACKGROUND COLOUR
colors = [
    PhotoImage(file="images/color1.png").subsample(1),
    PhotoImage(file="images/color2.png").subsample(1),
    PhotoImage(file="images/color3.png").subsample(1),
]

# -------------------------- BABAIES Laughign
babyImages = [
    PhotoImage(file="images/hello.png").subsample(1),
    PhotoImage(file="images/babyL3.png").subsample(1),
    PhotoImage(file="images/babyL4.png").subsample(1),
    PhotoImage(file="images/babyL6.png").subsample(1),
    PhotoImage(file="images/babyC1.png").subsample(1),
    PhotoImage(file="images/babyC2.png").subsample(1),
    PhotoImage(file="images/babyC3.png").subsample(1),
    PhotoImage(file="images/babyC4.png").subsample(1),
]


# -------------------------- POSITIVE MESSAGES
posMessages = [
    "Messages:...................",
    "Messages: Yes, you did it 🤞",
    "Messages: Keep going 💪",
    "Messages: Keep killing rats",
    "Messages: Well Done 👍",
]


# -------------------------- NEGATIVE MESSAGES
negMessages = [
    "Messages:...................",
    "Messages: Nooooooooooo 😭",
    "Messages: So Stupid ..... ",
    "Messages: Worst Player 👎 ",
    "Messages: You're a criminal",
]


navWindowStart()


window.mainloop()
