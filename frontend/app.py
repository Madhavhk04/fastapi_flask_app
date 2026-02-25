from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests

app = Flask(__name__)
app.secret_key = "super_secret_flask_session_key"

FASTAPI_URL = "http://127.0.0.1:8000"

@app.route("/")
def index():
    if "token" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            response = requests.post(f"{FASTAPI_URL}/register", json={"name": name, "email": email, "password": password})
            if response.status_code == 200:
                flash("Registration successful! Please login.", "success")
                return redirect(url_for("login"))
            else:
                flash(response.json().get("detail", "Registration failed"), "error")
        except Exception as e:
            flash(f"Connection error: {e}", "error")
            
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            # OAuth2 requires form data (not JSON)
            data = {"username": email, "password": password}
            response = requests.post(f"{FASTAPI_URL}/token", data=data)
            
            if response.status_code == 200:
                session["token"] = response.json().get("access_token")
                return redirect(url_for("dashboard"))
            else:
                flash(response.json().get("detail", "Invalid credentials"), "error")
        except Exception as e:
            flash(f"Connection error: {e}", "error")
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("token", None)
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "token" not in session:
        return redirect(url_for("login"))
        
    headers = {"Authorization": f"Bearer {session['token']}"}
    search_query = request.args.get("q", "")
    
    try:
        # Get Current User
        me_resp = requests.get(f"{FASTAPI_URL}/users/me", headers=headers)
        if me_resp.status_code == 401:
            session.pop("token", None)
            return redirect(url_for("login"))
        me = me_resp.json()
        
        # Get All Users (with optional search)
        params = {"q": search_query} if search_query else {}
        users_resp = requests.get(f"{FASTAPI_URL}/users/", headers=headers, params=params)
        users = users_resp.json() if users_resp.status_code == 200 else []
        
    except Exception as e:
        me = None
        users = []
        flash(f"Error connecting to backend: {e}", "error")
        
    return render_template("dashboard.html", user=me, users=users, search_query=search_query)

@app.route("/update_user", methods=["POST"])
def update_user():
    if "token" not in session:
        return redirect(url_for("login"))
        
    user_id = request.form.get("user_id")
    name = request.form.get("name")
    
    headers = {"Authorization": f"Bearer {session['token']}"}
    try:
        requests.put(f"{FASTAPI_URL}/users/{user_id}", headers=headers, json={"name": name})
        flash("Profile updated successfully", "success")
    except Exception as e:
        flash("Failed to update profile", "error")
        
    return redirect(url_for("dashboard"))

@app.route("/delete_user", methods=["POST"])
def delete_user():
    if "token" not in session:
        return redirect(url_for("login"))
        
    user_id = request.form.get("user_id")
    headers = {"Authorization": f"Bearer {session['token']}"}
    
    try:
        requests.delete(f"{FASTAPI_URL}/users/{user_id}", headers=headers)
        session.pop("token", None)
        flash("Account deleted successfully", "success")
        return redirect(url_for("login"))
    except Exception as e:
        flash("Failed to delete account", "error")
        return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
