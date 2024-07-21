def my_dec(cart):
    def wrapper(**kwargs) :
        emails=['mona@gmail.com','omar@gmail.com','moustafa@gmail.com']
        if kwargs['email']in emails:
            print('log in ')
            cart(**kwargs)
        else:
            print("sign up")    
            cart(**kwargs)
    return wrapper        
@my_dec
def cart( **kwargs):
    x=kwargs['course_name']
    y=kwargs['price']
    print(f'course is {x} and its price after sale is {y}')
cart(course_name='machin learning',price=300,email='momom',password=1234555)    

