from django.shortcuts import render
from .models import BMIRecord
from .forms import BMICalculatorForm
# Create your views here.

def calculate_bmi(weight, height):
    height = height * 0.01
    return round((weight / (height**2)),2)

def home(request):
    bmirecords = BMIRecord.objects.all().order_by('-created_at')[:5]
    return render(request, 'home.html', {'bmirecords':bmirecords})


def result(request):
    if request.method == 'POST':
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi= calculate_bmi(weight, height)
            # Save BMI record in model database
            BMIRecord.objects.create(name=name,weight=weight,height=height,bmi=bmi)
            if bmi < 18.5:
                bmi_note = 'Underweight'
            elif bmi >= 18.5 and bmi < 25:
                bmi_note = 'Normal weight'
            elif bmi >= 25 and bmi < 29.9:
                bmi_note = 'Overweight'
            else:
                bmi_note = bmi
            return render(request,'result.html', {'bmi': bmi, 'bmi_note': bmi_note})
    else:
        form = BMICalculatorForm()
        return render(request, 'calculation.html', {'form': form})