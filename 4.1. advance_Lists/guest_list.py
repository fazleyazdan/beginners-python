guest_list = ['tariq', 'ali', 'abdullah', 'anees', 'shahid']

def invite_func():
    for guest in guest_list:
        print(f"{guest} you are invited")
        
invite_func()    
not_coming = guest_list.pop(1)
print(f"\nsorry to inform you {not_coming} is not comming")

guest_list.append('adil')

invite_func()

print("\noh sorry but our table is small for the guests")

def pop_guests():
    remove_guests = guest_list.pop()
    print(f"{remove_guests} sorry you are not invited")

pop_guests()
pop_guests()
pop_guests()

print(guest_list)

invite_func()

del (guest_list)


