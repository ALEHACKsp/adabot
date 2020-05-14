from datetime import date
from datetime import datetime

class Bill:

    def __init__(self, description, value, expday):
        self.description = description
        self.value = float(value)
        self.expday = datetime.strptime(expday, '%d/%m/%Y').date()

    def __str__(self):
        return(f"Você tem a conta {self.description} no valor de R$ {self.value} com vencimento em {self.expday.strftime('%d/%m/%Y')}")

    def isNextExpiration(self, daysUntil):
        days = (self.expday - datetime.now().date()).days
        if days <= daysUntil:
            if days < 0:
                return(f"Sua conta {self.description}, no valor de R$ {self.value}, venceu há *{days * (-1)}* dias!")
            elif days == 0:
                return(f"Sua conta {self.description}, no valor de R$ {self.value}, vence *hoje*!")
            else:
                return(f"Sua conta {self.description}, no valor de R$ {self.value}, vencerá em *{days}* dias!")
        else:
            return("")