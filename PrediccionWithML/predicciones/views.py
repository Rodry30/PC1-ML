# predicciones/views.py

from django.shortcuts import render
from django.http import JsonResponse
import requests

def pagina_inicio(request):
    return render(request, 'predicciones/index.html')

def api_predict(request):
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            # Capturamos los datos del formulario
            datos = {
                'Age': int(request.POST.get('Age')),
                'Sex': int(request.POST.get('Sex')),
                'ChestPainType': int(request.POST.get('ChestPainType')),
                'RestingBP': int(request.POST.get('RestingBP')),
                'Cholesterol': int(request.POST.get('Cholesterol')),
                'FastingBS': int(request.POST.get('FastingBS')),
                'RestingECG': int(request.POST.get('RestingECG')),
                'MaxHR': int(request.POST.get('MaxHR')),
                'ExerciseAngina': int(request.POST.get('ExerciseAngina')),
                'Oldpeak': float(request.POST.get('Oldpeak')),
                'ST_Slope': int(request.POST.get('ST_Slope')),
            }

            # Convertimos en formato esperado por el API Flask (features como lista)
            features = list(datos.values())
            payload = {'features': features}

            # Llamada al API Flask en puerto 9080
            response = requests.post('http://127.0.0.1:9080/predict', json=payload)

            # Procesamos la respuesta
            if response.status_code == 200:
                resultado = response.json().get('prediction')
            else:
                error = f'Error API Flask: {response.status_code}'

        except Exception as e:
            error = str(e)

    return render(request, 'predicciones/index.html', {'resultado': resultado, 'error': error})

