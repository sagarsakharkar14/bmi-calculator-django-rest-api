from django.shortcuts import render
from .models import BMIRecord
from .serializers import BMIRecordSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# Create your views here.

def calculate_bmi(weight, height):
    height = height * 0.01
    return round((weight / (height**2)),2)


def bmi_category(bmi):
    
    if bmi < 18.5:
        return f'Underweight {bmi}'
    elif bmi >= 18.5 and bmi < 25:
        return f'Normal weight {bmi}'
    elif bmi >= 25 and bmi < 30:
        return f'Overweight {bmi}'
    else:
        return f'Obese {bmi}'



@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        bmirecords = BMIRecord.objects.all().order_by('-created_at')[:3]
        serializer = BMIRecordSerializer(bmirecords, many=True)
        return Response(serializer.data, status=200)
    
    if request.method == 'POST':
        serializer = BMIRecordSerializer(data=request.data)
        if serializer.is_valid():
            weight = serializer.validated_data['weight']
            height = serializer.validated_data['height']
            serializer.save()
            if height <=0 or weight <= 0:
                return Response({'errors':'Height and weight can not be less than zero'}, status=400)
            bmi= calculate_bmi(weight, height)
            bmi_note = bmi_category(bmi)
            return Response({'Result': bmi_note}, status=201)
        return Response(serializer.errors, status=400)    
        
class BMIRecordDetailView(APIView):
    def get(self, request, pk):
        bmi_record = get_object_or_404(BMIRecord, pk=pk)
        serializer = BMIRecordSerializer(bmi_record)
        return Response(serializer.data)
    
    def put(self, request, pk):
        bmi_record = get_object_or_404(BMIRecord, pk=pk)
        serializer = BMIRecordSerializer(bmi_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        bmi_record = get_object_or_404(BMIRecord, pk=pk)
        bmi_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    #     form = BMICalculatorForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         weight = form.cleaned_data['weight']
    #         height = form.cleaned_data['height']
    #         bmi= calculate_bmi(weight, height)
    #         # Save BMI record in model database
    #         BMIRecord.objects.create(name=name,weight=weight,height=height,bmi=bmi)
    #         
    #         return render(request,'result.html', {'bmi': bmi, 'bmi_note': bmi_note})
    # else:
    #     form = BMICalculatorForm()
    #     return render(request, 'calculation.html', {'form': form})