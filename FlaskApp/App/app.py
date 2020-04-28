from flask import Flask, render_template

import sqlite3


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', passthrough_errors=True)


@app.route('/')
def homepage():

    #!Titre
    title = "Grady"

    return render_template("index.html", title = title)
    
@app.route('/app')
def appli():
    return render_template("app.html")

    
@app.route('/projet')
def projectPage():
    return render_template("projet.html")
    
@app.route('/projet/documentation')
def documentationPage():
    return render_template("doc.html")
    
@app.route('/projet/credits')
def creditsPage():
    return render_template("credits.html")

@app.route('/stat/LEPL1402')
def LEPL():
    return render_template("LEPL1402.html")

@app.route('/stat/LSINF1101_PYTHON')
def pyth():
    return render_template("LSINF1101_PYTHON.html")

@app.route('/stat/LSINF1252')
def lsinf():
    return render_template("LSINF1252.html")

"""
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    
    DEBUT DES PAGES SUR LES DIFFERENTES TACHES INGINIOUS
    
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
"""

@app.route('/stat/ASCIIDecoder')
def ASCIIDecoder():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ASCIIDecoder'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/AbstractClass')
def AbstractClass():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'AbstractClass'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/AccessModifiers')
def AccessModifiers():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'AccessModifiers'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Array2D')
def Array2D():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Array2D'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BlackBox')
def BlackBox():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'BlackBox'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BoundedBuffer')
def BoundedBuffer():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'BoundedBuffer'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BubbleSortInvariant')
def BubbleSortInvariant():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'BubbleSortInvariant'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Casting')
def Casting():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Casting'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CircularLL')
def CircularLL():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'CircularLL'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CodeAccuracy')
def CodeAccuracy():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'CodeAccuracy'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CodeAccuracy2')
def CodeAccuracy2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'CodeAccuracy2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CommonErrors')
def CommonErrors():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'CommonErrors'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComparatorAndCollections')
def ComparatorAndCollections():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ComparatorAndCollections'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComparatorvsComparable')
def ComparatorvsComparable():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ComparatorvsComparable'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComplexityArraySearch')
def ComplexityArraySearch():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ComplexityArraySearch'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComplexityMCQ1')
def ComplexityMCQ1():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ComplexityMCQ1'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)@app.route('/stat/Coverage')
def Coverage():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Coverage'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CyclicBarrier')
def CyclicBarrier():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'CyclicBarrier'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FList')
def FList():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'FList'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FListMergeSort')
def FListMergeSort():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'FListMergeSort'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FTree')
def FTree():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'FTree'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Factory')
def Factory():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Factory'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Future')
def Future():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Future'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Generics')
def Generics():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Generics'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Generics2')
def Generics2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Generics2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Generics3')
def Generics3():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Generics3'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/HanoiTower')
def HanoiTower():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'HanoiTower'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/InfiniteStreams')
def InfiniteStreams():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'InfiniteStreams'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Inheritance')
def Inheritance():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Inheritance'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Introduction')
def Introduction():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Introduction'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LambdaExpressioninJava')
def LambdaExpressioninJava():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'LambdaExpressioninJava'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LearnException')
def LearnException():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'LearnException'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MakeMistakeToUnderstandThem')
def MakeMistakeToUnderstandThem():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MakeMistakeToUnderstandThem'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MaximumSumSubarray')
def MaximumSumSubarray():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MaximumSumSubarray'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MergeSortImplementation')
def MergeSortImplementation():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MergeSortImplementation'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MidTermQuiz')
def MidTermQuiz():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MidTermQuiz'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MidTermQuizMCQ')
def MidTermQuizMCQ():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MidTermQuizMCQ'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MidTermQuizMCQ2')
def MidTermQuizMCQ2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MidTermQuizMCQ2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MyArrayList')
def MyArrayList():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'MyArrayList'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Observer')
def Observer():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Observer'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Optional')
def Optional():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Optional'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ParallelelMergeSort')
def ParallelelMergeSort():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ParallelelMergeSort'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PostScript')
def PostScript():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'PostScript'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ProducerConsumer')
def ProducerConsumer():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ProducerConsumer'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QueueWithStacks')
def QueueWithStacks():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'QueueWithStacks'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SharedCounter')
def SharedCounter():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'SharedCounter'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SieveOfEratosthenesImplementation')
def SieveOfEratosthenesImplementation():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'SieveOfEratosthenesImplementation'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SieveOfEratosthenesMCQ')
def SieveOfEratosthenesMCQ():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'SieveOfEratosthenesMCQ'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/StackWithQueue')
def StackWithQueue():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'StackWithQueue'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Streams')
def Streams():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Streams'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Streams2')
def Streams2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Streams2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/StringUtils')
def StringUtils():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'StringUtils'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)@app.route('/stat/ThreadsIntroduction')
def ThreadsIntroduction():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ThreadsIntroduction'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/TreeCombineWith')
def TreeCombineWith():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'TreeCombineWith'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/TreeInorder')
def TreeInorder():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'TreeInorder'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/TreeSame')
def TreeSame():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'TreeSame'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ValueOrReference')
def ValueOrReference():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ValueOrReference'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Visitor')
def Visitor():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Visitor'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/VisitorBasic')
def VisitorBasic():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'VisitorBasic'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/complexityMCQ2')
def complexityMCQ2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'complexityMCQ2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/fail')
def fail():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'fail'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/valley')
def valley():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'valley'"
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Fibonacci')
def Fibonacci():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'Fibonacci'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComplexitySpaceMCQ')
def ComplexitySpaceMCQ():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'ComplexitySpaceMCQ'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/2degree')
def degree():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'degree'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/2degree2')
def degree2():
    names = []
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    var = "'degree2'"
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Acc')
def Acc():
    names = []
    var = "'Acc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Ajoute')
