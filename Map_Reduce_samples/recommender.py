import sys
import math


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
 weighted_average(rating_dic)
 

def weighted_average(rating_dic):
 user='Ayushi'
 predict=[]
 for item, users in rating_dic.items():
     if user not in users.keys():
      sum_wt_avg=0
      wt_avg_l=[]
      sorted_wt_l=[]
      for movies,u_name in rating_dic.items():
        if item!=movies:
            #print(movies)
         if user in u_name.keys():
            #print(users)
            #print(u_name)
            corated_users=users.keys() & u_name.keys()
            sum_item=0
            sum_movies=0
            mean_item=0
            mean_movies=0
            numerator=0
            den1=0
            den2=0
            denominator=0
            weigted_average=0
            
            
            #print(len(corated_users))
            
            for c in corated_users:
                 
                sum_item+=rating_dic[item][c]
                sum_movies+=rating_dic[movies][c]
            mean_item=float(sum_item/len(corated_users))
            mean_movies=sum_movies/len(corated_users)
            
            for c in corated_users:
                
                 numerator+=(rating_dic[item][c]-mean_item)*(rating_dic[movies][c]-mean_movies)
                 den1+=math.pow((rating_dic[item][c]-mean_item),2)
                 den2+=math.pow((rating_dic[movies][c]-mean_movies),2)
            denominator=float(math.sqrt(den1)*math.sqrt(den2))
            try:weighted_average=float(numerator/denominator)
            except:weighted_average=0.0
            #print(weighted_average)
            #sum_wt_avg+=weighted_average
             
            wt_avg_l.append([weighted_average,item,movies])
      #print(wt_avg_l)
      sorted_wt_l=sorted(wt_avg_l, key=lambda x: x[0],reverse=True)
      print(sorted_wt_l)
      p_coeff=prediction_item(rating_dic,user,sorted_wt_l)
      #print(p_coeff)
      predict.append([item,p_coeff])
 print(predict)
def prediction_item(rating_dic,user ,wt_av):
      n=2
      num=0
      sum_wt=0
      for w in range(0,n):
          sum_wt+=wt_av[w][0]
          
      for r_item,r_user in rating_dic.items():
          if user in r_user.keys():
                for w in range(0,n):
                    if r_item in wt_av[w][2]:
                        num+=r_user[user]*wt_av[w][0]
                        
      pearson_coeff='%.5f'%(num/sum_wt)
      return pearson_coeff
      

 
 
 
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  create_dic(inputdata)