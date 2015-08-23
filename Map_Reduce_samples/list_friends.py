import MapReduce
import sys

"""
List of friends  for each person Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # personA: name of person
    # personB:person A's friends
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA,personB)

def reducer(person, list_of_friends):
    # person: person's name
    # list_of_friends: list of friends
    #friend_list:removing duplicate friends
    friend_list=list(set(list_of_friends))
    mr.emit((person, friend_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
