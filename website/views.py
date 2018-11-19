from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib import messages
from .forms import pessoaForm
from .models import *
import PyPDF2

def index(request):
    return render(request, 'index.html')

def vote(request):
    if request.method == 'POST':
        form = pessoaForm(request.POST or None)
        if form.is_valid():
            formEmail = form.cleaned_data['email_pessoa']
            form.save()
            return redirect(voting, email=form.cleaned_data['email_pessoa'])
        else:
            emailPessoa = request.POST.get('email_pessoa')
            checkEmail = pessoa.objects.get(email_pessoa=emailPessoa)
            if checkEmail.pessoa_votou == 1:
                messages.add_message(request, messages.ERROR, 'O e-mail apresentado já votou')

            else:
                return redirect(voting, email=checkEmail.email_pessoa)

    form = pessoaForm()
    return render(request, 'vote.html', {'form':form})

def voting(request,email):
    if request.method == 'POST':
        choose1 = request.POST['option1']
        choose2 = request.POST['option2']
        choose3 = request.POST['option3']
        choose4 = request.POST['option4']
        choose5 = request.POST['option5']
        choose6 = request.POST['option6']
        choose7 = request.POST['option7']
        choose8 = request.POST['option8']

        chooseObra1 = obra.objects.get(nome_obra=choose1)
        chooseObra2 = obra.objects.get(nome_obra=choose2)
        chooseObra3 = obra.objects.get(nome_obra=choose3)
        chooseObra4 = obra.objects.get(nome_obra=choose4)
        chooseObra5 = obra.objects.get(nome_obra=choose5)
        chooseObra6 = obra.objects.get(nome_obra=choose6)
        chooseObra7 = obra.objects.get(nome_obra=choose7)
        chooseObra8 = obra.objects.get(nome_obra=choose8)
        emailPerson = pessoa.objects.get(email_pessoa=email)
        pessoaSave = pessoaVoto.objects.create(pessoa=emailPerson, obra1=chooseObra1, obra2=chooseObra2, obra3=chooseObra3, obra4=chooseObra4, obra5=chooseObra5, obra6=chooseObra6, obra7=chooseObra7, obra8=chooseObra8)
        pessoaSave.save()

        person = pessoa.objects.get(email_pessoa=email)
        person.pessoa_votou=1
        person.save()

        votoNew1 = obra.objects.get(nome_obra=choose1)
        chooseCategory1 = request.POST['category1']
        chooseCat1 = category.objects.get(nome_category=chooseCategory1)

        votoNew2 = obra.objects.get(nome_obra=choose2)
        chooseCategory2 = request.POST['category2']
        chooseCat2 = category.objects.get(nome_category=chooseCategory2)

        votoNew3 = obra.objects.get(nome_obra=choose3)
        chooseCategory3 = request.POST['category3']
        chooseCat3 = category.objects.get(nome_category=chooseCategory3)

        votoNew4 = obra.objects.get(nome_obra=choose4)
        chooseCategory4 = request.POST['category4']
        chooseCat4 = category.objects.get(nome_category=chooseCategory4)

        votoNew5 = obra.objects.get(nome_obra=choose5)
        chooseCategory5 = request.POST['category5']
        chooseCat5 = category.objects.get(nome_category=chooseCategory5)

        votoNew6 = obra.objects.get(nome_obra=choose6)
        chooseCategory6 = request.POST['category6']
        chooseCat6 = category.objects.get(nome_category=chooseCategory6)

        votoNew7 = obra.objects.get(nome_obra=choose7)
        chooseCategory7 = request.POST['category7']
        chooseCat7 = category.objects.get(nome_category=chooseCategory7)

        votoNew8 = obra.objects.get(nome_obra=choose8)
        chooseCategory8 = request.POST['category8']
        chooseCat8 = category.objects.get(nome_category=chooseCategory8)

        votos = voto.objects.all()

        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose1:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew1).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose2:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew2).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose3:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew3).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose4:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew4).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose5:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew5).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose6:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew6).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose7:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew7).update(quantidadeVotos=votosNew)


        for votoss in votos:
            if votoss.obraVotada.nome_obra == choose8:
                votosNew = votoss.quantidadeVotos
                votosNew+=1
                voto.objects.filter(obraVotada=votoNew8).update(quantidadeVotos=votosNew)


        if request.method=='POST':

            return redirect(index)

    obras = obra.objects.all()

    return render(request, 'voting.html', {'obras':obras})

def error(request):
    return render(request, 'error404.html')
