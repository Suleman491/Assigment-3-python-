for hyp in range(1,500):
    hyp+=1
    for s1 in range(1,hyp):
        s1+=1
        for s2 in range(1,s1):
            s2+=1
            if(hyp*hyp==s1*s1 + s2*s2):
                print(str(hyp)+"        "+str(s1)+"        "+str(s2))

