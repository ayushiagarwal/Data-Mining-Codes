import sys
import math
from math import sqrt

 #Function to calculate the minimum distance and print the final cluster
def cluster_cal(data,k,i,initial_points):
 dataset=data.read()
 centroids=[]
 for points in initial_points:
         points=points.strip('\n')
         points=points.split(',')
         centroids.append(points)
 num=0
 if(len(centroids)!=k):
     print("Error ,Initial points does not match the no of cluster")
 else:
  while(num<i):#if iterations are over
   cluster_dict={}
   for line in dataset.split():
     line=line.split(',')
     initial_dict={}
     for c in centroids:
         a=line[:-1]
         b=c[:-1]
         distance=sqrt(sum( (float(a) - float(b))**2 for a, b in zip(a, b))) #calculate euclidean distance
         t_point=tuple(c)
         initial_dict[t_point]=distance
     val=min(initial_dict, key=lambda x: initial_dict[x])#pick minimum distance
     if val not in  cluster_dict:
         cluster_dict[val]=[line]
     else:
       cluster_dict[val].append(line)
   new_centre=centroid_cal(cluster_dict) #call to function to calculate new centroid
   if(new_centre==centroids): # if new centroid becomes equal
       return final_cluster(cluster_dict) #print the clusters
       break
   centroids=new_centre
   num=num+1
  return final_cluster(cluster_dict) #print the clusters
  
#to calculate new centoid
def centroid_cal(cluster_dic):
 new_centroid=[]
 for key,value in cluster_dic.items():
     c=[]
     for j in range (len(value[0])-1):
       c.append(sum(float(row[j])/len(value) for row in value))
     c.append(key[-1])
     new_centroid.append(c)
 return new_centroid

#To print the final clusters
def final_cluster(f_cluster):
     accuracy=0
     for key,value in sorted(f_cluster.items(), key=lambda p: p[1][-1]):
        label_c=[]
        for v in value:
            label_c.append(v[-1])
        label=max(label_c, key=label_c.count)
        print("cluster:",label)
        for x in value:   
             print(x)
             if(label!=x[-1]):
                accuracy+=1
        print('\n')         
     print("Number of points wrongly assigned",'\n',accuracy)
    
if __name__ == '__main__':
 data = open(sys.argv[1])
 k=int(sys.argv[2])
 iter=int(sys.argv[3])
 initial_points= open(sys.argv[4])
 cluster_cal(data,k,iter,initial_points)
 