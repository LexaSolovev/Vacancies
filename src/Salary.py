class Salary:
    def __init__(self, salary_from=0, salary_to=0, currency='RUR'):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self):
        if self.salary_from and self.salary_to:
            return f'{self.salary_from} - {self.salary_to} {self.currency}'
        elif self.salary_from:
            return f'{self.salary_from} {self.currency}'
        else:
            return 'Зарплата не указана'
