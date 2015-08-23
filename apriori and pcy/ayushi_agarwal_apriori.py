import itertools
def apriori(dataset,support):
 #support=3
 candidates =[]
 k=2
 data=dataset.read()
 for basket in data.split():
   for item in basket.split(","):
    candidates.append([item])#all candidate item in list
 u_candidates= [list(j) for j in set(tuple(x) for x in candidates)]
 
 fr=frequent_items(data,u_candidates,support)
 print('Frequent Itemsets of size 1')
 for l in fr:
    print ((',').join(l[0:]))
 print('\n')
 while (len(fr)!=0):
  u_candidates= candidate_items(fr,k)
  #print(u_candidates)
  fr=frequent_items(data,u_candidates,support)
  if(len(fr)!=0):
   print('Frequent Itemsets of size',k)
   for l in fr:
    print ((',').join(l[0:]))
   print('\n')
  k=k+1

def frequent_items(data,u_candidates,support):
 sdict={}
 
 for s in data.split() :
  j=s.split(",")
  for c in u_candidates:
      t=tuple(c)
      if (set(c).issubset(set(j))):
          if t not in sdict:
            sdict[t]=1
          else:                
            sdict[t]+=1
 f_item=[]
 for d in sdict:
      if (sdict[d]>=support):
        f_item.append(list(d))
 frequent_item=sorted(f_item)
 return frequent_item
 


def candidate_items(frequent_item,k):
#canddates of size 2 :
 #can=list(itertools.combinations(f_item,k))
 #u_c = []                                                          
 #for x in can:
   #u_c.append(list(x))
 #print(u_c)
 l=[]
 for i in range(len(frequent_item)):
    for j in range(i+1,len(frequent_item)):
         a=set(frequent_item[i])
         b=set(frequent_item[j])
         cd=a.union(b)
         u_c=sorted(cd)
         if(len(u_c)==k):
             l.append(list(u_c))
 #print(l)
 unique_candidate= [list(j) for j in set(tuple(x) for x in l)]
 return unique_candidate


# frequent_item of size 2
 
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  support= open(sys.argv[2])
  apriori(inputdata,support)