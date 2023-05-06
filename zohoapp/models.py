from django.db import models
from django.contrib.auth.models import User

class company_details(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    contact_number = models.CharField(max_length=100,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    company_email = models.CharField(max_length=255,null=True,blank=True)
    business_name = models.CharField(max_length=255,null=True,blank=True)
    company_type = models.CharField(max_length=255,null=True,blank=True)
    industry_type = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/patient')




class Sales(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name
    


class Purchase(models.Model):
    Account_type=models.TextField(max_length=255)
    Account_name=models.TextField(max_length=255)
    Acount_code=models.TextField(max_length=255)
    Account_desc=models.TextField(max_length=255)
    def __str__(self):
        return self.Account_name




class Unit(models.Model):
    unit=models.TextField(max_length=255)

    def __str__(self):
        return self.unit

    
    
    
class AddItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.TextField(max_length=255)
    Name=models.TextField(max_length=255)
    unit=models.ForeignKey(Unit,on_delete=models.CASCADE)
    sales=models.ForeignKey(Sales,on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    s_desc=models.TextField(max_length=255)
    p_desc=models.TextField(max_length=255)
    creat=models.CharField(max_length=255)
    s_price=models.CharField(max_length=255)
    p_price=models.TextField(max_length=255)
    satus=models.TextField(default='active')
    interstate=models.CharField(max_length=255)
    intrastate=models.CharField(max_length=255)

class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=255)
    p=models.ForeignKey(AddItem,on_delete=models.CASCADE)

class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    expense_account=models.TextField(max_length=255)
    amount=models.TextField(max_length=255)
    expense_type=models.TextField(max_length=255)
    paid=models.TextField(max_length=255)
    vendor=models.TextField(max_length=255)
    notes=models.TextField(max_length=255)
    hsn_code=models.TextField(max_length=255)
    gst_treatment =models.TextField(max_length=255)
    destination_of_supply=models.TextField(max_length=255)
    reverse_charge=models.TextField(max_length=255)
    tax=models.TextField(max_length=255)
    invoice=models.TextField(max_length=255)
    customer_name=models.TextField(max_length=255)
    reporting_tags=models.TextField(max_length=255)
    date = models.DateField()

class Account(models.Model):
    name = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True)