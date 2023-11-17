#!/usr/bin/env python
# coding: utf-8

# In[ ]:


horas = int(input("Ingresar las horas trabajadas: "))
tarifa_por_hora = int(input("Ingresar la tarifa: "))
if horas <= 35:
    pago = (35*10)
    print("El pago semanal por ",horas," hora es $", pago)
else:
     print("Parámetros incorrectos")   


# In[ ]:


horas = int(input("Ingresar las horas trabajadas: "))
tarifa_por_hora = int(input("Ingresar la tarifa: "))
if horas >= 47:
    extras = horas - 47
    hextras = float (extras * (pago * 0.5)) * (.10)
    pago = (47*8) + (extras * (pago * 0.5))
    print("El pago semanal por ",horas," hora es $", pago)
    print("Horas extras trabajadas: ", extras)
    print("El sueldo extra es: $", int(extras * (pago * 0.5)))
    print("El aumento extra es: $", (extras * (pago * 0.5)) * (.10))
else:
    pago = horas * 8
    print("Parámetro incorrecto")


# In[ ]:


horas = int(input("Ingresar las horas trabajadas: "))
tarifa_por_hora = int(input("Ingresar la tarifa: "))
if horas >= 47:
    extras = horas - 47
    hextras = float (extras * (pago * 0.5)) * (.20)
    pago = (47*8) + (extras * (pago * 0.5))
    print("El pago semanal por ",horas," hora es $", pago)
    print("Horas extras trabajadas: ", extras)
    print("El sueldo extra es: $", int(extras * (pago * 0.5)))
    print("El aumento extra es: $", (extras * (pago * 0.5)) * (.20))
else:
    pago = horas * 8
    print("Parámetro incorrecto")