def Ajoute():
    names = []
    var = "'Ajoute'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/AmazonConstructor')
def AmazonConstructor():
    names = []
    var = "'AmazonConstructor'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/AmazonPay')
def AmazonPay():
    names = []
    var = "'AmazonPay'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Average')
def Average():
    names = []
    var = "'Average'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Append')
def Append():
    names = []
    var = "'Append'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Assistant')
def Assistant():
    names = []
    var = "'Assistant'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Bath')
def Bath():
    names = []
    var = "'Bath'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BinarySearch')
def BinarySearch():
    names = []
    var = "'BinarySearch'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Carre')
def Carre():
    names = []
    var = "'Carre'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Compose')
def Compose():
    names = []
    var = "'Compose'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ComprehensionTranslation')
def ComprehensionTranslation():
    names = []
    var = "'ComprehensionTranslation'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Coordinates')
def Coordinates():
    names = []
    var = "'Coordinates'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Count')
def Count():
    names = []
    var = "'Count'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Count2')
def Count2():
    names = []
    var = "'Count2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/CountNested')
def CountNested():
    names = []
    var = "'CountNested'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Counters')
def Counters():
    names = []
    var = "'Counters'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DebtReminder')
def DebtReminder():
    names = []
    var = "'DebtReminder'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DeepConcat')
def DeepConcat():
    names = []
    var = "'DeepConcat'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DestroyAllEnnemies')
def DestroyAllEnnemies():
    names = []
    var = "'DestroyAllEnnemies'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DestroyAnEnnemy')
def DestroyAnEnnemy():
    names = []
    var = "'DestroyAnEnnemy'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DictCreation')
def DictCreation():
    names = []
    var = "'DictCreation'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DictCreationMax')
def DictCreationMax():
    names = []
    var = "'DictCreationMax'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DictKeyAccess')
def DictKeyAccess():
    names = []
    var = "'DictKeyAccess'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DiffCount')
def DiffCount():
    names = []
    var = "'DiffCount'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DoubleLink')
def DoubleLink():
    names = []
    var = "'DoubleLink'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DummyScript')
def DummyScript():
    names = []
    var = "'DummyScript'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Equals')
def Equals():
    names = []
    var = "'Equals'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exam-ClientListUpdate')
def Exam_ClientListUpdate():
    names = []
    var = "'Exam-ClientListUpdate'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exam-Enonce')
def Exam_Enonce():
    names = []
    var = "'Exam-Enonce'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exam-LoadMatrix')
def Exam_LoadMatrix():
    names = []
    var = "'Exam-LoadMatrix'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exam-PlusFrequent')
def Exam_PlusFrequent():
    names = []
    var = "'Exam-PlusFrequent'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exam-RainFall')
def Exam_RainFall():
    names = []
    var = "'Exam-RainFall'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Exceptions')
def Exceptions():
    names = []
    var = "'Exceptions'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Factorial')
def Factorial():
    names = []
    var = "'Factorial'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/fibonacci')
