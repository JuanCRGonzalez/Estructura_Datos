from flask import Flask, render_template, request, redirect, url_for, jsonify
from biblioteca import Biblioteca, Libro, Usuario, Prestamo, Bibliotecario
from datetime import datetime
from asistente_ia import buscar_libros_por_ia

app= Flask(__name__)
biblioteca = Biblioteca()
bibliotecario = Bibliotecario(1, "Juanito")


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/libros", methods=["GET", "POST"])
def manejar_libros():
    if request.method =='POST':
        data= request.form.to_dict()
        nuevo_libro = Libro(
            titulo = data['titulo'],
            autor = data['autor'],
            isbn = data['isbn'],
            editorial = data['editorial'],
            fecha_publicacion = data['fecha_publicacion']
        )
        bibliotecario.añadir_libro(biblioteca, nuevo_libro)
        return redirect(url_for('manejar_libros'))
    elif request.method == 'GET':
        return render_template("libros.html", libros=biblioteca.libros)

    return render_template("libros.html")


@app.route('/usuarios', methods=['GET', 'POST'])
def manejar_usuarios():
    if request.method == 'POST':
        data = request.form.to_dict()
        nuevo_usuario = Usuario(
            id_usuario=str(data['id_usuario']),
            nombre=data['nombre'],
            email=data['email'],
        )
        biblioteca.registrar_usuarios(nuevo_usuario)
        return redirect(url_for('manejar_usuarios'))
    elif request.method == 'GET':
        return render_template('usuarios.html', usuarios=biblioteca.usuarios)


@app.route('/prestamos', methods=['GET', 'POST'])
def gestionar_prestamos():
    if request.method == 'POST':
        data = request.form.to_dict()
        id_usuario = str(data['id_usuario'])
        isbn = str(data['isbn'])
        usuario = next((u for u in biblioteca.usuarios if str(u.id_usuario)==id_usuario), None)
        libro = next((l for l in biblioteca.libros if str(l.isbn)), None)
        if not usuario or not libro:
            return jsonify({'mensaje': 'Usuario o libro o encontrado'}), 404
        if 'fecha_prestamo' in data:
            if not libro.disponible:
                return jsonify ({'mensaje': f'El libro "{libro.titulo}" ya esta prestado'}), 400
            
            fecha_prestamo = datetime.strptime(data['fecha_prestamo'], '%Y-%m-%d')
            fecha_devolucion = datetime.strptime(data['fecha_devolucion'], '%Y-%m-%d')
            usuario.prestar_libro()
            nuevo_prestamo = Prestamo(
                id_prestamo=len(biblioteca.prestamo) + 1,
                libro = libro,
                usuario = usuario,
                fecha_prestamo = fecha_prestamo,
                fecha_devolucion = fecha_devolucion,
            )
            biblioteca.prestamos.append(nuevo_prestamo)
            resultado= f"Libro {libro.titulo} prestado a {usuario.nombre}"

        else:
            prestamo=next((p for p in biblioteca.prestamos if str(p.libro.isbn) == isbn and str(p.usuario.id_usuario) == id_usuario), None)

            if not prestamo:
                return jsonify({'mensaje:"{libro.titulo}" no esta prestado al usuario {usuario.nombre}'}), 400

            usuario.devolver_libro(libro)
            biblioteca.prestamos.remove(prestamo)
            resultado = f"libro {libro.titulo} devuelto por {usuario.nombre}"
        return jsonify({'mensaje': resultado})
    elif request.method == 'GET':
        return render_template('prestamos.html', usuarios = biblioteca.usuarios, libros=biblioteca.libros, prestamo=biblioteca.prestamo)
    

@app.route('/asistente', methods=['GET', 'POST'])
def asistente_virtual():
    resultado = ""
    if request.method == 'POST':
        consulta = request.form['consulta']
        libros_encontrados = buscar_libros_por_ia(consulta, biblioteca.libros)

        if libros_encontrados:
            resultado = "Resultados encontrados:<br>"
            for libro in libros_encontrados:
                resultado += f"{libro.titulo} por {libro.autor} (ISBN: {libro.isbn})<br>"
        else:
            resultado = "No se encontraron libros que coincidan con tu consulta."
    return render_template("asistente.html", resultado=resultado)

@app.route('/buscar', methods=['POST'])
def buscar_libros():
    consulta = request.form.get('consulta', '')
    libros_encontrados = buscar_libros_por_ia(consulta, biblioteca.libros)

    return render_template("resultados_busqueda.html", consulta=consulta, resultados=libros_encontrados)    




if __name__ == "__main__":
    app.run(debug=True)