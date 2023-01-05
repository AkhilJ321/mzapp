from django.shortcuts import render
from . import k
import urllib.request
import json
import ast
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
    if request.method=='POST':
        context = {"f":1}
    else:
        context = {"f":0}
    return render(request ,'contact.html',context)
def water(request):
    return render(request ,'water.html')
def endemic(request):
    if request.method=="POST":
        city = request.POST.get('city')
        pre =1
        week= request.POST.get('Week')
        precipitation = request.POST.get('precipitation')
        humidity = request.POST.get('humidity')
        temp = request.POST.get('temp')
        data =  {
  "Inputs": {
    "input1": [
      {
        "City": city,
        "WeekofYear": week,
        "Total_Cases": 0,
        "Precipitation_mm":precipitation,
        "R_humidity_percent": humidity,
        "Diural_Temp":temp
      }
      
    ]
  },
  "GlobalParameters": {}
     }
        body = str.encode(json.dumps(data))
        url = 'http://24735aca-330b-445f-a0f8-7321485970f3.eastus.azurecontainer.io/score'
        api_key = 'tbfFaYbEHmtBLLIdftgvxxInvlA4VIgL'
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")


        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
          response = urllib.request.urlopen(req)

          result = response.read()
          prob = round(ast.literal_eval(result.decode("utf8"))['Results']['WebServiceOutput0'][0]['Scored Labels'],3)
          context = {'prob':prob,'p':pre}
          return render(request,'endemic.html',context)

        except urllib.error.HTTPError as error:
         print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
         print(error.info())
         print(error.read().decode("utf8", 'ignore'))
         
    context= {'p':0
    }  

    return render(request,'endemic.html',context)
