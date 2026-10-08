#Hasan Hamirani
#Python Project
#12/18/18
#Data Analysis Google Playstore

'''
Analyze the Google Play store apps and create data visualizations to graphically answer questions such as:
Top ranked apps overall?
Paid vs Free, which are higher rated on average? Which are more popular?
Most popular app category?

App look-up to return information based on name

Allow for users to update the current database either through manual input, or through file feeding
        read from an input file and produce an output
        
'''

import pandas
import matplotlib.pyplot as plt
import numpy as np
import projectLib


#use pandas library to open/close file and store in dataframe
original = pandas.read_csv("googleplaystore.csv")
df = pandas.read_csv("googleplaystore.csv", usecols = [0,1,2,3,5,6,7,8,9])

#need to clean data to swap type
df.Installs = df.Installs.str.replace(",", "")
df.Installs = df.Installs.str.replace("+", "")
df.Price = df.Price.str.replace("$","")

df[["Installs","Reviews","Price"]] = df[["Installs","Reviews","Price"]].astype("float")
paid = df[df.Type == "Paid"]

#initialize option and app object
option = 0
a = projectLib.GoogleApp()

#OPTIONS
print (" Press 1 to display the PlayStore database.", "\n",
       "Press 2 to search for an app(s).", "\n",
       "Press 3 to add an app to the database.", "\n",
       "Press 4 to export the database to a new file.", "\n"
       " Press 5 to view data analysis.", "\n",
       "Press 6 to exit the program.")

while option !=6:

    option = input("Select an option: ")

    if (option == "1"):
        #print (df)
        print (df.head())
        print (df.tail())

    if (option == "2"):
        #return information based on app name & similar
        search = input("Enter a term to search for: ")
        print (df[df["App"].str.contains(search)])

    if (option == "3"):
        a.createApp()

        #appending the newly created app to the pre-existing dataframe
        raw_data = a.getApp()
        df_b = pandas.DataFrame(raw_data)
        df = pandas.concat([df, df_b], sort=True, ignore_index = True)

    if (option == "4"):
        #creating output file of modified dataframe
        #dataExport = df_new
        dataExport = df
        dataExport.to_csv("Output_File.csv")
        print ("Export complete. Check destination folder.")

    if (option == "5"):
        
        #show apps that are above $250 in price
        print ("\n", "Apps above $250")
        print (repr(df[['App', 'Category', 'Price']][df.Price >= 250]))
        
        #We can see clearly reviews decreasing as the price increases.
        paid.plot(kind = "scatter", x = "Price", y = "Reviews", color = "b")
        plt.xlabel("Price")
        plt.ylabel("Reviews")
        plt.title("Paid App-Reviews")
        plt.show()

        #graph that shows star rating vs price
        paid.plot(kind = "scatter", x = "Rating", y = "Price", color = "b")
        plt.xlabel("Rating")
        plt.ylabel("Price")
        plt.title("Ratings vs. Price")
        plt.show()

        #Total Installations Based on App Category pie chart
        art = ((df[df["Category"]=="ART_AND_DESIGN"]["Installs"]).sum())
        auto = ((df[df["Category"]=="AUTO_AND_VEHICLES"]["Installs"]).sum())
        beauty = ((df[df["Category"]=="BEAUTY"]["Installs"]).sum())
        books = ((df[df["Category"]=="BOOKS_AND_REFERENCE"]["Installs"]).sum())
        business = ((df[df["Category"]=="BUSINESS"]["Installs"]).sum())
        com = ((df[df["Category"]=="COMMUNICATION"]["Installs"]).sum())
        dating = ((df[df["Category"]=="DATING"]["Installs"]).sum())
        education = ((df[df["Category"]=="EDUCATION"]["Installs"]).sum())
        entertainment = ((df[df["Category"]=="ENTERTAINMENT"]["Installs"]).sum())
        events = ((df[df["Category"]=="EVENTS"]["Installs"]).sum())
        fam = ((df[df["Category"]=="FAMILY"]["Installs"]).sum())
        finance = ((df[df["Category"]=="FINANCE"]["Installs"]).sum())
        food = ((df[df["Category"]=="FOOD_AND_DRINK"]["Installs"]).sum())
        game = ((df[df["Category"]=="GAME"]["Installs"]).sum())
        health = ((df[df["Category"]=="HEALTH_AND_FITNESS"]["Installs"]).sum())
        house = ((df[df["Category"]=="HOUSE_AND_HOME"]["Installs"]).sum())
        library = ((df[df["Category"]=="LIBRARIES_AND_DEMO"]["Installs"]).sum())
        life = ((df[df["Category"]=="LIFESTYLE"]["Installs"]).sum())
        maps = ((df[df["Category"]=="MAPS_AND_NAVIGATION"]["Installs"]).sum())
        med = ((df[df["Category"]=="MEDICAL"]["Installs"]).sum())
        news = ((df[df["Category"]=="NEWS_AND_MAGAZINES"]["Installs"]).sum())
        parent = ((df[df["Category"]=="PARENTING"]["Installs"]).sum())
        person = ((df[df["Category"]=="PERSONALIZATION"]["Installs"]).sum())
        photo = ((df[df["Category"]=="PHOTOGRAPHY"]["Installs"]).sum())
        productivity = ((df[df["Category"]=="PRODUCTIVITY"]["Installs"]).sum())
        shopping = ((df[df["Category"]=="SHOPPING"]["Installs"]).sum())
        social = ((df[df["Category"]=="SOCIAL"]["Installs"]).sum())
        sports = ((df[df["Category"]=="SPORTS"]["Installs"]).sum())
        tools = ((df[df["Category"]=="TOOLS"]["Installs"]).sum())
        travel = ((df[df["Category"]=="TRAVEL_AND_LOCAL"]["Installs"]).sum())
        vid = ((df[df["Category"]=="VIDEO_PLAYERS"]["Installs"]).sum())
        weather =((df[df["Category"]=="WEATHER"]["Installs"]).sum())

        labels = ["Art", "Auto & Vehicles", "Beauty", "Books", "Business", "Communication", "Dating", "Education",
        "Entertainment", "Events", "Family", "Finance", "Food", "Games", "Health", "House", "Library", "Lifestyle",
        "Navigation", "Medical", "News", "Parenting", "Personalization", "Photography", "Productivity", "Shopping",
        "Social", "Sports", "Tools", "Traveling", "Video Players", "Weather"]
        
        sizes = [art, auto, beauty, books, business, com, dating, education, entertainment, events, fam, finance,
                 food, game, health, house, library, life, maps, med, news, parent, person, photo, productivity,
                 shopping, social, sports, tools, travel, vid, weather]
        
        fig1, ax1 = plt.subplots()
        
        ax1.pie(sizes, labels = labels, autopct="%1.1f%%", shadow=False, startangle = 90)
        ax1.axis("equal")
        plt.title("App Install Total Number by Category")
        plt.show()

        
        '''
        #top ranked app names
        print ("\n")
        print ("Top ranked apps rated > 5")
        print ((df[df["Rating"] == 5]))
        '''
        

    if (option == "6"):
        print ("Terminating the program.")
        break

#testing methods
#a = projectLib.GoogleApp()
#a.createApp()
#a.printData()
#a.getApp()





