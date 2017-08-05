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

D=15
dat = eval(sys.argv[1])[0]
#data = json.loads(dat)
print json.dumps(dat)#json.dumps(data[0])