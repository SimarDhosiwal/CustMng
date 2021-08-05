from django.shortcuts import render
from .models import customer_query
# Create your views here.

from django.http import HttpResponse
import json
import os.path
import os
import csv
import datetime

# Create your views here.
def index(request):
    return render(request,'querypage.html')

def show_all_data(request):
    data1 = customer_query.objects.all().order_by("-row_id")
    return render(request,'displaydata.html',{'alldetails':data1})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename= CustomerData'+ \
       str(datetime.datetime.now())+ '.csv'
    writer = csv.writer(response)
    writer.writerow(['Name,Query Description'])

    d = customer_query.objects.all()
    
    for i in d:
        writer.writerow([i.name, i.query_description])
    
    return response

def save_data(request):
    context={}
  
    if request.method == "POST":
        first_name = request.POST.get('first_name')    
        querydesc = request.POST.get('querydesc')
        gendertype = request.POST.get('gendertype')   
        add_comm = request.POST.get('add_comm')

        custobj=customer_query.objects.create(
                name = first_name,
                query_description = querydesc,
                gender = gendertype,
                issue_photo_content_dir='',
                additional_ref1 = add_comm
                
        ) 


        custobj.save()

        if "image" in request.FILES:
            img = request.FILES.get('image')
            custobj.user_uploaded_img = img
            custobj.save()

            # data = customer_query.reverse()[0]
            data = customer_query.objects.latest('row_creation_time')
            print('data',data)

            context["data"] = data

        context["status"] = "Changes Saved Successfully"
    return render(request,'querypage.html',context)


def update_details(request):
    if request.is_ajax():
        if request.method == 'POST':
            status_code = 'F'
            status_desc = 'Failed'
            r_row_id = request.POST.get('r_row_id')
            new_comment = request.POST.get('new_comment')

            try:
                userObj=customer_query.objects.filter(row_id=r_row_id)
                if userObj.exists():
                  
                    userObj1 = customer_query.objects.filter(row_id=r_row_id).update(additional_ref1=new_comment)
                    status_code = 'S'
                    status_desc = 'Successfully added new comment!'
                else:
                    status_code = 'F'
                    status_desc = 'Error occured!Try after some time.'

            except Exception as e:
                    status_code = 'F'
                    status_desc = str(e)
               
            data={'status_code':status_code,
                    'status_desc':status_desc
            }
      
            return HttpResponse(json.dumps(data),content_type="application/json") 


    


# def save_data(request):
#     if request.is_ajax():
#         if request.method == 'POST':

#             status_code = 'F'
#             status_desc = 'Failed'
#             tchr_type = ''

#             first_name = request.POST.get('first_name') 
#             querydesc = request.POST.get('querydesc')
#             gendertype = request.POST.get('gendertype')
        
#             add_comm = request.POST.get('add_comm')

#             issue_img = request.FILES['issue_img']

#             # issue_photo_content_dir
#             # issue_photo

#             try:
               
#                 custobj=customer_query.objects.create(
#                         name = first_name,
#                         query_description = querydesc,
#                         gender = gendertype,
#                         issue_photo_content_dir='',
#                         issue_photo = issue_img.name,
#                         # cover = issue_img.name,
#                         additional_ref1 = add_comm
                   
#                 ) 
#                 custobj.issue_photo_content_dir = 'static/userImg/'+ str(custobj.row_id) + '/'

#                 custobj.save()
#                 getobj = customer_query.objects.all()
#                 # f_date = custobj.row_creation_time
#                 # dtdate = f_date.date()

#                 # os.mkdir('static/userImg/' + str(dtdate)+str(custobj.row_id)+'C')
           
#                 # file_path = os.path.join("static/userImg/",str(dtdate)+str(custobj.row_id)+'C')
#                 # with open(file_path, 'wb') as actual_file:
#                 #     actual_file.write(issue_img.read())

# #                  file_path = os.path.join("static/RC/",str(request.session['user_id'])+str(dtdate)+'F')
# # +                with open(file_path, 'wb') as actual_file:
# # +                    actual_file.write(frontrc.read()) 
              
#                 # os.mkdir('static/userImg/' + str(custobj.row_id))
                
#                 # file_path = os.path.join("static/userImg/" + str(custobj.row_id))
                
#                 # with open(file_path, 'wb') as actual_file:
#                 #     actual_file.write(issue_img.read())
              
                    
                    
#                 status_code = 'S'
#                 status_desc = 'Successfully Saved' 

#             except Exception as e:

#                 status_code='error'
#                 status_desc= str(e)
             
            
#             data={
#                         'status_code':status_code,
#                         'status_desc':status_desc
#                                          }
#             print('data=',data)
#             return HttpResponse(json.dumps(data),content_type="application/json") 


