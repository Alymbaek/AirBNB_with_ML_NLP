## 📩 Контакты
Автор: [Alymbek]
Linkedin: [https://www.linkedin.com/in/alymbek-ibragimov-447876336/]


# 🏠 AirBNB Comments Sentiment Analysis + DRF Backend

Этот проект — полный стек: от обучения NLP модели для анализа тональности отзывов до интеграции её в REST API на Django.

## 📋 Описание
Сервис имитирует платформу бронирования жилья, где пользователи могут оставлять комментарии и рейтинг. NLP модель автоматически определяет, положительный или отрицательный отзыв.

## 🔧 Технологии
- Python 3
- Pandas, Scikit-learn, NLTK
- Multinomial Naive Bayes
- Django REST Framework

## 🚀 Возможности
✅ Предобработка текста и обучение модели  
✅ Определение тональности комментария: `positive` / `negative`  
✅ REST API для управления:
  - объектами недвижимости
  - пользователями
  - отзывами

## 📦 Состав
- `AirBNB_comments_NLP.ipynb` — обучение и сохранение модели
- `model_airbnb.pkl` — обученная модель
- `vec_airbnb` — векторизатор текста
- `backend/` — папка с DRF-проектом

## 🔄 Как запустить
1. Клонируй репозиторий:
```bash
git clone https://github.com/your-username/your-repo-name.git

2. Установи зависимости:
pip install -r requirements.txt

3. python manage.py runserver

4. Зайди в админку или используйте API, чтобы оставить отзыв и увидеть результат анализа.

{
  "id": 4,
  "check_comment": [
    "negative"
  ],
  "rating": 3,
  "comment": "душ сломанный и не приятный",
  "created_at": "2025-07-12T19:39:06.226220+06:00",
  "property": 1,
  "guest": 2
}




