def remove_duplicates(li):
    li.sort()
    new_list = []
    for i in li:
        if i not in new_list:
            new_list.append(i)
        

def rem_duplicates(li):
    x=0   
    for i in range(1, len(li)):
        if li[x] != li[i]:
            x += 1
            li[x] = li[i]
    return li[:x+1]

li=[1,1,3,3,3,4,5,7,8,9,9,9,10]

print(rem_duplicates(li))
        
        
    