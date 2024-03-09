""" Stephen McGowan ENAE 450 HW2 - Merge sorting"""

import random

class MergeSort:
    def randomGen(self, num, max):
        """
        Generates a list of random non-negative integers.
        Parameters:
            num(int): Number of elements in the list.
            max(int): Maximum value for the random integers.
        Returns:
            list: A list of random integers between 0 and max with a length of num
        """
        return [random.randint(0, max) for _ in range(num)]
    

    def merge(self,list1,list2):
        list3 = list1 + list2
        return list3
     
    def mergeSort(self,list):
        """
        merge sort breaks down list into smaller more manageable list to quickly 
        compare and replace the values in ascending order 
        Parameters
        ----------
        alist : list(int)
        list of elements to sort
        Returns
        -------
        list
        sorted list in ascending order
        """
    
        if len(list)>1:

            #finding the middle of the list, and setting into two halves
            mid = len(list)//2
            lefthalf = list[:mid]
            righthalf = list[mid:]

            #sort both halves, how do we call the function we are creating?
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            #keep track of iterations
            i=0
            j=0
            k=0
            
            #put data in temporary list
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j]:
                    list[k]=lefthalf[i]
                    i=i+1
                else:
                    list[k]=righthalf[j]
                    j=j+1
                k=k+1
                #last check
            while i < len(lefthalf):
                list[k]=lefthalf[i]
                i=i+1
                k=k+1
            while j < len(righthalf):
                list[k]=righthalf[j]
                j=j+1
                k=k+1
            
        return(list)
 

"""Prompt Answers"""
if __name__ == '__main__':
 m = MergeSort() 

 
# genrate two random list of 50 numbers up to 1000
lista = m.randomGen(50,1000)
listb = m.randomGen(50,1000)
listc = m.merge(lista,listb)

# print first two list unsorted
print('\n List 1: \n\n', lista)
print('\n List 2: \n\n', listb)

# sort list
listd = m.mergeSort(listc)

# print sorted list
print('\n Sorted List: \n\n', listd)
