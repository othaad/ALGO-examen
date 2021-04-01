def LeSousEnsemble(set,n,Somme):
    SousEnsemble=[[False for i in range(Somme+1)]for i in range(n+1)]
    for i in range(n+1):
        SousEnsemble[i][0]=True
    for j in range(Somme+1):
        SousEnsemble[0][j]=False
# Explication 1 code sur le PowerPoint
    for i in range(n+1):
        for j in range(Somme+1):
            if j<set[i-1]:
                SousEnsemble[i][j]=SousEnsemble[i-1][j]
            if j>=set[i-1]:
                SousEnsemble[i][j]= (SousEnsemble[i-1][j] or SousEnsemble[i-1][j-set[i-1]])
    return SousEnsemble[n][Somme]
# Explication 2 code sur le PowerPoint
set = [0, 2, 3, 4, 5]
Somme = 13
n = len(set)
if LeSousEnsemble(set, n, Somme):
    print("VRAI")
else:
    print("FAUX")