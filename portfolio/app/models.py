from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Intro(models.Model):
    fullname=models.CharField(max_length=250)
    short_Intro=models.TextField(max_length=600)
    cv=models.FileField(upload_to="cv")
    image=models.ImageField(upload_to="introimg/")
    phoneNo=models.PositiveBigIntegerField()
    address=models.CharField(max_length=300)
    

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.fullname
        
        
class AboutMe(models.Model):
    availablefor=models.CharField(max_length=200)
    short_intro=models.TextField()
    completedProjects=models.PositiveBigIntegerField()
    clients=models.PositiveIntegerField()
    image=models.ImageField(upload_to="aboutme")
    facebookUrl=models.URLField(null=True,blank=True)
    instagramUrl=models.URLField(null=True,blank=True)
    linkendinUrl=models.URLField(null=True,blank=True)
    github=models.URLField(null=True,blank=True)
    gmail=models.EmailField()
    whatsApp=models.PositiveBigIntegerField(null=True,blank=True)
    locationUrl=models.URLField(max_length=1050)
    class Meta:
        ordering =['-id',]


    def __str__(self):
        return self.availablefor
        
        

class Experience(models.Model):
    designation=models.CharField(max_length=300)
    companyName=models.CharField(max_length=300)
    startedDate=models.DateField()
    endDate=models.DateField(null=True,blank=True)
    short_description_about_work=models.TextField(null=True,blank=True)
    class Meta:
        ordering =['-id',]
        
        
    def __str__(self):
        return self.companyName


class Skills(models.Model):
    title=models.CharField(max_length=200)
    rateSkill_1to100=models.PositiveBigIntegerField()

    class Meta:
        ordering =['-id',]


    def __str__(self):
        return self.title
    
        
        
projecttype =(
    ('MobileApp',"Mobile Application"),
    ('Website',"Website"),
  
)


class Portfolio(models.Model):
    projectType =models.CharField(max_length=150, choices=projecttype)
    projectName=models.CharField(max_length=200)
    languageUsed=models.TextField()
    image=models.ImageField(upload_to='portflio/')
    image2=models.ImageField(upload_to='portfoilo2')
    image3=models.ImageField(upload_to='portfoilo3')
    image4=models.ImageField(upload_to='portfoilo4')
    country=models.CharField(max_length=200)
    projectUrl=models.URLField(null=True,blank=True,max_length=500)
    short_description=models.TextField()

    class Meta:
        ordering =['-id',]
        
    def __str__(self):
        return self.projectName
    

class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete= models.SET_NULL, null=True, blank=True, related_name ='portfolioimages')
    image = models.ImageField(upload_to='Portfolioimage/')


    class Meta:
        ordering  =['-id']


class Contact(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=500)
    email=models.EmailField()
    message=models.TextField()

    class Meta:
        ordering =['-id']
        
    def __str__(self):
        return self.name