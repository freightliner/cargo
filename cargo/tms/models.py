import datetime

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
#
#
#class Question(models.Model):
#    question_text = models.CharField(max_length = 200)
#    pub_date = models.DateTimeField('Date published')
#    
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete = models.CASCADE)
#    choice_text = models.CharField(max_length = 200)
#    votes = models.IntegerField(default = 0)
#    

################################################################################
## SECUENCIAS
class Sec(models.Model):
    version = models.BigIntegerField(default = 0)
    seccod = models.CharField(_('seccod'), max_length = 20, primary_key = True)
    secval = models.BigIntegerField(_('secval'), default = 0)
    secfmt = models.CharField(_('secfmt'), max_length = 20, blank = True)

################################################################################
## VARIABLES INTERNAS
class Vin(models.Model):
    vincod = models.CharField(_('vincod'), max_length = 80, primary_key = True)
    vinalf = models.CharField(_('vinalf'), max_length = 80, blank = True)
    vinnum = models.DecimalField(_('vinnum'), max_digits = 15, decimal_places = 6, 
                                 default = 0)
    vinfec = models.DateField(_('vinfec'), default = datetime.date(1, 1, 1))

################################################################################
## IDIOMAS
class Lng(models.Model):
    lngcod = models.CharField(_('lngcod'), max_length = 2, primary_key = True)
    lngnom = models.CharField(_('lngnom'), max_length = 40, blank = True)
    lngdef = models.BooleanField(_('lngdef'), default = False)
    lngact = models.BooleanField(_('lngact'), default = True)
    
################################################################################
## MONEDAS
class Moa(models.Model):
    moacod = models.CharField(_('moacod'), max_length = 5, primary_key = True)
    moanom = models.CharField(_('moanom'), max_length = 40, blank = True)
    moadec = models.SmallIntegerField(_('moadec'), default = 2)
 
################################################################################
## MONEDAS, TIPO DE CAMBIO
class Mob(models.Model):
    mobcod = models.BigIntegerField(_('mobcod'), default = 0, primary_key = True)
    mobmoacod = models.ForeignKey(Moa, on_delete = models.PROTECT,
                                  db_column = 'mobmoacod')
    mobfec = models.DateField(_('mobfec'), default = datetime.date(1, 1, 1))
    mobrat = models.DecimalField(_('mobrat'), max_digits = 15, decimal_places = 6, 
                                 default = 0)

################################################################################
## ZONAS HORARIAS
class Tzn(models.Model):
    tzncod = models.CharField(_('tzncod'), max_length = 80, primary_key = True)
    tznabr = models.CharField(_('tznabr'), max_length = 5, blank = True)

################################################################################
## PAISES
class Pai(models.Model):
    paicod = models.CharField(_('paicod'), max_length = 2, primary_key = True)
    painom = models.CharField(_('painom'), max_length = 40, blank = True)
    paic3c = models.CharField(_('paic3c'), max_length = 3, blank = True)
    painum = models.SmallIntegerField(_('painum'), default = 0)
    
################################################################################
## ESTADOS
#
# De aplicación solo en aquellos países compuetos por diferentes estados
# como USA, UK, Canadá, etc, donde la dirección no está completa si no se 
# especifica.
#
class Est(models.Model):
    estcod = models.CharField(_('estcod'), max_length = 5, primary_key = True)
    estnom = models.CharField(_('estnom'), max_length = 40, blank = True)
    estpaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                               db_column = 'estpaicod')   
    
################################################################################
## POBLACIONES
class Pob(models.Model):
    pobcod = models.BigIntegerField(_('pobcod'), default = 0, primary_key = True)
    pobnom = models.CharField(_('pobnom'), max_length = 80)
    pobpaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                                  db_column = 'pobpaicod')
    pobestcod = models.ForeignKey(Est, on_delete = models.PROTECT, 
                                  null = True, db_column = 'pobestcod')
    pobtzncod = models.ForeignKey(Tzn, on_delete = models.PROTECT,
                                  db_column = 'pobtzncod')   
    pobloc = models.PointField(_('pobloc'), geography = True, spatial_index = True)
    
