class Node:
  def __init__(self,icerik=None):
    self.icerik=icerik
    self.ileri=None
  def __repr__(self):
    return self.icerik
class linkedlist:
  def __init__(self):
    self.bas=None
    self.son=None
  def __repr__(self):
    tmp=self.bas
    dizi=[]
    while tmp is not None:
      dizi.append(tmp.icerik)
      tmp=tmp.ileri
    dizi.append("None")
    
    return "->".join(str(dizi))
   # for j in dizi:
    #  return j
  def __init__(self,tmp=None):
    self.bas=None
    self.son=None
    if tmp is not None:
      tmp=Node(icerik=dizi.pop(0))
      self.bas=tmp
      for i in dizi:
        tmp.ileri=Node(icerik=i)
        tmp=tmp.ileri
  def __iter__(self):
    tmp=self.bas
    while tmp is not None:
      yield tmp
      tmp=tmp.ileri
      
 
  def basaekle(self,yen):
    yeni=Node(yen) 
    if self.son is None:
      self.bas=yeni
      self.son=yeni
    else:
      yeni.ileri=self.bas
      self.bas=yeni
  def sonaekle(self,yen):
    yeni=Node(yen)
    if self.bas is None:
      self.bas=yeni
      self.son=yeni
    else:
      self.son.ileri=yeni
      self.son=yeni

  
