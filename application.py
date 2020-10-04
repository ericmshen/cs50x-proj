from flask import Flask, flash, jsonify, redirect, render_template, request
import math

app = Flask(__name__)
app.secret_key = "dfjwo$2//fei"

values = [0, 5, 0, 5, 0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simple", methods=["GET", "POST"])
def simple():
    if request.method == "POST":
        if not request.form.get("principal") or not request.form.get("rate") or not request.form.get("time"):
            flash("Missing fields! Ensure all fields are completed.")
            return render_template("simple.html")

        principal = float(request.form.get("principal"))
        rate = float(request.form.get("rate"))/100
        time = float(request.form.get("time"))
        if principal < 0 or rate < 0 or time < 1:
            flash("Invalid information entered.")
            return render_template("compound.html")

        totals = []
        interests = []
        for i in range(1, int(time)+1):
            totals.append(principal*(1+rate*i))
            interests.append(principal*rate*i)

        width = str(max(time*30, 800))
        return render_template("simpleresults.html", principal="{:,.2f}".format(principal), time="{:,.0f}".format(time), rate="{:.3f}".format(rate*100), total="{:,.2f}".format(totals[int(time)-1]), interest="{:,.2f}".format(interests[int(time)-1]), width=width, chartinterests=interests, periods=round(time))
    else:
        return render_template("simple.html")

@app.route("/compound", methods=["GET", "POST"])
def compound():
    if request.method == "POST":
        if not request.form.get("principal") or not request.form.get("rate") or not request.form.get("period") or not request.form.get("time") :
            flash("Missing fields! Ensure all fields are completed.")
            return render_template("compound.html")

        principal = float(request.form.get("principal"))
        rate = float(request.form.get("rate"))/100
        period = request.form.get("period")
        if period == "Daily":
            n = 365
        elif period == "Weekly":
            n = 52
        elif period == "Monthly":
            n = 12
        elif period == "Yearly":
            n = 1
        time = float(request.form.get("time"))
        if principal < 0 or rate < 0 or time < 1:
            flash("Invalid information entered.")
            return render_template("compound.html")

        ptime = time*n
        prate = rate/n
        totals = []
        interests = []
        for i in range(1, int(ptime)+1):
            totals.append(principal*((1+prate)**i))
            interests.append(principal*((1+prate)**i)-principal)

        width = str(max(ptime*30, 800))
        return render_template("compoundresults.html", principal="{:,.2f}".format(principal), time="{:,.0f}".format(time), rate="{:.3f}".format(rate*100), period=period.lower(), total="{:,.2f}".format(totals[int(ptime)-1]), interest="{:,.2f}".format(interests[int(ptime)-1]), width=width, chartinterests=interests, periods=round(ptime))
    else:
        return render_template("compound.html")

@app.route("/annuity", methods=["GET", "POST"])
def annuity():
    if request.method == "POST":
        if not request.form.get("deposit") or not request.form.get("rate") or not request.form.get("period") or not request.form.get("time") :
            flash("Missing fields! Ensure all fields are completed.")
            return render_template("compound.html")

        deposit = float(request.form.get("deposit"))
        rate = float(request.form.get("rate"))/100
        period = request.form.get("period")
        if period == "Weekly":
            n = 52
        elif period == "Monthly":
            n = 12
        elif period == "Yearly":
            n = 1
        time = float(request.form.get("time"))
        if deposit < 0 or rate < 0 or time < 1:
            flash("Invalid information entered.")
            return render_template("annuity.html")

        ptime = time*n
        prate = rate/n
        deposits = []
        interests = []
        totals = []
        for i in range(1, int(ptime)+1):
            deposits.append(i*deposit)
            interests.append((1/prate)*(deposit*((1+prate)**i-1)) - deposit*i)
            totals.append(deposits[i-1]+interests[i-1])

        width = str(max(ptime*30, 800))
        return render_template("annuityresults.html", period=period.lower(), deposit="{:,.2f}".format(deposit), time="{:,.0f}".format(time), rate="{:.3f}".format(rate*100), total="{:,.2f}".format(totals[int(ptime)-1]), deposittotal="{:,.2f}".format(deposits[int(ptime)-1]), interest="{:,.2f}".format(interests[int(ptime)-1]), width=width, chartinterests=interests, chartdeposits=deposits, periods=round(ptime))
    else:
        return render_template("annuity.html")

@app.route("/loan", methods=["GET", "POST"])
def loan():
    if request.method == "POST":
        if not request.form.get("price") or not request.form.get("down") or not request.form.get("rate") or not request.form.get("period") or not request.form.get("time") :
            flash("Missing fields! Ensure all fields are completed.")
            return render_template("loan.html")

        price = float(request.form.get("price"))
        down = float(request.form.get("down"))/100
        rate = float(request.form.get("rate"))/100
        period = request.form.get("period")
        if period == "Weekly":
            n = 52
        elif period == "Monthly":
            n = 12
        elif period == "Yearly":
            n = 1
        time = float(request.form.get("time"))
        if price < 0 or down < 0 or rate < 0 or time < 1:
            flash("Invalid information entered.")
            return render_template("loan.html")

        principal = price*(1-down)
        periods = time*n
        prate = rate/n
        interests = []
        principals = []

        installment = math.ceil(100*(principal*prate)/(1-((1+prate)**(0-periods))))/100
        total = installment*periods
        totalinterest = total - principal
        totalint = totalinterest

        for i in range(1, int(periods)+1):
            if i == int(periods):
                interesttopay = totalinterest
                principaltopay = principal
            else:
                interesttopay = principal*prate
                principaltopay = installment-interesttopay
            interests.append(interesttopay)
            principals.append(principaltopay)
            principal -= principaltopay
            totalinterest -= interesttopay

        width = str(max(periods*30, 800))
        return render_template("loanresults.html", principal="{:,.2f}".format(price*(1-down)), price="{:,.2f}".format(price), down=down*100, rate="{:.3f}".format(rate*100), time="{:.0f}".format(time), payments="{:.0f}".format(periods), period=period.lower(), installment="{:,.2f}".format(installment), total="{:,.2f}".format(total), totalinterest="{:,.2f}".format(totalint), width=width, chartinterests=interests, chartprincipals=principals)
    else:
        return render_template("loan.html")