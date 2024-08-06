# extract 'firstName' of accounting only in sales.


from munch import Munch

sales = { 
    "accounting" : [   
                       { "firstName" : "John",  
                         "lastName"  : "Doe",
                         "age"       : 23 },
  
                       { "firstName" : "Mary",  
                         "lastName"  : "Smith",
                          "age"      : 32 }
                   ],                            
    "sales"      : [ 
                       { "firstName" : "Sally", 
                         "lastName"  : "Green",
                          "age"      : 27 }
                       
                 ]
}


# split_sales = Munch(sales)                  OR

accounting_names = sales["accounting"]

for names in accounting_names:
    for k,v in names.items():
        if k == 'firstName':
            print(v)
        else:
            continue
        

