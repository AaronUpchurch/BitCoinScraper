import requests
import matplotlib.pyplot as plt
import random
import time

x = []
y = []
plt.ion()
i = 1
fig = plt.figure()
ax = fig.add_subplot(111)
while(True):
    
    urlString = "https://www.blockchain.com/explorer/"

    page = requests.get(urlString)

    location = page.text.find('</span><a href="https://www.blockchain.com/prices"')

    price = page.text[location-9:location]
    price = price[0:2] + price[3:]
    x.append(i)
    y.append(float(price))
    line1, = ax.plot(x, y, 'b-')
    i = (i + 1)
    plt.ylim(min(y),max(y))
    fig.canvas.draw()
    fig.canvas.flush_events()

