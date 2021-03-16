# import required module
import matplotlib.pyplot as plt
# create 2 dictionaries to store data
dictionary = {'USA': 29862124, 'India': 11285561, 'Brazil': 11205972, 'Russia': 4360823, 'UK': 423492}
print(dictionary)
# draw the pie plot using plt
plt.pie(dictionary.values(), labels=dictionary.keys(), autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')
plt.show()




