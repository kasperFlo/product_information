import main
productNum1 = main.product()
while True:
    try:
        productNum1.productCode = int(input("Enter Product Code : ")) #(e.g. an integer greater than or equal to 0)
        break 
    except : print("an integer from 100 to 1000")
while True:
    try:
        productNum1.productName = input("Enter Product Name : ") # must be a String
        break
    except : print("only a string ")
while True:
    try:
        productNum1.productSalePrice = float(input("Enter Sales Price : "))#(e.g., a real number greater than zero)
        break
    except : print("a real number greater than zero ")
while True:
    try:
        productNum1.productManufactureCost = float(input("Enter product Manufacture Cost : ")) #(e.g., a real number greater than zero)
        break
    except : print("a real number greater than zero ")
while True:
    try:
        productNum1.stockLevel = input("Enter stockLevel : ") #(an integer number greater than 0)
        break
    except : print("an integer number greater than 0")
while True:
    try:
        productNum1.estimatedMonthlyUnitsManufactured = int(input("Enter Estimated Monthly Units Manufactured : ")) #(e.g. an integer greater than or equal to 0)
        break
    except : print("an integer greater than or equal to 0")

productNum1.next12Months()

# coc.productCode = 642
# coc.productName = "cocandbalz"
# coc.productSalePrice = 3
# coc.productManufactureCost = 1
# coc.stockLevel = 100
# coc.estimatedMonthlyUnitsManufactured = 120