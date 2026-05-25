from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import os

DATABASE_URL = "postgresql://quizuser:RskwkZS2VhbUlbAp9yc6p4w7uV1rthKB@dpg-d8a69iml51nc73chek8g-a.oregon-postgres.render.com/quizdb_nax6"

conn = psycopg2.connect(DATABASE_URL)   

cursor = conn.cursor()

app = Flask(__name__)
app.secret_key = "quizsecret"

questions = [
    {
        "number": 1,
        "question": "The first newspaper published in India was?",
        "options": ["The Hindu", "The Amrita Bazar Patrika", "The Bengal Gazette", "The Times of India"],
        "answer": "The Bengal Gazette"
    },
    {
        "number": 2,
        "question": "Who was the first Home Minister of India?",
        "options": ["Dr S. Radhakrishnan", "Lal Bahadur Shastri", "Dr.Rajendra prasad", "Sardar VallabhBhai Patel"],
        "answer": "Sardar VallabhBhai Patel"
    },
    {
        "number": 3,
        "question": "Who was the first Indian to win a Nobel Prize?",
        "options": ["C. V. Raman", "Rabindranath Tagore", "Mother Teresa", "sarojini Naidu"],
        "answer": "Rabindranath Tagore"
    },
    {
        "number": 4,
        "question": "The first woman Governor of a state in free india was ?",
        "options": ["Sarojini Naidu", "Indira Gandhi", "Pratibha Patil", "Sucheta Kripalani"],
        "answer": "Sarojini Naidu"
    },
    {
        "number": 5,    
        "question": "Which was the first satellite launched by India?",
        "options": ["Rohini", "Aryabhata", "Bhaskara", "Kalpana-1"],
        "answer": "Aryabhata"
    },
    {
        "number": 6,
        "question": "First indigenously built aircraft carrier ?",
        "options": [ "INS Vikrant", "INS Viraat", "INS Arihant", "INS Chakra"],
        "answer": "INS Vikrant"
    },
    {
        "number": 7,
        "question": "First Indian Olympic medal ?",
        "options": ["K. D. Jadhav", "Abhinav Bindra","Norman Pritchard", "Milkha Singh"],
        "answer": "Norman Pritchard"
    },
    {
        "number": 8, 
         "question": "Who was the first indian woman to climb Mount Everest?",
         "options": ["Santosh Yadav", "Bachendri Pal", "Arunima Sinha", "premlata Agrawal"],
         "answer": "Bachendri Pal"
     },
     {      "number": 9,
            "question": "Gautam Buddha was born in?",
            "options": ["Lumbini", "Kushinagar", "Varanasi", "Sarnath"],
            "answer": "Lumbini"
        },
        {
            "number": 11,
            "question": "Red Fort was built by?",
            "options": ["Akbar", "Jahangir","Shah Jahan", "Shivaji"],
            "answer": "Shah Jahan"
        },
        {
            "number": 12,
            "question": "largest fresh water lake in India?",
            "options": [ "Dal Lake", "Chilika Lake", "Sambhar Lake","Wular Lake"],
            "answer": "Wular Lake"
        },
        {
            "number": 13,
            "question": "Nageen lake is located in?",
            "options": [ "Himachal Pradesh","Jammu and Kashmir",  "Uttarakhand", "Punjab"],
            "answer": "Jammu and Kashmir"
        },
        {
            "number": 14,
            "question": "Which is the largest river in India?",
            "options": ["Ganga", "Yamuna", "Brahmaputra", "Indus"],
            "answer": "Ganga"
        },
        {
            "number": 15,
            "question": "Which is the largest desert in India?",
            "options": ["Rann of Kutch", "Thar Desert","Great Indian Desert", "Sambhar Desert"],
            "answer": "Thar Desert"
     },
     {
        "number": 16,
        "question": "How many Articles were there in the original Constitution of India?",
        "options": ["395", "396", "397", "398"],
        "answer": "395"
     },
        {
            "number": 17,
            "question": "Which Article provides the right to freedom of religion in India?",
            "options": ["Article 25", "Article 26", "Article 27", "Article 28"],
            "answer": "Article 25"
        },
        {
            "number": 18,
            "question": "First Recipient of param Vir Chakra Award of India?",
            "options": ["Captain Gurbachan Singh Salaria", "Subedar Joginder Singh", "Naik Jadunath Singh", "Major Somnath Sharma"],
            "answer": "Major Somnath Sharma"
        },
        {
            "number": 19,
            "question": "Hirakud Dam is located in which state?",
            "options": ["Odisha", "Chhattisgarh", "Jharkhand", "Bihar"],
            "answer": "Odisha"
        },
        {
            "number": 20,
            "question": "Which Range Separates North India from South India?",
            "options": ["Aravalli Range", "Vindhya Range", "Satpura Range", "Nilgiri Hills"],
            "answer": "Vindhya Range"
        },
        {
            "number": 21,
            "question": "What is the Highest peak in India?",
            "options": ["Mount Everest", "K2", "Nanda Devi", "kangchenjunga"],
            "answer": "Kangchenjunga"
        },
        {
            "number": 22,
            "question": "Indian National Congress was founded in?",
            "options": ["1885", "1920", "1905", "1888"],
            "answer": "1885"
         },
            {
                "number": 23,
                "question": "Who was the first man to walk on the moon?",
                "options": [ "Buzz Aldrin","Neil Armstrong", "Michael Collins", "John Glenn"],
                "answer": "Neil Armstrong"
            },
                {
                    "number": 24,
                    "question":"The spiritual capital of India is?",
                    "options": [ "Haridwar","Varanasi", "Rishikesh", "Ayodhya"],
                    "answer": "Varanasi"
                },
                {
                    "number": 25,
                    "question": "Which City is known as the 'Electronic City of India'?",
                    "options": ["Bangalore", "Hyderabad", "Chennai", "Pune"],
                    "answer": "Bangalore"
                },
                {               
                    "number": 26,
                    "question": "Which place Receives maximum rainfall in India?",
                    "options": [ "Cherrapunjee", "Mawsynram", "Gangtok","Shillong"],
                    "answer": "Mawsynram"
                 },
                 {
                    "number": 27,
                    "question": "The Capital of South Korea is?",
                    "options": ["Pyongyang", "Busan", "Incheon", "Seoul"],
                    "answer": "Seoul"
                 },
                 {
                    "number": 28,
                    "question": "What is the Capital of Andhra Pradesh?",
                    "options": ["Hyderabad", "Vijayawada", "Amaravati", "Visakhapatnam"],
                    "answer": "Amaravati"
                 },
                {
                    "number": 29,
                    "question": "Anand Math is anationalist Novel that inspired the song Vande mataram.Who wrote this book?",
                    "options": ["Rabindranath Tagore","Bankim Chandra Chatterjee",  "Ishwar Chandra Vidyasagar", "Dinabandhu Mitra"],
                    "answer": "Bankim Chandra Chatterjee"
                },
                 {
                    "number": 30,
                    "question": "Indus river originates from?",
                    "options": [ "Ladakh", "Uttarakhand", "Himachal Pradesh", "Tibet"],
                    "answer": "Tibet"
                },
                {
                    "number": 31,
                    "question": "Which is the largest state in India by area?", 
                    "options": ["Maharashtra", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh"],
                    "answer": "Rajasthan"
                }

              



]
import random

random.shuffle(questions)

# ================= DATABASE =================

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS records(
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone TEXT,
    score INTEGER,
    attempted INTEGER DEFAULT 1
)
""")

conn.commit()
conn.close()

# ================= LOGIN PAGE =================

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM records WHERE phone=%s AND attempted=1",
            (phone,)
        )

        existing = cursor.fetchone()

        if existing:

            conn.close()

            return """
            <h2 style='color:red; text-align:center;'>
            This phone number already attempted quiz!
            </h2>
            """

        session["name"] = name
        session["phone"] = phone

        conn.close()

        return redirect("/quiz")

    return render_template("login.html")

# ================= ADMIN =================

ADMIN_USERNAME = "susheel tora"
ADMIN_PASSWORD = "tora@2006"

@app.route("/tora-admin-2026-secret", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session["admin"] = True

            return redirect("/records")

        else:

            return """
            <h2 style='color:red; text-align:center;'>
            Wrong Admin Credentials!
            </h2>
            """

    return render_template("admin.html")

# ================= QUIZ PAGE =================

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if "phone" not in session:
        return redirect("/")

    score = 0
    correct = []
    wrong = []

    if request.method == "POST":

        for i, q in enumerate(questions):

            user_answer = request.form.get(str(i))

            if user_answer == q["answer"]:

                score += 1

                correct.append({
                    "question": q["question"],
                    "answer": q["answer"]
                })

            else:

                wrong.append({
                    "question": q["question"],
                    "correct_answer": q["answer"],
                    "your_answer": user_answer
                })

        percentage = (score / len(questions)) * 100

        name = session["name"]
        phone = session["phone"]

        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO records(name, phone, score, attempted) VALUES (%s, %s, %s, %s)",
            (name, phone, score, 1)
        )

        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            name=name,
            score=score,
            total=len(questions),
            percentage=percentage,
            correct=correct,
            wrong=wrong
        )

    return render_template("home.html", questions=questions)

# ================= RESET =================

@app.route("/reset/<phone>")
def reset(phone):

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM records WHERE phone=%s",
        (phone,)
    )

    conn.commit()
    conn.close()

    return f"{phone} reset successful!"

# ================= RECORDS =================

@app.route("/records")
def records():

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")

    data = cursor.fetchall()

    conn.close()

    return render_template("records.html", records=data)

# ================= MY RESULT =================

@app.route("/myresult")
def myresult():

    if "phone" not in session:
        return redirect("/")

    phone = session["phone"]

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM records WHERE phone=%s",
        (phone,)
    )

    data = cursor.fetchone()

    conn.close()

    return render_template("myresult.html", data=data)

# ================= RUN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)