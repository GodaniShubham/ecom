from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
# Create your views here.

# ====================> Index
def index(request):
    return HttpResponse("This is my second or third django")

# ====================> Home
def home(request):
    if 'email' in request.session:
        # a = Userregister.objects.all() ##This is Only For Get DATA
        b = Userregister.objects.get(email = request.session['email'])
        # a = Userregister()
        if request.method == 'POST':
            b.name = request.POST['name']
            b.email = request.POST['email']
            b.mobile = request.POST['mob']
            b.address = request.POST['add']
            b.password = request.POST['password']
            # b.image = request.FILES['image']
            if request.FILES:
                b.image = request.FILES['image']
            b.save()
        return render(request,'index.html',{'session':b})
    else:
        a = Userregister.objects.all() 
        return render(request,'index.html',{'user':a})
        
# ====================> Register   
def register(request):
    a = Userregister() ## This is Only For THROW Data into database
    if request.method == 'POST' and request.FILES['image']:
        a.name = request.POST['name']
        a.email = request.POST['email']
        a.mobile = request.POST['mob']
        a.address = request.POST['add']
        a.password = request.POST['password']
        a.image = request.FILES['image']
        b = Userregister.objects.filter(email = request.POST['email'])
        c = request.POST['password'] == request.POST['cpassword']
        if len(b)>0 :
            return render(request,'register.html',{'email_alert':'Email Already exists!!'})
        if not c:
            return render(request,'register.html',{'password_alert':'Please enter password and confirm password same'})
        else:
            a.save()
            send_mail(
                'Hiii' + a.name,
                'Thank you for Joining us',
                'godanishubham30@gmail.com',
                [a.email],
                fail_silently=False
            )
        # for i in b:
        #     if i.email == a.email:
        #         return HttpResponse("Email address already exists.")
        #         break
        # a.save()
        return redirect('home')
    else:
        return render(request,'register.html')

# ====================> Login
def login(request):
    if request.method == 'POST':
        a = Userregister.objects.get(email = request.POST['mail'])
        if a.password == request.POST['Password']:
            request.session['email'] = a.email
            request.session['password'] = a.password
            request.session['id'] = a.id
            # print(request.session['email'],"\n",request.session['password'])
            # return redirect('private')
            return redirect('main')
        elif a.password != request.POST['Password']:
            return render(request,'login.html',{'invalid':'Invalid Password'})
        else:
            return render(request,'login.html',{'invalidemail':'Invalid eamil'})
    else:
        return render(request,'login.html')

# ====================> Logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('main')
    elif 'wemail' in request.session:
        del request.session['wemail']
        return redirect('main')
    else:
        return render(request,'login.html')

# ====================> User 
def user(request):
    if 'email' in request.session:
        b = Userregister.objects.get(email = request.session['email'])
        return render(request,'user.html',{'session':b})
    
# ====================> main
def main(request):
    if 'email' in request.session:
        a = Categ.objects.all()
        b = Userregister.objects.get(email = request.session['email'])
        return render(request,'main.html',{'cate':a,'session':b})
    elif 'wemail' in request.session:
        a = Categ.objects.all()
        b = wandersignup.objects.get(email = request.session['wemail'])
        return render(request,'main.html',{'cate':a,'session':b})
    else:
        a = Categ.objects.all()
        return render(request,'main.html',{'cate':a})

# ====================> product
def product(request,id):
    if 'email' in request.session:
        cat = Categ.objects.get(pk = id)
        pro = Product.objects.filter(Product_categ = cat)
        b = Userregister.objects.get(email = request.session['email'])
        return render(request,'product.html',{'pro':pro,'session':b})
    elif 'wemail' in request.session:
        cat = Categ.objects.get(pk = id)
        pro = Product.objects.filter(Product_categ = cat)
        b = wandersignup.objects.get(email = request.session['wemail'])
        return render(request,'product.html',{'pro':pro,'session':b})