def fibonacci():
    names = []
    var = "'Fibonacci'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FileReading')
def FileReading():
    names = []
    var = "'FileReading'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FirstSum')
def FirstSum():
    names = []
    var = "'FirstSum'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/FizzBuzz')
def FizzBuzz():
    names = []
    var = "'FizzBuzz'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Flatten')
def Flatten():
    names = []
    var = "'Flatten'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/GCD')
def GCD():
    names = []
    var = "'GCD'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/GD')
def GD():
    names = []
    var = "'GD'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/GUI')
def GUI():
    names = []
    var = "'GUI'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hello')
def Hello():
    names = []
    var = "'Hello'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/HighOrder')
def HighOrder():
    names = []
    var = "'HighOrder'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hogwarts-I')
def Hogwarts_I():
    names = []
    var = "'Hogwarts-I'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hogwarts-II')
def Hogwarts_II():
    names = []
    var = "'Hogwarts-II'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hogwarts-III')
def Hogwarts_III():
    names = []
    var = "'Hogwarts-III'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hogwarts-IV')
def Hogwarts_IV():
    names = []
    var = "'Hogwarts-IV'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Hogwarts-V')
def Hogwarts_V():
    names = []
    var = "'Hogwarts-V'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Interests')
def Interests():
    names = []
    var = "'Interests'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Interval')
def Interval():
    names = []
    var = "'Interval'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedList')
def LinkedList():
    names = []
    var = "'LinkedList'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListChildren')
def LinkedListChildren():
    names = []
    var = "'LinkedListChildren'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListEndRemove')
def LinkedListEndRemove():
    names = []
    var = "'LinkedListEndRemove'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListInit')
def LinkedListInit():
    names = []
    var = "'LinkedListInit'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListInsert')
def LinkedListInsert():
    names = []
    var = "'LinkedListInsert'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListRemove')
def LLR():
    names = []
    var = "'LinkedListRemove'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LinkedListStr')
def LinkedListStr():
    names = []
    var = "'LinkedListStr'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/LoadSaveGame')
def LoadSaveGame():
    names = []
    var = "'LoadSaveGame'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Map')
def Map():
    names = []
    var = "'Map'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Max')
def Max():
    names = []
    var = "'Max'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Median')
def Median():
    names = []
    var = "'Median'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Memoization')
def Memoization():
    names = []
    var = "'Memoization'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/MergeList')
def MergeList():
    names = []
    var = "'MergeList'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Min')
def Min():
    names = []
    var = "'Min'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Morse')
def Morse():
    names = []
    var = "'Morse'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/NCompose')
def NCompose():
    names = []
    var = "'NCompose'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/NestParticipants')
def NestParticipants():
    names = []
    var = "'NestParticipants'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/NestedMin')
def NestedMin():
    names = []
    var = "'NestedMin'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PairOpposite')
def PairOpposite():
    names = []
    var = "'PairOpposite'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PairOrdered')
def PairOrdered():
    names = []
    var = "'PairOrdered'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PairSame')
def PairSame():
    names = []
    var = "'PairSame'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Participants')
def Participants():
    names = []
    var = "'Participants'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PathModule')
def PathModule():
    names = []
    var = "'PathModule'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PatternExtraction-I')
def PatternExtraction_I():
    names = []
    var = "'PatternExtraction-I'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PatternExtraction-II')
def PatternExtraction_II():
    names = []
    var = "'PatternExtraction-II'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PatternExtraction-III')
def PatternExtraction_III():
    names = []
    var = "'PatternExtraction-III'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Polynomial')
def Polynomial():
    names = []
    var = "'Polynomial'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Prime')
def Prime():
    names = []
    var = "'Prime'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Primes')
def Primes():
    names = []
    var = "'Primes'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF02')
def QBF02():
    names = []
    var = "'QBF02'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF03')
def QBF03():
    names = []
    var = "'QBF03'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF04')
def QBF04():
    names = []
    var = "'QBF04'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF05')
def QBF05():
    names = []
    var = "'QBF05'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF06')
def QBF06():
    names = []
    var = "'QBF06'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF07')
def QBF07():
    names = []
    var = "'QBF07'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF08')
def QBF08():
    names = []
    var = "'QBF08'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF09')
def QBF09():
    names = []
    var = "'QBF09'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF10')
def QBF10():
    names = []
    var = "'QBF10'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF11')
