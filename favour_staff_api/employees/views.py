# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern

class StaffRoleView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()

        roles = [{"name": m.full_name, "role": m.get_role()} for m in managers]
        roles += [{"name": i.full_name, "role": i.get_role()} for i in interns]

        return Response(roles)