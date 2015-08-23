import MapReduce
import sys

"""
Size Count Example to count word of different sizes in document in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # document_id: document identifier
    # text: document contents
    document_id= record[0]
    text = record[1]
    words = text.split()
    size_count={} #a dictionary that will store size of text and counts
   
    #Loop to calculate size of words and place them in dictionary
    #using combiner logic
    for v in words:
      if len(v)>=10:
        size='large'
        if size not in size_count:
          size_count[size]=1
        else:                
          size_count[size]+=1
      elif (len(v)>=5 and len(v)<=9):
        size='medium'
        if size not in size_count:
          size_count[size]=1
        else:
          size_count[size]+=1
      elif (len(v)>=2 and len(v)<=4):
        size='small'
        if size not in size_count:
          size_count[size]=1
        else:
          size_count[size]+=1
      else:
        size='tiny'
        if size not in size_count:
          size_count[size]=1
        else:
          size_count[size]+=1
    
    mr.emit_intermediate(document_id,size_count)
         
def reducer(document_id, list_of_values):
    # document_id: document_identifier
    # value: list of size counts
    #size_list:formatting to produce output of size and counts
    size_list=[]
    for s in list_of_values:
      for size,count in sorted(s.items()):
        size_list.append([size,count])

    mr.emit((document_id,size_list))

# Do not modify below this line
# =============================


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
