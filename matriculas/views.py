from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Perfil, Docente, Estudiante, Matricula
from .forms import Formularioperfil,Formulariodocente,Formularioestudiante,Formulariomatricula
# Create your views here.

class Viendomatricula(PermissionRequiredMixin, ListView):
    permission_required = 'matriculas.view_matricula'
    login_url = 'login'
    model=Matricula
    template_name = 'vermatricula.html'

    def get_queryset(self):
        queryset = super(Viendomatricula, self).get_queryset()

        if self.request.user.groups.filter(name="Estudiante").exists():
            queryset = queryset.filter(estudiante__user=self.request.user)
        if self.request.user.groups.filter(name="Matricula").exists():
            queryset = queryset.filter(matricula__user=self.request.user)

        return queryset


class Viendodocente(PermissionRequiredMixin, ListView):
    permission_required = 'matriculas.view_docente'
    login_url = 'login'
    model=Docente
    template_name = 'verdocente.html'

    def get_queryset(self):
        queryset=super(Viendodocente, self).get_queryset()

        if self.request.user.groups.filter(name="Estudiante").exists():
            queryset=queryset.filter(estudiante__user=self.request.user)
        if self.request.user.groups.filter(name="Matricula").exists():
            queryset=queryset.filter(matricula__user=self.request.user)



        return queryset

class Viendoestudiante(PermissionRequiredMixin, ListView):
    permission_required = 'matriculas.view_estudiante'
    login_url = 'login'
    model = Estudiante
    template_name = 'verestudiante.html'

    def get_queryset(self):
        queryset = super(Viendoestudiante, self).get_queryset()

        if self.request.user.groups.filter(name="Estudiante").exists():
            queryset = queryset.filter(estudiante__user=self.request.user)
        if self.request.user.groups.filter(name="Matricula").exists():
            queryset = queryset.filter(matricula__user=self.request.user)

        return queryset


class Viendoperfil(PermissionRequiredMixin, ListView):
    permission_required = 'matriculas.view_perfil'
    login_url = 'login'
    model=Perfil
    template_name = 'verperfil.html'

    def get_queryset(self):
        queryset = super(Viendoperfil, self).get_queryset()

        if self.request.user.groups.filter(name="Estudiante").exists():
            queryset = queryset.filter(estudiante__user=self.request.user)
        if self.request.user.groups.filter(name="Matricula").exists():
            queryset = queryset.filter(matricula__user=self.request.user)

        return queryset


class Editperfil(UpdateView):
    model = Perfil
    form_class = Formularioperfil
    template_name = 'editperfil.html'
    success_url = '/verperfil'

    def form_valid(self, form):
        form.save()
        return super ().form_valid(form)

class Insertarperfil(FormView):
    form_class = Formularioperfil
    template_name = 'insertarperfil.html'
    success_url = '/verperfil'

    def form_valid(self, form):
        form.save()
        return super ().form_valid(form)

class Editdocente(UpdateView):
     model = Docente
     form_class = Formulariodocente
     template_name = 'editdocente.html'
     success_url = '/verdocente'

     def form_valid(self, form):
         form.save()
         return super ().form_valid(form)

class Insertardocente(FormView):
    form_class = Formulariodocente
    template_name = 'insertardocente.html'
    success_url = '/verdocente'

    def form_valid(self, form):
        form.save()
        return super ().form_valid(form)


class Editestudiante(UpdateView):
    model = Estudiante
    form_class = Formularioestudiante
    template_name = 'editestudiante.html'
    success_url = '/verestudiante'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Insertarestudiante(FormView):
    form_class = Formularioestudiante
    template_name = 'insertarestudiante.html'
    success_url = '/verestudiante'

    def form_valid(self, form):
        form.save()
        return super ().form_valid(form)

class Editmatricula(UpdateView):
    model = Matricula
    form_class = Formulariomatricula
    template_name = 'editmatricula.html'
    success_url = '/vermatricula'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Insertarmatricula(FormView):
    form_class = Formulariomatricula
    template_name = 'insertarmatricula.html'
    success_url = '/vermatricula'

    def form_valid(self, form):
        form.save()
        return super ().form_valid(form)

class Elimperfil(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model =  Perfil
    template_name = 'elimperfil.html'
    success_url = '/verperfil'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimmatricula(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model =  Matricula
    template_name = 'elimmatricula.html'
    success_url = '/vermatricula'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimestudiante(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model =  Estudiante
    template_name = 'elimestudiante.html'
    success_url = '/verestudiante'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Elimdocente(LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model =  Docente
    template_name = 'elimdocente.html'
    success_url = '/verdocente'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)







