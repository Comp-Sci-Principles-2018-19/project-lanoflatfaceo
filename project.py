import sys
import matplotlib.pyplot as plt #sets up a pyplot graph as p
import pandas as pd
import numpy as np


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def  calc_damage_ratio():
    dollars=250000000
    r=7.8
    p=164000
    ra=dollars/(r*p)
    return ra


def calc_wounded_ratio():
    w=71
    r=7.8
    p=164000
    ra=w/(r*p)
    return ra

def calc_death_ratio():
    d=48
    r=7.8
    p=164000
    ra=d/(r)
    return ra
    
def earthquake(r, ra):
    """r=richter scale, p=popuation of affected area"""
    #ra=calc_death_ratio()
    
    d=(r**2*ra)-(ra/.055)
    print(d)
    #if d>p:
        #d=p
        #return d
    #if d<1:
        #return 0
    return d
    #return d (deaths), w(wounded), do(dollars), return (d,w,do)
    

def test_suite():
     """ Run the suite of tests for code in this module (this file).
    """
     test(earthquake(7.8,164000) == 48)
     test(calc_death_ratio()==3.75234521575985e-05)
     test(calc_wounded_ratio()==5.550343964978111e-05)
     test(calc_damage_ratio()==195.43464665415885)
     """Using data from Guam because it is an island"""

#t = np.arange(0, 10, 0.5)

#test_suite()

ric=150
df=pd.read_csv('data_utf.csv')
#df1 = df.reindex(index=dates[0:4], columns=list(df.columns))
r=df["R"]
deaths=df["D"]
#p=df["pop"]
print("deaths*******************************************")
print(deaths)
#deaths.clip(0.00, 0.2)
print(deaths)
#plt.plot(t, ric)
#pop=1000
popscale=np.linspace(0.0, 250000.0)
y1 = np.linspace(5, 10)
x1 = earthquake(y1-0.75, ric+100)
x2=earthquake(y1-0.6, 150)
x3=earthquake(y1-0.55, ric-100)
slope=deaths/r
plt.subplot(1,1,1)
plt.plot( x1, y1,  "-")
plt.title('deaths from eartquakes')
plt.ylabel('deaths')
plt.plot(deaths, r, "o")
plt.plot(x2, y1, "r-")
plt.plot(x3, y1, "g-")
#plt.plot(slope, r, "rs")
plt.xlabel('deaths')
plt.ylabel("richter scale")
#r=float(input("How strong is the earthquake on the Richter scale?"))
#p=int(input("what is the population of the area?"))
print("Richter scale is how the human race scales earthquakes")
#print("There will be",earthquake(r,p),"deaths.")
plt.show()

