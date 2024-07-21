
def login_required(cart):
    def wrapper(**kwargs) :
        emails=['mona@gmail.com','omar@gmail.com','moustafa@gmail.com']
        product_name=kwargs['product_name']
        price=kwargs['price']
        quantity=kwargs['quantity']
        sub_total=kwargs['sub_total'] 
        if kwargs['email']in emails:
            print('log in ')
            cart(product_name=product_name,price=price,quantity=quantity,sub_total=sub_total)
        else:
            print("sign up")    
            cart(product_name=product_name,price=price,quantity=quantity,sub_total=sub_total)
    return wrapper        
@login_required
def cart( **kwargs):
    product_name=kwargs['product_name']
    price=kwargs['price']
    quantity=kwargs['quantity']
    sub_total=kwargs['sub_total']
    print(f'product is : {product_name} and its price after sale is:  {price} the number of this product is : {quantity} the  total number of required order is :{sub_total}')
cart(product_name='lap top',price=3000,quantity=1,sub_total=1,email='momom',password=1234555)    