arr = [['a', 'b', 'c', 'd'],  
        ['h', 'g', 'f', 'e'],  
        ['i', 'k', 'l', 'm'],  
        ['q', 'p', 'o', 'n']] 
  
n = len(arr[0]) 
                   
# Print mentioned row 
k=int(input("Enter your row and column value: ")); 
i=k-1
for j in range(0, n): 
    print(arr[i][j], end = " ") 

#print mentioned column  
j=k-1;
for i in range(0, n): 
    print(arr[i][j], end = " ") 