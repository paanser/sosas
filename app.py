
import streamlit as st
import urllib.parse
st.markdown("""<style>html, body, [class*='css']  { font-size: 18px; }</style>""", unsafe_allow_html=True)

# Encabezado
st.markdown("<h1 style='text-align:center;'>Calculador de Precios</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Vidres de Sosa, basado en Regulass</h3>", unsafe_allow_html=True)
st.image("logo.png", width=120)
st.markdown("---")

# Entrada de medidas
alto = st.number_input("Ingresa el alto (m)", min_value=0.0, step=0.01)
ancho = st.number_input("Ingresa el ancho (m)", min_value=0.0, step=0.01)

if alto == 0 or ancho == 0:
    st.warning("Por favor, introduce alto y ancho mayores a 0")
    st.stop()

# Categorías y productos
categorias = {}
categorias["Otros"] = {
    "GUARDIAN SELECT SUSTITUCION": 20.5,
    "GUARDIAN SELECT BASE": 20.5,
    "GUARDIAN SELECT TRIPLE": 46.4,
    "BALDOSILLA ARMADA": 41.35,
    "BALDOSILLA ARMADA (SUST)": 31.4,
    "NEOCERAM 4 MM": 266.6,
    "UGLAS ARMADO": 79.5,
    "RAYWALL 45 CLEAR 4MM": 34.5,
    "RAYWALL 45 CLEAR 4MM (SUST)": 27.6,
    "MATE ACIDO 3 MM": 29.1,
    "MATE ACIDO 4 MM": 32.7,
    "MATE ACIDO 4 MM (SUST)": 24.2,
    "MATE ACIDO 5 MM": 36.7,
    "MATE ACIDO 5 MM (SUST)": 27.4,
    "MATE ACIDO 6 MM": 40.7,
    "MATE ACIDO 6 MM (SUST)": 30.6,
    "NOVOMAT 5 MM": 41.75,
    "NOVOMAT 5 MM (SUST)": 31.4,
    "CLIMAGUARD 4 MM": 6.0,
    "CLIMAGUARD 6 MM": 10.0,
    "GUARDIAN SUN 4 MM": 11.2,
    "GUARDIAN SUN 6 MM": 18.9,
    "STOPSOL CLASSIC INC. 5 MM": 53.8,
    "STOPSOL CLASSIC INC. 5 MM (SUST)": 40.6,
    "STOPSOL SUPERSILVER GRIS 6 MM": 74.45,
    "STOPSOL SUPERSILVER GRIS 6 MM (SUST)": 57.6,
    "SUNGUARD ROYAL BLUE 6MM": 71.4,
    "SUNGUARD ROYAL BLUE 6MM (SUST)": 55.2,
    "CLIMAGUARD PREMIUM 44.1": 29.3,
    "GUARDIAN SUN 44.1": 35.6,
    "GUARDIAN SUN 66.1": 58.3,
    "CLIMAGUARD PREMIUM 33.1": 25.9,
    "LAMINAR ACUSTICO 3+3": 48.3,
    "LAMINAR ACUSTICO 3+3 (SUST)": 27.0,
    "LAMINAR ACUSTICO 4+4": 35.0,
    "LAMINAR ACUSTICO 4+4 (SUST)": 40.1,
    "LAMINAR ACUSTICO 5+5": 63.4,
    "LAMINAR ACUSTICO 5+5 (SUST)": 44.4,
    "LAMINAR ACUSTICO 6+6": 71.4,
    "LAMINAR ACUSTICO 6+6 (SUST)": 50.7,
    "BARROTILLO LAC. BL ANCHO INGLET": 9.0,
    "BARROTILLO LAC. BL ESTRECH CRUCET": 4.88,
    "BARROTILLO LAC. BL ESTRE INGLET": 9.0,
}
categorias["Float"] = {
    "FLOAT 2 MM": 11.6,
    "FLOAT 3 MM": 12.6,
    "FLOAT 4 MM": 13.1,
    "FLOAT 5 MM": 18.1,
    "FLOAT 5 MM (SUST)": 6.0,
    "FLOAT 6 MM": 21.65,
    "FLOAT 6 MM (SUST)": 7.5,
    "FLOAT 8 MM": 32.2,
    "FLOAT 8 MM (SUST)": 16.1,
    "FLOAT 10 MM": 36.2,
    "FLOAT 10 MM (SUST)": 28.2,
}
categorias["Tintado / Reflejado"] = {
    "PARSOL BRONCE 4 MM": 24.2,
    "PARSOL BRONCE 4 MM (SUST)": 18.4,
    "PARSOL BRONCE 5 MM": 27.8,
    "PARSOL BRONCE 5 MM (SUST)": 21.1,
    "PARSOL GRIS 4 MM": 24.2,
    "PARSOL GRIS 4 MM (SUST)": 18.4,
    "PARSOL GRIS 5 MM": 27.8,
    "PARSOL GRIS 5 MM (SUST)": 21.1,
    "PARSOL GRIS 6 MM": 42.8,
    "PARSOL GRIS 6 MM (SUST)": 32.5,
    "PLATA 3 MM": 26.0,
    "PLATA 3 MM (SUST)": 19.8,
    "PLATA 5 MM": 34.2,
    "PLATA 5 MM (SUST)": 26.0,
    "PLATA 6 MM": 41.35,
    "PLATA 6 MM (SUST)": 31.4,
    "PLATA GRIS 5 MM": 48.1,
    "PLATA ROSA 5MM": 80.5,
}
categorias["Texturados"] = {
    "CARGLAS INCOLORO": 21.4,
    "CARGLAS INCOLORO (SUST)": 12.6,
    "CARGLAS NEW": 24.2,
    "CARGLAS NEW (SUST)": 18.4,
    "CARGLAS 6 INCOLORO": 46.8,
    "CARGLAS 6 INCOLORO (SUST)": 36.2,
    "CARGLAS BRONCE": 42.3,
    "CARGLAS BRONCE (SUST)": 20.2,
    "CATEDRAL ARMADO INCOLORO": 41.35,
    "CATEDRAL ARMADO INCOLORO (SUST)": 31.4,
    "CARGLAS ARMADO INCOLORO": 41.35,
    "CARGLAS ARMADO INCOLORO (SUST)": 31.4,
}
categorias["Decorativos"] = {
    "MADRAS ESCARCHA": 118.7,
    "MADRAS ESCARCHA (SUST)": 93.0,
    "MADRAS ESPIGAS": 118.7,
    "MADRAS ESPIGAS (SUST)": 93.0,
    "MADRAS NEBULOSA": 118.7,
    "MADRAS NEBULOSA (SUST)": 93.0,
    "MADRAS PICS": 118.7,
    "MADRAS PICS (SUST)": 93.0,
    "MADRAS PINO": 118.7,
    "MADRAS PINO (SUST)": 93.0,
    "MADRAS MIL RAYAS": 128.7,
    "MADRAS MIL RAYAS (SUST)": 101.0,
    "MADRAS NEBULOSA ROSA": 178.1,
    "MADRAS NEBULOSA ROSA (SUST)": 142.5,
    "BRILL GLASS ELEGANT ORO": 205.75,
    "BRILL GLASS ELEGANT ORO (SUST)": 164.6,
    "BRILL GLASS TON AZUL": 205.75,
    "BRILL GLASS TON AZUL (SUST)": 162.6,
    "BRILL GLASS TON ROJO": 205.75,
    "BRILL GLASS TON ROJO (SUST)": 162.6,
    "BRILL GLASS HOJAS": 205.75,
    "BRILL GLASS HOJAS (SUST)": 162.6,
    "BRILL GLASS GAUDI": 205.75,
    "BRILL GLASS GAUDI (SUST)": 162.6,
}
categorias["Laminado"] = {
    "LAMINADO 3+3": 26.73,
    "LAMINADO 3+3 (SUST)": 17.0,
    "LAMINADO 4+4": 31.72,
    "LAMINADO 4+4 (SUST)": 23.0,
    "LAMINADO 5+5": 36.18,
    "LAMINADO 5+5 (SUST)": 26.0,
    "LAMINADO 6+6": 46.8,
    "LAMINADO 6+6 (SUST)": 37.4,
    "LAMINADO 8+8": 43.06,
    "LAMINADO 8+8 (SUST)": 58.4,
    "LAMINADO 3+3 MATE": 39.42,
    "LAMINADO 3+3 MATE (SUST)": 33.0,
    "LAMINADO 4+4 MATE": 43.87,
    "LAMINADO 4+4 MATE (SUST)": 37.0,
    "LAMINADO 5+5 MATE": 55.57,
    "LAMINADO 5+5 MATE (SUST)": 46.2,
    "LAMINADO 6+6 MATE": 66.9,
    "LAMINADO 6+6 MATE (SUST)": 51.5,
    "LAMINADOS 3+3 MATE+GRIS": 71.95,
    "LAMINADOS 3+3 MATE+GRIS (SUST)": 57.6,
    "LAMINADO 3+3 AZUL": 45.3,
    "LAMINADO 3+3 AZUL (SUST)": 34.2,
    "LAMINADO 4+4 AZUL": 53.35,
    "LAMINADO 4+4 AZUL (SUST)": 40.6,
    "LAMINADO 4+4 AZUL + MATE": 76.95,
    "LAMINADO 4+4 AZUL + MATE (SUST)": 59.6,
    "LAMINADO 3+3 BRONCE": 45.3,
    "LAMINADO 3+3 BRONCE (SUST)": 34.2,
    "LAMINADO 4+4 BRONCE": 53.35,
    "LAMINADO 4+4 BRONCE (SUST)": 40.6,
    "LAMINADO 4+4  BRONCE + MATE": 76.95,
    "LAMINADO 4+4  BRONCE + MATE (SUST)": 59.6,
    "LAMINADO 3+3 GRIS": 45.3,
    "LAMINADO 3+3 GRIS (SUST)": 34.2,
    "LAMINADO 4+4 GRIS": 53.35,
    "LAMINADO 4+4 GRIS (SUST)": 40.6,
    "LAMINADO 5+5 GRIS": 56.8,
    "LAMINADO 5+5 GRIS (SUST)": 43.5,
    "LAMINADO 3+3 MATE+AZUL": 76.95,
    "LAMINADO 3+3 MATE+AZUL (SUST)": 59.6,
    "LAMINADO  4+4 GRIS + MATE": 76.95,
    "LAMINADO  4+4 GRIS + MATE (SUST)": 59.6,
    "LAMINADO 4+4 POLAR WHITE": 90.5,
    "LAMINADO 4+4 POLAR WHITE (SUST)": 72.4,
    "LAMINADO 4+4 MINT GREEN+POLAR WHITE": 150.9,
    "LAMINADO 6+6.2 MINT GREEN": 163.5,
    "LAMINADO 6+6.2 MINT GREEN (SUST)": 130.8,
    "LAMINADO 4+4 STOPSOL CLASSIC": 62.9,
    "LAMINADO 4+4 STOPSOL CLASSIC (SUST)": 50.3,
    "LAMINADO 5+5 STOPSOL SUPERSILVER GRIS": 115.5,
    "LAMINADO 5+5 STOPSOL SUPERSILVER GRIS (SUST)": 92.4,
    "LAMINADO 5+5 SG ROYAL BLUE 20": 105.6,
    "LAMINADO 5+5 SG ROYAL BLUE 20 (SUST)": 84.5,
    "LAMINADO 10+DREAMS 10 SATINADO,2": 313.6,
    "LAMINADO 10+DREAMS 10 SATINADO,2 (SUST)": 238.4,
    "LAMINADO 10+DREAMS10 TRANSP.,2": 313.6,
    "LAMINADO 10+DREAMS10 TRANSP.,2 (SUST)": 238.4,
}
categorias["Seguridad"] = {
    "ANTIRROBO 6+6+6": 110.65,
    "ANTIRROBO 6+6+6 (SUST)": 86.5,
    "44.4 ANTII AGRESION PS9": 83.0,
    "44.4 ANTII AGRESION PS9 (SUST)": 64.4,
    "66.4 ANTI  AGRESION P4A": 110.65,
    "66.4 ANTI  AGRESION P4A (SUST)": 86.5,
    "44.6 ANTI AGRESION P5A": 95.6,
    "44.6 ANTI AGRESION P5A (SUST)": 74.4,
    "66.6 ANTI AGRESION P6B": 130.8,
    "66.6 ANTI AGRESION P6B (SUST)": 102.6,
    "ANTIBALA 10+10+2.5(BR1)": 164.5,
    "ANTIBALA 10+10+2.5(BR1) (SUST)": 130.0,
    "ANTIBALA 3+6+6+6+3 (BR2)": 181.1,
    "ANTIBALA 3+6+6+6+3 (BR2) (SUST)": 142.8,
}
categorias["Templado"] = {
    "TEMPLADO 4 MM": 30.2,
    "TEMPLADO 4 MM (SUST)": 24.2,
    "TEMPLADO 5 MM": 35.25,
    "TEMPLADO 5 MM (SUST)": 28.2,
    "TEMPLADO 6 MM": 40.2,
    "TEMPLADO 6 MM (SUST)": 32.2,
    "TEMPLADO 8 MM": 50.3,
    "TEMPLADO 8 MM (SUST)": 40.2,
    "TEMPLADO 10 MM": 60.4,
    "TEMPLADO 10 MM (SUST)": 48.3,
    "TEMPLADO 12 MM": 110.65,
    "TEMPLADO 12 MM (SUST)": 88.5,
    "TEMPLADO MATE 4 MM.": 60.4,
    "TEMPLADO MATE 4 MM. (SUST)": 48.3,
    "TEMPLADO MATE 5 MM.": 65.4,
    "TEMPLADO MATE 5 MM. (SUST)": 52.3,
    "TEMPLADO MATE 6 MM.": 75.5,
    "TEMPLADO MATE 6 MM. (SUST)": 60.4,
    "TEMPLADO MATE 8 MM.": 108.15,
    "TEMPLADO MATE 8 MM. (SUST)": 86.5,
    "TEMPLADO MATE 10 MM.": 125.75,
    "TEMPLADO MATE 10 MM. (SUST)": 100.6,
}

