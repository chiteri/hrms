from django.db import models
from django.contrib.auth.models import User 
import datetime 

class Nationality(models.Model): 
    country_code = models.IntegerField(blank=False, unique=True) 
    country = models.CharField(blank=False, unique=True, max_length=50)
    nationality_name = models.CharField(blank=False, unique=True, max_length=50) 

    class Meta: 
        verbose_name = "Nationalities"
        verbose_name_plural = "Nationalities" 

    def __unicode__(self): 
        return self.nationality_name 

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
    user = models.ForeignKey(User, unique=True)  
    
    # Personal Information  
    date_of_birth = models.DateField() 
    gender=models.CharField(max_length=2, choices=GENDER_CHOICES) 
    blood_group = models.IntegerField(max_length=2, blank=False, choices=BLOOD_TYPE_CHOICES) 	
    marital_status = models.IntegerField(max_length=2, blank=False, choices=MARITAL_STATUS_CHOICES)
    nationality = models.ForeignKey(Nationality, blank=False) 
    citizen = models.BooleanField(default=True)
	
    # Contact Information 
    cellphone_number = models.CharField(blank=False, max_length=20, unique=True)
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
        return u"%s's Profile"%(self.user)		

# Model the department first, the Employee entity needs it 			
class Department(models.Model): 
    name_of_department=models.CharField(max_length=30, blank=False, unique=True) 
    manager=models.ForeignKey(User, unique=False, related_name='head_of_department') 
    description=models.TextField()
	
    def __unicode__(self): 
        return self.name_of_department 
		
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
    national_id_or_passport = models.CharField(blank=False, max_length=10, unique=True, 
	help_text='National ID number (Foreign employees should provide Passport number).')
    employee_number = models.CharField(blank=False, max_length=10, unique=True) 
    date_of_hire = models.DateField(blank=False) 
    department = models.ForeignKey(Department, blank=False) 
    supervisor=models.ForeignKey('Employee', blank=True, null=True, related_name='employees_supervisor') 
    job_title = models.IntegerField(max_length=2, blank=False, choices=JOB_TITLE_CHOICES)
    employee_category = models.IntegerField(max_length=1, blank=False, choices=EMPLOYEE_CATEGORY_CHOICES)
    contract_type = models.IntegerField(max_length=1, blank=False, choices=CONTRACT_TYPE_CHOICES) 
    # entitled_leaves = models.ManyToManyField('LeaveCategory')
    pin_number = models.CharField(blank=False, max_length=10, unique=True)
    nssf_number = models.CharField(blank=False, max_length=15, unique=True)
    nhif_number = models.CharField(blank=False, max_length=15, unique=True)

    def __unicode__(self): 
        return u"%s %s"%(self.user.first_name, self.user.last_name ) 		

# These are contacts for Foreign employees 		
class HomeContact(models.Model): 
    postal_address = models.CharField(blank=False, max_length=50) 
    zip_or_postal_code = models.CharField(blank=True, max_length=10) 
    city_or_state = models.CharField(blank=True, max_length=20)  
    country_of_birth = models.CharField(blank=False, max_length=20) 
    employee = models.ForeignKey(Employee, unique=True) # An employee has a single home contact 
    # , edit_inline=models.STACKED, num_in_admin=1,min_num_in_admin=1, max_num_in_admin=1,num_extra_on_change=0

    def __unicode__(self): 
        return u"%s - %s, %s | %s"%(self.zip_or_postal_code, self.postal_address, self.city_or_state, self.country_of_birth.upper())
		
# In case the employees go for summer, these are their contacts 
class SummerContact(models.Model): 
    cellphone_no = models.CharField(blank=False, max_length=20, help_text='Cellphone number.')
    postal_address = models.CharField(blank=False, max_length=50) 
    zip_or_postal_code = models.CharField(blank=True, max_length=10) 
    city_or_state = models.CharField(blank=True, max_length=20)    
    employee = models.ForeignKey(Employee, unique=True) #, edit_inline=models.STACKED, num_in_admin=1,  min_num_in_admin=1, max_num_in_admin=2,num_extra_on_change=1) 

    def __unicode__(self): 
        return u"%s (%s - %s) | %s"%( self.cellphone_no, self.zip_or_postal_code, self.postal_address, self.city_or_state.upper())
	
# The details of Emergency Contacts 
class NextOfKin(models.Model): 
    # Types of Relationships 
    # Marital statuses  
    MOTHER = 1 
    FATHER = 2 
    BROTHER = 3 
    SISTER = 4 
    COUSIN = 5  
    HUSBAND = 6 
    WIFE = 7 
    FRIEND  = 8 
    GRANDMOTHER = 9 
    GRANDFATHER = 10
    NIECE = 11 
    NEPHEW = 12 
    AUNT = 13 
    UNCLE = 14 
    OTHER = 15 
    RELATIONS_CHOICES = (
        (MOTHER, 'Mother'), 
        (FATHER, 'Father'), 
        (BROTHER, 'Brother'), 
        (SISTER, 'Sister'), 
        (COUSIN, 'Cousin'), 
        (HUSBAND, 'Husband'), 
        (WIFE, 'Wife'), 
        (FRIEND, 'Friend'), 
        (GRANDMOTHER, 'Grandmother'), 
        (GRANDFATHER, 'Grandfather'), 
        (NIECE, 'Niece'), 
        (NEPHEW, 'Nephew'), 
        (AUNT, 'Aunt'), 
        (UNCLE, 'Uncle'), 
        (OTHER, 'Other'), 
    )    

    first_names = models.CharField(blank=False, max_length=30) 
    surname = models.CharField(blank=False, max_length=20) 
    relationship = models.IntegerField(blank=False, max_length=2, choices=RELATIONS_CHOICES) 
    telephone_number = models.CharField(blank=True, max_length=20) 
    location = models.CharField(blank=True, max_length=40, help_text='Place of work, school, home (Optional).') 
    employee = models.ForeignKey(Employee, unique=False) # An employee can have e number of kinsmen

    def __unicode__(self): 
        return u"%s %s"%(self.first_names, self.surname)

