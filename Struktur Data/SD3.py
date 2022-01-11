test_list = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# printing original list 
print("The original list : " + str(test_list))

# declaring magnitude of repetition
K = 2

# using list comprehension
# repeat elements K times
res = [ele for ele in test_list for i in range(K)]

# printing result 
print("The list after adding elements :  " + str(res))