dic={10:"e",20:"f",30:"c",40:"a",50:"b",60:"d",70:"g",80:"h",90:"i",100:"j"}
list=['a', 'b','c','d','e','f','g','h',"i",'j']
sum=0
print(list)
y=input("you are choose in any alphabet type ok")
if(y=='ok'):
 slideone=['f', 'a','g','i','j']
 print(slideone)
 l=input("you choose alphabet in list type yes")
 if(l=='yes'):
  sum=sum+20
 slidetwo=['e','c','d','h','j'] 
 print(slidetwo)
 n=input("you choose alphabet in list type yes")
 if(n=='yes'):
  sum=sum+10
 slidethree=['b', 'd','g','h','i','j']
 print(slidethree)
 o=input("you choose alphabet in list type yes")
 if(o=='yes'):
  sum=sum+50
 slidefour=['a', 'c','h','i','j']
 print(slidefour)
 s=input("you choose alphabet in list type yes")
 if(s=="yes"):
  sum=sum+20
 print(dic[sum])
else:
 print("once again run")
