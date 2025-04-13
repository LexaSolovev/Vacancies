class Salary:
    def __init__(self, salary_from=0, salary_to=0, currency='RUR'):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self) -> str:
        if self.salary_from and self.salary_to:
            return f'{self.salary_from} - {self.salary_to} {self.currency}'
        elif self.salary_from:
            return f'от {self.salary_from} {self.currency}'
        elif self.salary_to:
            return f'до {self.salary_to} {self.currency}'
        else:
            return 'Зарплата не указана'

    def __lt__(self, other) -> bool:
        if isinstance(other, self.__class__):
            if self.salary_from:
                if other.salary_from and self.salary_from != other.salary_from:
                    return self.salary_from < other.salary_from
                elif other.salary_to:
                    return self.salary_from < other.salary_to
                else:
                    return False
            elif self.salary_to:
                if other.salary_to:
                    return self.salary_to < other.salary_to
                elif other.salary_from:
                    return self.salary_to < other.salary_from
                else:
                    return False
            else:
                return True
        raise TypeError(f"Попытка некорректного сравнения объекта "
                        f"{self} c объектом {other}")

    def in_interval(self, salary_begin : int, salary_end : int) -> bool:
        if ((salary_begin <= self.salary_from) and (salary_end >= self.salary_from)) or ((salary_begin >= self.salary_from) and (salary_begin <= self.salary_to)):
            return True
        else:
            return False
