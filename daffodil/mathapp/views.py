from django.shortcuts import render
def mileagecalc(request):
    context = {
        "d": "0",
        "f": "0",
        "mileage": "0",
    }

    if request.method == 'POST':
        print("POST method is used")
        d = request.POST.get('distance', "0")
        f = request.POST.get('fuel', "0")
        print("Distance =", d)
        print("Fuel =", f)
        mileage = float(d) / float(f)  
        context['mileage'] = round(mileage, 2)
        context['d'] = d
        context['f'] = f
        print("Mileage =", mileage)
    return render(request, 'mathapp/math.html', context)