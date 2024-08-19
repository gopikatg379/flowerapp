from django.shortcuts import render, redirect
from flowerapp.models import Flower, AddCart, UserRegister


# Create your views here.

def add_flower(request):
    if request.method == 'POST':
        flower_obj = Flower()
        flower_obj.flower_name = request.POST.get('flower_name')
        flower_obj.flower_price = request.POST.get('flower_price')
        flower_obj.flower_description = request.POST.get('flower_description')
        flower_obj.flower_image = request.POST.get('flower_image')
        flower_obj.save()
        return redirect('/home')
    return render(request, 'add.html')


def home(request):
    if 'user_name' in request.session:
        flower_obj = Flower.objects.all()
        flowers = flower_obj
        if request.method == 'POST':
            search_text = request.POST.get('search_text')
            if search_text:
                flowers = Flower.objects.filter(flower_name__icontains=search_text)

        return render(request, 'home.html', {'data': flowers})
    else:
        return redirect('/')


def add_cart(request, flower_id):
    flower = Flower.objects.get(flower_id=flower_id)
    cart_obj = AddCart(flower=flower)
    cart_obj.save()
    return redirect('/home')


def more(request, flower_id):
    flower = Flower.objects.get(flower_id=flower_id)
    return render(request, 'view.html', {'data': flower})


def view_cart(request):
    cart_obj = AddCart.objects.all()
    print(cart_obj)
    return render(request, 'viewcart.html', {'data': cart_obj})


def remove_cart(request, flower_id):
    cart_obj = AddCart.objects.get(flower_id=flower_id)
    cart_obj.delete()
    return redirect('/viewcart')


def login_user(request):
    data = 'Valid'
    if request.method == "POST":
        name = request.POST.get('user_name')
        pwd = request.POST.get('password')
        user_obj = UserRegister.objects.filter(user_name=name, password=pwd)
        if user_obj:
            print("login successfully")
            request.session['user_name'] = name
            return redirect('/home')
        else:
            print("Invalid username or password")
            data = 'Invalid'
    return render(request, 'login.html', {'msg': data})


def register_user(request):
    if request.method == "POST":
        reg_obj = UserRegister()
        reg_obj.user_name = request.POST.get('user_name')
        reg_obj.email = request.POST.get('email')
        reg_obj.phone_number = request.POST.get('phone_number')
        reg_obj.password = request.POST.get('password')
        reg_obj.image = request.POST.get('image')
        reg_obj.save()
        return redirect('/')
    return render(request, 'register.html')


def user_logout(request):
    return redirect('/')


def myprofile(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user = UserRegister.objects.get(user_name=user_name)
        return render(request, 'myprofile.html', {'data': user})
    else:
        return redirect('/login')


def update_user(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user = UserRegister.objects.get(user_name=user_name)
        if request.METHOD == "POST":
            user = UserRegister.objects.get(user_name=user_name)
            user.user_name = request.POST.get('user_name')
            user.email = request.POST.get('email')
            user.phone_number = request.POST.get('phone_number')
            user.save()
            return render(request, 'update.html')
        return render(request, 'myprofile.html', {'data': user})
    else:
        return redirect('/login')


def edit_image(request):
    global user_obj
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        if request.method == "POST":
            user_obj = UserRegister.objects.get(user_name=user_name)
            user_obj.image = request.POST.get("photo")
            user_obj.save()
            return redirect('/myprofile')
    return render(request, 'editimage.html', {'data': user_obj})


def edit_mobile(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        if request.method == "POST":
            user_obj = UserRegister.objects.get(user_name=user_name)
            user_obj.phone_number = request.POST.get('phone_number')
            user_obj.save()
            return redirect('/myprofile')
    return render(request, 'myprofile.html', {'data': user_obj})


def edit_email(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        if request.method == "POST":
            user_obj = UserRegister.objects.get(user_name=user_name)
            user_obj.email = request.POST.get('email')
            user_obj.save()
            return redirect('/myprofile')
    return render(request, 'myprofile.html', {'data': user_obj})


def edit_name(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        if request.method == "POST":
            user_obj = UserRegister.objects.get(user_name=user_name)
            user_obj.name = request.POST.get('name')
            user_obj.save()
            return redirect('/myprofile')
        return render(request, 'myprofile.html', {'data': user_obj})


def edit_address(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        if request.method == "POST":
            user_obj = UserRegister.objects.get(user_name=user_name)
            user_obj.address = request.POST.get('address')
            user_obj.save()
            return redirect('/myprofile')
        return render(request, 'myprofile.html', {'data': user_obj})


def delete_account(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
        user_obj = UserRegister.objects.get(user_name=user_name)
        user_obj.delete()
        return redirect('/')
