string = """
 2014  7 4 0154 27.9 L  33.192  49.716 14.9  TES  7 0.2 1.5LTES                1
 GAP=313        0.53       2.6     3.6  2.6 -0.1045E+01 -0.2642E+01  0.1957E+01E
 ACTION:UP  14-11-19 11:15 OP:atab STATUS:               ID:20140704015219     I
 dsasdas
 2014-07-04-0152-19S.par___021                                                 6
 STAT SP IPHASW D HRMM SECON CODA AMPLIT PERI AZIMU VELO AIN AR TRES W  DIS CAZ7
 MHC  EE ESg       154 33.25                             159   -0.2210 5.86 210 
 MHC  EE  IAML     154 33.51      1481.8 0.19                          5.86 210 
 MHC  EN  IAML     154 33.62       471.9 0.20                          5.86 210 
 KAK  EE ESg       154 36.08                             125    0.3110 19.1 199 
 KAK  EN  IAML     154 38.04        46.5 0.43                          19.1 199 
 KAK  EE  IAML     154 38.94        52.1 0.28                          19.1 199 
 BHR  EE EPg       154 33.65                             113    0.1810 28.2 172 
 BHR  EE ESg       154 38.16                             113    0.0510 28.2 172
"""
endofheader = 0
lines = string.split("\n")

for i in range(0,len(lines)):
    if (lines[i].__contains__("IPHASW")):
        endofheader = i
for j in range(endofheader + 1  , len(lines)):
    lines2  = lines[j].split(" ")
    lines3 = list(filter(None, lines2))
    for k in range(0, len(lines3) ):
        print(lines3[2])
