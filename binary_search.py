
def binary_search(a_list,item):
    first=0
    last=len(a_list)-1
    found=False
    
    while first<=last and not found :
        middle_point=(first+last)//2
        if a_list[middle_point]==item:
            found=True
        else:
            if item > a_list[middle_point]:
                first=middle_point+1
            else:
                last=middle_point-1
    return found


test_list2=[1,20,21,56,99]
resoult=binary_search(test_list2,20)

print("resoult:"+str(resoult))



            
    