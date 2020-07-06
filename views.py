from django.shortcuts import render, redirect
from .models import registros, algun_modelo_de_la_base_de_datos

def registro(request):

    if request.method == 'POST':
        covidd = request.POST.get('covidd','')
        habituales = request.POST.get('habituales', '')
        menos = request.POST.get('menos', '')
        graves = request.POST.get('graves', '')
        fecha = request.POST.get('fecha', '')

        if (menos== '' or graves=='' or habituales==''):
            return redirect('registro.html')
        else:
            nuevo_registro = registros()
            nuevo_registro.dia = fecha
            nuevo_registro.covid = covidd
            nuevo_registro.sintomas = habituales
            nuevo_registro.sintomas = menos
            nuevo_registro.sintomas = graves
            nuevo_registro.save()
            return redirect('estadistica.html')
    
    sintomass = {'habituales': ['Fiebre', 'Tos seca', 'Cansancio', 'Ninguno'],
                  'menos' : ['Molestias y Dolores', 'Dolor de Garganta', 'Diarrea', 'Conjuntivitis', 'Dolores de cabeza', 'Pérdida del olfato o del gusto', 'Erupciones cutáneas o pérdida del color en extremidades', 'Insuficiencia Respiratorias', 'Ninguno'],
                  'graves' : ['Dificultad para respirar o sensación de falta de aire', 'Dolor o presión en el pecho', 'Incapacidad para hablar o moverse', 'Ninguno']}
    return render(request, 'registro.html', sintomass)


def estadistica(request):
    return render(request, 'estadistica.html')



def formulario(request):
  if request.method == "POST":
    nombre = request.POST.get('nombre','')
    edad = request.POST.get('edad','')

    if(nombre != '' and edad != ''): 
      #Esto pasa si el usuario si completa toda la informacion
      edad = int(edad) #convertimos la edad de string a interger para poder hacer operaciones                                      matematicas si queremos

      if(edad >= 18):
        #esto pasa si el usurio es mayor de edad

        nuevo_registro = algun_modelo_de_la_base_de_datos() #importamos el modelo                                                                                                                "vacio"
        nuevo_registro.nombre = nombre #llenamos del nuevo registro
        nuevo_registro.edad = edad
        nuevo_registro.save() #guardamos el registro en la base de datos del modelo                                                               correspondiente

        return redirect('estadistica.html')

      else:
        #esto pasa si el usuario es menor de edad
        return redirect('estadistica.html')

    else:
      #Esto pasa si es usuario no completa toda la informacion del formulario
      return redirect('estadistica.html')

  else:
    return render(request, 'formulario.html')