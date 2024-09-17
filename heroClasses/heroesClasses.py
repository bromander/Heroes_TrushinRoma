class Hero:
    """Базовый класс Hero с защищенными полями"""
    _mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    _warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    _ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name):
        """Конструктор класса с защищенными полями"""
        self._name = name
        self._my_hero_skills = []
        self._level = 0
        self._exp = 0

    # Геттеры для всех полей
    def get_name(self):
        return self._name

    def get_my_hero_skills(self):
        return self._my_hero_skills

    def get_level(self):
        return self._level

    def get_exp(self):
        return self._exp

    def get_skills(self, character_class):
        """Геттер для навыков в зависимости от выбранного класса"""
        if character_class == 'воин':
            return self._warrior_skills
        elif character_class == 'маг':
            return self._mage_skills
        elif character_class == 'рейнджер':
            return self._ranger_skills
        else:
            exit("Ошибка, перезапустите программу!")

    def get_new_level(self):
        if self._exp >= 1000:
            self._level = 3
            self.add_skill()
        elif self._exp >= 500:
            self._level = 2
            self.add_skill()
        elif self._exp >= 200:
            self._level = 1
            self.add_skill()
        else:
            self._level = 0
        return f"Герой {self._name}, теперь {self._level} уровня, навыки: {', '.join(self._my_hero_skills)}"

    def add_exp(self, exp):
        self._exp += exp
        new_level = self.get_new_level()
        return new_level


class MyHero(Hero):
    """Класс-наследник MyHero"""

    def __init__(self, name, character_class):
        """Инициализация с учетом класса персонажа"""
        super().__init__(name)
        self._character_class = character_class
        self._skill_list = self.get_skills(character_class)

    # Геттер для skill_list
    def get_skill_list(self):
        return self._skill_list

    def add_skill(self):
        """Добавление навыков в зависимости от уровня"""
        while self._level > len(self._my_hero_skills):
            print(f"Выберите навык из: {', '.join(self._skill_list)}")
            chosen_skill = input(">Введите навык: ")
            if chosen_skill in self._skill_list:
                self._my_hero_skills.append(chosen_skill)
                self._skill_list.remove(chosen_skill)

                print(f"Навык {chosen_skill} добавлен.")
            else:
                print("Неверный навык. Попробуйте снова.")

            # Прерывание цикла, если количество навыков соответствует уровню
            if len(self._my_hero_skills) == self._level:
                break