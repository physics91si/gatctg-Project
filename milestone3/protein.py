#Biomolecules Code

'''This code will help define some of the biomolecules useful in biological simulations'''


class Protein:
    '''Protein class encapsulates all interactions of a protein to abstract away a lot of the parameters and make the rest of the coding more intuitive'''
    def __init__(self, amount=0, mRNA=0, kd=1, kdm=1, transc=1, transl=1, promoter=1):
        '''Initializes protein mRNA amounts and protein amounts, as well as crucial biochemical parameters'''
        self.amount = amount
        self.mRNA = mRNA
        self.kd = kd
        self.kdm = kdm
        self.transc = transc
        self.transl = transl
        self.promoter = promoter
class gRNA:

    '''Class of RNAs that direct Cas9 and dCas9 to bind and, in the first case, edit DNA. In the latter case, used for system activation/repression. This instantiation encapsulates much of the function for the latter'''

    def __init__(self, amount=0, mRNA=0, kd=1, dCas9=0, transc=1, kdcas9m=1, promoter=1):
        '''Initializes vital parameters for gRNA function'''
        self.amount = amount
        self.kd = kd
        self.dCas9 = dCas9
        self.transc = transc
        self.kdcas9m = kdcas9m
        self.promoter = promoter

def rungeKutta(f, t0, y0, h, N):
    '''use the runge kutta method to calculate the updated value for y in a deterministic simulation. x is the function. Not sure how to implement at this point, so I will try later.'''
    t = t0 + arange(N+1)*h
    y = zeros((N+1, size(y0)))
    y[0] = y0
    for n in range(N):
        xi1 = y[n]
        f1 = f(t[n], xi1)
        xi2 = y[n] + (h/2.)*f1
        f2 = f(t[n+1], xi2)
        xi3 = y[n] + (h/2.)*f2
        f3 = f(t[n+1], xi3)
        xi4 = y[n] + h*f3
        f4 = f(t[n+1], xi4)
        y[n+1] = y[n] + (h/6.)*(f1 + 2*f2 + 2*f3 + f4)
    return y
