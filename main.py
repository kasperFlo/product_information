from random import randint
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
        else: raise TypeError("an integer from 100 to 1000")
    @property
    def productName(self):
        return self._productName
    @productName.setter
    def productName(self,args):
        if (args.isalpha()):
            self._productName = args
        else: raise TypeError("only a string ")
    @property
    def productSalePrice(self):
        return self._productSalePrice
    @productSalePrice.setter    
    def productSalePrice(self,args:float):
        if (isinstance(args,(int,float)) and args > 0):
            self._productSalePrice = args
        else: raise TypeError("a real number greater than zero ")
    @property
    def productManufactureCost(self):
        return self._productManufactureCost
    @productManufactureCost.setter
    def productManufactureCost(self,args):
        if (isinstance(args,(int,float)) and args > 0):
            self._productManufactureCost = args
        else: raise TypeError("a real number greater than zero ")
    @property
    def stockLevel(self):
        return self._stockLevel
    @stockLevel.setter
    def stockLevel(self,args):
        if (str(args) != str(float(args))) and int(args) > 0:
            self._stockLevel = int(args)
        else: raise TypeError("an integer number greater than 0")
    @property
    def estimatedMonthlyUnitsManufactured(self):
        return self._estimatedMonthlyUnitsManufactured
    @estimatedMonthlyUnitsManufactured.setter
    def estimatedMonthlyUnitsManufactured(self,args):
        if (isinstance(args,int)) and args >= 0:
            self._estimatedMonthlyUnitsManufactured = args
        else: raise TypeError("an integer greater than or equal to 0")
    def next12Months(self):
        print(f"{'*'*30}\nProduct Code: {self.productCode}\nProduct Name: {self.productName}\n\n Sale Price :{self.productSalePrice}CAD\nManifacture Cost : {self.productManufactureCost}\nMonthly Production : {self.estimatedMonthlyUnitsManufactured} Units\n\n{'*'*30}")
        stock = self.stockLevel
        for i in range(1,13):
            diviation = randint(-10,11)
            stock -= diviation
            print(f"Month {i}:\n{' '*5}Manufactured: {self.estimatedMonthlyUnitsManufactured} Units\n{' '*5}Sold: {stock+diviation}\n{' '*5}Stock: {(stock)}")

coc = product()
while True:
    try:
        coc.productCode = int(input("Enter Product Code : ")) #(e.g. an integer greater than or equal to 0)
        break 
    except : pass
while True:
    try:
        coc.productName = input("Enter Product Name : ") # must be a String
        break
    except : pass
while True:
    try:
        coc.productSalePrice = float(input("Enter Sales Price : "))#(e.g., a real number greater than zero)
        break
    except : pass 
while True:
    try:
        coc.productManufactureCost = float(input("Enter product Manufacture Cost : ")) #(e.g., a real number greater than zero)
        break
    except : pass
while True:
    try:
        coc.stockLevel = input("Enter stockLevel : ") #(an integer number greater than 0)
        break
    except : pass
while True:
    try:
        coc.estimatedMonthlyUnitsManufactured = int(input("Enter Estimated Monthly Units Manufactured : ")) #(e.g. an integer greater than or equal to 0)
        break
    except : pass 
coc.next12Months()