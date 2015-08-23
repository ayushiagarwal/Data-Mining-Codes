import sys
import itertools
#Function generation of PCY
def pcy(dataset,support,bucket):
 #Identify all unique items in data
 candidates =[]
 k=2
 data=dataset.read()
 for basket in data.split():
   for item in basket.split(","):
    candidates.append([item])#all candidate item in list
 u_candidates= [list(j) for j in set(tuple(x) for x in candidates)]#unique candidates
 u_can=sorted(u_candidates)

 #Make frequent items of size 1 :
 fr=frequent_items(data,u_candidates,support)#frequent item of size 1
 print('Frequent Itemsets of size 1')
 for l in fr:
    print ((',').join(l[0:]))
 print('\n')
 
 #Do the hashing and count frequent item till the frequent item become zero
 while (len(fr)!=0):
  h_dict,h_candidates=hashing(u_can,k,bucket)
  b_m=bit_map(h_candidates,data,h_dict,support)
  candidate_item= candidate_items(fr,k,b_m,h_dict)
  fr=frequent_items(data,candidate_item,support)
  if(len(fr)!=0):
   print('Frequent Itemsets of size',k)
   for l in fr:
    print ((',').join(l[0:]))
   print('\n')
  k=k+1

#Function defination for hashing:
# The function generates the possible items of size k  and hash them into buckets:
 #Expression for hashing = sum of items
def hashing(u_candidates,k,bucket):
 #Assigning individual item a value
 i=1
 item_dict={}
 for c in u_candidates:
      t=tuple(c)
      item_dict[t]=i
      i=i+1
 #Possible item of size k for hashing
 hash_candidates=list(itertools.combinations(list(set(itertools.chain.from_iterable(u_candidates))), k))
 h_c= [list(j) for j in set(tuple(x) for x in hash_candidates)]
 h_candidates=[]
 for h in h_c:
     h_cn=sorted(h)
     h_candidates.append(h_cn)
 #Assign bucket value to these h_candidates using hash function :a+b%bucket
 h_dict={}
 for p in h_candidates:
     v=0
     p_t=tuple(p)
     for i in range(k):
      v+=item_dict[(p[i],)]
     value=v%bucket
     h_dict[p_t]=value
 return (h_dict,h_candidates)

#Function definition for bit map vector
def bit_map(h_candidates,data,h_dict,support):
 b_dict={}
 # keeping the item count in each bucket
 for c in h_candidates:
  t=tuple(c)
  key=h_dict[t]
  for line in data.split() :
   bc=line.split(",")
   if (set(c).issubset(set(bc))):
      if key not in b_dict:
          b_dict[key]=1
      else:
          b_dict[key]+=1
#Assign bit map vector 1 and 0
 bit_map={}
 for d in b_dict:
    if (b_dict[d]>=support):
          bit_map[d]=1
    else:
        bit_map[d]=0
 return(bit_map)


#Make frquent item function
def frequent_items(data,u_candidates,support):
 sdict={}
 for s in data.split() :
  j=s.split(",")
  for c in u_candidates:
      t=tuple(c)
      if (set(c).issubset(set(j))): #if candidate is in mainset ,count the candidate
          if t not in sdict:
            sdict[t]=1
          else:                
            sdict[t]+=1
 f_item=[]
 for d in sdict:
      if (sdict[d]>=support):
        f_item.append(list(d)) #append if support greater than min support
 frequent_item=sorted(f_item)
 return frequent_item

#Make candidate function  based on two conditions : if item is present in frequent_item and bit map is 1
def candidate_items(frequent_item,k,b_m,h_dict):
 l=[]
 for i in range(len(frequent_item)):
    for j in range(i+1,len(frequent_item)):
         a=set(frequent_item[i])
         b=set(frequent_item[j])
         cd=a.union(b)          #finding candidates of size k
         u_c=sorted(cd)
         if(len(u_c)==k):
             sub=list(itertools.combinations(u_c,k-1))
             f_l = [tuple(s) for s in frequent_item] 
             int=set(f_l).intersection(set(sub))#check for monotonocity
             if(len(int)==len(sub)):
              l.append(list(u_c))
 
 candidate_item= [list(j) for j in set(tuple(x) for x in l)]#removing duplicates
 c_item=[]
 for g in candidate_item: #check if bit_map is 1 
     z=tuple(g)
     if(b_m[h_dict[z]]==1):
       c_item.append(g)
 return c_item

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  support = sys.argv[2]
  bucket=sys.argv[3]
  pcy(inputdata,int(support),int(bucket))
  