def QBF11():
    names = []
    var = "'QBF11'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF10_2019')
def QBF10_2019():
    names = []
    var = "'QBF10_2019'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Quetelet')
def Quetelet():
    names = []
    var = "'Quetelet'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/QBF01')
def QBF01():
    names = []
    var = "'QBF01'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL01')
def REAL01():
    names = []
    var = "'REAL01'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL02')
def REAL02():
    names = []
    var = "'REAL02'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL03')
def REAL03():
    names = []
    var = "'REAL03'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL04')
def REAL04():
    names = []
    var = "'REAL04'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL05')
def REAL05():
    names = []
    var = "'REAL05'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL06')
def REAL06():
    names = []
    var = "'REAL06'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL07')
def REAL07():
    names = []
    var = "'REAL07'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL07Review')
def REAL07Review():
    names = []
    var = "'REAL07Review'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL08')
def REAL08():
    names = []
    var = "'REAL08'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL09')
def REAL09():
    names = []
    var = "'REAL09'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL10')
def REAL10():
    names = []
    var = "'REAL10'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL11')
def REAL11():
    names = []
    var = "'REAL11'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL12')
def REAL12():
    names = []
    var = "'REAL12'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/REAL10_2019')
def REAL10_2019():
    names = []
    var = "'REAL10_2019'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/RSTTable')
def RSTTable():
    names = []
    var = "'RSTTable'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Recherche')
def Recherche():
    names = []
    var = "'Recherche'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/RecursiveFactorial')
def RecursiveFactorial():
    names = []
    var = "'RecursiveFactorial'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/RecursiveFibonacci')
def RecursiveFibonacci():
    names = []
    var = "'RecursiveFibonacci'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/RecursiveSum')
def RecursiveSum():
    names = []
    var = "'RecursiveSum'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Remainder')
def Remainder():
    names = []
    var = "'Remainder'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SMSStore')
def SMSStore():
    names = []
    var = "'SMSStore'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SessTest_QCM')
def SessTest_QCM():
    names = []
    var = "'SessTest_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session10_2019_QCM')
def Session10_2019_QCM():
    names = []
    var = "'Session10_2019_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session10_QCM')
def Session10_QCM():
    names = []
    var = "'Session10_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session11_QCM')
def Session11_QCM():
    names = []
    var = "'Session11_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session1_QCM')
def Session1_QCM():
    names = []
    var = "'Session1_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session2_QCM')
def Session2_QCM():
    names = []
    var = "'Session2_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session3_QCM')
def Session3_QCM():
    names = []
    var = "'Session3_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session4_QCM')
def Session4_QCM():
    names = []
    var = "'Session4_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session5_QCM')
def Session5_QCM():
    names = []
    var = "'Session5_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session6_QCM')
def Session6_QCM():
    names = []
    var = "'Session6_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session7_QCM')
def Session7_QCM():
    names = []
    var = "'Session7_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session8_QCM')
def Session8_QCM():
    names = []
    var = "'Session8_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Session9_QCM')
def Session9_QCM():
    names = []
    var = "'Session9_QCM'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Sieve')
def Sieve():
    names = []
    var = "'Sieve'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SimpleFactorial')
def SimpleFactorial():
    names = []
    var = "'SimpleFactorial'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SimpleMath')
def SimpleMath():
    names = []
    var = "'SimpleMath'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SimpleMax')
def SimpleMax():
    names = []
    var = "'SimpleMax'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Sort')
def Sort():
    names = []
    var = "'Sort'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SpeedingFine')
def SpeedingFine():
    names = []
    var = "'SpeedingFine'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/StudentConstructor')
def StudentConstructor():
    names = []
    var = "'StudentConstructor'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/StudentFileReading')
def StudentFileReading():
    names = []
    var = "'StudentFileReading'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/StudentInit')
def StudentInit():
    names = []
    var = "'StudentInit'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Sum')
def Sum():
    names = []
    var = "'Sum'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/SumToComplete')
def SumToComplete():
    names = []
    var = "'SumToComplete'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Testing')
def Testing():
    names = []
    var = "'Testing'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/TextToDic')
def TextToDic():
    names = []
    var = "'TextToDic'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Ticket')
def Ticket():
    names = []
    var = "'Ticket'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Translator')
def Translator():
    names = []
    var = "'Translator'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Triangle')
def Triangle():
    names = []
    var = "'Triangle'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/unittest1')
