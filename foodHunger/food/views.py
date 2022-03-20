from email import message
from pickle import FALSE, TRUE
import secrets
import string

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth 
from datetime import date
from food.models import HotelDetails, foodDetails, userFoodRegistration
# Create your views here.
def food(request):
    if request.method=="POST":
        print('hi')
        return redirect("userRegistration")
    else:
        if User.is_authenticated:
            registrationNumber = request.user.username
            hotel = HotelDetails.objects.all()
            print(generate_alphanum_string(5))
            return render(request,'home.html',{'hotels':hotel})
        else:
            return render(request,'home.html')

def foodHome(request):
    if request.method=="POST":
        print('hi')
        return redirect("userRegistration")
    else:
        if User.is_authenticated:
            registrationNumber = request.user.username
            hotel = HotelDetails.objects.all()
            print(generate_alphanum_string(5))
            return render(request,'home.html',{'hotels':hotel})
        else:
            return render(request,'home.html')

def generate_alphanum_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    print("Cryptic Random string of length", length, "is:", crypt_rand_string)
    return crypt_rand_string

def userRegistration(request):
    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        phoneNumber = request.POST['phoneNumber']
        registrationNumber = request.POST['registrationNumber']
        hotel = request.POST['hotel']
        today = date.today()
        print("Today date is: ", today)
        food = foodDetails.objects.filter(registrationNumber = registrationNumber) and foodDetails.objects.filter(date = today)
        for f in food:
            print(f.foodBoxes)
            if f.registrationNumber == registrationNumber:
                fb = f.foodBoxes
        print(food)
        if food is not None:
            No_of_food_boxes = fb
            print("No_of_food_boxes : ", No_of_food_boxes)
            foodUser = userFoodRegistration.objects.filter(registrationNumber = registrationNumber) and userFoodRegistration.objects.filter(date = today)
            print('len of foodUser : ',print(len(foodUser)))
            count = 1
            nf = userFoodRegistration.objects.all()
            fo = foodDetails.objects.all()
            # for ffo in fo:
            for nfo in nf:
                if (nfo.registrationNumber == registrationNumber) and (nfo.date == today):
                    count = count+1
            # for fu in foodUser:
            #     if fu.registrationNumber == registrationNumber:
            #         county = fu.status
            print(count)
            if count > No_of_food_boxes:
                message = "Food Boxes are unavailable for selected hotel"
                flag = 0
                H = HotelDetails.objects.all()
                return render(request,'userRegistration.html',{'hotel':H,'message':message,'name':name,'flag':flag})
            else:
                alphaString = generate_alphanum_string(4)
                f = userFoodRegistration(registrationNumber = registrationNumber,hotel=hotel,name = name,country=country,phoneNumber=phoneNumber,date = today,alphaString=alphaString)
                f.save()
                flag = 1
                message = "You are Registered Successfully"
                H = HotelDetails.objects.all()
                return render(request,'userRegistration.html',{'hotel':H,'message':message,'name':name,'flag':flag,'alphaString':alphaString})
        else:
            flag = 3
            message = "Food Boxes are not available"
            H = HotelDetails.objects.all()
            return render(request,'userRegistration.html',{'hotel':H,'flag':flag})
    else:
        flag = 3
        H = HotelDetails.objects.all()
        return render(request,'userRegistration.html',{'hotel':H,'flag':flag})

def registerHotel(request):
    print('1')
    print(request.method)
    print('2')
    if request.method == 'POST':
        print('Inside Register Hotel function')
        hotel = request.POST['Hotel']
        registrationNumber = request.POST['registrationNumber']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
        address = request.POST['address']
        zipCode = request.POST['zip']
        city = request.POST['city']
        # country = request.POST['country']
        countryCode = request.POST['countryCode']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        image = request.FILES['image']
        website = request.POST['website']
        star = request.POST['type']
        print('')

        if(password == confirmPassword):
            if(HotelDetails.objects.filter(registrationNumber=registrationNumber).exists()):
                messages.info(request,'Hotel is already registered..!!')
                return redirect('hotelRegistration')
            else:
                h = HotelDetails(hotel=hotel,password=password,image=image,address=address,zipCode=zipCode,city=city,countryCode=countryCode,phoneNumber=phoneNumber,email=email,registrationNumber=registrationNumber,website=website,star=star)
                h.save()
                user = User.objects.create_user(username=registrationNumber,password=password,first_name=hotel,email=email)
                user.save()
                messages.info(request,'Hotel is registered..!!')
                return redirect('hotelRegistration')
        else:
            messages.info(request,'Password is not matching..!!')
            return redirect('hotelRegistration')
    else:
        return render(request,'hotelregistration.html')

def userLogin(request):
    # print('1')
    # print(request.method)
    # print('2')
    if request.method == "POST":
        registrationNumber = request.POST['registrationNumber']
        password = request.POST['password']

        user = auth.authenticate(username = registrationNumber, password = password)
        # print('user is:',user)
        if user is not None:
            auth.login(request,user)
            # H = HotelDetails.objects.get(registrationNumber = registrationNumber)
            # hotel = H.hotel
            # print(hotel)
            # food_Details = foodDetails.objects.filter(registrationNumber = request.user.username)
            # food = food_Details[::-1]
            # flag = 0
            # return render(request,'dashboard.html',{'Hotel':H,'food':food,'flag':flag})
            return redirect('dashboard')
        else:
            message = 'Hotel is not registered with us or Password is Wrong!! Please check the credentials'
            return render(request,'login.html',{'message':message})
    else:
        return render(request,'login.html')

