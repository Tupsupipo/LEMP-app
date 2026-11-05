from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)

@app.route('/')
def home():
        # Connect to MySQL/MariaDB
        conn = mysql.connector.connect(
                host="localhost",
                user="censored",
                password="censored",
                database="censoreddb"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE visit_counter SET count = count + 1 WHERE counterID = 1")
        conn.commit()
        cursor.execute("SELECT count FROM visit_counter WHERE counterID = 1")
        result = cursor.fetchone()
	# Clean up
        cursor.close()
        conn.close()
        return render_template("index.html", result=result[0])
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)