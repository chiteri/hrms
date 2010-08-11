from django.db import models
from django.contrib.auth.models import User  
import datetime 

class Nationality(models.Model): 
    country_code = models.IntegerField(blank=False, unique=True) 
    nationality_name = models.CharField(blank=False, unique=True, max_length=50)

# Create your models here. 	
class UserProfile(models.Model): 
    # Sexes 
    GENDER_CHOICES = (
        (u'M', u'Male'), 
        (u'F', u'Female'), 
    )    
    # Marital statuses  
    SINGLE_STATUS = 1 
    MARRIED_STATUS = 2 
    DIVORCED_STATUS = 3 
    WIDOWED_STATUS = 4 
    MARITAL_STATUS_CHOICES = (
        (SINGLE_STATUS, 'Single'), 
        (MARRIED_STATUS, 'Married'), 
        (DIVORCED_STATUS, 'Divorced'), 
        (WIDOWED_STATUS, 'Widowed'), 
    )	
    # Blood types 	
    O_NEGATIVE = 1 
    O_POSITIVE = 2 
    A_NEGATIVE = 3 
    A_POSITIVE = 4 
    B_NEGATIVE = 5 
    B_POSITIVE = 6 
    AB_NEGATIVE = 7 
    AB_POSITIVE = 8 
    BLOOD_TYPE_CHOICES = (
        (O_NEGATIVE, 'O -'), 
        (O_POSITIVE, 'O +'), 
        (A_NEGATIVE, 'A -'), 
        (A_POSITIVE, 'A +'), 
        (B_NEGATIVE, 'B -'), 
        (B_POSITIVE, 'B +'), 
        (AB_NEGATIVE, 'AB -'), 
        (AB_POSITIVE, 'AB +'),
    )	

    # Core Fields 	
    user = models.ForeignKey(User, unique=True) #, edit_inline=models.TABULAR, num_in_admin=1,min_num_in_admin=1, max_num_in_admin=1,num_extra_on_change=0)     
    
    # Personal Information  
    date_of_birth = models.DateField() 
    gender=models.CharField(max_length=2, choices=GENDER_CHOICES) 
    blood_group = models.IntegerField(max_length=2, blank=False, choices=BLOOD_TYPE_CHOICES) 	
    marital_status = models.IntegerField(max_length=2, blank=False, choices=MARITAL_STATUS_CHOICES)
    nationality = models.ForeignKey(Nationality, blank=False)
	
    # Contact Information 
    cellphone_number = models.CharField(blank=False, max_length=20)
    postal_address = models.CharField(blank=False, max_length=50)
    postal_code = models.CharField(blank=True, max_length=10) 
    physical_address = models.CharField(blank=False, max_length=50) 	
    town = models.CharField(blank=True, max_length=20) 
    road = models.CharField(blank=True, max_length=20)
    residence_area = models.CharField(blank=False, max_length=30) 
    house_number = models.CharField(blank=True, max_length=20)
	
    class Meta: 
        abstract = True 
		
    def __unicode__(self): 
        return "%s's Profile"%(self.user)		

# Model the department first, the Employee entity needs it 			
class Department(models.Model): 
    name=models.CharField(max_length=30, blank=False) 
    manager=models.ForeignKey(User, unique=True) #, edit_inline=models.TABULAR, num_in_admin=1,min_num_in_admin=1, max_num_in_admin=1,num_extra_on_change=0) 	
    description=models.TextField()
	
    def __unicode__(self): 
        return self.name 
		
# Create the employee model 
class Employee(UserProfile): 
    # Employee categories 
    CERTIFIED = 1 
    NON_CERTIFIED = 2 
    EMPLOYEE_CATEGORY_CHOICES = (
        (CERTIFIED, 'Certified Employee'), 
        (NON_CERTIFIED, 'Non-certified Employee'), 
    )	
	
    # Job titles
    DIRECTOR = 1 
    HIGH_SCHOOL_PRINCIPAL = 2 
    MIDDLE_SCHOOL_PRINCIPAL = 3 
    ELEMENTARY_SCHOOL_PRINCIPAL = 4 
    HUMAN_RESOURCES_MANAGER = 5 
    ADMIN_ASSISTANT = 6
    CENTRAL_OFFICE = 7 
    TEACHER = 8 
    TEACHER_ASSISTANT = 9 
    BUS_MONITOR = 10 
    DRIVER = 11 
    CLEANER = 12 
    CARPENTER = 13 
    JOB_TITLE_CHOICES = (
        (DIRECTOR, 'Director'), 
        (HIGH_SCHOOL_PRINCIPAL, 'High-School Principal'), 
        (MIDDLE_SCHOOL_PRINCIPAL, 'Middle-School Principal'),  
        (ELEMENTARY_SCHOOL_PRINCIPAL, 'Elementary-School Principal'), 
        (HUMAN_RESOURCES_MANAGER, 'Human Resources Manager'), 
        (ADMIN_ASSISTANT, 'Administration Assistant'), 
        (CENTRAL_OFFICE, 'Central Office'), 
        (TEACHER, 'Teacher'), 
        (TEACHER_ASSISTANT, 'Teacher Assitant'), 
        (BUS_MONITOR, 'Bus Monitor'), 
        (DRIVER, 'Driver'), 
        (CLEANER, 'Cleaner'), 
        (CARPENTER, 'Carpenter'), 
    )	

    # Contract types  
    ONE_YEAR_CONTRACT = 1 
    TWO_YEARS_CONTRACT = 2 
    PERMANENT_CONTRACT = 3 
    CONTRACT_TYPE_CHOICES = (
        (ONE_YEAR_CONTRACT, 'One-year Contract'), 
        (TWO_YEARS_CONTRACT, 'Two-years\' Contract'), 
        (PERMANENT_CONTRACT, 'Permanent Contract'), 
    )	
  
	# Core Fields 
    employee_number = models.CharField(blank=False, max_length=10) 
    date_of_hire = models.DateField(blank=False) 
    department = models.ForeignKey(Department,blank=False) 
    # supervisor=models.ForeignKey(User, blank=True) 
    job_title = models.IntegerField(max_length=2, blank=False, choices=JOB_TITLE_CHOICES)
    employee_category = models.IntegerField(max_length=1, blank=False, choices=EMPLOYEE_CATEGORY_CHOICES)
    contract_type = models.IntegerField(max_length=1, blank=False, choices=CONTRACT_TYPE_CHOICES)
    pin_number = models.CharField(blank=False, max_length=10)
    nssf_number = models.CharField(blank=False, max_length=15)
    nhif_number = models.CharField(blank=False, max_length=15)
	
    # Educational Information 

    # Documents checklist 
	
    # 
	