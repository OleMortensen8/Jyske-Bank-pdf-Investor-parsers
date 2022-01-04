import tabula as tb
import pandas as pd
import re
def Danske_Nummer(falsk_streng):
    return int(falsk_streng.replace(".","").replace(",","."))
file = 'Jyske+Bank+Årsrapport+2018.pdf'
df = tb.read_pdf(file, pages='4', stream=True)
ncolumns = df[0].iloc[1,[0,1,2,4,5,6]]
df1 = df[0].iloc[3:,:6]
df1.columns = ncolumns
netto_renteIntægter = df1.iloc[0,1]
resultat_før_skat = df1.iloc[11,1]
resultat_før_skat = Danske_Nummer(resultat_før_skat)
netto_renteIntægter = Danske_Nummer(netto_renteIntægter)
omskæringsgrad = netto_renteIntægter
omskæringsgrad = omskæringsgrad/resultat_før_skat
print(omskæringsgrad)
