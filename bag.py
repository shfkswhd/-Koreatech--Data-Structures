def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

myBag = []
insert(myBag, 'apple')
insert(myBag, 'banana')
print("내 가방의 물건 : ",myBag)

insert(myBag, 'orange')
remove(myBag, 'banana')
print("내 가방의 물건 : ",myBag)