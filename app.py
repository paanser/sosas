import streamlit as st

# Lista de múltiplos desde 0.24 hasta 4.50 en pasos de 0.06
multiples = [round(0.24 + 0.06 * i, 2) for i in range(int((4.5 - 0.24) / 0.06) + 1)]

# Generar tabla de áreas (m²)
tabla = {}
for alto in multiples:
    fila = {}
    for ancho in multiples:
        area = round(alto * ancho, 2)
        fila[ancho] = area
    tabla[alto] = fila

def buscar_multiplo_superior(valor):
    for m in multiples:
        if m >= valor:
            return m
    return multiples[-1]

# Interfaz
st.title("Vidres SOSA - Presupuesto de Vidrios")

alto = st.number_input("Ingresa el alto (m)", min_value=0.0, step=0.01)
ancho = st.number_input("Ingresa el ancho (m)", min_value=0.0, step=0.01)

if alto > 0 and ancho > 0:
    area_original = alto * ancho
    st.write(f"Área original: **{area_original:.4f} m²**")

    alto_aj = buscar_multiplo_superior(alto)
    ancho_aj = buscar_multiplo_superior(ancho)
    st.write(f"Medidas ajustadas: Alto = **{alto_aj} m**, Ancho = **{ancho_aj} m**")

    area_ajustada = tabla[alto_aj][ancho_aj]
    st.write(f"Área ajustada según tabla: **{area_ajustada:.4f} m²**")

    if area_ajustada > 7:
        st.warning("¡Ojo, medida especial!")

    precio_m2 = st.number_input("Precio por m² del vidrio", min_value=0.0, step=0.1)
    if precio_m2 > 0:
        precio_vidrio = area_ajustada * precio_m2
        st.write(f"Precio total del vidrio: **${precio_vidrio:.2f}**")

        cantos = st.number_input("¿Cuántos cantos anchos?", min_value=0, step=1)
        lados = st.number_input("¿Cuántos cantos largos?", min_value=0, step=1)
        metros_lineales = (cantos * ancho_aj) + (lados * alto_aj)
        st.write(f"Metros lineales: **{metros_lineales:.2f} m**")

        total = precio_vidrio

        if st.checkbox("¿Agregar costo de canto pulido?"):
            precio_lineal = st.number_input("Precio por metro lineal", min_value=0.0, step=0.1)
            total_canto = metros_lineales * precio_lineal
            total += total_canto
            st.write(f"Costo de canto pulido: **${total_canto:.2f}**")

        if st.checkbox("¿Aplicar incremento porcentual?"):
            porcentaje = st.slider("Porcentaje (%)", 0.0, 100.0, 0.0)
            total *= (1 + porcentaje / 100)
            st.write(f"Total con incremento del {porcentaje:.1f}%: **${total:.2f}**")
        else:
            st.write(f"Total final: **${total:.2f}**")
