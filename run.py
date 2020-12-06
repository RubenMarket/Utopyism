from flask import Flask, render_template

app = Flask(__name__)


#####################################
TotalProfit = 0
# Total Profit this period(2 weeks)
GrossSales = 0
# Gross Sales this period(2 weeks)
PrevProfitCap = 0
# Prev Profit Cap
PrevBasicIncome = 0
# Previous Weeks Basic Income(before dispersed)
ProfitCap = 0
# Winning Profit Cap(12:00am)
BasicIncome = 0
# Lump sum of profit minus its cap(12:00am)
######################################
# Databse Data
AccountHolders = 0
# Number of Accounts in Database
hasVotingEnded = False
# 12:00am Monday
votesfor1 = 0
votesfor2 = 0
votesfor3 = 0
# Votes for each option
#######################################
# User Specific Information
MyAwecoin = 0
isAweMember = True
hasVoted = False
personalidentifier = 0


def voted1(a, x):
    # a = hasVoted , x = total votes for first option
    if a is False:
        x += 1
        # update database for vote 1
    return


def voted2(a, y):
    # a = hasVoted , y = total votes for second option
    if a is False:
        y += 1
        # update database for vote 2
    return


def voted3(a, z):
    # a = hasVoted , z = total votes for third option
    if a is False:
        z += 1
        # update database for vote 3
    return


def showlivecount(x, y, z):
    # showing count on info page
    votesfor1label = x
    print(votesfor1label)
    votesfor2label = y
    print(votesfor2label)
    votesfor3label = z
    print(votesfor3label)
    # update labels on count
    return


def updateEarningsInfo(a, b, c, d):
    print("Company Profit After Expenses")
    print(a)
    print("Company Gross/Total Sales Before Expenses")
    print(b)
    print("Previous Weeks Profit Max/Cap")
    print(c)
    print("Amount Given to Basic Income last cycle")
    print(d)
    return


def calcvotingnumbers(a, b, c, d):
    votevalues = [a, b, c, d]
    votevalues.sort()
    # Sorting values from smallest to largest

    newvote1 = (votevalues[0] + votevalues[1]) / 2
    print("first/smallest voting option")
    print(newvote1)
    # smallest/first voting number
    newvote2 = (votevalues[1] + votevalues[2]) / 2
    print("second/middlest voting option")
    print(newvote2)
    # middle/second voting number
    newvote3 = (votevalues[2] + votevalues[3]) / 2
    print("third/largest voting option")
    print(newvote3)
    # largest/third voting number

    return


def calcUBI(x, y, a, b):
    # x = number of accounts in database , y = personalawecoin
    # a = profit(total) , b = profit cap(voted)
    print("Personal AweCoin")
    print(y)
    if a >= b:
        UBI = a - b
        BI = UBI / x
        print("Basic Income Per Person")
        print(BI)
        MyNewAwecoin = y + BI
        print("New AweCoin Total")
        print(MyNewAwecoin)
        # Setting the New Awe Coin(database)
    else:
        print("Less Profit Than The Cap")
        MyNewAwecoin = y
        print("New AweCoin Total(same as prev)")
        print(MyNewAwecoin)
        # Setting the New Awe Coin(database)
    return


if hasVotingEnded is True:

    calcvotingnumbers(PrevProfitCap, GrossSales, TotalProfit, PrevBasicIncome)

    calcUBI(AccountHolders, MyAwecoin, TotalProfit, ProfitCap)

# Information PAGE
updateEarningsInfo(TotalProfit, GrossSales, PrevProfitCap, PrevBasicIncome)

showlivecount(votesfor1, votesfor2, votesfor3)


class NewsPost:
    DateandTime = 0
    MessageText = ""
    MessageImage = ""
    ImageLink = ""


class Products:
    ProductImage = ""
    ProductAweCoin = ""
    ProductDescription = ""


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/Info")
def info():
    return "INFO PAGE"


@app.route("/News")
def news():
    return "NEWS PAGE"


@app.route("/Shop")
def shop():
    return "Shop PAGE"


if __name__ == '__main__':
    app.run(debug=True)