################################################################################
## CONCEPTOS DE FACTURACION
#class Cfa(models.Model):
#    cfacod = models.CharField(max_length = 10, primary_key = True)
#    cfanom = models.CharField(max_length = 40)
# 
################################################################################
## CLIENTES
class Cli(models.Model):
    clicod = models.IntegerField(_('clicod'), default = 0, primary_key = True)
    cliextcod = models.CharField(_('cliextcod'), max_length = 20, blank = True,
                                 db_index = True)
    
    clinom = models.CharField(_('clinom'), max_length = 80, blank = True, db_index = True)
    clinif = models.CharField(_('clinif'), max_length = 20, blank = True, db_index = True)
    clidir = models.CharField(_('clidir'), max_length = 80, blank = True)
    clipcp = models.CharField(_('clipcp'), max_length = 20, blank = True)
    clipob = models.CharField(_('clipob'), max_length = 80, blank = True)
    cliestcod = models.ForeignKey(Est, on_delete = models.PROTECT, null = True,
                               db_column = 'cliestcod')
    clipaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                               db_column = 'clipaicod')
    clitzncod = models.ForeignKey(Tzn, on_delete = models.PROTECT,
                                  db_column = 'pobtzncod')   
    cliloc = models.PointField(_('pobloc'), geography = True, spatial_index = True)
    clitlf = models.CharField(_('clitlf'), max_length = 20, blank = True)
    clifax = models.CharField(_('clifax'), max_length = 20, blank = True)
    clieml = models.EmailField(_('clieml'), blank = True)
    
    climoacod = models.ForeignKey(Moa, on_delete = models.PROTECT,
                                  db_column = 'climoacod')
    
    clida1 = models.CharField(_('clida1'), max_length = 20, blank = True)
    clida2 = models.CharField(_('clida2'), max_length = 20, blank = True)
    clida3 = models.CharField(_('clida3'), max_length = 20, blank = True)
    clida4 = models.CharField(_('clida4'), max_length = 20, blank = True)
#   
################################################################################
## PROVEEDORES
class Pro(models.Model):
    procod = models.IntegerField(_('procod'), default = 0, primary_key = True)
    proextcod = models.CharField(_('proextcod'), max_length = 20, blank = True,
                                 db_index = True)
    
    pronom = models.CharField(_('pronom'), max_length = 80, blank = True, db_index = True)
    pronif = models.CharField(_('pronif'), max_length = 20, blank = True, db_index = True)
    prodir = models.CharField(_('prodir'), max_length = 80, blank = True)
    propcp = models.CharField(_('propcp'), max_length = 20, blank = True)
    propob = models.CharField(_('propob'), max_length = 80, blank = True)
    proestcod = models.ForeignKey(Est, on_delete = models.PROTECT, null = True,
                               db_column = 'proestcod')    
    propaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                               db_column = 'propaicod')
    protzncod = models.ForeignKey(Tzn, on_delete = models.PROTECT,
                                  db_column = 'pobtzncod')   
    proloc = models.PointField(_('pobloc'), geography = True, spatial_index = True)
    protlf = models.CharField(_('protlf'), max_length = 20, blank = True)
    profax = models.CharField(_('profax'), max_length = 20, blank = True)
    proeml = models.EmailField(_('proeml'), blank = True)  

    promoacod = models.ForeignKey(Moa, on_delete = models.PROTECT,
                                  db_column = 'promoacod')

    proda1 = models.CharField(_('proda1'), max_length = 20, blank = True)
    proda2 = models.CharField(_('proda2'), max_length = 20, blank = True)
    proda3 = models.CharField(_('proda3'), max_length = 20, blank = True)
    proda4 = models.CharField(_('proda4'), max_length = 20, blank = True)
    
################################################################################
## DELEGACIONES
class Del(models.Model):
    delcod = models.CharField(_('delcod'), max_length = 5, primary_key = True)
    
    delnom = models.CharField(_('delnom'), max_length = 80, blank = True, db_index = True)
    deldir = models.CharField(_('deldir'), max_length = 80, blank = True)
    delpcp = models.CharField(_('delpcp'), max_length = 20, blank = True)
    delpob = models.CharField(_('delpob'), max_length = 80, blank = True)
    delestcod = models.ForeignKey(Est, on_delete = models.PROTECT, null = True,
                               db_column = 'delestcod')    
    delpaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                               db_column = 'delpaicod')
    deltzncod = models.ForeignKey(Tzn, on_delete = models.PROTECT,
                                  db_column = 'pobtzncod')   
    delloc = models.PointField(_('pobloc'), geography = True, spatial_index = True)
    deltlf = models.CharField(_('deltlf'), max_length = 20, blank = True)
    delfax = models.CharField(_('delfax'), max_length = 20, blank = True)
    deleml = models.EmailField(_('deleml'), blank = True)       
    
    delkvs = models.IntegerField(_('delkvs'), default = 0)                      # kilómetros vacíos de salida
    delbps = models.DecimalField(_('delbps'), max_digits = 13,                  # beneficio/pérdida de salida
                                 decimal_places = 2, default = 0)    

