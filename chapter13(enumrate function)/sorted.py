guitars= [
{"model1" : 'famaha f310' ,"price": 8400},
{"model2" : 'faith neptune' ,"price": 100000},
{"model3" : 'faith appolo venus' ,"price": 35000},
{"model4" : 'taylor' ,"price": 450000}
]

sorted_guitars = sorted(guitars, key= lambda d: d["price"],reverse = True)
print(sorted_guitars)