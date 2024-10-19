from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
inscripciones = []
usuarios = []
productos = []
libros = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        inscripciones.append({'nombre': nombre, 'apellidos': apellidos, 'curso': curso})
        return redirect(url_for('inscripcion_curso'))  
    return render_template('inscripcion_curso.html', inscripciones=inscripciones)



@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contraseña = request.form['contraseña']   
        usuarios.append({'nombre': nombre, 'apellidos': apellidos, 'correo': correo})
        return redirect(url_for('registro_usuario')) 
    return render_template('registro_usuario.html', usuarios=usuarios)


@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        nombre_producto = request.form['nombre_producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        
        
        productos.append({
            'nombre_producto': nombre_producto,
            'categoria': categoria,
            'existencia': existencia,
            'precio': precio
        })
        return redirect(url_for('registro_productos'))  
    return render_template('registro_productos.html', productos=productos)

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        
     
        libros.append({
            'titulo': titulo,
            'autor': autor,
            'resumen': resumen,
            'medio': medio
        })
        return redirect(url_for('registro_libros'))  
    return render_template('registro_libros.html', libros=libros)

if __name__ == '__main__':
    app.run(debug=True)