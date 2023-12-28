from django.conf import settings
from django.db import transaction
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.exceptions import APIException

from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer
from assignments.tasks import task_execute


class AssignmentViewSet(viewsets.ModelViewSet):

    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                # save instance
                instance = serializer.save()
                instance.save()

                # create task params
                job_params = {"db_id": instance.id}

                # submit task for background execution
                transaction.on_commit(lambda: task_execute.delay(job_params))

        except Exception as e:
            raise APIException(str(e))


def indexView(request):
    print(settings.SECRET_KEY_WILSON)
    print("\n\n ---*-*-*-*-*-*-*")
    return HttpResponse("Bienvenidos al app base #2")
