INSTAGRAM AND TIK TOK BOTS

This project consists of two bots that I have made using the Selenium library in Python. This is made with a GUI using the Tkinter library to allow the user to pick and choose what bots they wanted to be deployed specific to their needs. This is then followed by a basic two-factor authentication which uses the SMTP protocol in Python to send an email to a user with a 6 digit code made using the library 'randint'. It also has a comment array which consists of three random comments which the bot chooses using 'randint' again. The Instagram bot has two functions which are stated below:

FOLLOW USERS WHO FOLLOW A SOCIAL MEDIA INFULENCER 

The bot begins by logging into the user's account by automatically entering the user's username and password into the textboxes. These were obtained by the prior mentioned Tkinter selector. Then, the bot makes its way over to the search bar on Instagram before entering a user (ideally a account with over 100,000 followers), before then clicking on their account and selecting the 'followers' tab. From here, the bot then looks to find the 'follow' button on all the users that appear on the screen. If it is found, then it can be clicked and that user is now followed. This will also print in the terminal as 'X' users followed. The bot then repeats this until it has followed all the users or the user terminates the program. 

SPAM LIKE AND COMMENT ON POSTS

The bot again begins by logging into the user's account using the method I previously mentioned. From there, it finds the 'explore' tab on Instagram, which is where things that you interact with such as liking and commenting will appear the most frequently due to the nature of Instagrams alogorithm. From there, the bot will find posts on the page and begin to like and comment on them, giving the account a lot more intercation in the social media space. This is put in a 'while' loop so it will continue infintely until the page runs out of posts and needs refreshing, or the user decides to terminate the program. 

The TikTok bot works as follows:

TIK TOK LIKE AND COMMENT 

This TikTok bot will log into the user's page using the same methods as mentioned above. However, this time it will complete a Captcha as TikTok implement this feature when it suspects an automated bot is trying to log in. From there, a keyword, which is entered by the user during the menu stage of the program, will be entered after the bot has found the search bar. From there, the bot will click on the first user's page that appears and will begin to scroll through their posts, liking and commenting along the way by using the arrow buttons on the right hand side. The bot will then keep repeating this until there is no posts left on the account. If this occurs, then the next account that appears will be selected. The user can also terminate the program like before. 
