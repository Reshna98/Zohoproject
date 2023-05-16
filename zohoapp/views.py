from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q



def index(request):

    return render(request,'index.html')

def register(request):
   
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email1']
        phone = request.POST['phone']

      
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                company_details(contact_number = phone, user = u).save()
    
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('register')   
        return redirect('register')

    return render(request,'register.html')

def login(request):
        
    if request.method == 'POST':
        
        email_or_username = request.POST['emailorusername']
        password = request.POST['password']

        user = authenticate(request, username=email_or_username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return redirect('/')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def base(request):
   
    
    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'loginhome.html',context)

@login_required(login_url='login')
def view_profile(request):

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):

    company = company_details.objects.get(id = pk)
    user1 = User.objects.get(id = company.user_id)

    if request.method == "POST":

        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        # pat.age = request.POST.get('age')
        # pat.address = capfirst(request.POST.get('address'))
        # pat.gender = request.POST.get('gender')
        # user1.email = request.POST.get('email')
        # pat.email = request.POST.get('email')
        # pat.contact_num = request.POST.get('cnum')
        # #fkey1= request.POST.get('doc')
        # #pat.doctor = doctor.objects.get(id = fkey1)
        # if len(request.FILES)!=0 :
        #     doc.profile_pic = request.FILES.get('file')


        company.save()
        user1.save()
        return redirect('view_profile')

    context = {
        'company' : company,
        'user1' : user1,
    }
    context = {
                'company' : company,
            }
    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def itemview(request):
    viewitem=AddItem.objects.all()
    return render(request,'item_view.html',{'view':viewitem})


@login_required(login_url='login')
def additem(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    
    


  
    
        



    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

@login_required(login_url='login')
def add_account(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem")
        
    return render(request,'additem.html')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("itemview")
    return render(request,'additem.html')



@login_required(login_url='login')
def edititem(request,id):
    pedit=AddItem.objects.get(id=id)
    p=Purchase.objects.all()
    s=Sales.objects.all()
    u=Unit.objects.all()

    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))
    

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    return render(request,'edititem.html',{"account":account,"account_type":account_type,'e':pedit,'p':p,'s':s,'u':u,"accounts":accounts,"account_types":account_types})


@login_required(login_url='login')
def edit_db(request,id):
        if request.method=='POST':
            edit=AddItem.objects.get(id=id)
            edit.type=request.POST.get('type')
            edit.Name=request.POST['name']
            unit=request.POST['unit']
            edit.s_price=request.POST['sel_price']
            sel_acc=request.POST['sel_acc']
            edit.s_desc=request.POST['sel_desc']
            edit.p_price=request.POST['cost_price']
            cost_acc=request.POST['cost_acc']        
            edit.p_desc=request.POST['cost_desc']
            
            
            edit.unit=Unit.objects.get(id=unit)
            edit.sales=Sales.objects.get(id=sel_acc)
            edit.purchase=Purchase.objects.get(id=cost_acc)
            edit.save()
            return redirect('itemview')

        return render(request,'edititem.html')


@login_required(login_url='login')
def detail(request,id):
    user_id=request.user
    items=AddItem.objects.all()
    product=AddItem.objects.get(id=id)
    history=History.objects.filter(p_id=product.id)
    print(product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
       "history":history,
      
    }
    
    return render(request,'demo.html',context)


@login_required(login_url='login')
def Action(request,id):
    user=request.user.id
    user=User.objects.get(id=user)
    viewitem=AddItem.objects.all()
    event=AddItem.objects.get(id=id)
    

    print(user)
    if request.method=='POST':
        action=request.POST['action']
        event.satus=action
        event.save()
        if action == 'active':
            History(user=user,message="Item marked as Active ",p=event).save()
        else:
            History(user=user,message="Item marked as inActive",p=event).save()
    return render(request,'item_view.html',{'view':viewitem})

@login_required(login_url='login')
def cleer(request,id):
    dl=AddItem.objects.get(id=id)
    dl.delete()
    return redirect('itemview')