# def dashboardPost(request):
#         H = HotelDetails.objects.get(registrationNumber = User.username)
#         name = H.hotel
#         print(name)
#         return render(request,'dashboard.html',{'Hotel':H})

def dashboardDetails(request):
    if request.method=='POST':
        foodBoxes = request.POST['foodBoxes']
        food = request.POST['food']
        H = HotelDetails.objects.get(registrationNumber = request.user.username)
        # hotelName = H.name
        today = date.today()
        print("Today date is: ", today)
        F = foodDetails(registrationNumber = request.user.username,hotel = request.user.first_name,foodBoxes = foodBoxes,food=food,date=today)
        F.save()
        flag = 1
        count = 0
        food_Details = foodDetails.objects.filter(registrationNumber = request.user.username)
        for f in food_Details:
            if f.date == today:
                count = 1
                break
        food = food_Details[::-1]
        return render(request,'dashboard.html',{'Hotel':H,'flag':flag,'food':food,'count':count}) 
    else:    
        H = HotelDetails.objects.get(registrationNumber = request.user.username)
        name = H.hotel
        print(H.image.url)
        today = date.today()
        print("Today date is: ", today)
        flag = 0
        count = 0
        food_Details = foodDetails.objects.filter(registrationNumber = request.user.username)
        for f in food_Details:
            if f.date == today:
                count = 1
                break
        food = food_Details[::-1]
        # for f in food:
        #     print(f.foodBoxes)
        return render(request,'dashboard.html',{'Hotel':H,'flag':flag,'food':food,'count':count})


def distributeFood(request):
    if request.method == "POST":
        verifyText = request.POST['verifyText']
        if(userFoodRegistration.objects.filter(alphaString=verifyText).exists()):
            message = "Registered User is Verified"
            ufr = userFoodRegistration.objects.filter(alphaString=verifyText).update(status=1)
            # ufr.save()
        else:
            message = "User is not registered"
        registrationNumber = request.user.username
        print(registrationNumber)
        userFoodReg = userFoodRegistration.objects.filter(registrationNumber=registrationNumber)
        hotel = HotelDetails.objects.get(registrationNumber=registrationNumber)
        food = foodDetails.objects.filter(registrationNumber=registrationNumber)
        print(hotel.hotel)
        today = date.today()
        print(today)
        for f in food:
                # print(f.name)
                # print(f.date)
            if f.date == today:
                print(f.date)
                print(f.foodBoxes)
                foodDet = f.foodBoxes
                break
        flag = 1
        return render(request,'distributeFood.html',{'userFoodReg':userFoodReg,'hotel':hotel,'foodDet':foodDet,'message':message,'flag':flag})    

    else:
        registrationNumber = request.user.username
        print(registrationNumber)
        userFoodReg = userFoodRegistration.objects.filter(registrationNumber=registrationNumber)
        hotel = HotelDetails.objects.get(registrationNumber=registrationNumber)
        food = foodDetails.objects.filter(registrationNumber=registrationNumber)
        print(hotel.hotel)
        today = date.today()
        print(today)
        for f in food:
            if f.date == today:
                print(f.date)
                print(f.foodBoxes)
                foodDet = f.foodBoxes
                break
        flag = 0
        return render(request,'distributeFood.html',{'userFoodReg':userFoodReg,'hotel':hotel,'foodDet':foodDet,'flag':flag})

def hotels(request):
    if request.method=="POST":
        flag = 1
        country = request.POST['country']
        H = HotelDetails.objects.all()
        fh = foodDetails.objects.all()
        hotel = []
        food = []
        count = 0
        for h in H:
            for f in fh:
                if (h.country).lower() == country.lower():
                    today = date.today()
                    print(today)
                    print(h.registrationNumber)
                    if (h.registrationNumber == f.registrationNumber):
                        if f.date == today:
                            print(h.hotel)
                            hotel = h
                            food = f
                            count += 1
        print(hotel)
        if(count != 0):
            print(count)
            if count == 1:
                flag = 3
                return render(request,'hotels.html',{'flag':flag,'hotels':hotel,'food':food})
            else:
                print('Hi')
                return render(request,'hotels.html',{'flag':flag,'hotels':hotel,'food':food})
        else:
            message = "There is no any hotel available in this country"
            print(message)
            flag = 2
            return render(request,'hotels.html',{'flag':flag,'message':message})
    else:
        flag = 0
        return render(request,'hotels.html',{'flag':flag})

def hotelSummary(request,registrationNumber):
    if request.method == "POST":
        return redirect("userRegistration")
    else:
        print(registrationNumber)
        H = HotelDetails.objects.get(registrationNumber=registrationNumber)
        #print(H.image.url)
        today = date.today()
        F = foodDetails.objects.filter(registrationNumber=registrationNumber)
        print(F)
        food = []
        flag = 0
        count = 0
        for f in F:
            if f.date == today:
                food = f
                print(food.date)
                print(food.foodBoxes)
                print(food.food)
                flag = 1
                count = count + 1
            
        if count == 0:
            flag = 0
            return render(request,'hotelSummary.html',{'Hotel':H,'flag': flag})   
        print(food)
        return render(request,'hotelSummary.html',{'Hotel':H,'food':food,'flag': flag})

def logout(request):
    auth.logout(request)
    return redirect('login')

