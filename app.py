
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

# Lista completa de precios extraída del PDF
precios = {
    "44.4 ANTII AGRESION PS9": 83.0,
    "44.4 ANTII AGRESION PS9 (SUST)": 64.4,
    "44.6 ANTI AGRESION P5A": 95.6,
    "44.6 ANTI AGRESION P5A (SUST)": 74.4,
    "66.4 ANTI  AGRESION P4A": 110.65,
    "66.4 ANTI  AGRESION P4A (SUST)": 86.5,
    "66.6 ANTI AGRESION P6B": 130.8,
    "66.6 ANTI AGRESION P6B (SUST)": 102.6,
    "ANTIBALA 10+10+2.5(BR1)": 164.5,
    "ANTIBALA 10+10+2.5(BR1) (SUST)": 130.0,
    "ANTIBALA 3+6+6+6+3 (BR2)": 181.1,
    "ANTIBALA 3+6+6+6+3 (BR2) (SUST)": 142.8,
    "ANTIRROBO 6+6+6": 110.65,
    "ANTIRROBO 6+6+6 (SUST)": 86.5,
    "BALDOSILLA ARMADA": 41.35,
    "BALDOSILLA ARMADA (SUST)": 31.4,
    "BARROTILLO LAC. BL ANCHO INGLET": 9.0,
    "BARROTILLO LAC. BL ESTRE INGLET": 9.0,
    "BARROTILLO LAC. BL ESTRECH CRUCET": 4.88,
    "BRILL GLASS ELEGANT ORO": 205.75,
    "BRILL GLASS ELEGANT ORO (SUST)": 164.6,
    "BRILL GLASS GAUDI": 205.75,
    "BRILL GLASS GAUDI (SUST)": 162.6,
    "BRILL GLASS HOJAS": 205.75,
    "BRILL GLASS HOJAS (SUST)": 162.6,
    "BRILL GLASS TON AZUL": 205.75,
    "BRILL GLASS TON AZUL (SUST)": 162.6,
    "BRILL GLASS TON ROJO": 205.75,
    "BRILL GLASS TON ROJO (SUST)": 162.6,
    "CARGLAS 6 INCOLORO": 46.8,
    "CARGLAS 6 INCOLORO (SUST)": 36.2,
    "CARGLAS ARMADO INCOLORO": 41.35,
    "CARGLAS ARMADO INCOLORO (SUST)": 31.4,
    "CARGLAS BRONCE": 42.3,
    "CARGLAS BRONCE (SUST)": 20.2,
    "CARGLAS INCOLORO": 21.4,
    "CARGLAS INCOLORO (SUST)": 12.6,
    "CARGLAS NEW": 24.2,
    "CARGLAS NEW (SUST)": 18.4,
    "CATEDRAL ARMADO INCOLORO": 41.35,
    "CATEDRAL ARMADO INCOLORO (SUST)": 31.4,
    "CLIMAGUARD 4 MM": 6.0,
    "CLIMAGUARD 6 MM": 10.0,
    "CLIMAGUARD PREMIUM 33.1": 25.9,
    "CLIMAGUARD PREMIUM 44.1": 29.3,
    "FLOAT 10 MM": 36.2,
    "FLOAT 10 MM (SUST)": 28.2,
    "FLOAT 2 MM": 11.6,
    "FLOAT 3 MM": 12.6,
    "FLOAT 4 MM": 13.1,
    "FLOAT 5 MM": 18.1,
    "FLOAT 5 MM (SUST)": 6.0,
    "FLOAT 6 MM": 21.65,
    "FLOAT 6 MM (SUST)": 7.5,
    "FLOAT 8 MM": 32.2,
    "FLOAT 8 MM (SUST)": 16.1,
    "GUARDIAN SELECT BASE": 20.5,
    "GUARDIAN SELECT SUSTITUCION": 20.5,
    "GUARDIAN SELECT TRIPLE": 46.4,
    "GUARDIAN SUN 4 MM": 11.2,
    "GUARDIAN SUN 44.1": 35.6,
    "GUARDIAN SUN 6 MM": 18.9,
    "GUARDIAN SUN 66.1": 58.3,
    "LAMINADO  4+4 GRIS + MATE": 76.95,
    "LAMINADO  4+4 GRIS + MATE (SUST)": 59.6,
    "LAMINADO 10+DREAMS 10 SATINADO,2": 313.6,
    "LAMINADO 10+DREAMS 10 SATINADO,2 (SUST)": 238.4,
    "LAMINADO 10+DREAMS10 TRANSP.,2": 313.6,
    "LAMINADO 10+DREAMS10 TRANSP.,2 (SUST)": 238.4,
    "LAMINADO 3+3": 26.73,
    "LAMINADO 3+3 (SUST)": 17.0,
    "LAMINADO 3+3 AZUL": 45.3,
    "LAMINADO 3+3 AZUL (SUST)": 34.2,
    "LAMINADO 3+3 BRONCE": 45.3,
    "LAMINADO 3+3 BRONCE (SUST)": 34.2,
    "LAMINADO 3+3 GRIS": 45.3,
    "LAMINADO 3+3 GRIS (SUST)": 34.2,
    "LAMINADO 3+3 MATE": 39.42,
    "LAMINADO 3+3 MATE (SUST)": 33.0,
    "LAMINADO 3+3 MATE+AZUL": 76.95,
    "LAMINADO 3+3 MATE+AZUL (SUST)": 59.6,
    "LAMINADO 4+4": 31.72,
    "LAMINADO 4+4  BRONCE + MATE": 76.95,
    "LAMINADO 4+4  BRONCE + MATE (SUST)": 59.6,
    "LAMINADO 4+4 (SUST)": 23.0,
    "LAMINADO 4+4 AZUL": 53.35,
    "LAMINADO 4+4 AZUL (SUST)": 40.6,
    "LAMINADO 4+4 AZUL + MATE": 76.95,
    "LAMINADO 4+4 AZUL + MATE (SUST)": 59.6,
    "LAMINADO 4+4 BRONCE": 53.35,
    "LAMINADO 4+4 BRONCE (SUST)": 40.6,
    "LAMINADO 4+4 GRIS": 53.35,
    "LAMINADO 4+4 GRIS (SUST)": 40.6,
    "LAMINADO 4+4 MATE": 43.87,
    "LAMINADO 4+4 MATE (SUST)": 37.0,
    "LAMINADO 4+4 MINT GREEN+POLAR WHITE": 150.9,
    "LAMINADO 4+4 POLAR WHITE": 90.5,
    "LAMINADO 4+4 POLAR WHITE (SUST)": 72.4,
    "LAMINADO 4+4 STOPSOL CLASSIC": 62.9,
    "LAMINADO 4+4 STOPSOL CLASSIC (SUST)": 50.3,
    "LAMINADO 5+5": 36.18,
    "LAMINADO 5+5 (SUST)": 26.0,
    "LAMINADO 5+5 GRIS": 56.8,
    "LAMINADO 5+5 GRIS (SUST)": 43.5,
    "LAMINADO 5+5 MATE": 55.57,
    "LAMINADO 5+5 MATE (SUST)": 46.2,
    "LAMINADO 5+5 SG ROYAL BLUE 20": 105.6,
    "LAMINADO 5+5 SG ROYAL BLUE 20 (SUST)": 84.5,
    "LAMINADO 5+5 STOPSOL SUPERSILVER GRIS": 115.5,
    "LAMINADO 5+5 STOPSOL SUPERSILVER GRIS (SUST)": 92.4,
    "LAMINADO 6+6": 46.8,
    "LAMINADO 6+6 (SUST)": 37.4,
    "LAMINADO 6+6 MATE": 66.9,
    "LAMINADO 6+6 MATE (SUST)": 51.5,
    "LAMINADO 6+6.2 MINT GREEN": 163.5,
    "LAMINADO 6+6.2 MINT GREEN (SUST)": 130.8,
    "LAMINADO 8+8": 43.06,
    "LAMINADO 8+8 (SUST)": 58.4,
    "LAMINADOS 3+3 MATE+GRIS": 71.95,
    "LAMINADOS 3+3 MATE+GRIS (SUST)": 57.6,
    "LAMINAR ACUSTICO 3+3": 48.3,
    "LAMINAR ACUSTICO 3+3 (SUST)": 27.0,
    "LAMINAR ACUSTICO 4+4": 35.0,
    "LAMINAR ACUSTICO 4+4 (SUST)": 40.1,
    "LAMINAR ACUSTICO 5+5": 63.4,
    "LAMINAR ACUSTICO 5+5 (SUST)": 44.4,
    "LAMINAR ACUSTICO 6+6": 71.4,
    "LAMINAR ACUSTICO 6+6 (SUST)": 50.7,
    "MADRAS ESCARCHA": 118.7,
    "MADRAS ESCARCHA (SUST)": 93.0,
    "MADRAS ESPIGAS": 118.7,
    "MADRAS ESPIGAS (SUST)": 93.0,
    "MADRAS MIL RAYAS": 128.7,
    "MADRAS MIL RAYAS (SUST)": 101.0,
    "MADRAS NEBULOSA": 118.7,
    "MADRAS NEBULOSA (SUST)": 93.0,
    "MADRAS NEBULOSA ROSA": 178.1,
    "MADRAS NEBULOSA ROSA (SUST)": 142.5,
    "MADRAS PICS": 118.7,
    "MADRAS PICS (SUST)": 93.0,
    "MADRAS PINO": 118.7,
    "MADRAS PINO (SUST)": 93.0,
    "MATE ACIDO 3 MM": 29.1,
    "MATE ACIDO 4 MM": 32.7,
    "MATE ACIDO 4 MM (SUST)": 24.2,
    "MATE ACIDO 5 MM": 36.7,
    "MATE ACIDO 5 MM (SUST)": 27.4,
    "MATE ACIDO 6 MM": 40.7,
    "MATE ACIDO 6 MM (SUST)": 30.6,
    "NEOCERAM 4 MM": 266.6,
    "NOVOMAT 5 MM": 41.75,
    "NOVOMAT 5 MM (SUST)": 31.4,
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
    "RAYWALL 45 CLEAR 4MM": 34.5,
    "RAYWALL 45 CLEAR 4MM (SUST)": 27.6,
    "STOPSOL CLASSIC INC. 5 MM": 53.8,
    "STOPSOL CLASSIC INC. 5 MM (SUST)": 40.6,
    "STOPSOL SUPERSILVER GRIS 6 MM": 74.45,
    "STOPSOL SUPERSILVER GRIS 6 MM (SUST)": 57.6,
    "SUNGUARD ROYAL BLUE 6MM": 71.4,
    "SUNGUARD ROYAL BLUE 6MM (SUST)": 55.2,
    "TEMPLADO 10 MM": 60.4,
    "TEMPLADO 10 MM (SUST)": 48.3,
    "TEMPLADO 12 MM": 110.65,
    "TEMPLADO 12 MM (SUST)": 88.5,
    "TEMPLADO 4 MM": 30.2,
    "TEMPLADO 4 MM (SUST)": 24.2,
    "TEMPLADO 5 MM": 35.25,
    "TEMPLADO 5 MM (SUST)": 28.2,
    "TEMPLADO 6 MM": 40.2,
    "TEMPLADO 6 MM (SUST)": 32.2,
    "TEMPLADO 8 MM": 50.3,
    "TEMPLADO 8 MM (SUST)": 40.2,
    "TEMPLADO MATE 10 MM.": 125.75,
    "TEMPLADO MATE 10 MM. (SUST)": 100.6,
    "TEMPLADO MATE 4 MM.": 60.4,
    "TEMPLADO MATE 4 MM. (SUST)": 48.3,
    "TEMPLADO MATE 5 MM.": 65.4,
    "TEMPLADO MATE 5 MM. (SUST)": 52.3,
    "TEMPLADO MATE 6 MM.": 75.5,
    "TEMPLADO MATE 6 MM. (SUST)": 60.4,
    "TEMPLADO MATE 8 MM.": 108.15,
    "TEMPLADO MATE 8 MM. (SUST)": 86.5,
    "UGLAS ARMADO": 79.5,
}

