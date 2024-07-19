def login_required(cart):
    def wrapper(**kwargs) :
        emails=['mona@gmail.com','omar@gmail.com','moustafa@gmail.com']
        password=[12345,678765,8797654]
        if kwargs['email']in emails and if kwargs ['password']in  password:
            print('log in ')
            cart(**kwargs)
        else:
            print("please proceed to creat an account ")  
            print(sign up)  
            cart(**kwargs)
    return wrapper        
 @login_required
def cart( **kwargs):
    x=kwargs['product_name']
    y=kwargs['price']
    z=kwargs['quantity']
    m=kwargs[' sub total']
    print(f'product  is {x} and its price after sale is {y} and the amount of product  about {z} and  the total requirment is {m}')
cart(product_name='mobile',price=40000, tha quatity=1, subtotal=1,email='momom',password=1234555)    