
import streamlit as st

# Lista de múltiplos desde 0.24 hasta 4.50 en pasos de 0.06
multiples = [round(0.24 + 0.06 * i, 2) for i in range(int((4.5 - 0.24) / 0.06) + 1)]

def buscar_multiplo_superior(valor):
    for m in multiples:
        if m >= valor:
            return m
    return multiples[-1]

# Diccionario completo de precios
precios = {
    "FLOAT 4 MM": 13.1,
    "FLOAT 6 MM": 21.65,
    "LAMINADO 3+3": 26.73,
    "LAMINADO 4+4": 31.72,
    "TEMPLADO 6 MM": 35.5,
    "TEMPLADO 8 MM": 50.2,
    "TEMPLADO 10 MM": 65.4
    # Aquí irían todos los demás precios reales
}

# Agrupar precios por categoría
from collections import defaultdict
categorias = defaultdict(list)
for nombre, precio in precios.items():
    categoria = nombre.split()[0]
    categorias[categoria].append((nombre, precio))

# Paso 1: Medidas
st.title("Calculadora de Presupuesto de Cristales")

st.header("Paso 1: Introduce las medidas del cristal")
ancho_cm = st.number_input("Ancho (cm)", min_value=0.0, step=0.1)
alto_cm = st.number_input("Alto (cm)", min_value=0.0, step=0.1)

if ancho_cm > 0 and alto_cm > 0:
    area_real = round((ancho_cm / 100) * (alto_cm / 100), 2)
    alto_m = alto_cm / 100
    ancho_m = ancho_cm / 100
    area_ajustada = round(buscar_multiplo_superior(alto_m) * buscar_multiplo_superior(ancho_m), 2)

    st.markdown(f"**Área real:** {area_real} m²")
    st.markdown(f"**Área ajustada:** {area_ajustada} m²")

    st.header("Paso 2: Selecciona cómo calcular el precio por m²")
    modo_precio = st.radio("¿Cómo quieres ingresar el precio?", ["Ingresar manualmente", "Seleccionar desde tarifa"])

    if modo_precio == "Ingresar manualmente":
        st.subheader("Referencia de precios (chuleta)")
        st.dataframe({k: [v] for k, v in precios.items()})
        precio_m2 = st.number_input("Introduce el precio por m²", min_value=0.0, step=0.1)

    else:
        st.subheader("Selecciona una categoría")
        categoria = st.selectbox("Categoría de cristal", list(categorias.keys()))
        tabla_categoria = {nombre: precio for nombre, precio in categorias[categoria]}
        st.dataframe(tabla_categoria, use_container_width=True)
        seleccion = st.selectbox("Selecciona el tipo de cristal", list(tabla_categoria.keys()))
        precio_m2 = precios[seleccion]

    st.header("Paso 3: Resultado final")
    subtotal = area_ajustada * precio_m2
    st.markdown(f"**Subtotal:** {subtotal:.2f} €")

    if st.checkbox("¿Aplicar canto pulido?"):
        metros_lineales = ((ancho_cm + alto_cm) * 2) / 100
        total_canto = metros_lineales * 1.5  # ejemplo de costo lineal
        subtotal += total_canto
        st.markdown(f"Costo de canto pulido: {total_canto:.2f} €")

    if st.checkbox("¿Aplicar incremento porcentual?"):
        porcentaje = st.number_input("Porcentaje a aplicar (%)", min_value=0.0, step=0.1)
        subtotal *= (1 + porcentaje / 100)
        st.markdown(f"Total con incremento: **{subtotal:.2f} €**")
    else:
        st.markdown(f"**Total final: {subtotal:.2f} €**")
