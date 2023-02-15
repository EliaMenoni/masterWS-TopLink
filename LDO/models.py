from django.db import models

class Log(models.Model):
    ID = models.AutoField(name="ID", primary_key=True)
    time = models.DateTimeField(name="Timestamp", auto_now=True)
    user = models.CharField(name="User", max_length=50)
    input = models.TextField(name="Input", blank=True)
    result = models.TextField(name="Output", blank=True)
    status = models.BooleanField(name="Stato", default=True)
    error_code = models.IntegerField(name="Error Code", default=0)
    error_message = models.TextField(name="Error Message", blank=True)

    def __str__(self):
        if self.status == 'OK':
            return "[" + self.time + "] " + self.user + " - " + self.status
        else:
            return "[" + self.time + "] " + self.user + " - " + self.status + " [" + self.error_code + "]"


class LDO(models.Model):
    """
        LDO data class
    """
    NOSOLOGICO = models.CharField(max_length=20, null=True)
    COD_SERVIZIO = models.CharField(max_length=20, null=True)
    DATA_DIMISSIONE = models.DateField(auto_now=False)
    DATA_DIMISSIONE_VC = models.CharField(max_length=10, null=True)
    ORARIO_DIMISSIONE = models.CharField(max_length=5, null=True)
    DIAGNOSI = models.TextField(null=True)
    ANAMNESI = models.TextField(null=True)
    ESAME_OBIETTIVO = models.TextField()
    DECORSO = models.TextField()
    TERAPIA = models.TextField()
    INDICAZIONI = models.TextField()
    STILE_DI_VITA = models.CharField(max_length=500, null=True)
    STILE_DI_VITA_VALORE = models.CharField(max_length=4000, null=True)
    DIETA = models.CharField(max_length=500, null=True)
    DIETA_VALORE = models.CharField(max_length=4000, null=True)
    PROBLEMI_DOMICILIARI = models.CharField(max_length=500, null=True)
    EDUCAZIONE_PAZIENTE = models.CharField(max_length=500, null=True)
    EDUCAZIONE_PAZIENTE_VALORE = models.CharField(max_length=4000, null=True)
    DESTINAZIONE_DIM = models.CharField(max_length=100, null=True)
    DESTINAZIONE_DIM_VALORE = models.CharField(max_length=4000, null=True)
    RICHIESTA_PRESIDI = models.CharField(max_length=100, null=True)
    RICHIESTA_PRESIDI_VALORE = models.CharField(max_length=4000, null=True)
    PROGRAMMA = models.TextField()
    COD_MEDICO = models.CharField(max_length=20, null=True)
    DATA_MODIFICA = models.DateField(auto_now=False)
    MOD_UTENTE = models.CharField(max_length=20, null=True)
    WS_UTENTE = models.CharField(max_length=50, null=True)
    COD_UTENTE_VALIDAZIONE = models.CharField(max_length=20, null=True)
    DATA_VALIDAZIONE = models.DateField()
    PROTETTA = models.TextField()
    INTERVENTI = models.TextField()
    ESAMI_EMATOCHIMICI = models.TextField()
    ESAMI_STRUMENTALI = models.TextField()
    ALLERGIE = models.TextField()
    PROFILASSI = models.CharField(max_length=100, null=True)
    PROFILASSI_VALORE = models.CharField(max_length=4000, null=True)
    ESAMI_IN_CORSO = models.CharField(max_length=500, null=True)
    CONDIZIONI = models.CharField(max_length=100, null=True)
    CONDIZIONI_VALORE = models.CharField(max_length=4000, null=True)
    CANNULE_NASALI = models.IntegerField(max_length=1, null=True)
    CANNULE_NASALI_LMIN= models.IntegerField(max_length=3, null=True)
    MASCHERA_VENTURI = models.IntegerField(max_length=1, null=True)
    MASCHERA_VENTURI_FIO2 = models.IntegerField(max_length=3, null=True)
    MASCHERA_VENTURI_LMIN = models.IntegerField(max_length=3, null=True)
    CPAP = models.IntegerField(max_length=1, null=True)
    CPAP_PEEP_MMHG = models.IntegerField(max_length=3, null=True)
    CPAP_LMIN = models.IntegerField(max_length=3, null=True)
    BPAP = models.IntegerField(max_length=1, null=True)
    BPAP_IPAP_MMHG = models.IntegerField(max_length=3, null=True)
    BPAP_EPAP_MMHG = models.IntegerField(max_length=3, null=True)
    BPAP_LMIN = models.IntegerField(max_length=3, null=True)
    STR_STR = models.CharField(max_length=5, null=True)
    RIC_ANNO = models.CharField(max_length=4, null=True)
    RIC_CARTELLA = models.CharField(max_length=8, null=True)
    NOSOLOGICO_1 = models.CharField(max_length=17, null=True)
    DATA_RICOVERO = models.DateField(auto_now=False)
    DIAGNOSI_RICOVERO = models.CharField(max_length=4000, null=True)
    REP_REPARTO_ACC = models.CharField(max_length=10, null=True)
    REP_SEZIONE_ACC = models.CharField(max_length=4, null=True)
    COGNOME = models.CharField(max_length=50, null=True)
    NOME = models.CharField(max_length=50, null=True)
    SESSO = models.CharField(max_length=1, null=True)
    DATA_NASCITA = models.DateField(auto_now=False)
    DATA_NASCITA_VC = models.CharField(max_length=10, null=True)
    COD_FISCALE = models.CharField(max_length=16, null=True)
    COD_COM_NASCITA = models.CharField(max_length=6, null=True)
    COD_COM_RESIDENZA = models.CharField(max_length=6, null=True)
    COD_NAZIONE = models.CharField(max_length=8, null=True)
    INDIRIZZO_RESIDENZA = models.CharField(max_length=60, null=True)
    NUMCIV_RESIDENZA = models.CharField(max_length=10, null=True)
    CAP_RESIDENZA = models.CharField(max_length=5, null=True)
    TELEFONO = models.CharField(max_length=61, null=True)
    COD_ASL = models.CharField(max_length=6, null=True)
    DATA_DIMISSIONE_1 = models.DateField(auto_now=False)
    DESC_REPARTO = models.CharField(max_length=60, null=True)
    DATA_RICOVERO_1 = models.DateField(auto_now=False)
    DATA_RICOVERO_VC = models.CharField(max_length=10, null=True)
    EQUIPE = models.CharField(max_length=4000, null=True)
    PROGRESSIVO = models.IntegerField(max_length=3, null=False)
    COD_SERVIZIO_1 = models.CharField(max_length=10, null=False)
    DATA_INIZIO = models.DateField(auto_now=False, null=False)
    DATA_FINE = models.DateField(auto_now=False)
    RIGA1 = models.CharField(max_length=100, null=True)
    FONT_RIGA1 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA1 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA1 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA1 = models.IntegerField(max_length=1, null=True)
    RIGA2 = models.CharField(max_length=100, null=True)
    FONT_RIGA2 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA2 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA2 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA2 = models.IntegerField(max_length=1, null=True)
    RIGA3 = models.CharField(max_length=100, null=True)
    FONT_RIGA3 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA3 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA3 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA3 = models.IntegerField(max_length=1, null=True)
    RIGA4 = models.CharField(max_length=100, null=True)
    FONT_RIGA4 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA4 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA4 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA4 = models.IntegerField(max_length=1, null=True)
    RIGA5 = models.CharField(max_length=100, null=True)
    FONT_RIGA5 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA5 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA5 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA5 = models.IntegerField(max_length=1, null=True)
    RIGA6 = models.CharField(max_length=100, null=True)
    FONT_RIGA6 = models.CharField(max_length=50, null=True)
    FONT_SIZE_RIGA6 = models.IntegerField(max_length=2, null=True)
    GRASSETTO_RIGA6 = models.IntegerField(max_length=1, null=True)
    CORSIVO_RIGA6 = models.IntegerField(max_length=1, null=True)
    LOGO_SINISTRA = models.IntegerField(max_length=1, null=True)
    LOGO_DESTRA = models.IntegerField(max_length=1, null=True)
    DATA_MODIFICA_1 = models.DateField(auto_now=False, null=False)
    MOD_UTENTE_1 = models.CharField(max_length=20, null=False)
    WS_UTENTE_1 = models.CharField(max_length=50, null=False)
    COGNOME_FIRMA = models.CharField(max_length=50, null=True)
    NOME_FIRMA = models.CharField(max_length=50, null=True)

    class Meta:
        managed = False
