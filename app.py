
import streamlit as st
import urllib.parse

# Encabezado
st.markdown("<h1 style='text-align:center;'>Calculador de Precios</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Vidres de Sosa, basado en Regulass</h3>", unsafe_allow_html=True)
st.image("logo.png", width=120)
st.markdown("---")

# Estilo móvil
st.markdown("""<style>html, body, [class*='css']  { font-size: 18px; }</style>""", unsafe_allow_html=True)

# Múltiplos
multiples = [round(0.24 + 0.06 * i, 2) for i in range(int((4.5 - 0.24) / 0.06) + 1)]
def buscar_multiplo_superior(valor):
    for m in multiples:
        if m >= valor:
            return m
    return multiples[-1]

# Precios agrupados (simplificado)
categorias = {
    "Float": {
        "FLOAT 4 MM": 13.10,
        "FLOAT 6 MM": 21.65
    },
    "Laminado": {
        "LAMINADO 3+3": 26.73,
        "LAMINADO 4+4": 31.72
    },
    "Templado": {
        "TEMPLADO 4 MM": 30.20,
        "TEMPLADO 6 MM": 40.20
    }
}

# Entradas de usuario
alto = st.number_input("Alto (m)", min_value=0.0, step=0.01)
ancho = st.number_input("Ancho (m)", min_value=0.0, step=0.01)

cat = st.selectbox("Selecciona categoría", list(categorias.keys()))
producto = st.selectbox("Selecciona producto", list(categorias[cat].keys()))
precio_m2 = categorias[cat][producto]

# Expansor con todos los precios
with st.expander("Ver lista completa de precios"):
    for c in categorias:
        st.markdown(f"**{c}**")
        for p, v in categorias[c].items():
            st.write(f"- {p}: {v:.2f} €")

# Acción al presionar "Calcular"
if st.button("Calcular presupuesto"):
    if alto == 0 or ancho == 0:
        st.warning("Introduce alto y ancho mayores a 0")
        st.stop()

    alto_aj = buscar_multiplo_superior(alto)
    ancho_aj = buscar_multiplo_superior(ancho)
    area_aj = round(alto_aj * ancho_aj, 2)

    st.write(f"Medidas ajustadas: {alto_aj} m x {ancho_aj} m")
    st.write(f"Área ajustada: {area_aj:.2f} m²")

    subtotal = area_aj * precio_m2
    st.write(f"Subtotal vidrio: {subtotal:.2f} €")

    cantos = st.number_input("¿Cuántos cantos anchos?", min_value=0, step=1)
    lados = st.number_input("¿Cuántos cantos largos?", min_value=0, step=1)
    metros_lineales = (cantos * ancho_aj) + (lados * alto_aj)
    st.write(f"Metros lineales: {metros_lineales:.2f} m")

    total = subtotal
    resumen = f"Producto: {producto}\nÁrea ajustada: {area_aj:.2f} m²\nPrecio m²: {precio_m2:.2f} €\nSubtotal: {subtotal:.2f} €\n"

    if st.checkbox("¿Agregar canto pulido?"):
        precio_lineal = st.number_input("Precio por metro lineal", min_value=0.0, step=0.1)
        costo_canto = metros_lineales * precio_lineal
        total += costo_canto
        resumen += f"Canto pulido: {costo_canto:.2f} €\n"

    if st.checkbox("¿Aplicar incremento porcentual?"):
        porc = st.number_input("¿Qué porcentaje?", min_value=0.0, step=0.1)
        if porc > 0:
            incremento = total * (porc / 100)
            total += incremento
            resumen += f"Incremento ({porc:.1f}%): {incremento:.2f} €\n"

    resumen += f"TOTAL: {total:.2f} €"
    st.markdown(f"### Total final: **{total:.2f} €**")

    st.download_button("Descargar presupuesto", resumen, file_name="presupuesto.txt")

    mensaje = urllib.parse.quote(resumen.replace("\n", "\n"))
    whatsapp_url = f"https://wa.me/?text={mensaje}"
    st.markdown(f"[Compartir por WhatsApp]({whatsapp_url})")
