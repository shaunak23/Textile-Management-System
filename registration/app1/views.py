from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserMapping, AdminJobCard
from .models import Yarn,Winding,Warping,Looming,Checking,Repairing
from .loom import Picker



currentOrderNumber = 1
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    loom_analysis_list = []
    pi_list=[]
    
    
    loom_no=[]
    total_meter=[]
    loom =Looming.objects.all().values()
    
    for i in loom:
        data = AdminJobCard.objects.all().values()
        data=data.get(orderNo=i['orderNo_id'])
        print(i)
        picker = Picker(ppc=data['ppc'], rate=data['rate'],total_picks=i['totalPicks'])
        amount_generated = picker.calculate_amount( loom_per_day_charges=5000)
        dict={'date':i['date'], 
            'loom_no':i['loomNo'], 
            'order_no':i['orderNo_id'],
            'total_meter':picker.meter,
            'target':picker.amount,
            'rs_generated':amount_generated }
        
        pi_data={
            'loom_no':i['loomNo'], 
            'total_meter':picker.meter
        }
        loom_no.append(i['loomNo'])
        total_meter.append(picker.meter)

        loom_analysis_list.append(dict)
        pi_list.append(pi_data)
    pichart={0:loom_no, 1:total_meter}
    print('analysis ',pi_list)
   
    return render(request, "home.html",{'my_list': loom_analysis_list, 'pi_data':pi_list , 'chart_data':pichart})

def AdminLandingPage(request):
    return render(request, "adminlandingpage1.html")

def AddOrderPage(request):
    return render(request, 'addorder.html')

def SubmitOrder(request):
    if request.method == 'POST':
        print(request.POST)
        newOrder = AdminJobCard()
        newOrder.orderDate = request.POST['OrderDate']
        newOrder.companyName = request.POST['CompanyName']
        newOrder.gst = request.POST['Gst']
        newOrder.quality = request.POST['quality']
        newOrder.ppc = request.POST['PPC']
        newOrder.rate = request.POST['rate']
        newOrder.deadline = request.POST['DeadLine']
        newOrder.count = request.POST['count']
        newOrder.construction = request.POST['construction']
        newOrder.lengthOfCloth = request.POST['lengtofcloth']
        newOrder.color = request.POST['color']
        newOrder.target = request.POST['target']
        newOrder.save()
        return render(request, 'addorder.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            #print(user)
            login(request,user)
            Role = UserMapping.objects.get(userName=user)
            print(Role.userRole)
            currRole = Role.userRole
            if(currRole == 1):
                return redirect('yarnpage')
            elif(currRole == 2):
                return redirect('windingpage')
            elif(currRole == 3):
                return redirect('warpingpage')
            elif(currRole == 4):
                return redirect('loomingpage')
            elif(currRole == 5):
                return redirect('checkingpage')
            elif(currRole == 6):
                return redirect('repairingpage')
            # elif(currRole == 0):
            #     return redirect('dashboardpage')
            elif(currRole == 0):
                return redirect('adminlandingpage')

        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def YarnPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "yarnpage.html",{'data':data})

def SubmitYarnData(request):
    if request.method == 'POST':
        print(request.POST['currentOrderNo'])
        print(request.POST['isYarnReceived'])
        print(request.POST['weight'])
        newYarnEntry = Yarn()
        newYarnEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo']) 
        newYarnEntry.yarnReceived = request.POST['isYarnReceived']
        newYarnEntry.weightOfYarn = request.POST['weight']
        newYarnEntry.save()
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        print(getJobData.isYarningDone)
        getJobData.isYarningDone = True
        getJobData.save()
        data = AdminJobCard.objects.all().values()
        return render(request, "yarnpage.html",{'data':data})

def WindingPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "windingpage.html",{'data':data})

def SubmitWindingData(request):
    if request.method == 'POST':
        print(request.POST['currentOrderNo'])
        print(request.POST['received'])
        print(request.POST['conesnumber'])
        print(request.POST['conesize'])
        print(request.POST['doffsnumber'])
        print(request.POST['waste'])
        print(request.POST['weightfinal'])
        print(request.POST['defects'])
        newWindingEntry = Winding()
        newWindingEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo'])
        newWindingEntry.yarnReceived = request.POST['received']
        newWindingEntry.noOfCones = request.POST['conesnumber']
        newWindingEntry.sizeOfCones = request.POST['conesize']
        newWindingEntry.noOfDoffs = request.POST['doffsnumber']
        newWindingEntry.finalWeightOfCone = request.POST['waste']
        newWindingEntry.wasteCollectionWeight = request.POST['weightfinal']
        newWindingEntry.defects = request.POST['defects']
        newWindingEntry.save()
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        print(getJobData.isWindingDone)
        getJobData.isWindingDone = True
        getJobData.save()
        data = AdminJobCard.objects.all().values()
        print(data)
        return render(request, "windingpage.html", {'data':data})

def WarpingPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "warpingpage.html",{'data':data})

