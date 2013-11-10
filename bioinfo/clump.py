import collections
import operator
import itertools

#l = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
f = open('E-coli.txt', 'r')
l = f.read()

global total
total = []

kmers = 5
length = 50
t = 4

# d = {}
# for i in range(len(l)): 
#   d[i] = l[i:i+5]

d = []
for i in range(len(l)):
  d.append(l[i:i+kmers])


def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  #print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item

  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
      
    if count >= t:
      total.append(item)
      return count, -min_index
    return 0, -min_index
        
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]


g = []
for i in range(len(d)):
  most_common(d[i:i+length])

print ' '.join(set(total))