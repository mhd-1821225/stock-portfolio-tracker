from flask import Flask,render_template,request
import database as db




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        name = db.validate_user(username, password)
        if name == "USER_NOT_FOUND":
            return render_template("login.html", message="Username does not exist")
        elif name == "INVALID_PASSWORD":
            return render_template("login.html", message="Incorrect password")
        else:
            portfolio, total_money_invested, total_current_value, total_profit_loss = db.view_portfolio()
            return render_template("main.html", name=name, portfolio=portfolio, total_money_invested=total_money_invested, total_current_value=total_current_value, total_profit_loss=total_profit_loss)

        

    return render_template("login.html")

@app.route("/create-account", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        result = db.duplicate_user(username)
        if result == "DUPLICATE_USER":
            return render_template("create.html", message="Username already exists")
        else:
            db.create_user(username, password, name)
            return render_template("login.html", success="User created successfully. Please login.")
    return render_template("create.html")

@app.route("/add",methods=["GET", "POST"])
def add_stock():
    if request.method == "POST":
        ticker = request.form["ticker"]
        quantity = request.form["quantity"]
        purchase_price = request.form["purchase_price"]
        result = db.add_stock(ticker,purchase_price,quantity)
        if result == "STOCK_ADDED_SUCCESSFULLY":
            return render_template("add.html", message="Stock added successfully.")
        elif result == "DUPLICATE_STOCK":
            return render_template("add.html", message="Stock already exists in your portfolio.")
        else:
            return render_template("add.html", message="Failed to add stock.")
    return render_template("add.html")

@app.route("/logout")
def logout():
    return render_template("home.html")

@app.route("/main", methods=["GET", "POST"])
def main():
     name = db.get_name()
     portfolio, total_money_invested, total_current_value, total_profit_loss = db.view_portfolio()
     return render_template("main.html", name=name, portfolio=portfolio, total_money_invested=total_money_invested, total_current_value=total_current_value, total_profit_loss=total_profit_loss)



   
@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        ticker = request.form["ticker"]
        result = db.delete_stock(ticker)
        if result == "STOCK_DELETED_SUCCESSFULLY":
            return render_template("delete.html", message="Stock deleted successfully.")
        else:
            return render_template("delete.html", message="Failed to delete stock.")
        
    return render_template("delete.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        ticker = request.form["ticker"]
        new_quantity = request.form["quantity"]
        new_purchase_price = request.form["purchase_price"]
        result = db.edit_stock(ticker, new_quantity, new_purchase_price)
        if result == "STOCK_EDITED_SUCCESSFULLY":
            return render_template("edit.html", message="Stock edited successfully.")
        else:
            return render_template("edit.html", message="Failed to edit stock.")
    return render_template("edit.html")






        

if __name__ == "__main__":
    app.run(debug=True)