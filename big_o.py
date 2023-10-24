def print_items(n):
    ## O(N)
    # for i in range(n):
    #     print(i);
        
    ## O(2N)
    # for j in range(n):
    #     print(j);
        
    ## O(N^2) 
    for i in range(n):
        for j in range(n):
            print(i,j)
    ##    O(N^2 + N)     
    for k in range(n):
        print(k)
        
# DO NOT CHANGE THIS LINE:
print_items(10)