def unittest1():
    names = []
    var = "'unittest1'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/WrongIterations')
def WrongIterations():
    names = []
    var = "'WrongIterations'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/ZooGame')
def ZooGame():
    names = []
    var = "'ZooGame'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/truefalse')
def truefalse():
    names = []
    var = '"true""false"'
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BST')
def BST():
    names = []
    var = "'BST'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/BST_Insert_Delete')
def BST_Insert_Delete():
    names = []
    var = "'BST-Insert_Delete'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/DoubleLL')
def DoubleLL():
    names = []
    var = "'DoubleLL'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/EmployeList')
def EmployeList():
    names = []
    var = "'EmployeList'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Filemap')
def Filemap():
    names = []
    var = "'Filemap'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/PC')
def PC():
    names = []
    var = "'PC'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Search_and_replace')
def Search_and_replace():
    names = []
    var = "'Search_and_replace'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/Vectorfile')
def Vectorfile():
    names = []
    var = "'Vectorfile'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/absolute_value')
def absolute_value():
    names = []
    var = "'absolute_value'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/advanced_queue')
def advanced_queue():
    names = []
    var = "'advanced_queue'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/alist')
def alist():
    names = []
    var = "'alist'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/array_mmap')
def array_mmap():
    names = []
    var = "'array_mmap'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/asm1')
def asm1():
    names = []
    var = "'asm1'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/asm2')
def asm2():
    names = []
    var = "'asm2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/asm3')
def asm3():
    names = []
    var = "'asm3'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/asm4')
def asm4():
    names = []
    var = "'asm4'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/basic_linked_list')
def basic_linked_list():
    names = []
    var = "'basic_linked_list'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bits_leftmost')
def bits_leftmost():
    names = []
    var = "'bits_leftmost'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bits_rightmost')
def bits_rightmost():
    names = []
    var = "'bits_rightmost'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bits_spin')
def bits_spin():
    names = []
    var = "'bits_spin'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bits_strong')
def bits_strong():
    names = []
    var = "'bits_strong'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bits_sum')
def bits_sum():
    names = []
    var = "'bits_sum'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bitwise_ops')
def bitwise_ops():
    names = []
    var = "'bitwise-ops'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/bookstore')
def bookstore():
    names = []
    var = "'bookstore'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/btree_access')
def btree_access():
    names = []
    var = "'btree-access'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/calloc2')
def calloc2():
    names = []
    var = "'calloc2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/cmp_funct')
def cmp_funct():
    names = []
    var = "'cmp_funct'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/commandetest')
def commandetest():
    names = []
    var = "'commandetest'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/count_zero')
def count_zero():
    names = []
    var = "'count_zero'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/dames')
def dames():
    names = []
    var = "'dames'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/factorial')
def factorial():
    names = []
    var = "'factorial'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/fork')
def fork():
    names = []
    var = "'fork'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/gcd')
def gcd():
    names = []
    var = "'gcd'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/hexadecimal')
def hexadecimal():
    names = []
    var = "'hexadecimal'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/index_text')
def index_text():
    names = []
    var = "'index-text'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/insertion_sort')
def insertion_sort():
    names = []
    var = "'insertion-sort'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/intersection')
def intersection():
    names = []
    var = "'intersection'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/linked_lists_1')
def linked_lists_1():
    names = []
    var = "'linked_lists_1'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/linked_lists_2')
def linked_lists_2():
    names = []
    var = "'linked_lists_2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/linked_structs')
def linked_structs():
    names = []
    var = "'linked_structs'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/main_argc')
def main_argc():
    names = []
    var = "'main_argc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/malloc')
def malloc():
    names = []
    var = "'malloc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/matrix_mult')
def matrix_mult():
    names = []
    var = "'matrix-mult'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/mini_projet_string')
def mini_projet_string():
    names = []
    var = "'mini-projet-string'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/modem_read')
def modem_read():
    names = []
    var = "'modem_read'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/modem_read_bk')
def modem_read_bk():
    names = []
    var = "'modem_read_bk'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/multi_free')
def multi_free():
    names = []
    var = "'multi-free'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/my_sem')
def my_sem():
    names = []
    var = "'my-sem'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/my_strlen')
def my_strlen():
    names = []
    var = "'my_strlen'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/order_relation_linked_list')
def order_relation_linked_list():
    names = []
    var = "'order_relation_linked_list'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/p3check')
