"""
 You are an active traveler who have visited a lot of countries. The main city in the every country is its capital and each country can have only one capital city. So your task is to create the class Capital which has some special properties: the first created instance of this class will be unique and single, and all of the other instances should be the same as the very first one.
Also you should add the name() method which returns the name of the capital.
In this mission you should use the Singleton design pattern.

"""
class Capital:
    class __Capital:
        def __init__(self, city_name):
            self._name = city_name
            
        def name(self):
            return self._name
    
    instance = None
    
    def __new__(self, city_name):
        if not Capital.instance:
            Capital.instance = Capital.__Capital(city_name)
        return Capital.instance
