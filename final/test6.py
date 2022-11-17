bee = [1,0,1,0]
bee1 = ["the","big","cat"]
def removeDups(bee):
    listA = []
    for i in bee:
        if i not in  listA:
            listA.append(i)
           
        
    print(listA)    
        

removeDups(bee)
