import traceback
class product:
    def __init__(self,pC=111,pN="default",pSP=1,pMC=1,sL=1,eMUM=1) -> None:
        self.productCode = pC #(e.g., an integer from 100 to 1000)
        self.productName = pN #(e.g. Laser Printer)
        self.productSalePrice =pSP#(e.g., a real number greater than zero)
        self.productManufactureCost = pMC #(e.g., a real number greater than zero)
        self.stockLevel = sL #(an integer number greater than 0)
        self.estimatedMonthlyUnitsManufactured =eMUM #(e.g. an integer greater than or equal to 0)

    @property
    def productCode(self):
        # print("pc getter running")
        return self._productCode
    @productCode.setter
    def productCode(self,args:int):
        # print("pc setting running")
        if ((str(args)).isnumeric() and args >= 100 and args <= 1000):
            self._productCode = args
        else:
            print(type(args))
            raise TypeError("an integer from 100 to 1000")
    @property
    def productName(self):
        return self._productName
    @productName.setter
    def productName(self,args):
        if (args.isalpha()):
            self._productName = args
        else:
            raise TypeError("only a string ")
    @property
    def productSalePrice(self):
        return self._productSalePrice
    @productSalePrice.setter
    def productSalePrice(self,args):
        if (isinstance(args,(int,float)) and args > 0):
            self._productSalePrice = args
        else:
            raise TypeError("a real number greater than zero ")
    @property
    def productManufactureCost(self):
        return self._productManufactureCost
    @productManufactureCost.setter
    def productManufactureCost(self,args):
        if (isinstance(args,(int,float)) and args > 0):
            self._productManufactureCost = args
        else:
            raise TypeError("a real number greater than zero ")
    @property
    def stockLevel(self):
        return self._stockLevel
    @stockLevel.setter
    def stockLevel(self,args):
        if (isinstance(args,int)) and args > 0:
            self._stockLevel = args
        else:
            raise TypeError("an integer number greater than 0")
    @property
    def estimatedMonthlyUnitsManufactured(self):
        return self._estimatedMonthlyUnitsManufactured
    
    @estimatedMonthlyUnitsManufactured.setter
    def estimatedMonthlyUnitsManufactured(self,args):
        if (isinstance(args,int)) and args >= 0:
            self._estimatedMonthlyUnitsManufactured = args
        else:
            raise TypeError("an integer greater than or equal to 0")

coc = product()
while True:
    try:
        coc.productCode = int(input("Enter Product Code : ")) #(e.g. an integer greater than or equal to 0)
        break
    except Exception as e: print(e)

while True:
    try:
        coc.productName = input("Enter Product Name : ") # must be a String
        break
    except Exception as e: print(e)
        
while True:
    try:
        coc.productSalePrice =input("Enter Sales Price : ")#(e.g., a real number greater than zero)
        break
    except Exception as e: print(e)   

while True:
    try:
        coc.productManufactureCost = input("Enter product Manufacture Cost : ") #(e.g., a real number greater than zero)
        break
    except Exception as e: print(e) 

while True:
    try:
        coc.stockLevel = input("Enter stockLevel : ") #(an integer number greater than 0)
        break
    except Exception as e: print(e) 

while True:
    try:
        coc.estimatedMonthlyUnitsManufactured = input("Enter Estimated Monthly Units Manufactured : ") #(e.g. an integer greater than or equal to 0)
        break
    except Exception as e: print(e)   
    