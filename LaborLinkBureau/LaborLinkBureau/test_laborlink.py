import unittest
from datetime import date
from facade import LaborLinkFacade


class TestLaborLinkFacade(unittest.TestCase):

    def setUp(self):
        self.system = LaborLinkFacade()

    def test_add_employer_success(self):
        result = self.system.add_employer(
            company_name="ООО ТехноСфера",
            industry="IT-разработка",
            address="Красноярск, ул. Ленина 28",
            phone="+7 (391) 123-45-67",
            email="info@technosphere.ru"
        )
        self.assertIn("успешно добавлен", result.lower())

    def test_add_employer_empty_name_error(self):
        with self.assertRaises(ValueError):
            self.system.add_employer(
                company_name="",
                industry="IT",
                address="Красноярск",
                phone="+7 (391) 111-22-33",
                email="test@mail.ru"
            )

    def test_add_employer_invalid_email_error(self):
        with self.assertRaises(ValueError):
            self.system.add_employer(
                company_name="Тест Компания",
                industry="IT",
                address="Красноярск",
                phone="+7 (391) 111-22-33",
                email="invalid-email"
            )

    def test_add_candidate_success(self):
        result = self.system.add_candidate(
            full_name="Иванов Иван Иванович",
            birth_date=date(1998, 5, 15),
            phone="+7 (999) 111-22-33",
            email="ivanov@mail.ru",
            city="Красноярск",
            desired_salary=150000,
            skills="Python, Django",
            experience_years=4
        )
        self.assertIn("успешно добавлен", result.lower())

    def test_add_candidate_negative_salary_error(self):
        with self.assertRaises(ValueError):
            self.system.add_candidate(
                full_name="Петров Пётр",
                birth_date=date(2000, 1, 1),
                phone="+7 (999) 222-33-44",
                email="petrov@mail.ru",
                city="Красноярск",
                desired_salary=-5000,
                skills="Java",
                experience_years=2
            )

    def test_add_vacancy_success(self):
        result = self.system.add_vacancy(
            title="Senior Python Developer",
            description="Разработка backend",
            salary_from=150000,
            salary_to=200000,
            requirements="Python, Django, SQL"
        )
        self.assertIn("успешно создана", result.lower())

    def test_add_vacancy_empty_title_error(self):
        with self.assertRaises(ValueError):
            self.system.add_vacancy(
                title="",
                description="Тест",
                salary_from=100000,
                salary_to=150000,
                requirements="Python"
            )

    def test_create_deal_success(self):
        result = self.system.create_deal(
            candidate_id=1,
            vacancy_id=1,
            start_work_date=date(2026, 6, 1),
            salary=180000
        )
        self.assertIn("успешно оформлена", result.lower())
        self.assertIn("Комиссия", result)

    def test_create_deal_negative_salary_error(self):
        with self.assertRaises(ValueError):
            self.system.create_deal(
                candidate_id=1,
                vacancy_id=1,
                start_work_date=date(2026, 6, 1),
                salary=-10000
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)