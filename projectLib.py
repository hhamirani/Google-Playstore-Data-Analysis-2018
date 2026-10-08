#Hasan Hamirani
#Python Project Library

import pandas
import numpy as np

class GoogleApp:

    def __init__(self):
        self.app = {
            "App": ["Zephyr"],
            "Category" : ["WEATHER"],
            "Rating":[0],            
            "Reviews":[0],
            "Installs":[0],
            "Type": ["Free"],
            "Price": [0],
            "Content Rating" : ["Everyone"],
            "Genres": ["Weather"]
            }
        pass

    def printData(self):
        print (self.app)
        return

    def createApp(self):
        app = input("Enter the name of your app: ")
        category = input("Enter the category of your app: ").upper()
        rating = input("Enter the content rating of your app: ")
        reviews = int(input("Enter the amount of reviews you app has: "))
        installs = int(input("Enter the amount of installs your app has: "))
        app_type = input("Enter Free or Paid: ")
        price = input("Enter the cost of your app: ")
        star_rating = input("Enter the star rating: ")
        genre = input("Enter the genre of your app: ")

        self.app["App"] = [app]
        self.app["Category"] = [category]
        self.app["Rating"] = [star_rating]
        self.app["Reviews"] = [reviews]
        self.app["Installs"] = [installs]
        self.app["Type"] = [app_type]
        self.app["Price"] = [price]
        self.app["Content Rating"] = [rating]
        self.app["Genres"] = [genre]
        return

    def getApp(self):
        return self.app

    
        


        
        

    
        

    