# Interfaz principal
st.markdown("<h4 style='text-align:center;'>Calculador de precios de vidrio de SOSA, basado en Reuglass</h4>", unsafe_allow_html=True)
st.markdown("### Calculadora de presupuestos de vidrio", unsafe_allow_html=True)
st.markdown("**Calculadora de precios de vidrio de Sosa, basada en tarifa Reuglass 1610**")
st.markdown("---")

st.markdown("---")
st.markdown("<h1 style='text-align:center; color:#004d66;'>Vidres SOSA</h1>", unsafe_allow_html=True)

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

    # Menú desplegable de precios
    producto_seleccionado = st.selectbox("Selecciona el tipo de vidrio (Tarifa 1610 SOSA)", list(precios.keys()))
    precio_m2 = precios[producto_seleccionado]
    st.write(f"Precio por m²: **{precio_m2:.2f} €**")

    precio_vidrio = area_ajustada * precio_m2
    st.write(f"Precio total del vidrio: **{precio_vidrio:.2f} €**")

    cantos = st.number_input("¿Cuántos cantos anchos?", min_value=0, step=1)
    lados = st.number_input("¿Cuántos cantos largos?", min_value=0, step=1)
    metros_lineales = (cantos * ancho_aj) + (lados * alto_aj)
    st.write(f"Metros lineales: **{metros_lineales:.2f} m**")

    total = precio_vidrio

    if st.checkbox("¿Agregar costo de canto pulido?"):
        precio_lineal = st.number_input("Precio por metro lineal", min_value=0.0, step=0.1)
        total_canto = metros_lineales * precio_lineal
        total += total_canto
        st.write(f"Costo de canto pulido: **{total_canto:.2f} €**")

    if st.checkbox("¿Aplicar incremento porcentual?"):
        porcentaje = st.number_input("¿Qué porcentaje deseas aplicar?", min_value=0.0, step=0.1)
        total *= (1 + porcentaje / 100)
        st.write(f"Total con incremento del {porcentaje:.1f}%: **{total:.2f} €**")
    else:
        st.write(f"Total final: **{total:.2f} €**")
