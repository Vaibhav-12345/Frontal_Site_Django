from django.shortcuts import render,redirect

from home.models import contactform,carousel,defaultcarousel,servicecard

# from .forms import *
# or

# message show by djnago 
from django.contrib import messages

# Auth
from django.contrib.auth.models import User
# login or logout import 
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout


from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    a=carousel.objects.all()

    b=defaultcarousel.objects.all()
    
    c=servicecard.objects.all()

    slider={
        'data':a ,
        'data1':b,
        'data2':c,
    }

 

    return render(request,'home/index.html',slider)

@login_required
def resume(request):
    return render(request,'home/resume.html')


# error 409
def error(request):
    return render(request,'home/error.html')

    

@login_required
def contact(request):

    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_msg = request.POST.get('msg')
                      

                    #   notes model me dekho jo jo sequence me wahie dalo  name=username
        a=contactform(name=user_name,email=user_email,message=user_msg)
        a.save()
    
        # print(name,email,msg)
        return redirect('/')

    
#    now get show the data 
    allpost=contactform.objects.all()[::-1]
    context={'data':allpost}
    # print(allpost)

    return render(request,'home/contact.html',context)



@login_required
def about(request):

    return render(request,'home/about.html')






# Authentication system in django

def login(request):
    # if user is already login but it acces login page it stop the 
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        number=request.POST['number']
        # email=request.POST['email']
        password=request.POST['password']

        myuser=authenticate(request,username=number,password=password)
        # myuser=authenticate(request,email=email,password=password)
        
        
        # None return nhi hoga
        # print(myuser) notes -:  password or email any one incorect they give me None
        print(myuser)
        if myuser is not None:
            auth_login(request,myuser)
            messages.success(request," Succesfull login")
            return redirect('/')

        else:
            messages.error(request,'Something is wrong')
            return redirect('/login')

  



    return render(request,'login/login.html')





def signup(request):
     # if user is already login but it acces login page it stop the 
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        # show the post data if we go to signup and fill the form now see in the termianl all form data show
        # print(request.POST)

        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        # check that its number is already exist in my data base then do it 
        number_check=User.objects.filter(username=number).exists()
            #  agar email ko check karna h db me 
        email_check=User.objects.filter(email=email).exists()
        print(email_check)
        # print(number) # if exist then output give me True

        # if number_check == True :
        #     messages.error(request,'Already have an Account Exits')
        #     return redirect('/signup')

        if email_check == True :
            messages.error(request,'Email already exits create a new email')
            return redirect('/signup')



        if len(number) != 10:
            messages.error(request,'number should pe 10 digit')
            # messages.success(request,'number should pe 10 digit')
            return redirect('/signup')
        
        elif password != cpassword:
            messages.error(request,'Password and confirm password Did not Match')
            return redirect('/signup')

        else:
            myuser=User.objects.create_user(username=number,email=email,password=cpassword)
            # print(myuser)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"Your Account Succesfull created")
            return redirect('/login')


    return render(request,'login/signup.html')




def logout(request):
    auth_logout(request)
    messages.success(request,"Your Account Succesfull Log Out")

    return redirect('/')




def change_password(request):
    if request.method == 'POST':
        new_password=request.POST['newpassword']
        print(new_password)

        # method jo user login h uska usename ka data sara yaha data fech ho jayega form user models me se jo password 
        u=User.objects.get(username=request.user.username)
        u.set_password(new_password)
        u.save()
        messages.success(request,"Your password has been Succesfull changed")
        return redirect('/')

    return render(request,'login/change_password.html')