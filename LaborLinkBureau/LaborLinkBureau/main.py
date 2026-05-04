from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from datetime import date
from facade import LaborLinkFacade

app = FastAPI(title="LaborLink Bureau")
system = LaborLinkFacade()

def get_style():
    return """
    <style>
        body {font-family: Arial, sans-serif; background: #2B2F4A; color: #fff; margin: 0; padding: 0;}
        header {background: linear-gradient(#FF6600, #E65C00); padding: 20px; text-align: center; font-size: 26px; font-weight: bold;}
        .container {max-width: 800px; margin: 20px auto; padding: 20px;}
        .card {background: #3A3F5C; border-radius: 15px; padding: 25px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);}
        input, select, textarea {width: 100%; padding: 12px; margin: 8px 0; border-radius: 10px; border: none; background: #4A506E; color: white;}
        button {background: #FF6600; color: white; border: none; padding: 14px 20px; border-radius: 10px; font-size: 16px; cursor: pointer; margin: 5px;}
        button:hover {background: #E65C00;}
        .btn-back {background: #555;}
        h2 {color: #FF6600; text-align: center;}
    </style>
    """

# ====================== ГЛАВНЫЙ ЭКРАН ======================
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head><title>LaborLink Bureau</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {font-family: Arial, sans-serif; background: #2B2F4A; color: #fff; margin: 0; padding: 0;}
        header {background: linear-gradient(#FF6600, #E65C00); padding: 25px; text-align: center; font-size: 28px; font-weight: bold;}
        .welcome {text-align: center; padding: 30px 20px; background: #1F2337;}
        .welcome h1 {margin: 0; font-size: 24px;}
        .welcome p {margin: 8px 0 0; color: #ccc;}
        .container {padding: 20px;}
        .section-title {color: #FF6600; margin: 25px 0 15px 10px; font-size: 18px;}
        .card-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px;}
        .card {
            background: #3A3F5C; border-radius: 16px; padding: 20px; text-align: center;
            transition: all 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .card:hover {transform: translateY(-8px); box-shadow: 0 10px 25px rgba(255,102,0,0.3);}
        .card-icon {font-size: 48px; margin-bottom: 15px; color: #FF6600;}
        .card h3 {margin: 10px 0;}
        .card p {color: #bbb; font-size: 14px;}
        .orange-btn {
            background: #FF6600; color: white; border: none; padding: 12px; 
            border-radius: 10px; width: 100%; font-size: 16px; cursor: pointer; margin-top: 10px;
        }
        .quick-actions {display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0;}
        .quick-btn {
            flex: 1; background: #4A506E; color: white; border: none; 
            padding: 14px; border-radius: 10px; font-size: 15px; cursor: pointer;
        }
    </style>
    </head>
    <body>
        <header>LaborLink Bureau</header>
        
        <div class="welcome">
            <h1>Добро пожаловать!</h1>
            <p>Управляйте трудоустройством эффективно</p>
        </div>

        <div class="container">
            <div class="section-title">Быстрые действия</div>
            <div class="quick-actions">
                <button class="quick-btn" onclick="window.location.href='/add_candidate'">👤 Новый соискатель</button>
                <button class="quick-btn" onclick="window.location.href='/add_employer'">🏢 Новый работодатель</button>
                <button class="quick-btn" onclick="window.location.href='/vacancy_register'">💼 Новая вакансия</button>
            </div>

            <div class="section-title">Основные разделы</div>
            <div class="card-grid">
                <div class="card">
                    <div class="card-icon"><i class="fas fa-briefcase"></i></div>
                    <h3>Вакансии</h3>
                    <p>Просмотр и управление открытыми вакансиями</p>
                    <button class="orange-btn" onclick="window.location.href='/vacancy_register'">Перейти к вакансиям</button>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fas fa-users"></i></div>
                    <h3>Соискатели</h3>
                    <p>База кандидатов и их профили</p>
                    <button class="orange-btn" onclick="window.location.href='/candidates_list'">Просмотреть соискателей</button>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fas fa-building"></i></div>
                    <h3>Работодатели</h3>
                    <p>Компании и их контактные данные</p>
                    <button class="orange-btn" onclick="window.location.href='/employers_list'">Управление работодателями</button>
                </div>
                <div class="card">
                    <div class="card-icon"><i class="fas fa-handshake"></i></div>
                    <h3>Сделки</h3>
                    <p>Оформленные трудоустройства и комиссия</p>
                    <button class="orange-btn" onclick="window.location.href='/deals_list'">Просмотреть сделки</button>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
# ====================== 2. ФОРМА РАБОТОДАТЕЛЯ ======================
@app.get("/add_employer", response_class=HTMLResponse)
async def add_employer_form():
    return f"""
    <html><head><title>Форма работодателя</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card">
            <h2>Форма работодателя</h2>
            <form action="/add_employer" method="post">
                <label>Название компании</label>
                <input name="company_name" required><br>
                <label>Вид деятельности</label>
                <input name="industry"><br>
                <label>Адрес</label>
                <input name="address"><br>
                <label>Контактный телефон</label>
                <input name="phone"><br>
                <label>Email компании</label>
                <input name="email" type="email" required><br>
                <label>Краткое описание</label>
                <textarea name="description"></textarea><br><br>
                <button type="submit">Сохранить работодателя</button>
                <button type="button" class="btn-back" onclick="history.back()">Отмена</button>
            </form>
        </div>
    </div>
    </body></html>
    """

@app.post("/add_employer")
async def add_employer_post(company_name: str = Form(...), industry: str = Form(""), 
                           address: str = Form(""), phone: str = Form(""), 
                           email: str = Form(...), description: str = Form("")):
    result = system.add_employer(company_name, industry, address, phone, email, description)
    return HTMLResponse(f"<h3>{result}</h3><br><a href='/'>← На главную</a>")

# ====================== 3. ФОРМА СОИСКАТЕЛЯ ======================
@app.get("/add_candidate", response_class=HTMLResponse)
async def add_candidate_form():
    return f"""
    <html><head><title>Форма соискателя</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card">
            <h2>Регистрация соискателя</h2>
            <form action="/add_candidate" method="post">
                <label>ФИО</label><input name="full_name" required><br>
                <label>Дата рождения</label><input name="birth_date" type="date" required><br>
                <label>Телефон</label><input name="phone"><br>
                <label>Email</label><input name="email" type="email" required><br>
                <label>Город</label><input name="city"><br>
                <label>Желаемая зарплата</label><input name="desired_salary" type="number"><br>
                <label>Навыки</label><input name="skills"><br>
                <label>Опыт (лет)</label><input name="experience_years" type="number"><br>
                <label>О себе</label><textarea name="about"></textarea><br><br>
                <button type="submit">Сохранить соискателя</button>
                <button type="button" class="btn-back" onclick="history.back()">Отмена</button>
            </form>
        </div>
    </div>
    </body></html>
    """

@app.post("/add_candidate")
async def add_candidate_post(full_name: str = Form(...), birth_date: str = Form(...),
                           phone: str = Form(""), email: str = Form(...), city: str = Form(""),
                           desired_salary: float = Form(0), skills: str = Form(""), 
                           experience_years: int = Form(0), about: str = Form("")):
    result = system.add_candidate(full_name, date.fromisoformat(birth_date), phone, email, 
                                city, desired_salary, skills, experience_years, about)
    return HTMLResponse(f"<h3>{result}</h3><br><a href='/'>← На главную</a>")

# ====================== 4. ЭКРАН РЕГИСТРАЦИИ ВАКАНСИИ ======================
@app.get("/vacancy_register", response_class=HTMLResponse)
async def vacancy_register():
    return f"""
    <html><head><title>Регистрация вакансии</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card">
            <h2>Регистрация новой вакансии</h2>
            <button onclick="window.location.href='/add_vacancy'" style="width:100%; padding:18px; font-size:18px;">
                <i class="fas fa-plus"></i> Создать новую вакансию
            </button><br><br>
            <button onclick="window.location.href='/vacancies_list'" style="width:100%; padding:18px; font-size:18px;">
                📋 Просмотреть существующие вакансии
            </button><br><br>
            <button onclick="history.back()">Назад</button>
        </div>
    </div>
    </body></html>
    """

# ====================== 5. ФОРМА ДОБАВЛЕНИЯ ВАКАНСИИ ======================
@app.get("/add_vacancy", response_class=HTMLResponse)
async def add_vacancy_form():
    return f"""
    <html><head><title>Добавить вакансию</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card">
            <h2>Форма создания вакансии</h2>
            <form action="/add_vacancy" method="post">
                <label>Название должности</label><input name="title" required><br>
                <label>Описание</label><textarea name="description"></textarea><br>
                <label>Зарплата от</label><input name="salary_from" type="number"><br>
                <label>Зарплата до</label><input name="salary_to" type="number"><br>
                <label>Требования</label><textarea name="requirements"></textarea><br><br>
                <button type="submit">Сохранить вакансию</button>
                <button type="button" class="btn-back" onclick="history.back()">Отмена</button>
            </form>
        </div>
    </div>
    </body></html>
    """

@app.post("/add_vacancy")
async def add_vacancy_post(title: str = Form(...), description: str = Form(""), 
                          salary_from: float = Form(0), salary_to: float = Form(0), 
                          requirements: str = Form("")):
    result = system.add_vacancy(title, description, salary_from, salary_to, requirements)
    return HTMLResponse(f"<h3>{result}</h3><br><a href='/vacancy_register'>← Назад к регистрации</a>")

# ====================== 6. ОКНО ПРОСМОТРА СОИСКАТЕЛЕЙ ======================
@app.get("/candidates_list", response_class=HTMLResponse)
async def candidates_list():
    candidates = system.repo.get_all("candidates")
    html = f"""
    <html><head><title>Просмотр соискателей</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <h2>Окно просмотра соискателей</h2>
        <div class="card">
    """
    for c in candidates:
        html += f"""
        <div style="background:#4A506E; padding:15px; margin:10px 0; border-radius:10px;">
            <strong>{c['full_name']}</strong><br>
            {c['city']} | {c['desired_salary']} руб. | Опыт: {c['experience_years']} лет
        </div>"""
    html += "<br><button onclick='history.back()'>Назад</button></div></div></body></html>"
    return html

    
@app.post("/create_deal")
async def create_deal_post(candidate_id: int = Form(...), vacancy_id: int = Form(...),
                           start_date: str = Form(...), salary: float = Form(...)):
    result = system.create_deal(candidate_id, vacancy_id, date.fromisoformat(start_date), salary)
    return HTMLResponse(f"<h3>{result}</h3><br><a href='/'>← На главную</a>")
    
# После успешного добавления работодателя
@app.post("/add_employer")
async def add_employer_post(company_name: str = Form(...), industry: str = Form(""), 
                           address: str = Form(""), phone: str = Form(""), 
                           email: str = Form(...), description: str = Form("")):
    result = system.add_employer(company_name, industry, address, phone, email, description)
    return HTMLResponse(f"""
    <html><head><title>Успешно</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card" style="text-align:center; color:#0f0;">
            <h2>✅ Успешно!</h2>
            <p>{result}</p>
            <button onclick="window.location.href='/'" style="padding:15px 30px; font-size:18px;">Вернуться на главный экран</button>
        </div>
    </div>
    </body></html>
    """)

# После успешного добавления соискателя
@app.post("/add_candidate")
async def add_candidate_post(full_name: str = Form(...), birth_date: str = Form(...),
                           phone: str = Form(""), email: str = Form(...), city: str = Form(""),
                           desired_salary: float = Form(0), skills: str = Form(""), 
                           experience_years: int = Form(0), about: str = Form("")):
    result = system.add_candidate(full_name, date.fromisoformat(birth_date), phone, email, 
                                city, desired_salary, skills, experience_years, about)
    return HTMLResponse(f"""
    <html><head><title>Успешно</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <div class="card" style="text-align:center; color:#0f0;">
            <h2>✅ Успешно!</h2>
            <p>{result}</p>
            <button onclick="window.location.href='/'" style="padding:15px 30px; font-size:18px;">Вернуться на главный экран</button>
        </div>
    </div>
    </body></html>
    """)
        
@app.get("/vacancies_list", response_class=HTMLResponse)
async def vacancies_list():
    vacancies = system.repo.get_all("vacancies")
    html = f"""
    <html><head><title>Вакансии</title>{get_style()}</head><body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <h2>Существующие вакансии</h2>
        <div class="card">
    """
    if not vacancies:
        html += "<p>Пока нет вакансий.</p>"
    else:
        for v in vacancies:
            html += f"""
            <div style="background:#4A506E; padding:15px; margin:10px 0; border-radius:10px;">
                <strong>{v['title']}</strong><br>
                {v['salary_from']} — {v['salary_to']} руб.<br>
                <small>{v['status']}</small>
            </div>"""
    html += "<br><button onclick='history.back()'>Назад</button></div></div></body></html>"
    return html

# ====================== ПРОСМОТР СДЕЛОК ======================
@app.get("/deals_list", response_class=HTMLResponse)
async def deals_list():
    deals = system.repo.get_all("deals")
    html = f"""
    <html>
    <head><title>Сделки</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    {get_style()}
    </head>
    <body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <h2>Список сделок</h2>
        <div class="card">
    """
    if not deals:
        html += "<p>Пока нет оформленных сделок.</p>"
    else:
        for d in deals:
            html += f"""
            <div style="background:#4A506E; padding:15px; margin:12px 0; border-radius:10px;">
                <strong>Сделка №{d['deal_id']}</strong><br>
                Зарплата: {d['salary']} руб.<br>
                Комиссия: <strong style="color:#FF6600;">{d['commission']} руб.</strong><br>
                Дата выхода: {d['start_work_date']}<br>
                Статус: {d['status']}
            </div>"""
    
    html += """
        <br>
        <button onclick="window.location.href='/'">← На главный экран</button>
        </div>
    </div>
    </body></html>
    """
    return html    
    
# ====================== СПИСОК РАБОТОДАТЕЛЕЙ ======================
@app.get("/employers_list", response_class=HTMLResponse)
async def employers_list():
    employers = system.repo.get_all("employers")
    html = f"""
    <html>
    <head><title>Работодатели</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    {get_style()}
    </head>
    <body>
    <header>LaborLink Bureau</header>
    <div class="container">
        <h2>Управление работодателями</h2>
        <div class="card">
    """
    if not employers:
        html += "<p>Пока нет добавленных работодателей.</p>"
    else:
        for emp in employers:
            html += f"""
            <div style="background:#4A506E; padding:15px; margin:10px 0; border-radius:10px;">
                <strong>{emp['company_name']}</strong><br>
                {emp['industry']} • {emp['address']}<br>
                <small>{emp['email']} | {emp['phone']}</small>
            </div>"""
    
    html += """
        <br>
        <button onclick="window.location.href='/add_employer'">➕ Добавить нового работодателя</button><br><br>
        <button onclick="window.location.href='/'">← На главный экран</button>
        </div>
    </div>
    </body></html>
    """
    return html    
    
if __name__ == "__main__":
    import uvicorn
    print("🚀 LaborLink Bureau запущен!")
    print("Открывайте: http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)