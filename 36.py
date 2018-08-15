
if __name__=='__main__':
  num=100
  lst = []
  if num <= 1:
    print( '0 ~ %d以内没有任何素数' % num)
  for i in range(2, num+1):
    for j in range(2, int(i/2)+1):
      if i % j==0:
        break
    
    else:
       lst.append(i)
  print(lst)
            
