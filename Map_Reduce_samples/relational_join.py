import MapReduce
import sys

"""
Relational join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #table_name: Relaton Name :Movie Names or Movie Ratings
    # key: Movie_Id
    # value: Content of tables
    table_name= record[0]
    if(table_name=='MovieNames'):
       key=record[2]
       value=record
    else:
        key=record[1]
        value=record
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: Movie_ID
    # list_of_values:Content of all the tables
    sum=0
    count=0
    movie_name=list_of_values[0] #Content of movie_name table
    user_ratings=list_of_values[1:] #Content of all movie_rating tables
    for m in range(len(user_ratings)):
        mr.emit(movie_name[1:]+user_ratings[m][1:])
        sum+=user_ratings[m][3] #sum of all movie_ratings for a movie id
        count+=1  #total no of ratings for a movie id

    AvgRating=sum/count #finding average
    mr.emit((movie_name[1],AvgRating))

tlab# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])

  mr.execute(inputdata, mapper, reducer)
