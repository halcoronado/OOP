class cellphone:
## define attributes
    def __init__(self,manufacture,models, price):
        self.__manufact = manufacture
        self.__model = models
        self.__retail_price = price
  ## set the attributes  
    def set_manufact(self,manufacture):
        self.__manufact = manufacture
    
    def set_model(self,models):
        self.__model = models

    def set_retail_price(self,price):
        self.__retail_price = price
## get attributes
    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
        
    def get_retail_price(self):
        return self.__retail_price