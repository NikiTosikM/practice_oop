from datetime import datetime


class Bank:
    __percentage_contribution = 5 

    def __init__(self, name, last_name, amount_deposit, date_deposit):
        self.__name = name
        self.__last_name = last_name
        self.__amount_deposit = amount_deposit
        self.__date_deposit = self.__checking_correctness_date(date_deposit)

    @staticmethod
    def __checking_correctness_date(date):
        if not isinstance(date, str):
            raise ValueError('Ошибка в дате. Неверный формат')
        try:
            day_month_year = datetime.strptime(date,  '%d.%m.%Y')
        except:
            raise ValueError('Введен неверный формат даты. Используйте ДД.ММ.ГГГГ')

        return day_month_year
    
    def __accrual_percentages(self, date):
        day_month_year = self.__checking_correctness_date(date)
        assert isinstance(day_month_year, datetime), 'В дате неверный формат'
        number_interest_accruals = (day_month_year - self.__date_deposit).days // 30
        amount_with_interest = self.__amount_deposit
        deposit_rate = self.__percentage_contribution / 100
        for _ in range(number_interest_accruals):
            amount_with_interest+= self.__amount_deposit * deposit_rate
            
        return amount_with_interest
  
    @property
    def balance(self):
        date = input('Введите дату в формате ДД.ММ.ГГГГ :  ')
        amount_with_interest = self.__accrual_percentages(date)
        return f'На счету {self.__name} {self.__last_name} {amount_with_interest}'

    @balance.setter
    def balance(self, how_much_withdraw):
        if not isinstance(how_much_withdraw, (int, float)):
            raise ValueError(
                'Ошибка при списании со счета. Указан неверный тип данных')
        elif how_much_withdraw > self.__amount_deposit:
            raise ValueError(
                'Нельзя списать данное количество денег. Проверьте сумму депозита')
        elif how_much_withdraw <= 0:
            raise ValueError(
                'Сумма списания не должна быть меньше или равна 0')

        self.__amount_deposit -= how_much_withdraw
        assert self.__amount_deposit > 0, 'Баланс депозита меньше 0'
        

if __name__ == '__main__':
    user1 = Bank('Никита', 'Марыков', 20000, '1.01.2024')
    print(user1.balance)
    user1.balance = 10000
    print(user1.balance)