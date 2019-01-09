from django.shortcuts import render
from app.models import User
from app.forms import NewUserForm
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
	return HttpResponse("your data has been saved")
def user(request):
	form=NewUserForm()
	if(request.method=="POST"):
		form =NewUserForm(request.POST)
		if(form.is_valid()):
			form.save(commit=True)
			return index(request)
		else:
			print("something went wrong")
	return render(request,'app/abc.html',{'form':form})
def show(request):
	obj=User.objects.order_by('name')
	hello={'obj':obj}
	return render (request,'app/show.html',context=hello)					