################################################################################
## DELEGACIONES, REGLAS
class Dem(models.Model):
    demcod = models.BigIntegerField(_('demcod'), primary_key = True)

    demdelcod = models.ForeignKey(Del, on_delete = models.PROTECT,
                               db_column = 'demdelcod')
    dempcp = models.CharField(_('demnom'), max_length = 20)

################################################################################
## DIRECCIONES
class Dda(models.Model):
    ddacod = models.BigIntegerField(_('ddacod'), primary_key = True)

    ddanom = models.CharField(_('ddanom'), max_length = 80, blank = True, db_index = True)
    ddadir = models.CharField(_('ddadir'), max_length = 80, blank = True)
    ddapcp = models.CharField(_('ddapcp'), max_length = 20, blank = True)
    ddapob = models.CharField(_('ddapob'), max_length = 80, blank = True)
    ddaestcod = models.ForeignKey(Est, on_delete = models.PROTECT, null = True,
                               db_column = 'ddaestcod')    
    ddapaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
                               db_column = 'ddapaicod')
    ddatzncod = models.ForeignKey(Tzn, on_delete = models.PROTECT,
                                  db_column = 'pobtzncod')   
    ddapol = models.PolygonField(_('ddapol'), geography = True, spatial_index = True)
    ddatlf = models.CharField(_('ddatlf'), max_length = 20, blank = True)
    ddafax = models.CharField(_('ddafax'), max_length = 20, blank = True)
    ddaeml = models.EmailField(_('ddaeml'), blank = True)       
#
################################################################################
## DIRECCIONES POR CLIENTE
class Ddb(models.Model):
    ddbcod = models.BigIntegerField(_('ddbcod'), primary_key = True)
    
    ddbclicod = models.ForeignKey(Cli, on_delete = models.PROTECT,
                                  db_column = 'ddbclicod')  
    ddbextcod = models.CharField(_('ddbextcod'), max_length = 20)
    
    ddbddacod = models.ForeignKey(Dda, on_delete = models.PROTECT,
                                  db_column = 'ddbddacod') 
    
################################################################################
## CLASES DE TRANSPORTE
class Tct(models.Model):
    tctcod = models.CharField(_('tctcod'), max_length = 5, primary_key = True)
    tctnom = models.CharField(_('tctnom'), max_length = 40)

    tctact = models.BooleanField(_('tctact'), default = True)
    
################################################################################
## CLASES DE EXPEDICIÓN
class Tce(models.Model):
    tcecod = models.CharField(_('tcecod'), max_length = 5, primary_key = True)
    tcenom = models.CharField(_('tcenom'), max_length = 40)
    
    tcedimlar = models.DecimalField(_('tcedimlar'), max_digits = 13, decimal_places = 3, 
                                    default = 0)
    tcedimpes = models.DecimalField(_('tcedimpes'), max_digits = 13, decimal_places = 3, 
                                    default = 0)
   
    tcefrg = models.BooleanField(_('tcefrg'), default = False)
    tcefrgset = models.DecimalField(_('tcefrgset'), max_digits = 5, decimal_places = 2, 
                                    default = 0)
    tcefrgmin = models.DecimalField(_('tcefrgmin'), max_digits = 5, decimal_places = 2, 
                                    default = 0)
    tcefrgmax = models.DecimalField(_('tcefrgmax'), max_digits = 5, decimal_places = 2, 
                                    default = 0)    
    
    tcetctcod = models.ForeignKey(Tct, on_delete = models.PROTECT, null = True,
                               db_column = 'tcetctcod')
        
    tceact = models.BooleanField(_('tceact'), default = True)

