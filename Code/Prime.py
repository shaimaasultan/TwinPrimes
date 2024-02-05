import logging
import time
from datetime import datetime
from logging.handlers import MemoryHandler ,RotatingFileHandler

def InitiateLogger(loggerName , FilePath):
    lg = logging.getLogger(loggerName)
    lg.setLevel(logging.INFO)
    hnd=logging.FileHandler(FilePath,"w+")
    memory_handler = MemoryHandler(100, flushLevel=logging.INFO, target=hnd, flushOnClose=True)
    hnd.setLevel(logging.INFO)
    lg.addHandler(hnd)
    return lg , hnd

def check4(x ,y):
    return False #((y+x)*0.25 ) % 4 == 0

def check2(x,y):
    return x%2 == 0 and y % 2 == 0
def check3(x ,y):
    return (x%3 == 0 or y%3 ==0) and x != 3 and y!= 3
def check5(x ,y):
    return (x%5 == 0 or y%5 ==0) and x != 5 and y!= 5
def check7(x ,y):
    return (x%7 == 0 or y%7 ==0) and x != 7 and y!= 7
def check11(x ,y):
    return (x%11 == 0 or y%11 ==0) and x != 11 and y!= 11
def check13(x ,y):
    return (x%13 == 0 or y%13 ==0) and x != 13 and y!= 13
def check17(x ,y):
    return (x%17 == 0 or y%17 ==0) and x != 17 and y!= 17
def check19(x ,y):
    return (x%19 == 0 or y%19 ==0) and x != 19 and y!= 19
def check29(x ,y):
    return (x%29 == 0 or y%29 ==0) and x != 29 and y!= 29
def check31(x ,y):
    return (x%31 == 0 or y%31 ==0) and x != 31 and y!= 31
def checkf(x,y):
    return str(x**0.5).endswith('.0') or str(y**0.5).endswith('.0') 
def exists(x,y , l):
     return [x,y] in l

def logtime(loggername, time_name_string):
    time_value = time.time()
    loggername.info('{} {} {}'.format(time_name_string , time_value,datetime.now()))
    loggername.info('==============================================')

filename = "c:\\np_problem_shaimaa_soltan_up\\sqsquare\\pairswithcomposit.txt"
filename2 = "c:\\np_problem_shaimaa_soltan_up\\sqsquare\\compositsonly.txt"
filename3 = "c:\\np_problem_shaimaa_soltan_up\\sqsquare\\twinprimes.txt"
filename4 = "c:\\np_problem_shaimaa_soltan_up\\sqsquare\\primes.txt"



p = []
with open(filename2,"r") as f:
    while l:= f.readline() :
        l = l.replace("[","")
        l = l.replace("]","")
        l = l.replace("\n","")
        l = l.split(',')
        #print(l[0] , l[1] , l[2])
        d = int(l[2].strip(" "))
        if d  not in p:
            p.append(d)

p.sort()
f = open(filename4, "w+")
for i in p:
    f.write(str(i)+"\n")


'''

f = open(filename4, "r")
l = f.readlines()
print('1 : {}'.format(l[0].count('1')))
print('2 : {}'.format(l[0].count('2')))
print('3 : {}'.format(l[0].count('3')))
print('4 : {}'.format(l[0].count('4')))
print('5 : {}'.format(l[0].count('5')))
print('6 : {}'.format(l[0].count('6')))
print('7 : {}'.format(l[0].count('7')))
print('8 : {}'.format(l[0].count('8')))
print('9 : {}'.format(l[0].count('9')))
print('0 : {}'.format(l[0].count('0')))
'''

