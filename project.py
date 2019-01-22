import sys

    
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
    ra=d/(r*p)
    return ra
    
def earthquake(r,p):
    """r=richter scale, p=popuation of affected area"""
    ra=calc_death_ratio()
  
    d=r*p*ra
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
test_suite()


ric=float(input("How strong is the earthquake on the Richter scale?"))
pop=int(input("what is the population of the area?"))


    

print("There will be",earthquake(ric,pop),"deaths.")
    