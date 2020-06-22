from django.db import models

class Patient(models.Model):
    """患者管理用モデル"""
    name = models.CharField('患者名',max_length=255)
    birth = models.DateField('生年月日')
    # age_year = models.IntegerField('年齢_Y')
    # age_month = models.IntegerField('年齢_M')
    # age_day = models.IntegerField('年齢_D')

    def __str__(self):
        return self.name

class Appointment(models.Model):
    """予約管理用モデル"""
    bookDateTime = models.DateTimeField('予約日時')

    #verbose_nameは列名らしい。
    #on_deleteは参照先が消えたときに同時に消すかどうか、患者が消えれば予約も消えていい。
    patient = models.ForeignKey(Patient,verbose_name='患者',related_name='appointments',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient} / {self.bookDateTime}'


# class Setting(models.Model):
#     """設定管理用モデル"""