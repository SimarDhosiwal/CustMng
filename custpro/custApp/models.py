from django.db import models

# Create your models here.

class customer_query(models.Model) :
    row_id = models.BigAutoField(primary_key=True)
    row_creation_time = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=1)
    query_description = models.TextField(blank=True, null=True)
    issue_photo_content_dir = models.CharField(max_length=255, blank=True, null=True)
    issue_photo = models.CharField(max_length=255, blank=True, null=True)
    additional_ref1 = models.TextField(null = True, blank = True)
    additional_ref2 = models.TextField(null = True, blank = True)
    cover = models.ImageField(upload_to='images/',null = True, blank = True)
    user_uploaded_img = models.ImageField(upload_to="profiles/%Y/%m/%d",null=True,blank=True)

    
    class Meta:
        managed = True
        db_table = 'customer_query'