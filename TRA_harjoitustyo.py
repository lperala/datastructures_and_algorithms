"""
Lassi Perälä 2559371 lassi0205@hotmail.fi
811312A Tietorakenteet ja algoritmit 2019-2020 harjoitustyö
"""

import time
from collections import deque

lista = []
INF = float("inf")
result = []
edellinen = 0
korkein = 0

#MOODLE
class WeightedEdgeNode:
    def __init__(self,nde,wght=0):
        self.node = nde
        self.weight = wght
        
#MOODLE
class WeightedGraph:
    
    def __init__(self,nVerts):
        self.nVertices = nVerts
        self.adj_list = {}
        self.vertices = []
        
        for x in range(1,nVerts+1):
            self.adj_list[x] = []
            self.vertices.append(x)
            
        self.dist = {}
        for x in range(1,nVerts+1):
            self.dist[x] = INF
            
        self.pred = {}
        for x in range(1,nVerts+1):
            self.pred[x] = None

#MOODLE
# adds edge (x,y)       
def add_edge(g, x,y,wght):
    g.adj_list[x].append(WeightedEdgeNode(y,wght))
    g.adj_list[y].append(WeightedEdgeNode(x,wght))
    
#MOODLE            
def dijkstra(g,s):
    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0
    g.dist[s] = 0
    
    queue = [i for i in g.vertices]
    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert
        if u == 0:
            #Check if list has gone trough
            break
        
        queue.remove(u)
            
        for edge in g.adj_list[u]:
            v = edge.node
            if g.dist[v] > g.dist[u] + edge.weight:                
                    g.dist[v] = g.dist[u] + edge.weight
                    g.pred[v] = u

#Kruskalin algoritmi, jolla saadaan Pienin virittävä puu (minimum spanning tree)
def kruskal(): 
        #loop vakiot i ja e
        i = 0
        e = 0
        
        #lajitellaan kaupungit korkeuksien mukaan suuruus järjestyksessä ja luodaan tarvittavat listat
        lajiteltu_lista = sorted(lista, key=lambda item: item[2]) 
        parent = []
        luokka = [] 
        
        #funktion huomioitavien nousujen määrä
        nousut = int_nousuja - 1
        
        #luodaan parent ja luokka -listat
        for j in range(nousut): 
            parent.append(j) 
            luokka.append(0)
       
        while i < nousut : 
            
            u,v,w = lajiteltu_lista[i]
            i += 1

            x = find(parent, u) 
            y = find(parent ,v) 

           
            #lisätään tiedot (lähtö, pääte, korkeus) result-listaan, jos sykliä ei synny
            if x != y: 
                e = e + 1   
                result.append([u,v,w]) 
                union(parent, luokka, x, y)
            print(result)
        #lisätään result-listasta löytyviä tietoja dijkstran graaffiin
        for u,v,weight in result:   
            print(u,v,weight)
            add_edge(wgraph, u, v, weight)
                  


#apufunktio, joukon i löytämiseen
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
    
#funktio, joka yhdistää kaksi joukkoa x ja y  
def union(parent, luokka, x, y): 
    xjuuri = find(parent, x) 
    yjuuri = find(parent, y) 
    
    #pienemmän luokan puu juureen
    if luokka[xjuuri] < luokka[yjuuri]: 
        parent[xjuuri] = yjuuri
            
    elif luokka[xjuuri] > luokka[yjuuri]: 
        parent[yjuuri] = xjuuri 
        
    #jos luokat samat, toisesta tehdään juuri ja kasvatetaan luokkaa yhdellä
    else: 
        parent[yjuuri] = xjuuri 
        luokka[xjuuri] += 1

#printataan kuljettu polku sekä tämän hetkinen korkein nousu      
def print_polku(g,u):
    global edellinen, korkein
    if g.pred[u] != 0:
        print_polku(g,g.pred[u])
    kasvu = g.dist[u]
    ero = kasvu - edellinen
    edellinen = kasvu
    if korkein < ero:   
        korkein = ero           
    print("\n->",u, "\nTämän hetkinen korkein nousu: ", korkein)

#loputksi todetaan vielä mikä korkein nousu lopulta oli     
def print_korkein():
    if korkein == INF:
        print("\nPääte kaupunkiin ei löytynyt polkua.")
    else:
        print("\nKorkein nousu on: ", korkein)


while True:
    try:
        tiedosto = input("\nAnna tiedoston nimi (muista .txt pääte): ")
        f = open(tiedosto, "r")
        polku = str(input("\nPrintataanko polku (y/n) (Aikaa mitatessa kannattaa valita n): "))
        tallennus = input("\nTallennetaanko kaupunkien lkm ja aika tiedostoon (y/n): ")
        break
    except FileNotFoundError: 
        print("\nTiedostoa ei löydy")
        
        
#ohjelman suoritus alkaa tästä       
start_time = time.time()
paate, kaupunkeja = (f.readline()).split()
int_nousuja = int(kaupunkeja)
int_kaupunkeja = int(kaupunkeja)
print("\nPääte kaupunki: {}".format(paate))
print("\nKaupunkien lkm: {}".format(kaupunkeja))
wgraph = WeightedGraph(int(paate))
#luodaan lista, josta tarvittavia tietoja löydetään (lahtökaupunki, päätekaupunki, nousun korkeus)
i = 0
for j in f:
    if int_kaupunkeja > 0:
        lahto, paate, korkeus = (j).split()
        lista.append([int(lahto),int(paate),int(korkeus)]) 
        i += 1
        int_kaupunkeja -= 1    
print(lista)        
print("\nNousujen lkm: ", i)
kruskal()
dijkstra(wgraph,1)
print("\nPolku 1 ->", int(paate))
print("\nPääte kaupunki: ", paate)
if polku == "y":
    print_polku(wgraph,int(paate)) #aikakompleksisuutta mitatessa kannattaa jättää polku printtaamatta
print_korkein() 
aika = (time.time() - start_time)
str_aika = str((time.time() - start_time))
print("\nOhjelman suorituksessa kesti: %.10f sekuntia" % aika)
tallennus = "y"
if tallennus == "y":    #tallennetaan aikoja tiedostoihin
    tallennus = open("tallennus.txt", "a")
    tallennus.write("Solmuja: {}, Aika: {} \n".format(paate, str_aika)) 
    
