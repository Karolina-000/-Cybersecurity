numbers = list(map(int, input().split()))

def count_even(numbers):
    count = 0                      
    for i in numbers:             
        if i % 2 == 0:             
            count += 1             
    
    if count > 0:                  
        return count                
    else:                            
        return -1                    


print(count_even(numbers))