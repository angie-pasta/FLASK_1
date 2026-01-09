from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "twoj_tajny_klucz_2026"


@app.route("/")
def strona_glowna():
    """Strona główna"""
    return render_template("index.html")


@app.route("/about-me")
def o_mnie():
    """Strona o mnie"""
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def kontakt():
    """Strona kontaktu z formularzem"""
    if request.method == "POST":
        imie = request.form.get("imie")
        email = request.form.get("email")
        wiadomosc = request.form.get("wiadomosc")
        
        # Sprawdzenie, czy wszystkie pola są wypełnione
        if imie and email and wiadomosc:
            # W rzeczywistej aplikacji tutaj byśmy wysłali email
            print(f"\n--- NOWA WIADOMOŚĆ ---")
            print(f"Od: {imie}")
            print(f"Email: {email}")
            print(f"Wiadomość: {wiadomosc}")
            print(f"-------------------\n")
            
            flash(f"Dziękuję {imie}! Twoja wiadomość została wysłana!", "success")
            return redirect(url_for("kontakt"))
        else:
            flash("Wszystkie pola muszą być wypełnione!", "error")
    
    return render_template("contact.html")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 Aplikacja webowa Flask uruchomiona!")
    print("="*50)
    print("Otwórz przeglądarkę: http://localhost:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, host="localhost", port=5000)
