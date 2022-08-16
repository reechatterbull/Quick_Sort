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
    while arr[start] <= pivot:
      start +=1 #move right

  #Now we move end pointer to where the value is < 11
    while arr[end] > pivot:
      end-=1 #move left

  #Now swap the values of the start and end pointers if start pointer is still to the left of the end pointer. If end pointer has moved to the left of the start pointer, we terminate the process on this pass
    if start < end:
      arr[start],arr[end] = arr[end],arr[start]

  #Once the above condition is met, we want to swap pivot and end
  arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
    



def quick_sort(arr,start_pointer,end_pointer):
  #Initiating Hoare partitioning scheme
  partition(arr,start_pointer, end_pointer)

  
  







if __name__ == '__main__':
  list = [11,9,29,7,2,15,28]
  quick_sort(list,0,len(list)-1) #For the first pass of the recursion, we pass the start and end of the original array
  print(list)