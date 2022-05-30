def multiply_and_greet(*args,**kwargs):
    multiply=1
    for  num in args:
     multiply *=num   
    print (multiply)
    
    keys=kwargs.keys()
    if "country" in kwargs:
        print (f"Hello {kwargs['name'] } from {kwargs['country']}")
    elif 'age' in keys:
            year=2022-kwargs['age']
            print (f"Hello {kwargs['name']} you were born in {year}")
    elif 'age' in keys:
            print (f"Hello {kwargs['name']} you were born in {year}") 
    else:
            print (f"Hello Anonymous" )   
                     
