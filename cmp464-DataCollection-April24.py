import matplotlib.pyplot as plt
import urllib
import re
import numpy as np

#Collects the consoles, console initial release dates and console sales of the main video game consoles

#Collect the intial release years of each console
def getConsoleYears(url): #Work on this later

     #print("CONSOLE YEARSSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssss")

     years = []
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()
     
     for i in range(len(lines)):
          
          if lines[i].decode("utf8").find("<td><a href=") >= 0:
               m = i
               iry = re.search("[0-9]{4,5}", lines[m+2].decode("utf8"))

               if( iry is None):
                    years.append(0)

               else:
                    
                    years.append( int(iry.group(0) ) )

     #print(years)

     return years
               

#Get the million sale consoles     
def getConsoles(url):

     #print("CONSOLESSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssssss")

     c_sales2 = []
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()

     #print( len(lines) )#1193
     #'[0-9A-Za-z\.\s]+$'
     
     for i in range(len(lines)):
          if lines[i].decode("utf8").find("<td><a href=") >= 0:

               #so2 = re.search(r'"([^"]*)"', lines[i].decode("utf8") )
               #c_sales2.append( so2.group(0) )
               c_sales2.append( str(lines[i].decode("utf8"))[0:] )
               m = i

               #searchObj = re.search("[0-9\.]{3,7}", lines[m+3].decode("utf8"))
               #dates2.append( str(lines[i+1].decode("utf8"))[-14:]  )#[4:25]
               #c_sales3.append( float(searchObj.group(0))  )#[4:25]

     for j in range(0, 66):
         # print( c_sales2[j][0:35] )

         c_sales2[j] = (re.search(r'"([^"]*)"', c_sales2[j] ) ).group(0)
         c_sales2[j] = c_sales2[j][7: len(c_sales2) - 1]
         #print( c_sales2[j] )

     #print( c_sales2)
     #print( len(c_sales2) )
          
     #print( c_sales3)
     #print( len(c_sales3) )
          

     return c_sales2
     
#Get the # of sales of each console
def getConsoleSales(url):

     #print("CONSOLE SALESSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssss")

     c_sales3 = [] 
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()

     #'[0-9A-Za-z\.\s]+$'
     for i in range(len(lines)):
          if lines[i].decode("utf8").find("<td><a href=") >= 0:
               
               m = i

               searchObj = re.search("[0-9\.]{1,7}", lines[m+3].decode("utf8"))
               #print( lines[m+3] ) 
               #print( searchObj.group(0) )

               c_sales3.append( float(searchObj.group(0))  )
          
     return c_sales3

#Collects the initial release dates to compare total sales

def getFranchises(url):

     #print("FRANCHISEESSSSSSSSSSssssssssssssssssssssssssssssssssssssssssss")

     franchises = []
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()

     #print( len(lines) )
     
     for i in range(len(lines)):
          
          if lines[i].decode("utf8").find("<td><i><a href=") >= 0:

               franchises.append( str(lines[i].decode("utf8")).split('<td><i><a href="/wiki/' )[1] )

     #print( len(franchises) )

     for j in range(0, 187):

          franchises[j] = (franchises[j]).partition(' ')[0]

          #print( franchises[j] )

     return franchises

     
def getFranchiseSalesDates(url):

     #print("CFRANCHISE DATESESSSSSSSSSSSSSSSsssssssssssssssssssssssssssssssss")

     dates2 = []
     dates3 = [] * 187
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()
     
     for i in range(len(lines)):
          if lines[i].decode("utf8").find("<td><i><a") >= 0:
               
               m = i

               searchObj = re.search("[0-9]{4,7}", lines[m+1].decode("utf8"))
               #dates2.append( str(lines[i+1].decode("utf8"))[-14:]  )#[4:25]
               dates2.append( int(searchObj.group(0))  )#[4:25]

     #for j in range(0, 187):
      #    print( dates2[j] )
          

     return dates2
     
#Collects Franchise Total Sales so far
def getFranchiseSalesFromWeb(url):

     #print("FRANCHISE SALESSSSSSssssssssssssssssssssssssssssssssssssssssss")

     sales2 = []
     sales3 = [] * 187
    
     page = urllib.request.urlopen(url)
     lines = page.readlines()
     
     for i in range(len(lines)):
          if lines[i].decode("utf8").find("<td><i><a") >= 0:
               
               m = i
               searchObj = re.search('[0-9A-Za-z\.\s]+$', lines[m+2].decode("utf8"))
               sales2.append( str(lines[i+2].decode("utf8"))[4:25]  )

     #print( len(sales2) )

     for i in range(0,187):
          sales2[i] = sales2[i].split("million")[0]

     sales2[92] = "16"
     sales2[100] = "16"
     sales2[105] = "14"
     sales2[156] = "7"
     sales2[175] = "5.4"
     sales2[186] = "5"

     for j in range(0,187):

          sales2[j] = ( float(sales2[j]) )
          #print( sales2[j])

     #print(sales2)

     return sales2

def main():
     #The url is made up of the prefix, year, and suffix: 1282
     prefix = "https://en.wikipedia.org/wiki/List_of_best-selling_video_game_franchises"
     prefix2 = "https://en.wikipedia.org/wiki/List_of_best-selling_game_consoles"
     
     M = getFranchiseSalesFromWeb(prefix)
     print(M)
     M2 = getFranchiseSalesDates(prefix)
     print(M2)

     t = np.arange( len(M2) )
     
     M3 = getFranchises(prefix)
     print(M3)
     
     M4 = getConsoleSales(prefix2)
     print(M4)
     M6 = getConsoleYears(prefix2)
     print(M6)

     t2 = np.arange( len(M4) )

     M5 = getConsoles(prefix2)
     print(M5)

     plt.bar(M2, M,width = .35, color = 'r', label="Total Franchise Sales") #Plot max as red
     plt.title("Franchises Sales: 1981 to 2017 Junior Peralta")       #Title for plot
     plt.xlabel('Franchise Dates')                     #Label for x-axis
     plt.ylabel('Franchise Sales From Web')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()

     plt.scatter(M2,M, c=t)
     plt.title("Franchise Sales from 1981 to 2017")
     plt.xlabel("Franchise Dates")
     plt.ylabel("Franchise Sales")
     plt.show()

     plt.bar(M6,M4, width = .35, color='b', label="Console Sales") #Plot max as red
     plt.title("Console Sales")       #Title for plot
     plt.xlabel('Total Console Sales')                     #Label for x-axis
     plt.ylabel('Console Release Dates')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()

     plt.scatter(M6,M4, c=t2)
     plt.title("Franchise Sales from 1981 to 2017")
     plt.xlabel("Franchise Dates")
     plt.ylabel("Franchise Sales")
     plt.show()
     
          
main()
