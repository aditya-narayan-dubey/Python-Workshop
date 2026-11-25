#progrqm for nested Dictionary
products={
    1:{"code":1,"name":"printer","price":20000},
    2:{"code":1,"name":"pen drive","price":500},
    3:{"code":1,"name":"monitor","price":10000},  
}
print(products)
products[1]["code"]=101
print(products)
products[3]["price"]=2000
print(products)