from django.shortcuts import render, redirect, HttpResponse
from .forms import signupForm, cartform, updatecart1
from .models import Signup, add, cart
from django.contrib.auth import logout
from django.core.mail import send_mail
from new import settings
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == "POST":
        if request.POST.get("Signup") == "Signup":
            signup_form = signupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                print("User created successfully!")
                # email sending
                sub = "WELCOME"
                msg = f"Dear user !\n your account has been created with us !\n Enjoy our Services.\nif any query , contact on \n+6354222979  "
                from_email = settings.EMAIL_HOST_USER
                to_email = ["kp21043@gmail.com"]
                send_mail(
                    subject=sub,
                    message=msg,
                    from_email=from_email,
                    recipient_list=to_email,
                )

            else:
                print(signup_form.errors)
        elif request.POST.get("Login") == "Login":
            unm = request.POST["Email"]
            pas = request.POST["Password"]
            user = Signup.objects.filter(Email=unm, password=pas)
            uid = Signup.objects.get(Email=unm)
            if user:
                request.session["user"] = unm
                request.session["uid"] = uid.id
                print("login successfully")
            else:
                print("error")
    user1 = request.session.get("user")

    return render(request, "index.html", {"user": user1})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def products(request):
    products = add.objects.all()
    user = request.session.get("uid")
    return render(request, "products.html", {"products": products, "user": user})


def cart_p(request):
    uid = request.session.get("uid")
    cart1 = cart.objects.filter(userid=uid)
    count = cart1.count
    cart2 = {}
    subtotal = []
    for o in cart1:
        subtotal.append(o.price)
    total = sum(subtotal)
    for i in cart1:
        product1 = add.objects.filter(id=i.product_id)
        for j in product1:
            a = {}
            a["price"] = i.price
            a["p"] = j.price
            a["image"] = j.image
            a["contity"] = i.contity
            a["id"] = j.id
            # for i in cart1:
            cart2[i.id] = a
    return render(
        request,
        "cart.html",
        {"products": cart2, "uid": uid, "total": total, "count": count},
    )


# @login_required(login_url='/')
def addtocart(request):
    if request.method == "POST":
        pid = request.POST["product_id"]
        chekccontity = cart.objects.filter(
            userid=request.session.get("uid"), product_id=pid
        )
        if chekccontity:
            pid = request.POST["product_id"]
            c = cart.objects.get(userid=request.session.get("uid"), product_id=pid)
            if c:
                c1 = cart.objects.get(userid=request.session.get("uid"), product_id=pid)
                c1.contity = c1.contity + 1
                c1.price = c1.price + int(request.POST["price"])
                c1.save()
                return redirect("product")
        else:
            cartdata = cartform(request.POST)
            if cartdata.is_valid():
                cartdata.save()
                return redirect("product")
            else:
                print(cartdata.errors)


def editcontity(request):
    if request.method == "POST":
        pid = request.POST["product_id"]
        c = cart.objects.get(userid=request.session.get("uid"), product_id=pid)
        if c:
            if int(request.POST["contitycart"]) == 0:
                c1 = cart.objects.get(userid=request.session.get("uid"), product_id=pid)
                c1.delete()
            else:
                c1 = cart.objects.get(userid=request.session.get("uid"), product_id=pid)
                c1.contity = request.POST["contitycart"]
                pri = add.objects.get(id=pid)
                c1.price = pri.price * int(request.POST["contitycart"])
                c1.save()
            return redirect("product")


def Userlogout(request):
    logout(request)
    return redirect("/")
