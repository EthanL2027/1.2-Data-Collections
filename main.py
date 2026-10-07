# Lists - a data collection option that is ORDERED and MUTABLE
    # we declare lists using []
def main():
   # declaring an empty list that we can add to later
   my_list = []
   my_other_list = list()

   # declaring a list with items already in it
   my_classes = ["Math", "Post-AP Comp Sci", "English"]


    # using len to find the length of the list
   print(len(my_classes))
   # we can index using the name of the list followed by [x]
   print(my_classes[2])
   print(my_classes[len(my_classes)-1])
   # using a negative index always accesses from right to left
   print(my_classes[-1])
   # using a 0 index always gives us our first element
   print(my_classes[0])

   # we can update ad replace items of our list with indeces
   my_classes[1] = "AP Comp Sci"
   print(my_classes)

   # we can concatenate on to our list elements with += 
   my_classes[1] += " A"
   print(my_classes)

   print(len(my_classes) >= 4)

   #If you search function the index is found
   print(my_classes.index("Math"))

   print("Math" in  my_classes)

   #Adds item at the end
   my_classes.append("Journalism")

   #Adds item to specific spot
   my_classes.insert(3, "Biology")
   print(my_classes)

   # Pop function returns the last item in our list, and removes it from the list
   print(my_classes.pop())

   #we can sort our list 
   print(my_classes.sort())
   print(my_classes)

   numList = [6, -4, 3, 9]
   # sort returns none
   numList.sort()
   print(numList)

   my_classes.sort(reverse=True)
   numList.sort(reverse=True)
   print(my_classes)
   print(numList)

   # makes a copy of your list that is sorted with sorted
   print(sorted(my_classes, reverse=True))

   sorted_classes = sorted(my_classes)
   print(sorted_classes)


   



if __name__ == "__main__":
    main()

