import numpy as np

def true_roots(coeffs):
    roots = np.roots(coeffs)
    return roots 

def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def cross_over(a,b):
    pos = np.random.randint(1,5)
    sa = bindigits(a,6)
    sb = bindigits(b,6)
    a_tail = sa[pos:]
    b_tail = sb[pos:]
    sa = sa[:pos] + b_tail
    sb = sb[:pos] + a_tail 
    return int(sa,2), int(sb,2)

def mutation(a):
    sa = bindigits(a,6)
    pos = np.random.randint(0,6)
    ch = '0' if sa[pos] == '1' else '1'
    sa = sa[:pos] + ch + sa[pos+1:]
    return int(sa,2)

#2-polynomial
def my_roots(coeffs):
    #initial population (roots)
    nroots = np.random.randint(5,50) 
    roots = []
    for i in range(nroots):
        roots.append(np.random.randint(-32, 31)) 
   
    #calc fitness
    fitness_coef = np.random.randint(10,1000) 
    nroots -= 2
    loop = 0
    
    #breeding
    while True:
        fitness_value = [] 
        for root in roots:
            tmp = fitness_coef - (coeffs[0]*root**2 + coeffs[1]*root + coeffs[2])
            fitness_value.append(tmp)
        
        dif = [abs(x - fitness_coef) for x in fitness_value]
        fitness_value = [x for _,x in sorted(zip(dif, fitness_value))]
        roots = [x for _,x in sorted(zip(dif, roots))]

        #base case
        if(dif[0] == 0 or loop == 1e3):
            dif.sort()
            break

        #selection: get rid of the last 2 roots which have the lowest fitness value
        for i in range(2):
            fitness_value.pop(-1)
            roots.pop(-1)

        p1, p2 = roots[0], roots[1]
        f_p1, f_p2 = fitness_value[0], fitness_value[1]
        
        #cross over:
        for i in range(0,nroots,2):
            check = np.random.choice(2, p=[0.3, 0.7]) #probability of cross over = [0: 30%, 1: 70%]

            if(i < nroots-1 and check == 1):
                children = list(cross_over(roots[i], roots[i+1]))
                roots[i] = children[0]
                roots[i+1] = children[1]
       
        if(nroots % 2 != 0):
            i1 = np.random.randint(nroots)
            i2 = np.random.randint(nroots)
            roots[-1] = list(cross_over(roots[i1], roots[i2]))[0]
        
        roots.append(p1)
        roots.append(p2)    
          
        #mutation
        for i in range(len(roots)):
            check = np.random.choice(2, p=[1 - 0.001, 0.001])
            if(check == 1):
                roots[i] = mutation(roots[i])

        loop += 1
            
    res = [roots[0]]
    for i in range(len(roots)):
        if(dif[i] == 0 and roots[i] != res[0]):
            res.append(roots[i])
            break

    return res

    # print(loop)
    # print(roots)

#---MAIN
coeffs = [1, 3 - np.sqrt(2), -3*np.sqrt(2)] 

print('True roots: {}'.format(true_roots(coeffs)))
for i in range(10):
    print(my_roots(coeffs))


