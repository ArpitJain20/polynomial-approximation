#!/usr/bin/env python
from copy import copy, deepcopy
import MySQLdb
import matplotlib
matplotlib.use('Agg')
import numpy
import math
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.legend_handler import HandlerLine2D
import sys
import os
import pickle
import json
import csv
# db = MySQLdb.connect("localhost","root","","monetgurgaon")

# cursor=db.cursor()
# cursor.execute("SELECT P.ad_ar_id,P.ad_time,P.ad_valence from analysis_detail_premium_v2 P,analysis_results R,content_feedback F,content C WHERE P.ad_ar_id=R.ar_id AND R.ar_cf_id=F.cf_id AND F.cf_c_id=C.c_id AND C.c_id=%d"%c_id)

# data = cursor.fetchall()

# data = numpy.array(data)

# cursor.execute("SELECT DISTINCT P.ad_ar_id from analysis_detail_premium_v2 P,analysis_results R,content_feedback F,content C WHERE P.ad_ar_id=R.ar_id AND R.ar_cf_id=F.cf_id AND F.cf_c_id=C.c_id AND C.c_id=%d"%c_id)

# users=cursor.fetchall()

# users=numpy.array(users)

# #x=datetime.strptime(data[0][1],'%H:%M:%S')

# max=0
# for i in data:
#     time = i[1].split(":")
#     seconds = int(time[1])*60 + int(time[2])
#     i[1]=seconds
#     if max<seconds:
#     	max=seconds

# col=len(users)
# row=int(max)+1

# table=numpy.zeros((row+1,col))

# i=0
# j=0
# prev=int(users[0]);

# for row in data:
# 	k=0
# 	for j in range(0,col):
# 		if int(row[0]) == (users[j][0]):
# 			k=j
# 			break
# 	#if prev!=int(row[0]) and j<col-1:
# 	#	j=j+1
# 	r= int(row[1])
# 	table[r][k]=round(float(row[2]),3)
# 	#print row[0],users[k][0]
#  	#prev=int(row[0])
	

# db.close()
# leg = len(table)
# avg=numpy.zeros(leg)
# i=0
# for row in table:
# 	sum=0
# 	total=0
# 	for item in row:
# 		if(item!=0):
# 			sum=sum+item
# 			total=total+1
# 	if total == 0:
# 		total = 1
# 	avg[i]=sum/total
# 	i=i+1


D=int(sys.argv[1])
L=[]
with open('data.csv') as f:
	reader=csv.reader(f)
	for row in reader:
		#t=row.split(',')
		L.append(float(row[1]))
avg = numpy.zeros(len(L))
for i in range(len(L)):
	avg[i]=L[i]
#print L
time = numpy.arange(0,len(avg))

poly = numpy.polyfit(time,avg,D)


# with open('hello.pickle') as f:
#   	# table, users, avg, time = pickle.load(f)	
#   	#print avg
# 	poly = numpy.polyfit(time,avg,D)
X = numpy.arange(0,len(time),.1)
Y = numpy.zeros((len(X),))
for i in range(0,len(X)):
	for j in range(0,D+1):
		Y[i] += (X[i]**(D-j))*(poly[j])

for i in range(len(Y)):
	print Y[i]		


fig = plt.figure(2)		
txt="Polynomial approximation for a valence plot"
g,=plt.plot(time,avg,linewidth=1.0,label='valence',color='yellow')
s,=plt.plot(X,Y,linewidth=3.0,label='Polynomial approximation of Valence ',color='red')
plt.legend(handler_map={g: HandlerLine2D(numpoints=4)})
fig.text(0.03,.95,txt)
plt.savefig("graph")
#print Y