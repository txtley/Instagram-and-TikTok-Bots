from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from random import randint
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import smtplib

#variables
userCount = 0 

class Instagram():
    comments = [
        'Great Post!', 'Lets go!', 'I love fireworks!'
        ]
     
    def __init__(self):
        self.login('name', 'test12345')


    #function to log in
    def login(self, username, password):
    

        self.driver = webdriver.Chrome()
    
        self.driver.get("https://www.instagram.com/")

        #click decline cookies 
        cookie = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookie.click() 
        time.sleep(5)
        
        #Find username input area and write username
        username = WebDriverWait(self.driver, timeout=60).until(
            lambda d: d.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
        username.send_keys(username)
        
        #Find password input area and write password
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(password)
        
        #Click on Login Button
        enter = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        enter.click()
        time.sleep(10)

            #Click on Not Now in pop up - 'save info'
        SI_not_now = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
        SI_not_now.click()
        time.sleep(0.9)
        
        #Click on not now - 'notifications' 
        N_not_now = self.driver.find_element(By.CSS_SELECTOR, '._a9_1')
        N_not_now.click()
        time.sleep(0.9)

    def follow_users(self, targetUser):
            search = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/div[2]/span/div/a')
            search.click()
            
            search_input = WebDriverWait(self.driver, timeout=60).until(
                lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
            search_input.send_keys(targetUser)
            found = WebDriverWait(self.driver, timeout=60).until(
                lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div/div/span'))
            found.click()
            time.sleep(10)

            #spam following their followers
            followers = WebDriverWait(self.driver, timeout=60).until(
                lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span'))
            followers.click()


            time.sleep(10)
            buttons = WebDriverWait(self.driver, timeout=60).until(
                lambda d: d.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas'))
            time.sleep(5)
            count = 0
            while True:
                for btn in buttons:
                    try:
                        self.driver.execute_script("arguments[0].click();", btn)
                        count += 1
                        print(f"{count} buttons clicked")
                        time.sleep(5)
                    except:
                        print("Skipped something")
                        pass
                scr1 = WebDriverWait(self.driver, timeout=60).until(lambda d: d.find_element(By.XPATH,
                                                                                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'))
                time.sleep(5)
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                print("scrollled")
                buttons = WebDriverWait(self.driver, timeout=60).until(
                    lambda d: d.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas'))
                
    def commentLike(self):
        explore = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/span/div/a/div')
        explore.click()
        time.sleep(5) 

        while True:
           #getting the bot to click on post
            post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[2]/div/div[1]/div[2]/div/a/div[1]/div[2]')
            post.click()
            time.sleep(1) 

            #clicking the like button
            likeButton = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div')
            likeButton.click()
            time.sleep(1)

            #clicking on the comment button
            commentButton = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/div')
            #/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/div')
            commentButton.click()
            time.sleep(1) 

            #writing the comment into the comment box. 
            botComment = self.comments[randint(0,3)]
            commentBox = WebDriverWait(self.driver, timeout=60).until(
                lambda d: d.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea')) 
            commentBox.send_keys(botComment)
            count =+ 1 
            time.sleep(1)

            print('Number of posts commented on: ', count)

class TikTok():
    comments = [
        'Great Post!', 'Lets go!', 'I love fireworks!'
        ]
     
    def __init__(self):
        self.login('pythonautomation1', 'test123456!')

    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.tiktok.com/en/')
        time.sleep(10)

        #clicking log in button 
        loginButton = self.driver.find_element(By.XPATH, '//*[@id="header-login-button"]')
        loginButton.click()
        time.sleep(3) 

        #logging in with username 
        login_with_username = self.driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div/div/div/div[2]/div[2]')
        login_with_username.click()
        time.sleep(3) 

        #selecting #login with email or username 
        emailOrUsername = self.driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div/form/div[1]/a')
        emailOrUsername.click()
        time.sleep(3)

        #clicking on the username box and entering details
        usernameBox = WebDriverWait(self.driver, timeout=60).until(
            lambda d:d.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[1]/input'))
        usernameBox.send_keys(username)
        time.sleep(5)

        #clicking on the password boc and entering details
        passwordBox = WebDriverWait(self.driver, timeout=60).until(
            lambda d:d.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div/input'))
        passwordBox.send_keys(password)
        time.sleep(5)

        #hitting enter
        enter = self.driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/button')
        enter.click()
        time.sleep(10)

    def likeComment_userpage(self, keyword):
        userCount = 0 
        count = 1 
        #search for the search
        search = self.driver.find_element(By.XPATH, '//*[@id="app-header"]/div/div[2]/div/form')
        search.click() 
        time.sleep(1)

        #put the keys into the search
        search_input = self.driver.find_element(By.XPATH, '//*[@id="app-header"]/div/div[2]/div/form/input') 
        search_input.send_keys(keyword)
        time.sleep(1)

        #clicking 'users' button
        usersButton = self.driver.find_element(By.XPATH, '//*[@id="tabs-0-tab-search_account"]')
        usersButton.click()
        time.sleep(1)

       #checking to see which page to click on 
        if userCount == 0:
             #click onto the user's page
            clickUser = WebDriverWait(self.driver, timeout=60).until(
                lambda d:d.find_element(By.XPATH, '//*[@id="search_user-item-user-link-0"]/div/div/a[1]/div'))
            clickUser.click()
            time.sleep(3) 
        else:
            clickUser = WebDriverWait(self.driver, timeout=60).until(
                #adding 1 onto the user's XPATH so it gets the next user
                lambda d:d.find_element(By.XPATH, (f'//*[@id="search_user-item-user-link-{userCount+1}"]/div/div/a[1]/div')))
            clickUser.click()
            time.sleep(3)

        #click on one of the posts
        post = self.driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div[1]/div/div/div/a/div[1]/div[3]')
        post.click()
        time.sleep(1) 

        #comment on the users posts
        commentBox = WebDriverWait(self.driver, timeout=60).until(
            lambda d:d.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div/input'))
        commentBox.send_keys(self.comments[randint(0,2)])
        time.sleep(1)

        #clicking on post button
        postButton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div/div[2]')
        postButton.click()
        time.sleep(1)

        User = self.driver.find_element(By.XPATH, '//*[@id="tabs-0-panel-search_top"]/div/div/div[1]/div[2]/div/div[1]/a[2]/p[1]')

        #looping through the page 
        run = True
        while run:
            try:
                #checking to see whether there is more posts on the page
                nextButton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
                nextButton.click() 
                time.sleep(1)
                #if not then we will end the loop and load up a new page using an F string. 
            except ProcessLookupError:
                run = False 
                userCount =+ 1 #load the next user

            #comment on the users posts
            commentBox = WebDriverWait(self.driver, timeout=60).until(
                lambda d:d.find_element(By.XPATH, '//*[@id="loginContainer"]/div[2]/form/div[2]/div/input'))
            commentBox.send_keys(self.comments[randint(0,2)])
            time.sleep(1)

            #clicking on post button
            postButton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div/div[2]')
            postButton.click()
            time.sleep(1)

            count += 1 

            print('Number of posts commented on: ', count)

        print("No more posts on", User,"'s page. Total number of posts commented on was:", count)
    

class Menu:
    # main tkinter loop
    def __init__(self):
        screen = tk.Tk()
        screen.title('Bot Service')


        # setting the size of the screen
        screen.geometry('500x500')

        #displaying welcome text
        welcomeText = Label(screen, text='Welcome to the bot service!\n Simply input the username and password of the account\n and check which platform you want it to be deployed on!', font = ('Impact', 10))
        welcomeText.place(x=85, y=25)

        #images - speech bubble 
        speechBubbleImage = Image.open('BotService/speechbubble.png')
        speechBubbleImageSize = (50, 50)
        speechBubbleImage = speechBubbleImage.resize(speechBubbleImageSize)
        speechBubbleImage = ImageTk.PhotoImage(speechBubbleImage)

        #instagram
        instagramImage = Image.open('BotService/instagram.png')
        instagramImageSize = (150, 150)
        instagramImage = instagramImage.resize(instagramImageSize)
        instagramImage = ImageTk.PhotoImage(instagramImage)

        #tik tok
        tiktokImage = Image.open('BotService/tiktok.png')
        tiktokImageSize = (100, 100)
        tiktokImage = tiktokImage.resize(tiktokImageSize)
        tiktokImage = ImageTk.PhotoImage(tiktokImage)


        #creating a label for the image 
        speechBubbleImageLabel = tk.Label(screen, image=speechBubbleImage)
        instagramImageLabel = tk.Label(screen, image=instagramImage)
        tiktokImageLabel = tk.Label(screen, image=tiktokImage)

        #placing images 
        speechBubbleImageLabel.place(x=400, y=1)
        instagramImageLabel.place(x=75, y=350)
        tiktokImageLabel.place(x=325, y=375)

        # text boxes for the username and password - this will be stored as a value to send to the functions later on
        usernameLabel = Label(screen, text='Username')
        passwordLabel = Label(screen, text='Password')
        Username = Entry(screen)
        Password = Entry(screen)

        # placing the text boxes
        usernameLabel.place(x=160, y=270)
        passwordLabel.place(x=160, y=290)
        Username.place(x=230, y=270)
        Password.place(x=230, y=290)

        # variables for social media checkboxes
        instagram = tk.BooleanVar()
        tiktok = tk.BooleanVar()

        # variables for Instagram action checkboxes
        spamFollow = tk.BooleanVar()
        commentLike = tk.BooleanVar()

        # variable for Tik Tok checkbox
        userKeyword = tk.BooleanVar() 

        # create text boxes for the user to enter their email for 2fa
        userEmail = Entry(screen)

        # create option text boxes for instagram (dont place yet)
        spamFollowBox = Entry(screen)
        commentlikeBox = Entry(screen)

        # create option text box for tik tok (dont place yet)
        userKeywordBox = Entry(screen)

        #create box for user to enter 2fa code
        userCode = Entry(screen)

        # reminder text
        reminderText = Label(screen, text='Please only select one option!')
        
        # checking if the checkbox has been clicked
        def checkClicked():
            instagramClicked = instagram.get()
            tiktokClicked = tiktok.get()

            # checking if both boxes are clicked, if so uncheck instagram and display reminder
            if instagramClicked and tiktokClicked:
                instagram.set(False)
                reminderText.place(x=150, y=80)
            else:
                # placing the text off the screen
                reminderText.place(x=950, y=80)

            # show or hide the checkbuttons based on whether Instagram is clicked
            if instagramClicked:
                #set tik tok value to false 
                userKeyword.set(False)
                #adding check boxes to the screen
                checkbutton_followers.place(x=200, y=150)
                checkbutton_comments.place(x=200, y=200)
                #ensuring that the boxes and labels from TikTok are hidden
                userKeywordInput.place_forget()
                userKeywordBox.place_forget() 
            else: #if the checkbox isnt ticked, then we're going to hide the boxes, the user entry and the text boxes 
                checkbutton_followers.place_forget()
                checkbutton_comments.place_forget()
                spamFollowBox.place_forget()
                commentlikeBox.place_forget() 

            # show or hide checkbutton based on whether tik tok is clicked 
            if tiktokClicked:
                #set instagram checkboxes to false 
                spamFollow.set(False)
                commentLike.set(False) 
                #adding boxes to the screen
                checkbutton_keyword.place(x=150, y=150)
                checkbutton_comments.place_forget()
                spamfollowEnterUser.place_forget()  
                commentlikeEnterUser.place_forget() 
                #ensuring that the boxes and labels from Instagram are hidden
                spamFollowBox.place_forget()
                commentlikeBox.place_forget()
            else: #hiding the keyword checkbutton from the screen. 
                checkbutton_keyword.place_forget() 
        
        def twoFactorEnterClicked():
            if twoFactorAuthenticationEnterButton:
                twoFactorAuthentication()

        def twoFactorConfirmEnterClicked():
            if twoFactorAuthenticationConfirmEnterButton:
                twoFactorAuthenticationCode = twoFactorAuthentication()
                isCodeCorrect(twoFactorAuthenticationCode)
        

        def enterClicked():
            #if enter button has been clicked 
            if enterButton:
            #asking the user if they want to save their changes 
               quitScreen = messagebox.askquestion('Confirm', 'Are you sure you want to save your changes?')
            if quitScreen == 'yes':
                twoFactorAuthenticationScreen() # <- sending user to the 2fa screen so they can enter their email address

        
        def instagramOptions():
            spamFollowClicked = spamFollow.get()
            commentLikeClicked = commentLike.get()

            #checking to see if both the boxes have been ticked
            if spamFollowClicked and commentLikeClicked:
                spamFollowBox.place(x=270, y=170)
                commentlikeBox.place(x=270, y=220)
                #adding 'enter user' labels to the screen
                spamfollowEnterUser.place(x=160, y=170)
                commentlikeEnterUser.place(x=160, y=220)
            elif spamFollowClicked: #checking to see if one is clicked 
                spamFollowBox.place(x=270, y=170)
                spamfollowEnterUser.place(x=160, y=170)
                #hiding the opposite labels 
                commentlikeBox.place_forget()
                commentlikeEnterUser.place_forget()
            #checking to see if one is clicked 
            elif commentLikeClicked:
                commentlikeBox.place(x=270, y=220)
                commentlikeEnterUser.place(x=160, y=220)
                #hiding the opposite labels 
                spamFollowBox.place_forget()
                spamfollowEnterUser.place_forget()
            else: #checking to see if none have been clicked 
                spamFollowBox.place_forget()
                commentlikeBox.place_forget() 
                spamfollowEnterUser.place_forget()  
                commentlikeEnterUser.place_forget() 
            

        def tiktokOptions():
            userKeywordClicked = userKeyword.get()

            # check to see if the checkbox has been ticked 
            if userKeywordClicked:
                #adding the label and the text box
                userKeywordInput.place(x=160, y=170)
                userKeywordBox.place(x=270, y=170)
                spamfollowEnterUser.place_forget()  
                commentlikeEnterUser.place_forget() 
            else: #hide the label and text box
                userKeywordBox.place_forget() 
                userKeywordInput.place_forget()

        #function which will save the information the user has entered 
        def saveInformation():
            keyword = userKeywordBox.get()
            targetUser = spamFollowBox.get()
            targetUsercomments = commentLike.get()  
            username = Username.get()
            password = Password.get()

            valuesStoredinTextboxes = [keyword, targetUser, username, password, targetUsercomments] # <- getting the values that could be stored in the text boxes and putting them into a list

            ## Controlling the flow of data and running the correct bots and the correct functions that the user requested 
            for value in valuesStoredinTextboxes: # going through the array to check for any inputs 
                if value == '': # checking to see if the value is empty, if so we ignore it
                    pass
                else:
                    # activating the bots before sending over the parameters for the functions
                    if value == valuesStoredinTextboxes[0]: 
                        TikTok.login(valuesStoredinTextboxes[2], valuesStoredinTextboxes[3])
                        TikTok.likeComment_userpage(value)
                    elif value == valuesStoredinTextboxes[1] and value == valuesStoredinTextboxes[4]:
                        Instagram.login(valuesStoredinTextboxes[2], valuesStoredinTextboxes[3])
                        Instagram.follow_users(value)
                        Instagram.commentLike(value)
                    elif value == valuesStoredinTextboxes[1]:
                        Instagram.login(valuesStoredinTextboxes[2], valuesStoredinTextboxes[3])
                        Instagram.follow_users(value)
                    elif value == valuesStoredinTextboxes[4]:
                        Instagram.login(valuesStoredinTextboxes[2], valuesStoredinTextboxes[3])
                        Instagram.commentLike(value)
        
        #function to load the screen (front end)
        def twoFactorAuthenticationScreen():
            #hiding all the other buttons/checkboxes/labels 
            for value in elements:
                value.place_forget() 
            
            #placing all the labels and text boxes for the page 
            twoFactorAuthenticationTextForTextbox.place(x=130, y=250)
            twoFactorAuthenticationText.place(x=100, y=100)
            userEmail.place(x=230, y=250)
            twoFactorAuthenticationEnterButton.place(x=240, y=350)

            twoFactorAuthentication()


        #backend 2fa 
        def twoFactorAuthentication():
            ##checking to see if email is valid 
            #making a list to check if letters before @ are all letters
            emailList = [] 
            for letter in userEmail.get():
                emailList.append(letter)

            #making another list to store the values before the @
            validValues = ['1','2','3','4','5','6','7','8','9','0'] # <- values which are allowed in an email, stops the isalpha check from being false
            isListAlpha = [] # <- list to store the letters before the @ symbol
            for letter in emailList:
                if letter != '@': # <- checking if there is any values before the 
                    isListAlpha.append(letter) # <- if so, append to the list       
                else:
                    strUserEmail = ''.join(isListAlpha) # <- converting the list back to a string to compare
                    for value in strUserEmail:
                        if value in validValues: # <- compare the value to the list 'ValidValues', if its in there then set validNonAlpha to True 
                            validNonAlpha = True
                        else: 
                            validNonAlpha = False
                    if '.' in strUserEmail:  # <- wouldnt accept the dot in the list so it is embedded as an if statement 
                        validNonAlpha = True    
                    if strUserEmail.isalpha() or validNonAlpha == True: # <- check to see if the string is alphabetic or other non alphabetic values are in the string
                        #filtering out to only valud email components 
                        if '@' in userEmail.get():
                            if 'outlook' or 'gmail' or 'yahoo' or 'hotmail' or 'icloud' in userEmail.get():
                                if '.com' or '.co.uk' in userEmail.get():
                                    validEmail = True # <- if all these filtering conditions are met, this value will be set to true and email can be sent. 
                                else:
                                    validEmail = False 
                    
                    if validEmail == True:
                        print('True')
                        ## sending the generated code out to the user's email
                        #variables
                        SMTPportNumber = 587 #<- port number for the smtp protocol 
                        twoFactorAuthenticationCode = randint(100000, 999999) # <- making a random value between 100,000 and 999,999 so the code is six digits 

                        #finding where the @ symbol is in the string
                        count = 0
                        for host in emailList:
                            count += 1
                            if host == '@':
                                atSymbol = count
                        
                        #slicing the user email so that we only have the domain name 
                        userEmailHost = userEmail.get()
                        userEmailHost = userEmailHost[atSymbol:]
                        #starting the email session
                        emailSession = smtplib.SMTP(f'smtp.{userEmailHost}', SMTPportNumber)
                        emailSession.starttls() 
                        #log in 
                        emailSession.login('joshj.titley@outlook.com', 'CyberKid2007')
                        #message 
                        message = (f'Your two factor authentication code is: {twoFactorAuthenticationCode}')
                        #sending email
                        emailSession.sendmail(f'joshj.titley@outlook.com, {strUserEmail}', message)
                        #quitting session 
                        emailSession.quit()

                                    
                        for value in twoFactorAuthenticationElements:
                            value.place_forget() 

                        twoFactorAuthenticationConfirmTextForTextbox.place(x=130, y=250)
                        twoFactorAuthenticationConfirmText.place(x=100, y=100)
                        userCode.place(x=230, y=250)
                        twoFactorAuthenticationConfirmEnterButton.place(x=240, y=350)

                        return twoFactorAuthenticationCode

        def isCodeCorrect(twoFactorAuthenticationCode):
            userCodeValue = userCode.get() 
            if userCodeValue == twoFactorAuthenticationCode:
                saveInformation()
            else:
                twoFactorAuthenticationFailed = Label(screen, text="The code wasn't correct", font= ('Impact', 10))
                twoFactorAuthenticationFailed.place(x=200, y=220)

            
            
                              
         
            
        #making enter button
        enterButton = Button(screen, text='Enter', command=enterClicked)
        enterButton.place(x=240, y=350)

        #making 2fa button
        twoFactorAuthenticationEnterButton = Button(screen, text='Enter', command=twoFactorEnterClicked)

        #making confirm button
        twoFactorAuthenticationConfirmEnterButton = Button(screen, text='Enter', command=twoFactorConfirmEnterClicked)


        # check boxes for instagram and tiktok
        checkbutton_instagram = ttk.Checkbutton(screen, text='Instagram', variable=instagram, command=checkClicked)
        checkbutton_instagram.place(x=200, y=100)

        checkbutton_tiktok = ttk.Checkbutton(screen, text='TikTok', variable=tiktok, command=checkClicked)
        checkbutton_tiktok.place(x=200, y=120)

        # Create Instagram action checkbuttons (but don't place them yet)
        checkbutton_followers = ttk.Checkbutton(screen, text="Spam follow a user's followers", variable=spamFollow, command=instagramOptions)
        checkbutton_comments = ttk.Checkbutton(screen, text='Spam likes and comments on posts', variable=commentLike, command=instagramOptions)

        #create tiktok keyword checkbutton (but dont place yet)
        checkbutton_keyword = ttk.Checkbutton(screen, text='Spam like and comment a users page based off a keyword', variable=userKeyword, command=tiktokOptions)

        # labels and input boxes for usernames on Instagram 
        spamfollowEnterUser = Label(screen, text="Enter User's Page:", font= ('Impact', 10))
        commentlikeEnterUser = Label(screen, text="Enter User's page", font= ('Impact', 10))

        # labels and input for keywords on TikTok
        userKeywordInput = Label(screen, text="Enter a keyword:", font= ('Impact', 10))       

        #label for the 2fa 
        twoFactorAuthenticationText = Label(screen, text="Just to confirm it is you\n enter your email below and we will send you a code ", font= ('Impact', 12))
        twoFactorAuthenticationTextForTextbox = Label(screen, text="Enter Email here: ", font= ('Impact', 10)) 

        #label for 2fa confirm
        twoFactorAuthenticationConfirmText = Label(screen, text='A code shouldve been sent to your email. Enter it below', font=('Impact', 12))
        twoFactorAuthenticationConfirmTextForTextbox = Label(screen, text="Enter Code here: ", font= ('Impact', 10)) 
  


        #massive list of all the elements on the first screen, will run a for loop through this in 2fa
        elements = [
                userKeywordBox,
                spamFollowBox,
                Username,
                Password,
                userKeywordInput, 
                usernameLabel,
                passwordLabel,
                checkbutton_instagram,
                checkbutton_comments,
                checkbutton_followers,
                checkbutton_keyword,
                checkbutton_tiktok,
                welcomeText,
                reminderText,
                speechBubbleImageLabel, 
            ]   
        
        twoFactorAuthenticationElements = [
            twoFactorAuthenticationEnterButton,
            twoFactorAuthenticationTextForTextbox,
            twoFactorAuthenticationText
        ]
                                
        # start the tkinter main loop
        screen.mainloop()


Menu()



