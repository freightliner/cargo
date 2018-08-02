from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from .BaseBL import BaseBL
from tms.models import Sec


class SecBL(BaseBL):

    def next(self, s):
        sid = transaction.savepoint()
        try:
            sec = Sec.objects.get(seccod = s)
        except ObjectDoesNotExist:
            sec = Sec(seccod = s, secval = 0)
            sec.save()
        sec = Sec.objects.get(seccod = s)
        sec.secval += 1
        sec.save()
        transaction.savepoint_commit(sid)
        return sec.secval
            