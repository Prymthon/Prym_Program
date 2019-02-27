# Finished Program
target=1
while 1:
   i=2
   prime=True
   while i<target:
      if (target%i) == 0:
         prime=False
         break
      i=i+1
   if (prime):
      print(target, "is a prime")
   target=target+1
