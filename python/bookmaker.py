# -*- coding:utf-8 -*-
#!/usr/bin/python

import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import json
import twitter


north = []
west = []
east = []
south = []

p_n = []
p_w = []
p_e = []
p_s = []

x = [8, 10, 12, 14, 16, 17.3333, 17.6667, 18, 20, 22, 24]
xt = ["08:00", "10:00", "12:00", "14:00", "16:00",
      "17:20", "17:40", "18:00", "20:00", "22:00", "24:00"]

def dealWithData(data):
	data = json.loads(data)
	north.append(int(data["north"]))
	west.append(int(data["west"]))
	east.append(int(data["east"]))
	south.append(int(data["south"]))
	t = len(north) - 1
	maxNumber = max(north[t], west[t], east[t], south[t])
	p_n.append(round(north[t]/maxNumber*100, 4))
	p_w.append(round(west[t]/maxNumber*100, 4))
	p_e.append(round(east[t]/maxNumber*100, 4))
	p_s.append(round(south[t]/maxNumber*100, 4))
	xtemp = []
	xttemp = []
	for i in range(t + 1):
		xtemp.append(x[i])
		xttemp.append(xt[i])

	plt.figure(figsize=(12, 6), dpi=72)
	plt.xlabel("Time")
	plt.ylabel("percent")
	plt.xlim(8, 24)
	title = str(time.strftime("%Y-%m-%d", time.localtime())) + " " +str(xt[t])
	plt.title(title)
	plt.xticks(xtemp, xttemp, rotation=50)
	plt.plot(xtemp, p_n, color="green", label="north")
	plt.plot(xtemp, p_s, color="darkred", label="south")
	plt.plot(xtemp, p_w, color="gray", label="west")
	plt.plot(xtemp, p_e, color="navy", label="east")
	plt.grid(True)
	plt.legend(loc="best")
	plt.savefig(t+".png")
	plt.show()
	twitter.sendImage(t+".png", title)
	