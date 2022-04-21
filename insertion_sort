def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        temp_value = unsorted_list[i]
        j = i-1

        while j>=0 and unsorted_list[j] > temp_value:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1]=temp_value    
    return unsorted_list    
        
sort_list=insertion_sort([13,23,17,12,23,27])
print(sort_list)         
