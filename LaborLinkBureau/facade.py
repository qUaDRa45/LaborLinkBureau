from datetime import date
from entities import Employer, Candidate, Vacancy, Deal
from repository import LaborLinkRepository

class LaborLinkFacade:
    def __init__(self):
        self.repo = LaborLinkRepository()

    def add_employer(self, company_name: str, industry: str, address: str, 
                     phone: str, email: str, description: str = ""):
        if not company_name or not email:
            raise ValueError("Название компании и Email обязательны!")
        
        employer = Employer(
            employer_id=len(self.repo.get_all("employers")) + 1,
            company_name=company_name,
            industry=industry,
            address=address,
            phone=phone,
            email=email,
            description=description
        )
        self.repo.add("employers", employer.__dict__)
        return f"✅ Работодатель '{company_name}' успешно добавлен."

    def add_candidate(self, full_name: str, birth_date: date, phone: str, email: str,
                      city: str, desired_salary: float, skills: str, experience_years: int, about: str = ""):
        if not full_name or not email:
            raise ValueError("ФИО и Email обязательны!")
        if desired_salary <= 0:
            raise ValueError("Желаемая зарплата должна быть больше 0.")

        candidate = Candidate(
            candidate_id=len(self.repo.get_all("candidates")) + 1,
            full_name=full_name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            city=city,
            desired_salary=desired_salary,
            skills=skills,
            experience_years=experience_years,
            about=about
        )
        self.repo.add("candidates", candidate.__dict__)
        return f"✅ Соискатель '{full_name}' успешно добавлен."

    def add_vacancy(self, title: str, description: str, salary_from: float, 
                    salary_to: float, requirements: str):
        if not title or salary_from <= 0:
            raise ValueError("Название вакансии и зарплата обязательны!")

        vacancy = Vacancy(
            vacancy_id=len(self.repo.get_all("vacancies")) + 1,
            title=title,
            description=description,
            salary_from=salary_from,
            salary_to=salary_to,
            requirements=requirements
        )
        self.repo.add("vacancies", vacancy.__dict__)
        return f"✅ Вакансия '{title}' успешно создана."

    def create_deal(self, candidate_id: int, vacancy_id: int, start_work_date: date, salary: float):
        if salary <= 0:
            raise ValueError("Зарплата должна быть больше 0.")

        deal_id = len(self.repo.get_all("deals")) + 1
        commission = round(salary * 0.10, 2)

        deal = Deal(
            deal_id=deal_id,
            deal_date=date.today(),
            start_work_date=start_work_date,
            salary=salary,
            commission=commission,
            contract_url=f"contract_{deal_id}.pdf"
        )
        self.repo.add("deals", deal.__dict__)
        return f"✅ Сделка №{deal_id} успешно оформлена! Комиссия: {commission} руб."