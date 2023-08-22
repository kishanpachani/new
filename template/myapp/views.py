from django.shortcuts import render,redirect
from .forms import signupForm,cartform
from .models import Signup,add,cart
from django .contrib.auth import logout
from django.core.mail import send_mail
from new import settings
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        if request.POST.get('Signup')=='Signup':
            signup_form = signupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                print("User created successfully!")
            #email sending 
                sub="WELCOME"
                msg=f"Dear user !\n your account has been created with us !\n Enjoy our Services.\nif any query , contact on \n+6354222979  "
                from_email=settings.EMAIL_HOST_USER
                to_email=["madhavivekariya777@gmail.com","kp21043@gmail.com"]
                send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
                            
            else:
                print(signup_form.errors)
        elif request.POST.get('Login')=='Login':
            unm=request.POST['Email']
            pas=request.POST['Password']
            user=Signup.objects.filter(Email=unm,password=pas)
            uid = Signup.objects.get(Email=unm)
            if user:
                request.session['user']=unm
                request.session['uid']=uid.id
                print("login successfully")
            else:
                print('error')
    user1 = request.session.get('user')

    return render(request, 'index.html',{'user':user1})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def products(request):
    products = add.objects.all()
    user = request.session.get('uid')
    return render(request,'products.html',{'products':products,'user':user})

def cart_p(request):
    uid = request.session.get('uid')
    cart1 = cart.objects.filter(userid = uid)
    # cart2 = {}
    # cartprice = []
    # for i in cart1:
    #     product1 = add.objects.get(id=i.product_id)
        
    #     cart2[product1.price] = product1.image
    cart2 = {}
    for i in  cart1:
        product1 = add.objects.filter(id=i.product_id)
        for j in product1:
            a = {}
            a['price']=j.price
            a['image']=j.image
            cart2[i.id]=a

        
    print(cart2)
    return render(request,'cart.html',{'products':cart2})

# @login_required(login_url='/')
def addtocart(request):
    if request.method == 'POST':
        cartdata = cartform(request.POST)
        if cartdata.is_valid():
            cartdata.save()
            return redirect('product')
        else:
            print(cartdata.errors)


def Userlogout(request):
    logout(request)
    return redirect('/')
