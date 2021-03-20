# matriks adjacent
G = [[ 0, 1, 1, 0, 1, 0],
     [ 1, 0, 1, 1, 0, 1],
     [ 1, 1, 0, 1, 1, 0],
     [ 0, 1, 1, 0, 0, 1],
     [ 1, 0, 1, 0, 0, 1],
     [ 0, 1, 0, 1, 1, 0]]

# hitung derajatnya
degree =[]
for i in range(len(G)):
  degree.append(sum(G[i]))

# nama titik berdasarkan matriks adjacent
titik = "abcdef"
t_={}
for i in range(len(G)):
  t_[titik[i]] = i


# inisialisasi warna yang memungkinkan
warna = {}
for i in range(len(G)):
  warna[titik[i]]=["biru","merah","kuning","hijau"]


# sort titik berdasarkan derajatnya
sorted_node=[]
indeks = []
#pakai selection sort
for i in range(len(degree)):
  _max = 0
  j=0
  for j in range(len(degree)):
    if j not in indeks:
      if degree[j] > _max:
        _max = degree[j]
        idx = j
  indeks.append(idx)
  sorted_node.append(titik[idx])



node={}
for n in sorted_node:
  pil_warna = warna[n]
  node[n] = pil_warna[0]
  tetangga = G[t_[n]]
  for j in range(len(tetangga)):
    if tetangga[j]==1 and (pil_warna[0] in warna[titik[j]]):
      warna[titik[j]].remove(pil_warna[0])


# cetak hasilnya
for t,w in node.items():
  print("titik",t," = ",w)
