from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import models
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='berelic'
mysql=MySQL(app)
hola=models.categoria()
objCat=models.categoria()
# settings
app.secret_key='mysecretkey'
@app.route('/')
def home():
    hola.idCat=12
    print(hola.idCat)
    hola.nomCat="Patricio"
    print(hola.nomCat)
    return render_template('home.html')
#def home():
#    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/admin')
def admin():
    cur=mysql.connection.cursor()
    cur.execute('Select * From categoria')
    data=cur.fetchall()
    return render_template('admin.html', cat=data)
@app.route('/add_cat', methods=['POST'])
def add_categoria():
    if request.method=='POST':
        objCat.nomCat=request.form['nombre']
        print(type(objCat.nomCat))
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO categoria (nombre) VALUES (%s)',(objCat.nomCat,))
        mysql.connection.commit()
        flash('Categoria agragada exitosamente')
        return redirect(url_for('admin'))
@app.route('/delete_categoria/<string:id>')
def delete_categoria(id):
    cur= mysql.connection.cursor()
    cur.execute('DELETE FROM categoria WHERE id_categoria= (%s)', (id,))
    mysql.connection.commit()
    flash ('Categoria eliminada con exito')
    return redirect(url_for('admin'))
@app.route('/edit_categoria/<string:id>')
def get_categoria(id):
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM categoria WHERE id_categoria= (%s)', (id,))
    mysql.connection.commit()
    data=cur.fetchall()
    print(data[0])
    return render_template('admin.html', hola=data[0])
@app.route('/actualizar_categoria/<string:id>', methods=['POST'])
def actualizar_categoria(id):
        if request.method=='POST':
                nombre=request.form['nombre2']
                cur= mysql.connection.cursor()
                cur.execute("""
                UPDATE categoria
                set nombre= %s
                where id_categoria=%s
                 """,(nombre,id))
                mysql.connection.commit()
                flash('Categoria agregada exitosamente')
                return redirect(url_for('admin'))
if __name__=='__main__':
    app.run(debug=True)