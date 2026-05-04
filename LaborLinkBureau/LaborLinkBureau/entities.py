from dataclasses import dataclass
from datetime import date

@dataclass
class Employer:
    employer_id: int
    company_name: str
    industry: str
    address: str
    phone: str
    email: str
    description: str = ""

@dataclass
class Candidate:
    candidate_id: int
    full_name: str
    birth_date: date
    phone: str
    email: str
    city: str
    desired_salary: float
    skills: str
    experience_years: int
    about: str = ""

@dataclass
class Vacancy:
    vacancy_id: int
    title: str
    description: str
    salary_from: float
    salary_to: float
    requirements: str
    status: str = "Открыта"

@dataclass
class Deal:
    deal_id: int
    deal_date: date
    start_work_date: date
    salary: float
    commission: float
    status: str = "Оформлена"
    contract_url: str = ""