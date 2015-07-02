#We are visiting China,
    # In the following cities the temperature is:
     #Guangzhou: 34 degrees
     #Fuzhou: 35 degrees
#We are visiting China,
     #In the following cities the temperature is:
     #Guangzhou: 34 degrees
     #Fuzhou: 35 degrees
#We are visiting Portugal,
     #In the following cities the temperature is:
     #Lisbon: 34 degrees


country=['China','Portugal']
city=['Guangzhou','Fuzhou','Lisbon']
degrees=[34,35]

print "We are visiting {},\n In the following cities the temperature is:\n {}: {} degrees".format(country,city,degrees)




import request
query = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Lisbon,pt")
