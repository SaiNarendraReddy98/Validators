from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Validform(request):
    EVFO = Studentform()
    d={'EVFO':EVFO}
    if request.method == 'POST':
        VDO = Studentform(request.POST)
        if VDO.is_valid():
            sn = VDO.cleaned_data['Sname']
            sno = VDO.cleaned_data['Snumber']
            sl = VDO.cleaned_data['Slocation']
            em = VDO.cleaned_data['email']
            rem = VDO.cleaned_data['renteremail']
            SO = Student.objects.get_or_create(Sname=sn,Snumber=sno,Slocation=sl,email=em,renteremail=rem)[0]
            SO.save()
            return HttpResponse(str(VDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
        
    return render(request,'Validform.html',d)