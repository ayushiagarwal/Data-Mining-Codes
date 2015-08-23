import MapReduce
import sys

"""
Mutual Friends Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # person:person's name
    # friend_list: list of friends for a person
    person = record[0]
    friend_list = record[1]
    for f in friend_list:
      key=(person,f)
      unique_key=sorted(key) #unique key for a pair of friends
      mr.emit_intermediate((unique_key[0],unique_key[1]),friend_list)
      
def reducer(key, list_of_friends):
    # key: unique key for pair of friends
    # list_of_friends:list of frieds for both person's in a pair
    list_of_mutual_friends=[] #mutual friends's list
    if (len(list_of_friends)==2): #symmetric friendship check if there are two lists in a pair of friends
      for f in list_of_friends[0]:
        for m in list_of_friends[1]:
          if (f==m): #checking mutual friends if duplicates in both list
            list_of_mutual_friends.append(f)
    if(len(list_of_mutual_friends)>=1):
      unique_key=''.join(key) #joining the unique key for the given output 
      mr.emit((unique_key,list_of_mutual_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
