#Map in map we pass function as a arguement 
l=[2,3,4,5,6,7]
Sum=list(map(lambda x:x**3,l))
print(Sum)

#Filter in filter we give an condition or can filter unwanted
greaterThanFiveOnly=list(filter(lambda y:y>=5,l))
print(greaterThanFiveOnly)