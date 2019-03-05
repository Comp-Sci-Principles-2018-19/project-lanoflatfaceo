import sys



def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def earthquake(r,p):
    """r=richter scale, p=popuation of affected area"""
    d=r*p*5.550343964978111e-05
    return d


def test_suite():
     """ Run the suite of tests for code in this module (this file).
    """
     test(earthquake(7.8,164000) == 71)
test_suite()


ric=float(input("How strong is the earthquake on the Richter scale?"))
pop=int(input("what is the population of the area?"))


    

print("There will be",earthquake(ric,pop),"deaths.")
    