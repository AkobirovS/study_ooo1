from django.shortcuts import render
from main.models import Users
def index(request):

    text = Users.objects.all()
    #
    # users = Users.objects.update(name="Trump Administration to Lay Off Nearly All of U.S. Aid Agency’s Staff", content="""Officials for the agency were notified of the planned cuts on the same day they learned that about 800 awards and contracts administered through U.S.A.I.D. were being canceled, three people said.""")
    print(text)
    context = {
        "text": text
    }
    return render(request, "index.html",context)

