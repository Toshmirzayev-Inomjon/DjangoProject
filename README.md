# DjangoProject

DjangoProject — bu Django web framework yordamida yaratilgan veb-ilova. Ushbu loyiha yangiliklar (news) moduli, statik sahifalar, media fayllar bilan ishlash, shakllar (forms), ma’lumotlar bazasi, va boshqa asosiy Django imkoniyatlarini o‘z ichiga oladi.

---

## 📁 Loyiha tuzilmasi
DjangoProject/
├── core/ # Bosh sahifa, sozlamalar
├── news/ # Yangiliklar ilovasi
│ ├── migrations/ # Django migration fayllari
│ ├── models.py # Ma'lumotlar bazasi modellari
│ ├── views.py # View funksiyalar
│ ├── forms.py # Formlar
│ └── urls.py # URL marshrutlash
├── static/ # Statik fayllar (CSS, JS, rasmlar)
├── templates/ # HTML shablonlar
├── media/ # Yuklangan media fayllar
├── db.sqlite3 # SQLite ma'lumotlar bazasi
├── manage.py # Django CLI fayli
└── .gitignore # Git sozlamalari



---

## 🚀 O‘rnatish va ishga tushirish

### 1. Repozitoriyani klonlash

```bash
git clone https://github.com/your-username/your-repo-name.git
cd DjangoProject

python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
