import sqlite3

conn=sqlite3.connect('inginious.sqlite')
cursor=conn.cursor()

l=[]

for row in cursor.execute("select task from user_tasks group by task"):
    l.append(row[0])
for c in l:
    g=0
    w=0
    for row in cursor.execute("select submissions.username,user_tasks.task,submissions.result,user_tasks.succeeded from submissions left join user_tasks on submissions.id=user_tasks.id where user_tasks.task='" + str(c) + "' group by submissions.username"):
        if row[2] == 'success' or row[3] == 'true':
            g+=1
        else:
            w+=1
    if w == 0 and g!=0:
        print("Moyenne de 100% de réussite pour la tache " + str(c))
    if w == 0 and g==0:
        print("Moyenne de 0% de réussite pour la tache " + str(c))
    if w !=0:
        print("Moyenne de " + str(round(g/(g+w)*100)) + "% de réussite pour la tache " + str(c))
