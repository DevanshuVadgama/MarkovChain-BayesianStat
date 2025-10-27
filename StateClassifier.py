import numpy as np
import numpy.linalg as la

with open("TPM2.txt",'r') as f:
    lines=f.readlines()
    TPM=np.array([[float(num) for num in line.split()]for line in lines])

def state_classifier(M):
    P=np.copy(TPM)
    for i in range(M):
        P=P@TPM

    D=np.diag(P)
    for i in range(np.size(D)):
        if D[i]<1e-6:
            print("State ", i , "transient")
        else:
            print( "State ", i ," recurrent " )


def is_accessible(i,j,M):
    P=np.copy(TPM)
    for k in range(M):
        if P[i][j]>1e-12:
            print("i->j")
            break
        P=P@TPM
            
    else:
            
        print(" i-/>(not) j ")            

def communicates(i,j,M):
    P=np.copy(TPM)
    for k in range(M):
        if P[i,j]>1e-12 and P[j,i]>1e-12:
            print(" i<->j ")
            break
        P=P@TPM
    else:
        print(" i </-> (doesnt  commute) j")

def comm_classes(M):
    n = TPM.shape[0]
    t = 1e-12
    P = np.copy(TPM)
    for _ in range(M-1):
        P = P @ TPM

    classes = []

    for i in range(n):
        added_flag = 0
        for cls in classes:
            for j in cls:
                if P[i,j] > t and P[j,i] > t:
                    cls.append(i)
                    added_flag = 1
                    break
            if added_flag == 1:
                break

        if added_flag == 0:
            classes.append([i])

    # Remove duplicates and sort each class
    for k in range(len(classes)):
        classes[k] = sorted(list(set(classes[k])))

    return classes

print(comm_classes(20))



