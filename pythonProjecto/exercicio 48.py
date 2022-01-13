s=0
c=0
for cont in range(1,501,2):
    if cont%3==0:
      s+=cont
      #print(cont,end=' ')
      c+=1
print(' existem {} multiplos de 3 e a soma é {}'.format(c,s) )