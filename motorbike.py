import shelve

with shelve.open('bike2') as bike:
    bike['make']= 'Honda'
    bike['model']= '250 Dream'
    bike['color']= 'Red'
    bike['engin size']= '250'
    for key in bike:
        print(key)
    print(bike['engine size'])
    print(bike['color'])