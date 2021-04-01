def SommeMaximalDuSousTableau(List):
    Taille=len(List)
    SommeActuelle=0
    sommemaximal=List[0]
    for i in range(0,Taille):
        SommeActuelle=SommeActuelle+List[i]

        if(sommemaximal<SommeActuelle):
            sommemaximal=SommeActuelle

        if(SommeActuelle<0):
            SommeActuelle = 0


    print("Somme Maximal Du Sous Tableau est",sommemaximal)

List=[6,-2,-3,1,5]
SommeMaximalDuSousTableau(List)