# ====================> Product_detail
def product_details(request,id):
    if 'email' in request.session:
        ac = Product.objects.get(id = id)
        b = Userregister.objects.get(email = request.session['email'])
        # c = wandersignup.objects.get(email = request.session['wemail'])
        if request.method == 'POST':
            cart = Addcart()
            cart.orderid = '0'
            cart.productid = ac.id
            cart.userid = request.session['id']
            if request.POST['qty']:
                cart.quntity = request.POST['qty']
            else:
                cart.quntity = 1
            cart.price = ac.Product_price
            cart.tprice = int(cart.price) * int(cart.quntity)
            
            addcart = Addcart.objects.filter(userid = request.session['id']) & Addcart.objects.filter(productid = ac.id)
            # qut = int(request.POST['qty']) <= int(ac.Product_quntity)
            if int(ac.Product_quntity) > 0:
                # print(1111111111111111111111)
                if addcart:
                    # print(2222222222222222222)
                    return render(request,'productdetails.html',{'pro': ac,'session':b,'alreadycart':'Already in cart'})
                else:
                    if int(ac.Product_quntity) < int(request.POST['qty']) :
                    # print(33333333333333333333)
                        return render(request,'productdetails.html',{'pro': ac,'session':b,'more':'You are enter more than of quntity'})
                    
                    # if int(ac.Product_quntity) < int(request.POST['qty']):
                    #     print(6666666666666666)
                    else:
                        cart.save()
                        ac.Product_quntity = int(ac.Product_quntity) - int(cart.quntity)
                        ac.save()
                        return redirect('cart')
            else:
                return render(request,'productdetails.html',{'pro': ac,'session':b,'stock':'out of stock'})

        return render(request,'productdetails.html',{'pro': ac,'session':b})
    elif 'wemail' in request.session:
        return render(request,'productdetails.html',{'pro': ac,'session':b,'wander':'You are wander you can not add cart '})
    #     ac = Product.objects.get(id = id)
    #     b = wandersignup.objects.get(email = request.session['wemail'])
    #     # c = wandersignup.objects.get(email = request.session['wemail'])
    #     if request.method == 'POST':
    #         cart = Addcart()
    #         cart.orderid = '0'
    #         cart.productid = ac.id
    #         cart.userid = request.session['id']
    #         cart.quntity = request.POST['qty']
    #         cart.price = ac.Product_price
    #         cart.tprice = int(cart.price) * int(cart.quntity)
    #         cart.save()
    #         return render(request,'productdetails.html',{'pro': ac,'session':b})
    #     else:
    #         return render(request,'productdetails.html',{'pro': ac})
    else:
        ac = Product.objects.get(id = id)
        return render(request,'productdetails.html',{'pro': ac})

# ====================> wander Signup 
def Wandersignup(request):
    if request.method == 'POST':
        a = wandersignup()
        a.name = request.POST['name']
        a.email = request.POST['email']
        a.mobile = request.POST['mob']
        a.address = request.POST['add']
        a.password = request.POST['password']
        a.image = request.FILES['image']
        b = wandersignup.objects.filter(email = request.POST['email'])
        c = request.POST['password'] == request.POST['cpassword']
        if len(b)>0 :
            return render(request,'register.html',{'email_alert':'Email Already exists!!'})
        if not c:
            return render(request,'register.html',{'password_alert':'Please enter password and confirm password same'})
        else:
            a.save()
        #     send_mail(
        #         'Hiii' + a.name,
        #         'Thank you for Joining us You are now Seller',
        #         'godanishubham30@gmail.com',
        #         [a.email],
        #         fail_silently=False
        #     )
        return redirect(main)
    return render(request,'seller/signupseller.html')

# ====================> wander login 
def wanderlogin(request):
    if request.method == 'POST':
        a = wandersignup.objects.get(email = request.POST['mail'])
        if a.password == request.POST['Password']:
            request.session['wemail'] = a.email
            # request.session['wpassword'] = a.password
            request.session['wid'] = a.id
            # print(request.session['email'],"\n",request.session['password'])
            # return redirect('private')
            return redirect('main')
        elif a.password != request.POST['Password']:
            return render(request,'seller/wanderlogin.html',{'invalid':'Invalid Password'})
        else:
            return render(request,'seller/wanderlogin.html',{'invalidemail':'Invalid eamil'})
    else:
        return render(request,'seller/wanderlogin.html')

# ====================> wander logout 
def wanderlogout(request):
    if 'email' in request.session:
        del request.session['wemail']
        return redirect('main')
    else:
        return render(request,'login.html')
    
