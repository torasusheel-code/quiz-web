from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "quizsecret"

questions = [
    {
        "number": 1,
        "question": "1.The first newspaper published in India was?",
        "options": ["The Hindu", "The Amrita Bazar Patrika", "The Bengal Gazette", "The Times of India"],
        "answer": "The Bengal Gazette"
    },
    {
        "number": 2,
        "question": "2.Who was the first Home Minister of India?",
        "options": ["Dr S. Radhakrishnan", "Lal Bahadur Shastri", "Dr.Rajendra prasad", "Sardar VallabhBhai Patel"],
        "answer": "Sardar VallabhBhai Patel"
    },
    {
        "number": 3,
        "question": "3.Who was the first Indian to win a Nobel Prize?",
        "options": ["C. V. Raman", "Rabindranath Tagore", "Mother Teresa", "sarojini Naidu"],
        "answer": "Rabindranath Tagore"
    },
    {
        "number": 4,
        "question": "4.The first woman Governor of a state in free india was ?",
        "options": ["Sarojini Naidu", "Indira Gandhi", "Pratibha Patil", "Sucheta Kripalani"],
        "answer": "Sarojini Naidu"
    },
    {
        "number": 5,    
        "question": "5.Which was the first satellite launched by India?",
        "options": ["Rohini", "Aryabhata", "Bhaskara", "Kalpana-1"],
        "answer": "Aryabhata"
    },
    {
        "number": 6,
        "question": "6.First indigenously built aircraft carrier ?",
        "options": [ "INS Vikrant", "INS Viraat", "INS Arihant", "INS Chakra"],
        "answer": "INS Vikrant"
    },
    {
        "number": 7,
        "question": "7.First Indian Olympic medal ?",
        "options": ["K. D. Jadhav", "Abhinav Bindra","Norman Pritchard", "Milkha Singh"],
        "answer": "Norman Pritchard"
    },
    {
        "number": 8, 
         "question": "8.Who was the first indian woman to climb Mount Everest?",
         "options": ["Santosh Yadav", "Bachendri Pal", "Arunima Sinha", "premlata Agrawal"],
         "answer": "Bachendri Pal"
     },
     {      "number": 9,
            "question": "9.Gautam Buddha was born in?",
            "options": ["Lumbini", "Kushinagar", "Varanasi", "Sarnath"],
            "answer": "Lumbini"
        },
        {
            "number": 11,
            "question": "11.Red Fort was built by?",
            "options": ["Akbar", "Jahangir","Shah Jahan", "Shivaji"],
            "answer": "Shah Jahan"
        },
        {
            "number": 12,
            "question": "12.largest fresh water lake in India?",
            "options": [ "Dal Lake", "Chilika Lake", "Sambhar Lake","Wular Lake"],
            "answer": "Wular Lake"
        },
        {
            "number": 13,
            "question": "13.Nageen lake is located in?",
            "options": [ "Himachal Pradesh","Jammu and Kashmir",  "Uttarakhand", "Punjab"],
            "answer": "Jammu and Kashmir"
        },
        {
            "number": 14,
            "question": "14.Which is the largest river in India?",
            "options": ["Ganga", "Yamuna", "Brahmaputra", "Indus"],
            "answer": "Ganga"
        },
        {
            "number": 15,
            "question": "15.Which is the largest desert in India?",
            "options": ["Rann of Kutch", "Thar Desert","Great Indian Desert", "Sambhar Desert"],
            "answer": "Thar Desert"
     },
     {
        "number": 16,
        "question": "16.How many Articles were there in the original Constitution of India?",
        "options": ["395", "396", "397", "398"],
        "answer": "395"
     },
        {
            "number": 17,
            "question": "17.Which Article provides the right to freedom of religion in India?",
            "options": ["Article 25", "Article 26", "Article 27", "Article 28"],
            "answer": "Article 25"
        },
        {
            "number": 18,
            "question": "18.First Recipient of param Vir Chakra Award of India?",
            "options": ["Captain Gurbachan Singh Salaria", "Subedar Joginder Singh", "Naik Jadunath Singh", "Major Somnath Sharma"],
            "answer": "Major Somnath Sharma"
        },
        {
            "number": 19,
            "question": "19.Hirakud Dam is located in which state?",
            "options": ["Odisha", "Chhattisgarh", "Jharkhand", "Bihar"],
            "answer": "Odisha"
        },
        {
            "number": 20,
            "question": "20.Which Range Separates North India from South India?",
            "options": ["Aravalli Range", "Vindhya Range", "Satpura Range", "Nilgiri Hills"],
            "answer": "Vindhya Range"
        },
        {
            "number": 21,
            "question": "21.What is the Highest peak in India?",
            "options": ["Mount Everest", "K2", "Nanda Devi", "kangchenjunga"],
            "answer": "Kangchenjunga"
        },
        {
            "number": 22,
            "question": "22.Indian National Congress was founded in?",
            "options": ["1885", "1920", "1905", "1888"],
            "answer": "1885"
         },
            {
                "number": 23,
                "question": "23.Who was the first man to walk on the moon?",
                "options": [ "Buzz Aldrin","Neil Armstrong", "Michael Collins", "John Glenn"],
                "answer": "Neil Armstrong"
            },
                {
                    "number": 24,
                    "question":"24.The spiritual capital of India is?",
                    "options": [ "Haridwar","Varanasi", "Rishikesh", "Ayodhya"],
                    "answer": "Varanasi"
                },
                {
                    "number": 25,
                    "question": "25.Which City is known as the 'Electronic City of India'?",
                    "options": ["Bangalore", "Hyderabad", "Chennai", "Pune"],
                    "answer": "Bangalore"
                },
                {               
                    "number": 26,
                    "question": "26.Which place Receives maximum rainfall in India?",
                    "options": [ "Cherrapunjee", "Mawsynram", "Gangtok","Shillong"],
                    "answer": "Mawsynram"
                 },
                 {
                    "number": 27,
                    "question": "27.The Capital of South Korea is?",
                    "options": ["Pyongyang", "Busan", "Incheon", "Seoul"],
                    "answer": "Seoul"
                 },
                 {
                    "number": 28,
                    "question": "28.What is the Capital of Andhra Pradesh?",
                    "options": ["Hyderabad", "Vijayawada", "Amaravati", "Visakhapatnam"],
                    "answer": "Amaravati"
                 },
                {
                    "number": 29,
                    "question": "29.Anand Math is anationalist Novel that inspired the song Vande mataram.Who wrote this book?",
                    "options": ["Rabindranath Tagore","Bankim Chandra Chatterjee",  "Ishwar Chandra Vidyasagar", "Dinabandhu Mitra"],
                    "answer": "Bankim Chandra Chatterjee"
                },
                 {
                    "number": 30,
                    "question": "30.Indus river originates from?",
                    "options": [ "Ladakh", "Uttarakhand", "Himachal Pradesh", "Tibet"],
                    "answer": "Tibet"
                },
                {
                    "number": 31,
                    "question": "31.Which is the largest state in India by area?", 
                    "options": ["Maharashtra", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh"],
                    "answer": "Rajasthan"
                }





]

# Database create
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    score INTEGER
)
""")

conn.commit()
conn.close()

# Login Page
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM records WHERE username=?",
            (username,)
        )

        existing_user = cursor.fetchone()

        conn.close()

        # Agar already quiz de chuka hai
        if existing_user:
            return "<h2>User already attempted the quiz!</h2>"

        session["username"] = username

        return redirect("/quiz")

    return render_template("login.html")
# Quiz Page
@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if "username" not in session:
        return redirect("/")

    score = 0

    if request.method == "POST":

        for i, q in enumerate(questions):

            user_answer = request.form.get(str(i))

            if user_answer == q["answer"]:
                score += 1

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO records(username, score) VALUES(?, ?)",
            (session["username"], score)
        )

        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            score=score,
            total=len(questions)
        )

    return render_template("home.html", questions=questions)

# Records Page
@app.route("/records")
def records():

    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")

    data = cursor.fetchall()

    conn.close()

    return render_template("records.html", records=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)