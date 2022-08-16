""" THIS IS A CODE SNIPPET TO USE QUICK SORT """
""" ---------------------------------------- """
""" BASIC PHILOSOPHY - DEFINE PIVOT AND PUT IN THE RIGHT POSITION """

def partition(arr,start,end): #This function will return the pivot point at its correct position (i.e, all elements to the left as smaller and all to the right are larger)
  pivot_index = start
  pivot = arr[pivot_index]

  # start = pivot_index + 1 #start pointer is the next element to the pivot
  # end = len(arr) - 1 #Last element in the array


  while start < end:
  #Now we move start pointer to where the value is > 11
    while start < len(arr) and arr[start] <= pivot:
      start +=1 #move right

  #Now we move end pointer to where the value is < 11
    while arr[end] > pivot:
      end-=1 #move left

  #Now swap the values of the start and end pointers if start pointer is still to the left of the end pointer. If end pointer has moved to the left of the start pointer, we terminate the process on this pass
    if start < end:
      arr[start],arr[end] = arr[end],arr[start]

  #Once the above condition is met, we want to swap pivot and end
  arr[pivot_index],arr[end] = arr[end],arr[pivot_index]

  return end



def quick_sort(arr,start_pointer,end_pointer):



  if start_pointer < end_pointer:#When start and end pointer are the same, the array is sorted
  #Initiating Hoare partitioning scheme
    partition_index = partition(arr,start_pointer, end_pointer)

  #Now after every pass, we need to return the index of the pivot element's final position (which is basically tne end position). We need to return the end positin index from the partition function. This will create a partition on the original array

  #Now we need to call the quick sort function on the left partition array and the right partition array
    quick_sort(arr,start_pointer,partition_index - 1)
    quick_sort(arr,partition_index+1,end_pointer)


"""*****************************************************************
********************************************************************"""

""" THIS IS A CODE SNIPPET TO USE INSERTION SORT """
""" ---------------------------------------- """

def pivot_comp(arr,pivot_index):

  pivot = arr[pivot_index]
  end_pointer = len(arr) - 1

  while end_pointer > pivot_index:
    if pivot > arr[end_pointer]: #Swapping elements 
      arr[pivot_index],arr[end_pointer] = arr[end_pointer],arr[pivot_index]
      pivot = arr[pivot_index]

    end_pointer-=1

  pivot_index+=1
  return pivot_index  
  
  
#This function will return the new array with the pivot element as the min of the array for the current passed array. Also, returning pivot index since that will be used for the pivot point for the next pass

def insert_sort(arr,pivot_index):
  #We will use recursion here to call the pivot function

  if pivot_index < len(arr)-1:
    partition = pivot_comp(arr,pivot_index)

    insert_sort(arr,partition)
    


if __name__ == '__main__':
  tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
   ]
  for list in tests:
  #  quick_sort(list,0,len(list)-1) #For the first pass of the recursion, we pass the start and end of the original array
    insert_sort(list,0)
    print(f"The sorted list is\n:{list}")