import main as m
coc = m.product()
# coc.productCode = 642
# coc.productName = "cocandbalz"
# coc.productSalePrice = 2
# coc.productManufactureCost = 1
# coc.stockLevel = 100
# coc.estimatedMonthlyUnitsManufactured = 120
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