def SubmitWarpingData(request):
    if request.method == 'POST':
      print(request.POST['currentOrderNo'])
      print(request.POST['warp'])
      print(request.POST['waste'])
      print(request.POST['defect'])
      newWarpingEntry = Warping()
      newWarpingEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo'])
      newWarpingEntry.finalWeightOfWarpedYarn = request.POST['warp']
      newWarpingEntry.wasteCollectionWeight = request.POST['waste']
      newWarpingEntry.packageDefects = request.POST['defect']
      newWarpingEntry.save()
      getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
      print(getJobData.isWarpingDone)
      getJobData.isWarpingDone = True
      getJobData.save()
      data = AdminJobCard.objects.all().values()
      print(data)
      return render(request, "warpingpage.html",{'data':data})


def LoomingPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "loomingpage.html",{'data':data})

def SubmitLoomingData(request):
    if request.method == 'POST':
        print(request.POST)
        newLoomingEntry = Looming()
        newLoomingEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo'])
        newLoomingEntry.yarnReceived = request.POST['isYarnReceived']
        newLoomingEntry.date = request.POST['Date']
        newLoomingEntry.loomNo = request.POST['loomNumber']
        newLoomingEntry.totalPicks = request.POST['totalPicks']
        newLoomingEntry.target = request.POST['Target']
        newLoomingEntry.wasteCollectionWeight = request.POST['wasteCollection']
        newLoomingEntry.save()
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        print(getJobData.isLoomingDone)
        getJobData.isLoomingDone = True
        getJobData.save()
        data = AdminJobCard.objects.all().values()
        print(data)
        return render(request, "loomingpage.html",{'data':data})


def CheckingPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "checkingpage.html",{'data':data})

def SubmitCheckingData(request):
    if request.method == 'POST':
        print(request.POST)
        newCheckingEntry = Checking()
        newCheckingEntry.date = request.POST['DateOfChecking']
        newCheckingEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo'])
        newCheckingEntry.loom = request.POST['LoomNo']
        newCheckingEntry.worker = request.POST['workerNo']
        newCheckingEntry.defectInMeters = request.POST['Defect']
        newCheckingEntry.points = request.POST['Point']
        newCheckingEntry.grade = request.POST['Grade']
        newCheckingEntry.repairable = request.POST['isRepairable']
        newCheckingEntry.save()
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        getJobData.isCheckingDone = True
        getJobData.save()
        data = AdminJobCard.objects.all().values()
        print(data)
        return render(request, "checkingpage.html",{'data':data})


def RepairingPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "repairingpage.html",{'data':data})

def SubmitRepairingData(request):
    if request.method == 'POST':
        print(request.POST)
        newRepairingEntry = Repairing()
        newRepairingEntry.orderNo = AdminJobCard.objects.get(orderNo = request.POST['currentOrderNo'])
        newRepairingEntry.repairingMachine= request.POST['repairingmachine']
        newRepairingEntry.worker= request.POST['workerNo']
        newRepairingEntry.date= request.POST['DateOfRepairing']
        newRepairingEntry.save()
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        print(getJobData.isRepairingDone)
        getJobData.isRepairingDone = True
        getJobData.save()
        data = AdminJobCard.objects.all().values()
        print(data)
        return render(request, "repairingpage.html",{'data':data})


def DashboardPage(request):
    data = AdminJobCard.objects.all().values()
    print(data)
    return render(request, "dashboard2.html",{'data':data})

def GetDashboardData(request):
    if request.method == 'POST':
        global currentOrderNumber
        getJobData = AdminJobCard.objects.get(orderNo=request.POST['currentOrderNo'])
        currentOrderNumber = request.POST['currentOrderNo']
        print(currentOrderNumber)
        data = AdminJobCard.objects.all().values()
        return render(request, "dashboard2.html",{'getJobData':getJobData, 'data': data})

def ShowYarnCard(request):
    global currentOrderNumber
    getJobData = Yarn.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "yarncard.html", {'getJobData':getJobData.values()[0]})

def ShowWindingCard(request):
    global currentOrderNumber
    getJobData = Winding.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "windingcard.html", {'getJobData':getJobData.values()[0]})

def ShowWarpingCard(request):
    global currentOrderNumber
    getJobData = Warping.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "warpingcard.html", {'getJobData':getJobData.values()[0]})

def ShowLoomingCard(request):
    global currentOrderNumber
    getJobData = Looming.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "loomingcard.html", {'getJobData':getJobData.values()[0]})

def ShowCheckingCard(request):
    global currentOrderNumber
    getJobData = Checking.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "checkingcard.html", {'getJobData':getJobData.values()[0]})

def ShowRepairingCard(request):
    global currentOrderNumber
    getJobData = Repairing.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "repairingcard.html", {'getJobData':getJobData.values()[0]})

def ShowPackingCard(request):
    global currentOrderNumber
    getJobData = Packing.objects.filter(orderNo=currentOrderNumber)
    print(getJobData.values()[0])
    return render(request, "packingcard.html", {'getJobData':getJobData.values()[0]})

def DetailsNotFound(request):
    return render(request, "Detailsnotfound.html")

