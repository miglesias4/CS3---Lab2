"""
Created and Modified by: Matthew Iglesias
80591632
Dr. Diego Aguirre
T.A. Anitha Nath
"""
from Node import Node ##Import properties and variables from the Node class

##Solution A:  Every time you read a password from the file,
##check (using a loop) if that password has already been added to the linked list.
##That is, you need to traverse the linked list to see if that password has been added already.
##If the password is already in your linked list, update the number of times the password has been seen in the file.
##Otherwise, add a the password to the linked list. 
def sol_A(node, code):
    traverse = node
    while traverse is not None:
        if traverse.password is code:
            traverse.count += 1
            return True
    return False

##Solution B: This is a variation of Solution A.
##Instead of traversing the linked list to check if a password has been seen before,
##we will be using what is called ​a dictionary​
def sol_B(dic, pass_code):
    if pass_code in dic.keys():
        dic[pass_code] += 1 ##Increments count
        return True
    return False
            

##Bubble Sort: 
def is_sorted(x): ##Boolean function for Bubble Sort to determine if the linked list is assorted accordingly
    if x is None or x.next is not None:
        return True
    if x.password > x.next.password:
        return False
    
    is_sorted(x.next)
    return True

def bubble_sort(passcodeBubble):
    passcode = passcodeBubble
    if passcode is not None and passcode.next is None:
        return passcode
    if passcode.password > passcode.next.password:
        temp = passcode.password
        passcode.password = passcode.next.password
        passcode.next.password = temp
        bubble_sort(passcode, passcode.next)
    if not is_sorted(passcode): ##Calls the method is_sorted until the entire linked list is sorted
        passcode = passcode.next
        bubble_sort(passcode, passcode.next)
    return passcode
    ##print('Bubble Sort: ')
    ##print(passcodeBubble)
    

##Merge Sort:
def list_length(length):
    count = 0
    while length is not None:
        count += 1 ##Counter
        length = length.next
    return count
        
def merge_sort(passcodeMerge):
    mergeSort = passcodeMerge
    if passcodeMerge is None or passcodeMerge.next is None:
        return passcodeMerge
    length = list_length(passcodeMerge)
    for i in range(int(length/2) - 1): ##Half length of the total link list 
        mergeSort = mergeSort.next
    right = merge_sort.next
    merge_sort.next = None
    left = passcodeMerge
    
    side_1 = merge_sort(left)##Left side
    side_2 = merge_sort(right)##Right side
    
    complete_sort = None
    if side_1.password > side_2.password:
        complete_sort = side_1
        side_1 = side_1.next
    else:
        complete_sort = side_2
        side_2 = side_2.next
    head = complete_sort
    while side_1 is not None and side_2 is not None:
        if side_1.password > side_2.password:
            complete_sort.next = side_1
            side_1 = side_1.next
        else:
            complete_sort.next = side_2
            side_2 = side_2.next
        complete_sort = complete_sort.next
    
    while side_1 is not None:
        complete_sort.next = side_1
        side_1 = side_1.next
        complete_sort = complete_sort.next
        
    while side_2 is not None:
        complete_sort.next = side_2
        side_2 = side_2.next
        complete_sort = complete_sort.next
        
    return head
    ##print('Merge Sort: ')
    ##print(passcodeMerge)
    
    
##Main 
def main():
    file_read = open("10-million-combos.txt", "r")
    link_list = None ##Creates the linear linked list and set to null
    temp_list = link_list ##To avoid disrupting original list
    d = {}##Dictionary
    try:
        print(file_read.read())
        with open(file_read):
            for file in file_read:
                user_name = file.split("\t")
                user_password = user_name[1]
                if not sol_B(d, user_password):
                    d[user_password] = 1
                if not sol_A(link_list, user_password):
                    link_list = Node(user_password, 1, link_list) ##(password[string], count[int], reference)
    except:
        pass
    mergesort_list = merge_sort(temp_list)
    while mergesort_list is not None:
        print(mergesort_list.password)
        mergesort_list = mergesort_list.next
        
    
    print_bubble = bubble_sort(temp_list)
    while print_bubble is not None:
        print(print_bubble.password)
        print_bubble = print_bubble.next
        
        
    file_read.close()