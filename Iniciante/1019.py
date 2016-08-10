# -*- coding: utf-8 -*-

segundos_normal = int(input())
horas_normal = 3600
minutos_normal = 60
 
horas = int((segundos_normal/horas_normal))
minutos = int((segundos_normal % horas_normal) / minutos_normal)
segundos = int((segundos_normal % horas_normal) % minutos_normal)
 
print(str(horas) + ":" + str(minutos) + ":" + str(segundos))