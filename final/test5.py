
bee = [{ 'name' : "John", 'age' : 21 , 'budget' : 23000} ,{ 'name' : "Steve", 'age' : 32, 'budget' : 40000},{ 'name' : "Martin", 'age' : 16, 'budget' : 2700}]
def getBudgets(bee):
    dog = 0
    for i in bee:
        for j in i.keys():
            
            if j == "budget":
                cat = i[j]
                dog += cat
    print(dog)
                
        
    





getBudgets(bee)
