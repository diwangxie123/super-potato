#(i,j)
for i in range(1,10):
   for j in range(1, i + 1):
#(1,3)取1,2
      print(f"{j}×{i}={i*j}",end="\t")
   print()