@login_required(login_url='login')
def add_unit(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem')
    return render(request,"additem.html")


@login_required(login_url='login')
def add_sales(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem')
    return render(request,'additem.html')

def expensepage(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses': expenses,
       }
    return render(request,'expense.html',context)


def save_expense(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        select=request.POST['select']
        expense_account=Account.objects.get(id=select)
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        expense_type = request.POST.get('expense_type')
        paid = request.POST.get('paid')
        vendor = request.POST.get('vendor')
        notes = request.POST.get('notes')
        if request.POST.get('expense_type') == 'goods':
            hsn_code = request.POST.get('sac')
            sac = request.POST.get('hsn_code')
        else:
            hsn_code = request.POST.get('hsn_code')
            sac = request.POST.get('sac')
        attachment_file = request.FILES.get('attachment')
        gst_treatment = request.POST.get('gst_treatment')
        destination_of_supply = request.POST.get('destination_of_supply')
        reverse_charge = request.POST.get('reverse_charge',False)
        tax = request.POST.get('tax')
        invoice = request.POST.get('invoice')
        customer_name = request.POST.get('customer_name')
        reporting_tags = request.POST.get('reporting_tags')
        taxamt=request.POST.get('taxamt',False)
        expense = Expense.objects.create(
            user=request.user,
            date=date,
            expense_account=expense_account,
            amount=amount,
            currency=currency,
            taxamt=taxamt,
            sac=sac,
            expense_type=expense_type,
            paid=paid,
            vendor=vendor,
            notes=notes,
            hsn_code=hsn_code,
            gst_treatment=gst_treatment,
            destination_of_supply=destination_of_supply,
            reverse_charge=reverse_charge,
            tax=tax,
            invoice=invoice,
            customer_name=customer_name,
            reporting_tags=reporting_tags,
            attachment_file = attachment_file 
        )
        expense.save()
        return redirect('expensepage')  
    
    return render(request, 'addexpense.html') 

def add_accountE(request):
    accounts = Account.objects.all()
    account_types = set(Account.objects.values_list('type', flat=True))
    if request.method == 'POST':
        type = request.POST.get('type')
        name = request.POST.get('name')
        code = request.POST.get('code')
        pname = request.POST.get('pname')
        description=request.POST.get('description')
        new_account = Account(type=type,name=name,code=code,pname=pname,description=description)
        new_account.save()
        accounts = Account.objects.all()


    return render(request, 'addexpense.html', {
        'accounts': accounts,
        'account_types': account_types,
    })
        
    # return render(request,'addexpense.html')


def expense_details(request, pk):
    user = request.user
    expense=Expense.objects.all()
    expense_account=Expense.objects.get(id=pk)
    context = {
        'expenses': expense,
        'expense': expense_account,
    }
    return render(request, 'expenseview.html', context)

def edit_expense(request, pk):
    expense = Expense.objects.get(id=pk)

    if request.method == 'POST':
        expense.date = request.POST.get('date')
        expense.expense_account = request.POST.get('expense_account')
        expense.amount = request.POST.get('amount')
        expense.expense_type = request.POST.get('expense_type')
        expense.paid = request.POST.get('paid')
        expense.vendor = request.POST.get('vendor')
        expense.notes = request.POST.get('notes')
        
        if request.POST.get('expense_type') == 'goods':
            expense.hsn_code = request.POST.get('sac')
            expense.sac = request.POST.get('hsn_code')
        else:
            expense.hsn_code = request.POST.get('hsn_code')
            expense.sac = request.POST.get('sac')
        
        expense.gst_treatment = request.POST.get('gst_treatment')
        expense.destination_of_supply = request.POST.get('destination_of_supply')
        expense.reverse_charge = request.POST.get('reverse_charge', False)
        expense.tax = request.POST.get('tax')
        expense.invoice = request.POST.get('invoice')
        expense.customer_name = request.POST.get('customer_name')
        expense.reporting_tags = request.POST.get('reporting_tags')
        expense.taxamt = request.POST.get('taxamt', False)
        
        expense.save()
        return redirect('save_expense')

    context = {
        'expense': expense,
    }
    return render(request, 'editexpense.html', context)


# def add_acc(request):
#     account = Account.objects.all()
#     type = set(Account.objects.values_list('type', flat=True))
#     return render(request,'addexpense.html',{
               
#                             "account":account,"type":type,
                            
#                             })
# def add_acc(request):
#     accounts = Account.objects.all()
#     account_types = set(Account.objects.values_list('type', flat=True))
#     return render(request, 'addexpense.html', {
#         'accounts': accounts,
#         'account_types': account_types,
#     })
def add_customer(request):
    sb=payment_terms.objects.all()
    return render(request,'customer.html',{'sb':sb})
def entr_custmr(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            type=request.POST.get('type')
            txtFullName=request.POST['txtFullName']
            cpname=request.POST['cpname']
           
            email=request.POST.get('myEmail')
            wphone=request.POST.get('wphone')
            mobile=request.POST.get('mobile')
            skname=request.POST.get('skname')
            desg=request.POST.get('desg')      
            dept=request.POST.get('dept')
            wbsite=request.POST.get('wbsite')

            gstt=request.POST.get('gstt')
            posply=request.POST.get('posply')
            tax1=request.POST.get('tax1')
            crncy=request.POST.get('crncy')
            obal=request.POST.get('obal')

            select=request.POST.get('pterms')
            pterms=payment_terms.objects.get(id=select)
            pterms=request.POST.get('pterms')

            plst=request.POST.get('plst')
            plang=request.POST.get('plang')
            fbk=request.POST.get('fbk')
            twtr=request.POST.get('twtr')
        
            atn=request.POST.get('atn')
            ctry=request.POST.get('ctry')
            
            addrs=request.POST.get('addrs')
            addrs1=request.POST.get('addrs1')
            bct=request.POST.get('bct')
            bst=request.POST.get('bst')
            bzip=request.POST.get('bzip')
            bpon=request.POST.get('bpon')
            bfx=request.POST.get('bfx')

            sal=request.POST.get('sal')
            ftname=request.POST.get('ftname')
            ltname=request.POST.get('ltname')
            mail=request.POST.get('mail')
            bworkpn=request.POST.get('bworkpn')
            bmobile=request.POST.get('bmobile')

            bskype=request.POST.get('bskype')
            bdesg=request.POST.get('bdesg')
            bdept=request.POST.get('bdept')
            u = User.objects.get(id = request.user.id)

          
            ctmr=customer(customerName=txtFullName,customerType=type,
                        companyName=cpname,customerEmail=email,customerWorkPhone=wphone,
                         customerMobile=mobile,skype=skname,designation=desg,department=dept,
                           website=wbsite,GSTTreatment=gstt,placeofsupply=posply, Taxpreference=tax1,
                             currency=crncy,OpeningBalance=obal,PaymentTerms=pterms,
                                PriceList=plst,PortalLanguage=plang,Facebook=fbk,Twitter=twtr,
                                 Attention=atn,country=ctry,Address1=addrs,Address2=addrs1,
                                  city=bct,state=bst,zipcode=bzip,phone1=bpon,
                                   fax=bfx,CPsalutation=sal,Firstname=ftname,
                                    Lastname=ltname,CPemail=mail,CPphone=bworkpn,
                                    CPmobile= bmobile,CPskype=bskype,CPdesignation=bdesg,
                                     CPdepartment=bdept,user=u )
            ctmr.save()  
            
            return redirect("base")
        return render(request,'base.html')
def payment_term(request):
    if request.method=='POST':
        term=request.POST.get('term')
        day=request.POST.get('day')
        ptr=payment_terms(Terms=term,Days=day)
        ptr.save()
        return redirect("add_customer")
def view_customr(request):
    vc=customer.objects.all()
    return render(request,'view_customer.html',{'vc':vc})


def editcustomer(request,id):
    cu=customer.objects.get(id=id)
    pt=payment_terms.objects.all()
  
    return render(request,'edit_customer.html',{'cu':cu,'pt':pt})
def editEnter_customer(request,id):
        if request.method=='POST':
            edit=customer.objects.get(id=id)
            edit.customerType=request.POST.get('type')
            edit.customerName=request.POST['txtFullName']
            edit.companyName=request.POST['cpname']

            edit.customerEmail=request.POST['email']
            edit.customerWorkPhone=request.POST['wphone']
            edit.customerMobile=request.POST['mobile']
            edit.skype=request.POST['skname']
            edit.designation=request.POST['desg']
            edit.department=request.POST['dept']
            edit.website=request.POST['wbsite']
            edit.GSTTreatment=request.POST['gstt']
            
            edit.placeofsupply=request.POST['posply']
           
            edit.Taxpreference=request.POST['tax1']
            edit.currency=request.POST['crncy']
            edit.OpeningBalance=request.POST['obal']
            
            edit.PaymentTerms=request.POST['pterms']
            
            edit.PriceList=request.POST['plst']
            edit.PortalLanguage=request.POST['plang']
            edit .Facebook=request.POST['fbk']
            edit.Twitter=request.POST['twtr']
            edit.Attention=request.POST['atn']
            edit.country=request.POST['ctry']

            edit.Address1=request.POST['addrs']
            edit.Address2=request.POST['addrs1']
            edit.city=request.POST['bct']
            edit.state=request.POST['bst']
            edit.zipcode=request.POST['bzip']
            edit.phone1=request.POST['bpon']
            edit.fax=request.POST['bfx']

            edit.CPsalutation=request.POST['sal']
            edit.Firstname=request.POST['ftname']
            edit.Lastname=request.POST['ltname']
            edit.CPemail=request.POST['mail']
            edit.CPphone=request.POST['bworkpn']
            edit.CPmobile=request.POST['bmobile']
            edit.CPskype=request.POST['bskype']

            edit.CPdesignation=request.POST['bdesg'] 
            edit.CPdepartment=request.POST['bdept']
            
           
            edit.save()
            return redirect('view_customr')

        return render(request,'view_customer.html')