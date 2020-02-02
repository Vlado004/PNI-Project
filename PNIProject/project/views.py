from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import korisnici, predmeti, upisi

# Create your views here.

@login_required
def index(request):
    if request.method == 'GET':
        nazivi_predmeta = []
        svi_upisi = upisi.objects.all()
        upisani_predmeti = upisi.objects.filter(student_id=request.user.id)
        for predmet_id in upisani_predmeti.predmet_id:
            predmet = predmeti.objects.filter(id=predmet_id)
            nazivi_predmeta.append((predmet.ime, predmet.kod))
        #return render(request, 'insert_book.html', {'form':bookForm})

    elif request.method == 'POST':
        return redirect ('index')
