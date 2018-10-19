import django
import os

from tms import models

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cargo.settings")
    django.setup()
    
    pai = models.Pai()
    
    ff = {}
    ff['paicod__contains'] = 'ES'
    
    pais = models.Pai.objects.filter(**ff)
    for pai in pais:
        print(pai.painom)
    
    pass
