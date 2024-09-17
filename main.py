from heroClasses.heroesClasses import MyHero

if __name__ == "__main__":
    # Создаем героя с классом
    gendalf = MyHero("Гендальф", "маг")

    # Добавляем опыт, чтобы повысить уровень и выбрать навыки
    print(gendalf.add_exp(600))  # Достаточно опыта для уровня 2