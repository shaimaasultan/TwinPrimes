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

lg_pairs , hnd_pairs_composits= InitiateLogger("pairs_{}".format(str(7)) , filename )
lg_composit, hnd_composit = InitiateLogger("composit_{}".format(str(7)) , filename2 )
lg_twin, hnd_pairs = InitiateLogger("twin_{}".format(str(7)) , filename3 )

def range_PIR(start_from , end_at):

    pair = []
    start_from = start_from
    end_at =     end_at
    logtime(lg_pairs , 'start time')
    logtime(lg_twin , 'start time')



    lg_twin.info('primes twins between {} and {}'.format(start_from , end_at) )

    for i in range(start_from ,end_at):
        x = i
        y = i+2
        print("({},{}, {} , {}, {},{}, {} , {})".format(x,y , check2(x,y) ,check4(x,y) , check3(x,y) 
                                                        , check5(x,y) , check7(x,y), checkf(x,y) 
                                                        , check11(x,y), check13(x,y), check17(x,y)))
        if check2(x,y) == False and check4(x,y) == False and check3(x,y) == False and check5(x,y) == False\
            and check7(x, y) == False and check11(x, y) == False and check13(x, y) == False and check17(x, y) == False\
            and check19(x, y) == False and check29(x, y) == False and check31(x, y) == False\
            and checkf(x, y) == False  :
            pair.append([x,y])
            lg_pairs.info([x,y])


    search_untill = pair[0][0]
    l = pair.copy()

    # we can use s/2 as most of composits are fare a part, if not accurate data remove this divid and use full s range
    #search_untill = int(search_untill/2)

    # s = 4 * difference between start and end , if not accurate data remove this divid and use full s range

    search_untill =   end_at # 4 * (end_at - start_from )

    for n in range(1,search_untill,2):
        for i in l: 
            if (i[0]%n == 0 or i[1]%n ==0) and (i[0] != n or i[1] != n) and n > 1  and  exists(i[0],i[1], pair):
                lg_composit.info([[i[0],i[1]] , [n]])
                print("factbefore {} {}".format(i , n))
                if (i[0] != n and  i[1] != n):
                    pair.remove(i)
        
            
    lg_twin.info(pair)

    logtime(lg_pairs , 'end time')
    logtime(lg_twin , 'end time')

range_PIR(1, 5000)
range_PIR(5000, 10000)
range_PIR(10000, 15000)
range_PIR(15000, 20000)
range_PIR(20000, 22277)
range_PIR(22277, 22300)
range_PIR(22300, 25000)
range_PIR(25000, 40000)
range_PIR(40000, 45000)
range_PIR(45000, 50000)
range_PIR(50000, 55000)
range_PIR(55000, 75000)
range_PIR(75000, 95000)
range_PIR(95000, 115000)
range_PIR(115000, 145000)
range_PIR(145000, 195000)
range_PIR(195000, 235000)
range_PIR(235000, 275000)
range_PIR(275000, 315000)
range_PIR(315000, 365000)
range_PIR(365000, 405000)
range_PIR(405000, 445000)
range_PIR(445000, 500000)
range_PIR(500000, 545000)
range_PIR(545000, 600000)
range_PIR(600000, 650000)
range_PIR(650000, 700000)
range_PIR(750000, 800000)
range_PIR(800000, 850000)
range_PIR(850000, 900000)
range_PIR(900000, 950000)
range_PIR(950000, 1000000)

