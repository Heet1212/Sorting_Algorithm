def selection_sort(unsort_list):

    if(len(unsort_list)<1):
        return unsort_list
    for i in range (len(unsort_list)):
        min_value_index =i
        print(unsort_list)
        for j in range(i+1,len(unsort_list)):
            if unsort_list[j]<unsort_list[min_value_index]:
                min_value_index=j
            (unsort_list[i],unsort_list[min_value_index])=(unsort_list[min_value_index],unsort_list[i])
    return(unsort_list)       
sort_list=selection_sort([13,11,17,12,23,27])
print(sort_list)  



def selection(l):
    for i in range(len(l)-1,-1,-1):
        max_id =0
        for j in range(0,i+1):
            if l[j]>=l[max_id]:
                max_id=j

        l[max_id],l[i]=l[i],l[max_id]

    return l    




l=[3,4,2,1,7,9]
print(selection(l))

