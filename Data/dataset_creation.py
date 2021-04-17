"""Module for creating object data of flipkart"""
import json
from pprint import pprint
from Library.config import Config

data = {
    'clickOnMagnify': {'locatorType': 'xpath',
                       'locatorValue': "//button[@class='L0Z3Pu']"},
    
    'clickOnPopup': {'locatorType': 'xpath',
                       'locatorValue': "//button[@class='_2KpZ6l _2doB4z']"},
    
    'clickOnSearch': {'locatorType': 'xpath',
                       'locatorValue': "//div[@class='_3OO5Xc']/input[@name='q']"},
    
    'clickOnfAssured': {'locatorType': 'xpath',
                       'locatorValue': "//label/div[@class='_24_Dny _3tCU7L']"},
    
    'clickOnAddToCart': {'locatorType': 'xpath',
                       'locatorValue': "//button[text()='ADD TO CART']"},
    
    'clickOnCart': {'locatorType': 'xpath',
                       'locatorValue': "//span[text()='Cart']"},
    
    'clickOnPlaceOrder': {'locatorType': 'xpath',
                       'locatorValue': "//button/span[text()='Place Order']"},
    
    'clickOnRemove': {'locatorType': 'xpath',
                      'locatorValue': "//div[@class='_3dsJAO' and contains(text(), 'Remove')]"},
    
    'selectSpiderMan': {'locatorType': 'xpath',
                      'locatorValue': "//a[text()='Marvel’s Spider-Man: Miles Morales']"}
        }
fileobj = open(Config.OBJECT_JSON, 'w+')
json.dump(data, fileobj, indent=4)

fileobj = open(Config.OBJECT_JSON, "r")
info = json.load(fileobj)
pprint(info)

fileobj.close()
