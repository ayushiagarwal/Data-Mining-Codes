import sys
import math
#Recommend items based on k neighbours 
def recommender(dataset,user,n,k):
 rating_dic=create_dic(dataset) #call create dictionary
 predict=prediction_item(rating_dic,user,n) #call predict item and calculate predictions on input
 sorted_predict=sorted(predict, key=lambda x: (-(float(x[1])),x[0]))
 
 output_list=[]
 
 for i in range(0,len(sorted_predict)):
     if (i<k):
      output_list.append(sorted_predict[i])
 for l in output_list:
    print ((' ').join(l[0:]))
    
#Create dictionary of items :
def create_dic(dataset):
 data=dataset.readlines()
 rating_dic={}
 for line in data:
       line=line.strip('\n')
       line=line.split('\t')
       if line[2] not in rating_dic:
          rating_dic[line[2]]={line[0]:float(line[1])}
       else:                
          rating_dic[line[2]].update({line[0]:float(line[1])})
 return rating_dic

#Calculate weighted average and create prediction:
def prediction_item(rating_dic,user,n):
 predict=[]
 for item, users in rating_dic.items():
     if user not in users.keys():
      sum_wt_avg=0
      wt_avg_l=[]
      for movies,u_name in rating_dic.items():
        if item!=movies:
          if user in u_name.keys():
            corated_users=users.keys() & u_name.keys()
            if (len(corated_users)>0):
             sum_item=0;sum_movies=0;mean_item=0; mean_movies=0;numerator=0;den1=0;den2=0;denominator=0;weigted_average=0
             for c in corated_users:
                sum_item+=rating_dic[item][c]
                sum_movies+=rating_dic[movies][c]
             mean_item=sum_item/len(corated_users)
             mean_movies=sum_movies/len(corated_users)
             for c in corated_users:
                 numerator+=((rating_dic[item][c]-mean_item)*(rating_dic[movies][c]-mean_movies))
                 den1+=math.pow((rating_dic[item][c]-mean_item),2)
                 den2+=math.pow((rating_dic[movies][c]-mean_movies),2)
             denominator=float((math.sqrt(den1))*(math.sqrt(den2)))
             if (denominator==0):
               weighted_average=0.0
             else:
               weighted_average=float(numerator/denominator) #calculate weighted average 
             
             wt_avg_l.append([weighted_average,item,movies])
             #print(wt_avg_l)
      if (len(wt_avg_l)==0):
          pass
      else:
       sorted_wt_l=sorted(wt_avg_l, key=lambda x:(-(x[0]),x[2]))
       p_coeff=pearson_coefficient(rating_dic,user,n,sorted_wt_l) #calculate pearson coefficient and predict movies with ratings
       predict.append([item,str(p_coeff)])
 if(len(predict)==0):
  pass
 else : 
  return predict

#Calculate Pearson Coefficient :
def pearson_coefficient(rating_dic,user,n,wt_av):
      num=0
      sum_wt=0
      p_coeff=0
      
          
      for r_item,r_user in rating_dic.items():
          if user in r_user.keys():
                for w in range(0,len(wt_av)):
                    if (w<n):
                          if(wt_av[w][0]==0):
                             p_coeff=0.0
                             return p_coeff
                             
                          else:  
                             sum_wt+=abs(wt_av[w][0])
                             num+=(rating_dic[wt_av[w][2]][user]*wt_av[w][0])
                break
      if(sum_wt==0):
       p_coeff=0.0
      elif(n>len(wt_av)):
       p_coeff=0.0
      else:
       p_coeff=round((num/sum_wt),5)
      return p_coeff

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  user= str(sys.argv[2])
  n=int(sys.argv[3])
  k=int(sys.argv[4])
  recommender(inputdata,user,n,k)