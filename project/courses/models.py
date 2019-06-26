# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    CHOICES1 = (("Primavera", "Primavera"),("Otoño", "Otoño"),)
    CHOICES2 = ((1,1),(2, 2),)
    CHOICES3 = ((2018,2018),(2019, 2019),(2020,2020),(2021,2021),)
    title=models.CharField(max_length=200)

    # Llave primaria (no permitir nulls)
    code=models.CharField(max_length=20, blank=False, null=False)
    semester=models.CharField(choices=CHOICES1, default="Primavera", max_length=15, blank=False, null=False)
    section=models.IntegerField(choices=CHOICES2,default=1, blank=False, null=False)
    year=models.IntegerField(default=2019, blank=False, null=False)
    
    class Meta:
        unique_together= ('code', 'section', 'year', 'semester')

    def __str__(self):
        return self.title


class Team(models.Model):
    """Modelo que representa a los equipos"""
    name= models.CharField(max_length=200, help_text='Ingrese el nombre del equipo (Ej: ReAL Soluciones)')

    # Un equipo pertenece a lo más a un curso, pero un curso puede tener más de un equipo
    course= models.ForeignKey('Course', on_delete=models.CASCADE)

    class Meta:
        ordering= ['course', 'name']

    def __str__(self):
        return self.name


class Student(models.Model):
    """Modelo que representa a los estudiantes"""
    first_name = models.CharField(max_length=100, help_text='Ingrese el(los) nombre(s) del estudiante (Ej: Juan Pedro)')
    family_name = models.CharField(max_length=100,
                                   help_text='Ingrese el(los) apellido(s) del estudiante (Ej: Pérez González)')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('first_name', 'family_name')
        ordering = ['family_name', 'first_name']

    def __str__(self):
        return '{}, {}'.format(self.family_name, self.first_name)


class Student_Team(models.Model):
   """Modelo que representa la relacion entre estudiantes y equipos"""
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   team = models.ForeignKey(Team, on_delete=models.CASCADE)

   def __str__(self):
       return self.student.first_name + ' ' + self.student.family_name + '-' + self.team.name