# For married employees 	
class Spouse(models.Model): 
    first_names = models.CharField(blank=False, max_length=30) 
    surname = models.CharField(blank=False, max_length=20) 
    date_of_birth = models.DateField(blank=False)     
    contacts = models.CharField(blank=False, max_length=50)
    employee = models.ForeignKey(Employee, unique=True)

    def __unicode__(self): 
        return u"%s %s"%(self.first_names, self.surname)
	
# Dependants of an employee 
class Dependant(models.Model): 
    first_names = models.CharField(blank=False, max_length=30) 
    surname = models.CharField(blank=False, max_length=20) 
    date_of_birth = models.DateField(blank=False)  
    employee = models.ForeignKey(Employee, unique=False) # Allow an employe to have multiple dependants 
	# Think about the case where a dependant has both guardians / parents as Staff members 
    
    def __unicode__(self): 
        return u"%s %s"%(self.first_names, self.surname)

class AcademicQualification(models.Model): 
    CERTIFICATE = 1
    DIPLOMA = 2 
    HIGHER_DIPLOMA = 3 	
    UNDERGRADUATE_DEGREE = 4 
    GRADUATE_DEGREE = 5 
    POST_GRADUATE_DEGREE = 6 
    QUALIFICATION_TYPES = (
        (CERTIFICATE, 'Certificate'), 
        (DIPLOMA, 'Diploma'), 
        (HIGHER_DIPLOMA, 'Higher Diploma'), 
        (UNDERGRADUATE_DEGREE, 'Undergraduate Degree'), 
        (GRADUATE_DEGREE, 'Masters'), 
        (POST_GRADUATE_DEGREE, 'Ph.D'), 
	)
    title = models.CharField (blank=False, max_length=50) 
    institution_issued = models.CharField(blank=False, max_length=30) 
    date_of_issue =  models.DateField(blank=False)	
    type = models.IntegerField(blank=False, max_length=1, choices=QUALIFICATION_TYPES) 
    score = models.CharField(blank=False, max_length=30)
    employee = models.ForeignKey(Employee, unique=False) # An employee should can have several Academic qualifications 
	
    def __unicode__(self): 
        return u"%s"%(self.title) 

class WorkPermit(models.Model): 
    valid_from = models.DateField(blank=False, null=False, help_text="Date from when the work permit is effective.") 
    valid_until = models.DateField(blank=False, null=False, help_text="Date until to when work permit is effective.")
    employee = models.ForeignKey(Employee, unique=False) 
	
    def __unicode__(self): 
        return u"Permit valid from %s to %s"%(self.valid_from, self.valid_until)
	
# We define our financial periods here 		
class FinancialPeriod(models.Model): 
    begins_from = models.DateField(blank=False, null=False, help_text="Date when the financial period starts.") 
    ends_at = models.DateField(blank=False, null=False, help_text="Date when the financial period ends.") 
    description = models.TextField(blank=False, null=False, help_text="A short description of the period.") 

    def __unicode__(self): 
        return u"%s [%s to %s]"%(self.description, self.begins_from, self.ends_at)
	
class DocumentsChecklist(models.Model): 
    work_permit = models.BooleanField(blank=True, default=False) 
    re_entry_permit = models.BooleanField(blank=True, default=False) 
    pin_card = models.BooleanField(blank=True, default=False) 
    medical_certificate = models.BooleanField(blank=True, default=False) 
    photographs = models.BooleanField(blank=True, default=False) 
    id_or_passport_copies = models.BooleanField(blank=True, default=False) 
    physical_exam_forms = models.BooleanField(blank=True, default=False) 
    tax_forms = models.BooleanField(blank=True, default=False) 
    direct_deposit_forms = models.BooleanField(blank=True, default=False) 
    sick_bank_membership_forms =  models.BooleanField(blank=True, default=False) 
    nssf = models.BooleanField(blank=True, default=False) 
    nhif = models.BooleanField(blank=True, default=False) 
    certificate_of_good_conduct = models.BooleanField(blank=True, default=False) 
    transcripts = models.BooleanField(blank=True, default=False) 
    degree_certificate = models.BooleanField(blank=True, default=False) 
    employee = models.ForeignKey(Employee, unique=True)  

# A model for the leaves in the system  
class LeaveCategory(models.Model): 
    name = models.CharField(blank=False, max_length=35, unique=True) 
    days_assigned = models.IntegerField(blank=False, max_length=3, default=0) 
    description = models.TextField(blank=False)
    accumulates = models.BooleanField(default=False) 
	
    class Meta: 
        verbose_name_plural = 'Leave Categories' 
		
    def __unicode__(self): 
        return u"%s"%(self.name) 	
