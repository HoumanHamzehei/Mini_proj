from function import product_print, product_create, product_update, product_delete
from function import courier_list , courier_create , courier_update , courier_delete
from function import order_list , order_create 


print("Welcome to the Houman Restaurant")

menu_option = int(input(" exit(0), product_menu_option(1), courier_list(2) , order(3) : "))

num = int(input(" press 1 if you want to print menu, prest 2 if you want to create, press 3 to update, press 4 to remove: "))

while True:

    if menu_option ==0:
        exit()

    elif menu_option == 1:
        while True:
            if num == 0:
                  break
            elif  num == 1:
                product_print()
            elif num == 2:
                product_create()
            elif num == 3:
                product_update()
            elif num == 4:
              product_delete()

    elif menu_option == 2:
        while True:
            if num == 0:
                break
            elif num == 1 :
                courier_list()
            elif num == 2 :
                courier_create
            elif num == 3 :
                courier_update()
            elif num == 4 :
                courier_delete
    elif menu_option == 3 :

        if num == 0 :
            break
        elif num == 1 :
            order_list()
        elif num == 2 :
            order_create()
        elif num == 3 :
            order_update_status()
        elif num == 4 :
            order_update_order()
        elif num == 5 :
            order_delete
            