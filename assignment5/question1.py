#define the fibonacci function
def fib(nth_step, cache={}):
    #check if the step is already in the cache
    if nth_step in cache:
        #return value
        return cache[nth_step]
    #0 and 1 case
    if nth_step <2:
        cache[nth_step] = nth_step       
        return nth_step
    #recur using the previous two values
    fib_num = fib(nth_step-1, cache) + fib(nth_step-2, cache)    
    #add current value to cache                                                                    
    cache[nth_step] = fib_num                   
    #return fibonacci number                                                                              
    return fib_num    

#100 gives 354224848179261915075
print(fib(100))
#50 gives 12586269025
print(fib(50))