def p3check():
    names = []
    var = "'p3check'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/palindrome')
def palindrome():
    names = []
    var = "'palindrome'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/pointer_types')
def pointer_types():
    names = []
    var = "'pointer_types'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/poly')
def poly():
    names = []
    var = "'poly'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/printf')
def printf():
    names = []
    var = "'printf'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/reverse')
def reverse():
    names = []
    var = "'reverse'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/rpn_calc')
def rpn_calc():
    names = []
    var = "'rpn-calc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/run_redir')
def run_redir():
    names = []
    var = "'run_redir'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_ctf1')
def s1_ctf1():
    names = []
    var = "'s1_ctf1'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_ctf2')
def s1_ctf2():
    names = []
    var = "'s1_ctf2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_diff')
def s1_diff():
    names = []
    var = "'s1_diff'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_grep')
def s1_grep():
    names = []
    var = "'s1_grep'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT user_tasks.task , submissions.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by submissions.username order by submissions.grade desc"):
        names.append(row)
    for row in cursor.execute("SELECT user_tasks.task , user_tasks.username , user_tasks.course , max(submissions.grade,user_tasks.grade) from user_tasks left join submissions on submissions.id=user_tasks.id where user_tasks.task=" + var + " group by user_tasks.username order by user_tasks.grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_pipes')
def s1_pipes():
    names = []
    var = "'s1_pipes'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s1_tar')
def s1_tar():
    names = []
    var = "'s1_tar'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s2_make')
def s2_make():
    names = []
    var = "'s2_make'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s2_make_calc')
def s2_make_calc():
    names = []
    var = "'s2_make_calc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s2_make_mcq')
def s2_make_mcq():
    names = []
    var = "'s2_make_mcq'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s3_cunit_basics')
def s3_cunit_basics():
    names = []
    var = "'s3_cunit_basics'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from submissions where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s3_make')
def s3_make():
    names = []
    var = "'s3_make'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s3_make_mcq')
def s3_make_mcq():
    names = []
    var = "'s3_make_mcq'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s3_make_tests')
def s3_make_tests():
    names = []
    var = "'s3_make_tests'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s4_file_save_struct')
def s4_file_save_struct():
    names = []
    var = "'s4_file_save_struct'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s4_read_file_array_integer')
def s4_read_file_array_integer():
    names = []
    var = "'s4_read_file_array_integer'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s5_big_array_get_set')
def s5_big_array_get_set():
    names = []
    var = "'s5_big_array_get_set'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s5_file_copy')
def s5_file_copy():
    names = []
    var = "'s5_file_copy'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/s5_file_exists')
def s5_file_exists():
    names = []
    var = "'s5_file_exists'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/set_bit')
def set_bit():
    names = []
    var = "'set_bit'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/shell')
def shell():
    names = []
    var = "'shell'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/simple_stack')
def simple_stack():
    names = []
    var = "'simple_stack'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/sleep_malloc')
def sleep_malloc():
    names = []
    var = "'sleep_malloc'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/soumission_projet_cracker')
def soumission_projet_cracker():
    names = []
    var = "'soumission-projet-cracker'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/soumission_projet_fractale')
def soumission_projet_fractale():
    names = []
    var = "'soumission-projet-fractale'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/stack_vs_heap')
def stack_vs_heap():
    names = []
    var = "'stack_vs_heap'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/strcpy')
def strcpy():
    names = []
    var = "'strcpy'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/strsplit')
def strsplit():
    names = []
    var = "'strsplit'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/struct_cmp')
def struct_cmp():
    names = []
    var = "'struct_cmp'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/swap')
def swap():
    names = []
    var = "'swap'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/swap2int')
def swap2int():
    names = []
    var = "'swap2int'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/tab_find')
def tab_find():
    names = []
    var = "'tab_find'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/tri')
def tri():
    names = []
    var = "'tri'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/types')
def types():
    names = []
    var = "'types'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

@app.route('/stat/types2')
def types2():
    names = []
    var = "'types2'"
    conn=sqlite3.connect('inginious.sqlite')
    cursor=conn.cursor()
    for row in cursor.execute("SELECT task , username , course , max(grade) from user_tasks where task=" + var + " group by username order by grade desc"):
        names.append(row)
    return render_template("stat.html", names=names)

"""
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    
    FIN DES PAGES SUR LES DIFFERENTES TACHES INGINIOUS
    
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
     $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
    $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
"""



