
# this function working with sorted and non sorted lists
def sequentail_search(a_list,item):
    position=0
    found=False
    
    while position < len(a_list) and not found:
        if a_list[position]==item:
            found=True
        else:
            position=position+1
    return found


test_list=[1,55,18,19,21,48,70,12,19,8]
resoult1=sequentail_search(test_list,18)
# will stop after n steps
resoult2=sequentail_search(test_list,100)

print("resoult1:"+str(resoult1))
print("resoult2:"+str(resoult2))    


# this function works with sorted lists only. and the Benefits of this function stopped if found item or reached to the end of the list 
# or the item value is less than the current value and not found.
def sequentail_search_with_sorted_list(a_list,item):
    position=0
    found=False
    stop=False
    while position < len(a_list) and not found and not stop:
        if a_list[position]==item:
            found=True
        else:
            if item < a_list[position]:
                stop=True
            else:    
                position=position+1            
    return found


test_list2=[1,20,21,56,99]
# will stop after 2 steps becouse 19 less than 20
resoult3=sequentail_search_with_sorted_list(test_list2,19)

print("resoult3:"+str(resoult3))