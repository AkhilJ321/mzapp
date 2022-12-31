from django.shortcuts import render
from . import k
def home(request):
  return render(request,'category.html')

def detect(request):
    
    if request.method == "POST":
     try:
        img = request.FILES['image']

        print("hll")
        predictions = k.pred(img=img)
        if predictions.tag_name == 'culex':
            scanned = 2
        elif predictions.tag_name=='ades_aegypti':
            scanned= 1
        context = {'name':predictions.tag_name,'probability':predictions.probability,'scanned':scanned}
        return render(request,'classification.html',context=context)
     except:
        scanned =-1
        context={'scanned':scanned}
        return render(request,'classification.html',context=context)   


    context={'scanned':0}    

    return render(request,'classification.html',context=context)   
def classify(request):
    return render(request,'classification.html')
def about(request):
    return render(request,'about_us.html')
def contact(request):
    return render(request ,'contact.html')
def water(request):
    return render(request ,'water.html')
