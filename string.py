char= 256
def distinctchar(str, n): 
    cnt = [0] *char
    for i in range(n): 
        cnt[ord(str[i])] += 1
    distinct = 0
    for i in range(char): 
        if (cnt[i]!=0): 
            distinct += 1    
    return distinct 
def smallesteSubstring(s): 
    n=len(s)
    max_distinct=distinctchar(s, n)
    return max_distinct
str1= "abcda"  
l = smallesteSubstring(str1);  
print(l)
