from sentence_transformers import SentenceTransformer, util

# Cargar modelo de lenguaje
modelo = SentenceTransformer('all-MiniLM-L6-v2')  # Pequeño y rápido

def vectorizar_libros(libros):
    textos = [f"{libro.titulo} {libro.autor} {libro.editorial} {libro.isbn}" for libro in libros]
    embeddings = modelo.encode(textos, convert_to_tensor=True)
    return embeddings, libros

def buscar_libros_por_ia(consulta, libros):
    embeddings_libros, libros = vectorizar_libros(libros)
    embedding_consulta = modelo.encode(consulta, convert_to_tensor=True)

    similitudes = util.cos_sim(embedding_consulta, embeddings_libros)[0]
    top_k = 5
    indices = similitudes.argsort(descending=True)[:top_k]

    resultados = []
    for idx in indices:
        if similitudes[idx] > 0.4:  # umbral de similitud
            resultados.append(libros[idx])
    return resultados