# ====================> Add Product
def addproduct(request):
    if 'wemail' in request.session:
        b = wandersignup.objects.get(email = request.session['wemail'])
        a = Categ.objects.all()
        pro = Product()
        if request.method == 'POST' and request.FILES['image']:
            cate = request.POST['catego']
            categ = Categ.objects.get(id = cate)
            pro.Product_name = request.POST['proname']
            pro.Product_price = request.POST['price']
            pro.Product_quntity = request.POST['qty']
            pro.Product_brand = request.POST['brand']
            pro.Product_categ = categ
            pro.Product_disc = request.POST['disc']
            pro.Product_image = request.FILES['image']
            pro.save()
        return render(request,'seller/addproduct.html',{'session':b,'cat':a,'pro':pro})
    else:
        return redirect('wanderlogin')

def addcate(request):
    if 'wemail' in request.session:
        if request.method == 'POST':
            a = Categ()
            a.cat_name = request.POST['cate_name']
            a.image = request.FILES['cate_image']
            b = Categ.objects.filter(cat_name = request.POST['cate_name'])
            
            if len(b)>0:
                return render(request,'seller/addcate.html',{'invalid_cat':'Already Exists'})
            else:
                a.save()
                return render(request,'seller/addcate.html')
        else:
            return render(request,'seller/addcate.html')
    else:
        return render(request,'seller/addcate.html')
    
def cart(request):
    if 'email' in request.session:
        # ac = Product.objects.get(id = id)
        b = Userregister.objects.get(email = request.session['email'])
        c = Addcart.objects.filter(userid = b.pk)
        pro = []
        total = 0
        for i in c:
            ac = Product.objects.get(pk = i.productid)
            pimage = ac.Product_image
            pdisc = ac.Product_disc
            ptp = i.tprice
            pqty = i.quntity
            pprice = i.price
            pdic = {'id':i.productid,'pimage':pimage,'pdisc':pdisc,'ptp':ptp,'pqty':pqty,'pprice':pprice}
            pro.append(pdic)
            total += int(i.tprice)
            # print(pro)

        return render(request,'cart.html',{'session':b,'cartpro':pro,'total':total})
    else:
        return redirect('login')

def pluspro(request,id):
    if 'email' in request.session:

        # c = Addcart.objects.filter(userid = request.session['id'])
        pro = Addcart.objects.get(productid = id,userid = request.session['id'])
        pro.quntity = int(pro.quntity) + 1
        tprice = int(pro.price) * int(pro.quntity)
        pro.tprice = tprice
        pro.save()
        prod = Product.objects.get(id = id)
        prod.Product_quntity = int(prod.Product_quntity) - 1
        prod.save()
        return redirect('cart')
    else:
        return redirect('cart')
def subpro(request,id):
    if 'email' in request.session:

        # c = Addcart.objects.filter(userid = request.session['id'])
        pro = Addcart.objects.get(productid = id,userid = request.session['id'])
        pro.quntity = int(pro.quntity) - 1
        tprice = int(pro.price) * int(pro.quntity)
        pro.tprice = tprice
        if pro.quntity <= 0 :
            return redirect('remove',id)
        else:
            pro.save()
            prod = Product.objects.get(id = id)
            prod.Product_quntity = int(prod.Product_quntity) + 1
            prod.save()
            return redirect('cart')
    else:
        return redirect('cart')
    
def remove(request,id):
    if 'email' in request.session:
        pro = Addcart.objects.get(productid = id,userid = request.session['id'])
        pro.delete()
        # pro.save()
        return redirect('cart')
    else:
        return redirect('cart')

def removeall(request):
    if 'email' in request.session:
        pro = Addcart.objects.filter(userid = request.session['id'])
        pro.delete()
        # pro.save()
        return redirect('cart')
    else:
        return redirect('cart')
def cotp(request):
    if request.method == 'POST':
        a = Userregister.objects.get(email = request.session['email'])
        if request.POST['otp'] == a.otp:
            return HttpResponse('Your Otp Is confirm')
        else:
            return HttpResponse('Your Enter Wrong Otp')
    else:
        return render(request,'cotp.html')