import MapReduce
import sys

"""
Pair of Friends Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # person:person's name
    # friend_list:list of friends of person
    person = record[0]
    friend_list = record[1]
    for f in friend_list:
      key=(person,f)
      unique_key=sorted(key) #unique key for a pair of friends
      mr.emit_intermediate((unique_key[0],unique_key[1]),1)
    
def reducer(key, list_of_values):
    # key: unique key for pair of friends
    # list_of_values:occurence of unique key
    if(len(list_of_values)==2): #checking symmetric friendship if unique key occurs twice
      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