################################################################################
## ESTADOS OPERATIVOS
#class Teo(models.Model):
#    teocod = models.CharField(max_length = 5, primary_key = True)
#    teonom = models.CharField(max_length = 40)
#    teotip = models.IntegerField(default = 0)                                   # 
#
################################################################################
## ALBARANES
#class Taa(models.Model):
#    version = models.BigIntegerField(default = 0)
#    taacod = models.BigIntegerField(primary_key = True)
#    
#    taaclicod = models.ForeignKey(Cli, on_delete = models.PROTECT,
#                                  db_column = 'taaclicod')
#    taaclinom = models.CharField(max_length = 80, blank = True, db_index = True)
#    taaclinif = models.CharField(max_length = 20, blank = True, db_index = True)
#    
#    taateocod = models.ForeignKey(Teo, on_delete = models.PROTECT,
#                                  db_column = 'taateocod')
#    taaexp = models.BooleanField(default = False)
#
#    taasr1 = models.CharField(max_length = 20, blank = True)
#    taasr2 = models.CharField(max_length = 20, blank = True)
#    taasr3 = models.CharField(max_length = 20, blank = True)
#    taasr4 = models.CharField(max_length = 20, blank = True)
#    
#    taadimlar = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    taadimanc = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    taadimalt = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    taadimvol = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    taadimpes = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    taadimbul = models.IntegerField(default = 0)   
#    
#    taafrg = models.BooleanField(default = False)
#    taafrgset = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    taafrgmin = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    taafrgmax = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    
#    taada1 = models.CharField(max_length = 20, blank = True)
#    taada2 = models.CharField(max_length = 20, blank = True)
#    taada3 = models.CharField(max_length = 20, blank = True)
#    taada4 = models.CharField(max_length = 20, blank = True)    
#
################################################################################
## EXPEDICIONES
#class Tea(models.Model):
#    version = models.BigIntegerField(default = 0)
#    teacod = models.BigIntegerField(primary_key = True)
#    
#    teaclicod = models.ForeignKey(Cli, on_delete = models.PROTECT,
#                                  db_column = 'teaclicod')
#    teaclinom = models.CharField(max_length = 80, blank = True, db_index = True)
#    teaclinif = models.CharField(max_length = 20, blank = True, db_index = True)
#
#    teateocod = models.ForeignKey(Teo, on_delete = models.PROTECT,
#                                  db_column = 'teateocod')    
#    teaexp = models.BooleanField(default = False)
#    
#    teasr1 = models.CharField(max_length = 20, blank = True)
#    teasr2 = models.CharField(max_length = 20, blank = True)
#    teasr3 = models.CharField(max_length = 20, blank = True)
#    teasr4 = models.CharField(max_length = 20, blank = True)
#        
#    teadimlar = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    teadimanc = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    teadimalt = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    teadimvol = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    teadimpes = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    teadimbul = models.IntegerField(default = 0)    
#
#    teafrg = models.BooleanField(default = False)
#    teafrgset = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    teafrgmin = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    teafrgmax = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    
#    teada1 = models.CharField(max_length = 20, blank = True)
#    teada2 = models.CharField(max_length = 20, blank = True)
#    teada3 = models.CharField(max_length = 20, blank = True)
#    teada4 = models.CharField(max_length = 20, blank = True)    
#
#class Teb(models.Model):
#    tebcod = models.BigIntegerField(default = 0)
#    tebteacod = models.OneToOneField(Tea, on_delete = models.PROTECT)
#    
#    tebtpatot = models.SmallIntegerField(default = 0)
#    tebtpapdt = models.SmallIntegerField(default = 0)
#    
#    
#    
#    
#    
#    
#
################################################################################
## TRANSPORTES
#class Tta(models.Model):
#    version = models.BigIntegerField(default = 0)
#    ttacod = models.BigIntegerField(primary_key = True)
#    
#    ttaprocod = models.ForeignKey(Pro, on_delete = models.PROTECT,
#                                  db_column = 'ttaprocod')
#    ttapronom = models.CharField(max_length = 80, blank = True, db_index = True)
#    ttapronif = models.CharField(max_length = 20, blank = True, db_index = True)
#    
#    ttaexp = models.BooleanField(default = False)
#    
#    ttasr1 = models.CharField(max_length = 20, blank = True)
#    ttasr2 = models.CharField(max_length = 20, blank = True)
#    ttasr3 = models.CharField(max_length = 20, blank = True)
#    ttasr4 = models.CharField(max_length = 20, blank = True)
#    
#    ttadimlar = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    ttadimanc = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    ttadimalt = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    ttadimvol = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    ttadimpes = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    ttadimbul = models.IntegerField(default = 0)
#    
#    ttafrg = models.BooleanField(default = False)
#    ttafrgset = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    ttafrgmin = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    ttafrgmax = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
#    
#    ttada1 = models.CharField(max_length = 20, blank = True)
#    ttada2 = models.CharField(max_length = 20, blank = True)
#    ttada3 = models.CharField(max_length = 20, blank = True)
#    ttada4 = models.CharField(max_length = 20, blank = True)
#
################################################################################
## PARADAS    
#class Tpa(models.Model):
#    version = models.BigIntegerField(default = 0)
#    tpacod = models.BigIntegerField(primary_key = True)
#    
#    tpaclicod = models.ForeignKey(Cli, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpaclicod')    
#    tpateacod = models.ForeignKey(Tea, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpateacod')
#    tpataacod = models.ForeignKey(Taa, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpataacod')
#    tpaprocod = models.ForeignKey(Pro, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpaprocod')        
#    tpattacod = models.ForeignKey(Tta, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpattacod')
#    
#    tpatid = models.CharField(max_length = 20, blank = True)                    # tracking id
#    tpaxcl = models.BooleanField(default = False)                               # excluido
#    
#    tpasr1 = models.CharField(max_length = 20, blank = True)
#    tpasr2 = models.CharField(max_length = 20, blank = True)
#    tpasr3 = models.CharField(max_length = 20, blank = True)
#    tpasr4 = models.CharField(max_length = 20, blank = True)
#    
#    tpaddacod = models.ForeignKey(Dda, on_delete = models.PROTECT, null = True,
#                                  db_column = 'tpaddacod') 
#    tpaextcod = models.CharField(max_length = 20)  
#    tpanom = models.CharField(max_length = 80, blank = True, db_index = True)
#    tpadir = models.CharField(max_length = 80, blank = True)
#    tpapcp = models.CharField(max_length = 20, blank = True)
#    tpapob = models.CharField(max_length = 80, blank = True)
#    tpaestcod = models.ForeignKey(Est, on_delete = models.PROTECT, null = True,
#                               db_column = 'tpaestcod')    
#    tpapaicod = models.ForeignKey(Pai, on_delete = models.PROTECT,
#                               db_column = 'tpapaicod')
#    tpatlf = models.CharField(max_length = 20, blank = True)
#    tpafax = models.CharField(max_length = 20, blank = True)
#    tpaeml = models.EmailField(blank = True)         
#    
#    tpacliseq = models.IntegerField(default = 0)
#    tpaclifec = models.DateField(default = datetime.date(1, 1, 1))
#    tpaclife0 = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaclife1 = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaclille = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpacliini = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaclifin = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaclicnf = models.BooleanField(default = False)
#    
#    tpaproseq = models.IntegerField(default = 0)
#    tpaprofec = models.DateField(default = datetime.date(1, 1, 1))
#    tpaprofe0 = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaprofe1 = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))    
#    tpaprolle = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaproini = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    tpaprofin = models.DateTimeField(default = datetime.datetime(1, 1, 1, minute = 1))
#    
#    tpadimlar = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    tpadimanc = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    tpadimalt = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    tpadimvol = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    tpadimpes = models.DecimalField(max_digits = 13, decimal_places = 3, default = 0)
#    tpadimbul = models.IntegerField(default = 0)
#
################################################################################
## ESTADOS ADMINISTRATIVOS
#class Fea(models.Model):
#    feacod = models.CharField(max_length = 5, primary_key = True)
#    feanom = models.CharField(max_length = 40)
#    featip = models.IntegerField(default = 0)                                   # tipo 0=Abierto, 1=Cerrado, 2=Facturado
#    
################################################################################
## FACTURA/ABONO DE CLIENTE
#class Ffc(models.Model):
#    ffccod = models.BigIntegerField(primary_key = True)
#    ffcextcod = models.CharField(max_length = 20)
#    
#    
################################################################################
## FACTURA/ABONO DE PROVEEDOR
#class Ffp(models.Model):
#    ffpcod = models.BigIntegerField(primary_key = True)
#    ffpextcod = models.CharField(max_length = 20)
#    
#    
################################################################################
## CONEPTOS A COBRAR
#class Fcc(models.Model):
#    version = models.BigIntegerField(default = 0)
#    fcccod = models.BigIntegerField(primary_key = True)
#    
#    fcccfacod = models.ForeignKey(Cfa, on_delete = models.PROTECT,
#                                  db_column = 'fcccfacod')
#    fccclicod = models.ForeignKey(Cli, on_delete = models.PROTECT,
#                                  db_column = 'fccclicod')
#    
#    fccffccod = models.ForeignKey(Ffc, on_delete = models.PROTECT, null = True,
#                                  db_column = 'fccffccod')
#    
#    fccfeacod = models.ForeignKey(Fea, on_delete = models.PROTECT,
#                                  db_column = 'fccfeacod')
#    fccexp = models.BooleanField(default = False)                               # Exportación
#    fccsig = models.BooleanField(default = 1)                                   # Factura o abono
#    fccref = models.CharField(max_length = 20, blank = True)
#    fccfec = models.DateField(default = datetime.date(1, 1, 1))
#    fccmoacod = models.ForeignKey(Moa, on_delete = models.PROTECT,
#                                  db_column = 'fccmoacod')
#    fccrat = models.DecimalField(max_digits = 13, decimal_places = 6)
#    
#    fcccan = models.DecimalField(max_digits = 13, decimal_places = 3)
#    fccpor = models.DecimalField(max_digits = 5, decimal_places = 2)
#    
#    fccpun = models.DecimalField(max_digits = 13, decimal_places = 5)
#    fccpor = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fccdto = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fccnet = models.DecimalField(max_digits = 13, decimal_places = 2) 
#    fcctot = models.DecimalField(max_digits = 13, decimal_places = 2)
#    
#    fccsispun = models.DecimalField(max_digits = 13, decimal_places = 5)
#    fccsispor = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fccsisdto = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fccsisnet = models.DecimalField(max_digits = 13, decimal_places = 2) 
#    fccsistot = models.DecimalField(max_digits = 13, decimal_places = 2)
#    
################################################################################
## CONCEPTOS A PAGAR
#class Fcp(models.Model):
#    version = models.BigIntegerField(default = 0)
#    fcpcod = models.BigIntegerField(primary_key = True)
#    
#    fcpcfacod = models.ForeignKey(Cfa, on_delete = models.PROTECT,
#                                  db_column = 'fcpcfacod')
#    fcpprocod = models.ForeignKey(Pro, on_delete = models.PROTECT,
#                                  db_column = 'fcpprocod')
#    
#    fcpffpcod = models.ForeignKey(Ffp, on_delete = models.PROTECT, null = True,
#                                  db_column = 'fcpffpcod')
#    
#    fcpfeacod = models.ForeignKey(Fea, on_delete = models.PROTECT,
#                                  db_column = 'fcpfeacod')
#    fcpexp = models.BooleanField(default = False)                               # Exportación
#    fcpsig = models.IntegerField(default = 1)
#    fcpref = models.CharField(max_length = 20, blank = True)
#    fcpfec = models.DateField(default = datetime.date(1, 1, 1))
#    fcpmoacod = models.ForeignKey(Moa, on_delete = models.PROTECT,
#                                  db_column = 'fcpmoacod')
#    fcprat = models.DecimalField(max_digits = 13, decimal_places = 6)
#    
#    fcpcan = models.DecimalField(max_digits = 13, decimal_places = 3)
#    fcppor = models.DecimalField(max_digits = 5, decimal_places = 2)
#    
#    fcppun = models.DecimalField(max_digits = 13, decimal_places = 5)
#    fcppor = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fcpdto = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fcpnet = models.DecimalField(max_digits = 13, decimal_places = 2) 
#    fcptot = models.DecimalField(max_digits = 13, decimal_places = 2)
#    
#    fcpsispun = models.DecimalField(max_digits = 13, decimal_places = 5)
#    fcpsispor = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fcpsisdto = models.DecimalField(max_digits = 13, decimal_places = 2)
#    fcpsisnet = models.DecimalField(max_digits = 13, decimal_places = 2) 
#    fcpsistot = models.DecimalField(max_digits = 13, decimal_places = 2)
#    
#    
#    