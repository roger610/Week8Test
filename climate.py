import matplotlib.pyplot as plt
import sqlite3

        
years = []
co2 = []
temp = []

sqliteConnection = sqlite3.connect('climate.db')
cursor = sqliteConnection.cursor()
fetchA = cursor.fetchall()
print(fetchA)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()



