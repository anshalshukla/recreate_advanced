from django.shortcuts import render, redirect
from .models import Question, Options, AnswerKey, ResponseSheet


def QuestionBlock(request, **kwargs):
    if request.method == "POST":
        response = request.POST["response"]
    question = Question.objects.get(id=int(kwargs["pk"]))
    choice = Options.objects.filter(question=question)
    context = {"question": question, "choice": choice}
    return render(request, "quizApi/index.html", context)


def BuildQuestion(request):
    if request.method == "POST":
        question = request.POST["question"]
        option1 = request.POST["option1"]
        option2 = request.POST["option2"]
        option3 = request.POST["option3"]
        option4 = request.POST["option4"]
        marks = request.POST["marks"]
        negativeMarks = request.POST["negative marks"]
        subject = request.POST["subject"]
        q = Question(
            question=question, marks=marks, negativeMarks=negativeMarks, subject=subject
        )
        q.save()
        c1 = Options(question=q, choice=option1)
        c2 = Options(question=q, choice=option2)
        c3 = Options(question=q, choice=option3)
        c4 = Options(question=q, choice=option4)
        c1.save()
        c2.save()
        c3.save()
        c4.save()
        ans = request.POST["answer"]
        if ans == "option1":
            op = c1
        elif ans == "option2":
            op = c2
        elif ans == "option3":
            op = c3
        else:
            op = c4

        ans = AnswerKey(question=q, answer=op)
        ans.save()

        return redirect(f"question/{q.pk}")
    return render(request, "quizApi/buildQuestion.html")

