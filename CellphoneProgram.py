import CellphoneClass as cc

def main():
    ##initallize vaules 
    

    manufacture = 'Apple'
    models = 'iPhone 7'
    price = '$10'
    userphone = cc.cellphone(manufacture, models,price)

    print ("Manufacture is ", userphone.get_manufact())
    print ('Model is ', userphone.get_model())
    print ( 'Price is ', userphone.get_retail_price())

    ## set function
    userphone.set_model= 'iphone 10'
    userphone.set_manufact = 'Apple'
    userphone.set_retail_price = '$12'
    



main()