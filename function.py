import json
#product
def product_print():
    with open("products_list.json") as file:
        products=json.load(file)
        print(products)



def product_create():
    with open("products_list.json") as file:
        products=json.load(file)
        print(products)
        new_product=input("new product : ")
        new_number=input("new number : ")
        products[new_product]=int(new_number)
        print(products)
    with open("produts_list.json" , "w") as file:
        json.dump(products, file, indent=4)




def product_update():
    with open("products_list.json") as file:
        products=json.load(file)
        print(products)
        new_product=input("new product : ")
        new_number=input("new number : ")
        products[new_product]=int(new_number) 
        delete_products=input("delete products: ")
        del products[delete_products]
        print(products)
    with open("produts_list.json" , "w") as file:
        json.dump(products, file, indent=4)


def product_delete():
    with open("products_list.json") as file:
        products=json.load(file)
        print(products)
        delete_products=input("delete products: ")
        del products[delete_products]
        print(products)
    with open("products_list.json" , "w") as file:
        json.dump(products, file, indent=4)
#courier
def courier_list():
    with open("courier_list.json") as file:
        couriers=json.load(file)
        print(couriers)
        
def courier_create():
    with open("courier_list.json") as file:
        couriers=json.load(file)
        print(couriers)
        new_number=input("new number : ")
        new_courier=input("new courier : ")
        couriers[new_courier]=int[new_number]
        print(couriers)
        with open("courier_create.son" , "w") as file:
            json.dump(couriers, file, indent=4)

def courier_update():
    with open("courier_list.json") as file:
        couriers=json.load(file)
        print(couriers)
        new_number=int("new number : ")
        new_courier=int("new_courier : ")
        couriers[new_courier]=int[new_number]
        delete_couriers=input("delete courier :")
        del couriers[delete_couriers]
        print (couriers)
    with open("courier_list.json" , "w") as file:
        json.dump(couriers, file, indent=4)        


def courier_delete():
    with open("courier_list.json") as file:
        couriers=json.load(file)
        print(couriers)
        delete_couriers=input("new number :")
        del couriers[delete_couriers]
        print (couriers)
        json.dump(couriers, file, indent= 4)
#order


def order_list():
    with open("order_list.json") as file:
        orders=json.load(file)
        print(orders)



def order_create():
    with open("order_list.json") as file:
        orders=json.load(file)
        print(orders)
        customer_name=input("new customer name : ")
        customer_adress=input("new customer adress : ")
        customer_phone=input("new phone : ")



