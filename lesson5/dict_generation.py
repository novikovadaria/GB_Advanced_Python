def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Alice", "Bob", "Charlie"]
salaries = [10000, 15000, 20000]
bonuses = ["10%", "15%", "20%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)