cat_sel = st.selectbox("Selecciona una categoría de vidrio", list(categorias.keys()))
producto_sel = st.selectbox("Selecciona el producto", list(categorias[cat_sel].keys()))
precio_m2 = categorias[cat_sel][producto_sel]

# Mostrar lista completa de precios (opcional)
with st.expander("Ver lista completa de precios"):
    for c in categorias:
        st.markdown(f"**{c}**")
        for p, v in categorias[c].items():
            st.write(f"- {p}: {v:.2f} €")

# Opciones adicionales
precio_lineal = 0.0
if agregar_canto:

porc = 0.0
if agregar_incremento:

# Botón de cálculo
if st.button("Calcular presupuesto"):
    area = alto * ancho
    st.write(f"Área original: **{area:.4f} m²**")

    # Ajuste de área a múltiplos
    multiples = [round(0.24 + 0.06 * i, 2) for i in range(int((4.5 - 0.24) / 0.06) + 1)]
    def buscar_multiplo_superior(valor):
        for m in multiples:
            if m >= valor:
                return m
        return multiples[-1]

    alto_aj = buscar_multiplo_superior(alto)
    ancho_aj = buscar_multiplo_superior(ancho)
    area_aj = round(alto_aj * ancho_aj, 2)

    st.write(f"Área ajustada: **{area_aj:.2f} m²**")

    precio_base = area_aj * precio_m2
    st.write(f"Precio por m²: **{precio_m2:.2f} €**")
    st.write(f"Subtotal vidrio: **{precio_base:,.2f} €**")

    cantos = st.number_input("¿Cuántos cantos anchos?", min_value=0, step=1)
    lados = st.number_input("¿Cuántos cantos largos?", min_value=0, step=1)
    agregar_canto = st.checkbox("¿Agregar canto pulido?")
    precio_lineal = 0.0
    if agregar_canto:
        precio_lineal = st.number_input("Precio por metro lineal", min_value=0.0, step=0.1)
    metros_lineales = (cantos * ancho_aj) + (lados * alto_aj)
    st.write(f"Metros lineales: **{metros_lineales:.2f} m**")

    total = precio_base
    resumen = f"Producto: {producto_sel}\nÁrea ajustada: {area_aj:.2f} m²\nPrecio m²: {precio_m2:.2f} €\nSubtotal: {precio_base:.2f} €\n"

    if agregar_canto:
        costo_canto = metros_lineales * precio_lineal
        total += costo_canto
        resumen += f"Canto pulido: {costo_canto:.2f} €\n"

    if agregar_incremento:
        inc = total * (porc / 100)
        total += inc
        resumen += f"Incremento ({porc:.1f}%): {inc:.2f} €\n"

    resumen += f"TOTAL: {total:.2f} €"
    agregar_incremento = st.checkbox("¿Aplicar incremento porcentual?")
    porc = 0.0
    if agregar_incremento:
        porc = st.number_input("¿Qué porcentaje deseas aplicar?", min_value=0.0, step=0.1)
        inc = total * (porc / 100)
        total += inc
        resumen += f"Incremento ({porc:.1f}%): {inc:.2f} €\n"
    st.markdown(f"### Total final: **{total:,.2f} €**")

    st.download_button("Descargar presupuesto", resumen, file_name="presupuesto.txt")
    mensaje = urllib.parse.quote(resumen.replace("\n", "\n"))
    whatsapp_url = f"https://wa.me/?text={mensaje}"
    st.markdown(f"[Compartir por WhatsApp]({whatsapp_url})")