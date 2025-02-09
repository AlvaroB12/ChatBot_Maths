import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Función para resolver expresiones matemáticas con solución paso a paso
def resolver_expresion(expresion):
    try:
        expresion_simbolica = sp.sympify(expresion)
        pasos = sp.simplify(expresion_simbolica)
        return pasos
    except Exception as e:
        return f"Error al procesar la expresión: {e}"

# Función para resolver ecuaciones
def resolver_ecuacion(ecuacion):
    try:
        x = sp.symbols('x')
        solucion = sp.solve(sp.sympify(ecuacion), x)
        return solucion
    except Exception as e:
        return f"Error al resolver la ecuación: {e}"

# Función para calcular derivadas
def calcular_derivada(expresion):
    try:
        x = sp.symbols('x')
        expresion_simbolica = sp.sympify(expresion)
        derivada = sp.diff(expresion_simbolica, x)
        return derivada
    except Exception as e:
        return f"Error al calcular la derivada: {e}"

# Función para calcular integrales
def calcular_integral(expresion):
    try:
        x = sp.symbols('x')
        expresion_simbolica = sp.sympify(expresion)
        integral = sp.integrate(expresion_simbolica, x)
        return integral
    except Exception as e:
        return f"Error al calcular la integral: {e}"

# Función para operaciones con matrices
def operar_matrices(operacion, matriz1, matriz2=None):
    try:
        A = sp.Matrix(matriz1)
        if operacion == "inversa":
            return A.inv()
        elif operacion == "determinante":
            return A.det()
        elif operacion == "suma" and matriz2:
            B = sp.Matrix(matriz2)
            return A + B
        elif operacion == "resta" and matriz2:
            B = sp.Matrix(matriz2)
            return A - B
        elif operacion == "multiplicacion" and matriz2:
            B = sp.Matrix(matriz2)
            return A * B
        else:
            return "Operación no válida."
    except Exception as e:
        return f"Error en operación con matrices: {e}"

# Función para simplificar funciones trigonométricas
def simplificar_trigonometria(expresion):
    try:
        expresion_simbolica = sp.sympify(expresion)
        simplificada = sp.trigsimp(expresion_simbolica)
        return simplificada
    except Exception as e:
        return f"Error al simplificar: {e}"

# Función para graficar funciones matemáticas
def graficar_funcion(expresion):
    try:
        x = sp.symbols('x')
        funcion = sp.lambdify(x, sp.sympify(expresion), 'numpy')

        x_vals = np.linspace(-10, 10, 400)
        y_vals = funcion(x_vals)

        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label=f"y = {expresion}", color='blue')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        st.pyplot(plt)
    except Exception as e:
        st.write(f"Error al graficar la función: {e}")

# Interfaz de usuario con Streamlit
st.title("Chatbot Matemático 🤖📚")
st.write("Introduce una expresión matemática para resolver, graficar o analizar.")

entrada_usuario = st.text_input("Escribe una expresión matemática:")

if entrada_usuario:
    if "=" in entrada_usuario:
        st.write("**Resolviendo ecuación...**")
        solucion = resolver_ecuacion(entrada_usuario)
        st.write(f"**Solución:** {solucion}")
    else:
        resultado = resolver_expresion(entrada_usuario)
        st.write(f"**Resultado:** {resultado}")

        derivada = calcular_derivada(entrada_usuario)
        st.write(f"**Derivada:** {derivada}")

        integral = calcular_integral(entrada_usuario)
        st.write(f"**Integral:** {integral}")

        trig_simplificada = simplificar_trigonometria(entrada_usuario)
        st.write(f"**Forma simplificada (trigonometría):** {trig_simplificada}")

        if 'x' in entrada_usuario:
            st.write("**Gráfico de la función:**")
            graficar_funcion(entrada_usuario)

# Sección de matrices
st.subheader("Operaciones con Matrices")
opcion_matriz = st.selectbox("Selecciona una operación:", ["Suma", "Resta", "Multiplicación", "Determinante", "Inversa"])

if opcion_matriz:
    filas = st.number_input("Número de filas:", min_value=1, max_value=5, value=2)
    columnas = st.number_input("Número de columnas:", min_value=1, max_value=5, value=2)

    matriz1 = []
    st.write("Introduce los valores de la primera matriz:")
    for i in range(filas):
        fila = st.text_input(f"Fila {i+1} (separada por comas):")
        matriz1.append([num for num in fila.split(",")])

    matriz2 = None
    if opcion_matriz in ["Suma", "Resta", "Multiplicación"]:
        matriz2 = []
        st.write("Introduce los valores de la segunda matriz:")
        for i in range(filas):
            fila = st.text_input(f"Fila {i+1} de la segunda matriz (separada por comas):")
            matriz2.append([num for num in fila.split(",")])

    if st.button("Calcular Matriz"):
        resultado_matriz = operar_matrices(opcion_matriz.lower(), matriz1, matriz2)
        st.write(f"**Resultado:**\n{resultado_matriz}")
