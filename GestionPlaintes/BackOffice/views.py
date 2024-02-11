from UserPart.models import Problem, Subject,Keyword
from django.shortcuts import render, get_object_or_404
from .models import Problem, Message

def ViewInfo(request,problem_id):
    problem = Problem.objects.get(id=problem_id)
    context = {"title": "Responsable", "problem": problem}

    return render(request, "ViewInfo.html", context)


def back(request):
    problems = Problem.objects.all()
    subjects = Subject.objects.all()
    keyword = Keyword.objects.all()
    context = {"title": "Responsable", "problems": problems, "subjects": subjects, "keyword": keyword}

    return render(request, "BackOffice.html", context)


def feedback(request, problem_id):
    problems = Problem.objects.all()
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == 'POST':
        user = request.user
        content = "Votre demande à été prise en compte"
        message = Message.objects.create(user=user, problem=problem, content=content)
        problem.changer_etat_en_cours()

        return render(request, "BackOffice.html", {'title': "Responsable", "problems": problems})
    else:
        return render(request, 'BackOffice.html', {'problem': problem})


def cloturer(request, problem_id):
    problems = Problem.objects.all()
    context = {"title": "Responsable", "problems": problems}
    problem = Problem.objects.get(id=problem_id)

    if request.method == 'POST':
        user = request.user
        content = "Votre demande à été cloturé."
        message = Message.objects.create(user=user, problem=problem, content=content)
        problem.changer_etat_en_cours()
        problem.changer_etat_termine()

    return render(request, "BackOffice.html", context)



