# ls=[]
# ls=[i  for i in range(1,10) if i%2==0]
# print(ls)
#dictionary comprehensions
# dict1={ i :f"Item {i}" for i in range(1,20) if i%2==0}
#
# print(dict1)
# print("Reversing dictionary")
# dict2={value :key for key,value in dict1.items()}
# print(dict2)

#generator comprehensions
#
# evens=(i for i in range(20) if i%2==0)
# print(evens.__next__())
# for item in evens:
#     print(item)