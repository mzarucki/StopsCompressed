
CR = ["CR1aX","CR1aY","CR1cX"]
SR = ["SR1avlX","SR1alX","SR1amX","SR1ahX","SR1avlY","SR1alY","SR1amY","SR1ahY","SR1clX","SR1cmX","SR1chX"]

mapping = {
    0 : 4,
    1 : 4,
    2 : 4,
    3 : 4,
    4 : 3,
    5 : 3,
    6 : 4,
    7 : 4,
    8 : 4,
    9 : 4,
    10 : 3,
    11 : 3,
}


print mapping[1]
exit(0)

shift_CR = len(CR)
shift_SR = 0

for i_cr, cr in enumerate(CR) :
    print "create rate parameter tied to CR {}".format(i_cr)

    corr_SR = mapping["{}".format(i_cr)]
    for i_sr, sr in enumerate (corr_SR) :
        print "tie rate parameter {cr} to SR {sr}".format(cr=i_cr,sr=i_sr+shift_CR+shift_SR)
    
    shift_SR += len(corr_SR)