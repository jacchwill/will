

from jacchlibs.readxls import readxls

xls=readxls("db.xlsx")
sheet=xls.read("工作表1")  
print (sheet["A1"].value)
print (sheet["A2"].value)
print (sheet["A3"].value)

xls=readxls("db.xlsx")
sheet=xls.read("妙蛙種子")  
print (sheet["A1"].value)
print (sheet["A2"].value)
print (sheet["A3"].value)

xls=readxls("db.xlsx")
sheet=xls.read("伊布")  
print (sheet["A1"].value)
print (sheet["A2"].value)
print (sheet["A3"].value)

xls=readxls("db.xlsx")
sheet=xls.read("咚咚鼠")  
print (sheet["A1"].value)
print (sheet["A2"].value)
print (sheet["A3"].value)

#工作表2
#xls2=readxls("db.xlsx")
#sheet=xls.read("工作表2")
#print (sheet["A1"].value)

