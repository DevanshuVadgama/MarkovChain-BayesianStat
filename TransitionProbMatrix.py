import numpy as np
import numpy.linalg as la

with open("TPM.txt",'r') as f:
    lines=f.readlines()
    TPM=np.array([[float(num) for num in line.split()]for line in lines])

def P_n(n):
    p=TPM
    for k in range(n-1):
        x=la.matmul(p,TPM)
        p=x
    return p

# We ll use the proposition that a state i is:
#   -> recurrent iff sum_pii(n)= inf
#   -> transient iff sum_pii(n)<inf

def inf_sum(i,M):
    sum=0
    P=TPM
    for k in range(M):
        P=la.matmul(P,TPM)
        a=P[i][i]
        sum=sum+a
    return sum

def classifier(tol):
    for l in range(int(np.sqrt(np.size(TPM)))):
        if inf_sum(l,tol)<tol:
            print("state ", l , " is transient " )
        else:
            print("state ", l , " is recurrent " )   



#this method is inconsistent as it might be possible that pii(n) drops
# after the tolerance given. So we will rectify this.

# def pii_n(i,n):
#     P=TPM
#     for k in range(n-1):
#         P=la.matmul(P,TPM)
    
#     return P[i][i]

# def ratio_test(M):
#     for i in range(int(np.sqrt(np.size(TPM)))):
#         for l in range(M):
#             r=(pii_n(i,l+1))/(pii_n(i,l))
#         if r<1:
#             print(" State ", i , "transient")
#         else:
#             print(" State ", i , "recurrent")    

# ratio_test(1000)

def updated_classifier(TPM, M):
    n_states = TPM.shape[0]
    P_power = np.copy(TPM)

    for step in range(2, M + 1):
        P_power = np.matmul(P_power, TPM)  
        diag = np.diag(P_power)             
    for i in range(n_states):
        
        if diag[i] < 1e-6:  
            print(f"State {i} transient")
        else:
            print(f"State {i} recurrent")

updated_classifier(TPM,1000)