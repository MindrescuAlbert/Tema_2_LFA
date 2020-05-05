f = open ("intrare.in", "r")
nr_noduri = int(f.readline())

dict = {}
l = f.readline().split()
ct = -1
for ch in l:
    ct = ct + 1
    dict[ch] = ct

nr_finale = int(f.readline())
lst_finale = []
lst_finale = f.readline().split()
dfa_finale = []
for x in lst_finale:
    dfa_finale.append(dict[x])

lst_liste = [[[] for i in range(nr_noduri+1)] for i in range(nr_noduri+1)]
alfabet = []

for x in f:
    l = x.split()
    lst_liste[ dict[l[0]] ][ dict[l[1]] ].append( l[2] )
    if l[2] not in alfabet and l[2] != "lambda":
        alfabet.append(l[2])

lbd_inchideri = [[] for i in range(nr_noduri)]

coada = []
nr_coada = 0

for i in range(nr_noduri):
    lbd_inchideri [i].append(i)
    contor = 0;
    coada.append(i)
    while len(coada) != 0:
        contor = 0
        for x in lst_liste [coada[0]]:
            if "lambda" in x:
                lbd_inchideri [i].append(contor)
                coada.append(contor)
            contor = contor + 1
        coada.pop(0)

tabel = [[] for i in range(len(alfabet))]

contor_tabel = 0
for ch in alfabet:
    for i in range (nr_noduri):
        lst_aux = []
        lst_tabel = []
        for j in lbd_inchideri [i]:
            contor = 0
            for k in lst_liste [j]:
                if ch in k and contor not in lst_aux:
                    lst_aux.append(contor)
                contor = contor + 1

        for j in lst_aux:
            for k in lbd_inchideri [j]:
                if k not in lst_tabel:
                    lst_tabel.append(k)
        tabel [contor_tabel].append(lst_tabel)
    contor_tabel = contor_tabel + 1

ch = 'A'
ch = chr(ord(ch) - 1)
dict_dfa = {}
lst_dfa = []

tabel_dfa = []
lbd_inchideri[0].sort()
coada = []
coada.append(lbd_inchideri[0])
tabel_dfa.append((lbd_inchideri[0]))
print (lbd_inchideri[0])
ch = chr(ord(ch) + 1)
dict_dfa[ch] = coada[0]

while len(coada) != 0:
    for i in range(len(alfabet)):
        lst_noua = []
        for j in coada[0]:
            for k in tabel[i][j]:
                if k not in lst_noua:
                    lst_noua.append(k)
        lst_noua.sort()
        if lst_noua != []:
            if lst_noua not in tabel_dfa:
                coada.append(lst_noua)
                tabel_dfa.append(lst_noua)
                print(lst_noua)
                ch = chr(ord(ch) + 1)
                dict_dfa[ch] = lst_noua
                for k,v in dict_dfa.items():
                    if v == coada[0]:
                        poz1 = k
                    elif v == lst_noua:
                        poz2 = k
                print(poz1, poz2, alfabet[i])
            else:
                for k,v in dict_dfa.items():
                    if v == coada[0] == lst_noua:
                        poz1 = poz2 = k
                        break
                    elif v == coada[0]:
                        poz1 = k
                    elif v == lst_noua:
                        poz2 = k
                print(poz1, poz2, alfabet[i])
    coada.pop(0)

final = []

for k,v in dict_dfa.items():
    for x in v:
        if x in dfa_finale and k not in final:
            final.append(k)
print(final)