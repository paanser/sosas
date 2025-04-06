from tarifa_sosa_1610 import tarifas


import streamlit as st

# --------------------------
# CONFIGURACIÓN GENERAL
# --------------------------
st.set_page_config(page_title="Calculador Vidrio Reuglass", layout="centered")

# Tabla de múltiplos de 6 (en cm)
multiplos = [i for i in range(24, 250, 6)]

# Tarifa completa extraída del PDF
tarifa = {'GUARDIAN SELECT SUSTITUCION': 20.5, 'GUARDIAN SELECT BASE': 20.5, 'GUARDIAN SELECT TRIPLE': 46.4, 'FLOAT 2 MM': 11.6, 'FLOAT 3 MM': 12.6, 'FLOAT 4 MM': 13.1, 'FLOAT 5 MM': 18.1, 'FLOAT 6 MM': 21.65, 'FLOAT 8 MM': 32.2, 'FLOAT 10 MM': 36.2, 'PARSOL BRONCE 4 MM': 24.2, 'PARSOL BRONCE 5 MM': 27.8, 'PARSOL GRIS 4 MM': 24.2, 'PARSOL GRIS 5 MM': 27.8, 'PARSOL GRIS 6 MM': 42.8, 'PLATA 3 MM': 26.0, 'PLATA 5 MM': 34.2, 'PLATA 6 MM': 41.35, 'PLATA GRIS 5 MM': 48.1, 'PLATA ROSA 5 MM': 80.5, 'CARGLAS INCOLORO': 21.4, 'CARGLAS NEW': 24.2, 'CARGLAS 6 INCOLORO': 46.8, 'CARGLAS BRONCE': 42.3, 'CATEDRAL ARMADO INCOLORO': 41.35, 'BALDOSILLA ARMADA': 41.35, 'CARGLAS ARMADO INCOL ORO': 41.35, 'NEOCERAM 4 MM': 266.6, 'UGLAS 6000x262': 75.5, 'UGLAS ARMADO': 79.5, 'RAYWALL 45 CLEAR 4MM': 34.5, 'MATE ACIDO 3 MM': 29.1, 'MATE ACIDO 4 MM': 32.7, 'MATE ACIDO 5 MM': 36.7, 'MATE ACIDO 6 MM': 40.7, 'NOVOMAT 5 MM': 41.75, 'MADRAS ESCARCHA': 118.7, 'MADRAS ESPIGAS': 118.7, 'MADRAS NEBULOSA': 118.7, 'MADRAS PICS': 118.7, 'MADRAS PINO': 118.7, 'MADRAS MIL RAYAS': 128.7, 'MADRAS NEBULOSA ROSA': 178.1, 'BRILL GLASS ELEGANT ORO': 205.75, 'BRILL GLASS TON AZUL': 205.75, 'BRILL GLASS TON ROJO': 205.75, 'BRILL GLASS HOJAS': 205.75, 'BRILL GLASS GAUDI': 205.75, 'CLIMAGUARD 4 MM': 6.0, 'CLIMAGUARD 6 MM': 10.0, 'GUARDIAN SUN 4 MM': 11.2, 'GUARDIAN SUN 6 MM': 18.9, 'STOPSOL CLASSIC INC. 5 MM': 53.8, 'STOPSOL SUPERSILVER GRIS 6 MM': 74.45, 'SUNGUARD ROYAL BLUE 6MM': 71.4, 'LAMINADO 3+3': 26.73, 'LAMINADO 4+4': 31.72, 'LAMINADO 5+5': 36.18, 'LAMINADO 6+6': 46.8, 'LAMINADO 8+8': 43.06, 'LAMINADO 3+3 MATE': 39.42, 'LAMINADO 4+4 MATE': 43.87, 'LAMINADO 5+5 MATE': 55.57, 'LAMINADO 6+6 MATE': 66.9, 'LAMINADOS 3+3 MATE+GRIS': 71.95, 'LAMINADO 3+3 AZ UL': 45.3, 'LAMINADO 4+4 AZ UL': 53.35, 'LAMINADO 4+4 AZ UL + MATE': 76.95, 'LAMINADO 3+3 BRONCE': 45.3, 'LAMINADO 4+4 BRONCE': 53.35, 'LAMINADO 4+4  BRONCE + MATE': 76.95, 'LAMINADO 3+3 GRIS': 45.3, 'LAMINADO 4+4 GRIS': 53.35, 'LAMINADO 5+5 GRIS': 56.8, 'LAMINADO 3+3 MATE+AZUL': 76.95, 'LAMINADO  4+4 GRIS + MATE': 76.95, 'LAMINADO 4+4 POLAR WHITE': 90.5, 'LAMINADO 4+4 MINT GREEN+POLAR WHITE': 150.9, 'LAMINADO 6+6.2 MINT GREEN': 163.5, 'ANTIRROBO 6+6+6': 110.65, '44.4 ANTII AGRESION PS9': 83.0, '66.4 ANTI  AGRESION P4A': 110.65, '44.6 ANTI AGRESION P5A': 95.6, '66.6 ANTI AGRESION P6B': 130.8, 'ANTIBALA 1 0+ 10 +2 .5(BR1 )': 164.5, 'ANTIBALA 3 +6 +6 +6 +3  (BR2)': 181.1, 'CLIMAGUARD PREMIUM 44.1': 29.3, 'GUARDIAN SUN 44.1': 35.6, 'GUARDIAN SUN 66.1': 58.3, 'LAMINADO 4+4 STOPSOL CLASSIC': 62.9, 'LAMINADOS 4+4 LIGHT BLUE 62/52': 62.9, 'LAMINADO 10+10 LIGHT BLUE 62/52': 171.0, 'CLIMAGUARD PREMIUM 33.1': 25.9, 'LAMINADO 5+5 LIGHT BLUE 62/52': 74.25, 'LAMINADO 5+5 STOPSOL SUPERSILVER GRIS': 115.5, 'LAMINADO 5+5 SG ROYAL BLUE 20': 105.6, 'LAMINADO 10+DREAMS 10 SATINADO,2': 313.6, 'LAMINADO 10+DREAMS10 TRANSP.,2': 313.6, 'LAMINAR ACUST ICO 3+3': 48.3, 'LAMINAR ACUST ICO 4+4': 35.0, 'LAMINAR ACUST ICO 5+5': 63.4, 'LAMINAR ACUST ICO 6+6': 71.4, 'TEMPLADO 4 MM': 30.2, 'TEMPLADO 5 MM': 35.25, 'TEMPLADO 6 MM': 40.2, 'TEMPLADO 8 MM': 50.3, 'TEMPLADO 10 MM': 60.4, 'TEMPLADO 12 MM': 110.65, 'TEMPLADO MATE 4 MM.': 60.4, 'TEMPLADO MATE 5 MM.': 65.4, 'TEMPLADO MATE 6 MM.': 75.5, 'TEMPLADO MATE 8 MM.': 108.15, 'TEMPLADO MATE 10 MM.': 125.75, 'GAS TERMICO': 6.25, 'GAS ACUST ICO': 6.25, 'CANTO PULIDO MONOLITICO': 0.88, 'CANTO PULIDO LAMINAR': 1.0, 'CANTO PULIDO DIAGONAL MONOLITICO': 1.0, 'CANTO PULIDO DIAGONAL LAMINADO': 1.13, 'TALADRO  de 3 a 10mm de Ø': 2.0, 'TALADRO LAMINAR  de 3 a 10 mm de Ø': 2.13, 'PUNTA ROMA C.PULIDO radio hasta 15 mm': 2.5, 'PUNTA ROMA C.PULIDO radio de 16 a 60 mm.': 4.5, 'PUNTA MATADA': 1.5, 'PUNTA MATADA LAMINAR': 2.0, 'PUNTA ROMA C.PULIDO LAMINAR radio hasta 15mm.': 3.25, 'PUNTA ROMA C.PULIDO LAM. radio de 16 a 60 mm.': 5.75, 'TAQUILLA AL CORTE MONOLITICO': 5.0, 'TAQUILLA AL CORTE LAMINADO': 5.0, 'ESCUADRA AL CORTE MONOLITICO': 3.75, 'PULIR ESCUADRA MONOLIT ICO': 4.5, 'ESCUADRA AL CORTE LAMINAR': 5.25, 'PULIR ESCUADRA LAMINAR': 6.25, 'MUESCAS PARA HERRAJES': 5.0, 'CRISLIMP': 17.25, 'CRISLIMP CAMARA': 17.25, 'PEGADO UVA': 35.5, 'CANTO ARISTADO MONOLITICO': 0.38, 'CANTO ARISTADO LAMINAR': 0.38, 'CANTO ARISTADO DIAGONAL MONOLITICO': 0.63, 'CANTO ARISTADO DIAGONAL LAMINAR': 0.63, 'CANTO ARISTADO LAMINAR FORMA': 0.63, 'MATEADO A LA ARENA': 120.0, 'VITRIFICADO': 56.25, 'BARROTILLO LAC. BL ANCHO CRUC 25mm': 6.25, 'BARROTILLO LAC. BL ANCHO INGLET': 9.0, 'BARROTILLO LAC. BL ESTRECH CRUCET': 4.88, 'BARROTILLO LAC. BL ESTRE INGLET': 9.0}

def ajustar_a_multiplo(valor_m):
    """Redondea hacia arriba al múltiplo de 6 cm más cercano"""
    valor_cm = valor_m * 100
    for m in multiplos:
        if valor_cm <= m:
            return m / 100
    return multiplos[-1] / 100  # Valor máximo

# --------------------------
# ENTRADA DE MEDIDAS
# --------------------------
st.title("Calculador de Vidrio - Reuglass")
st.header("Paso 1: Medidas del vidrio")

ancho = st.number_input("Ancho del vidrio (en metros)", min_value=0.01, step=0.01)
alto = st.number_input("Alto del vidrio (en metros)", min_value=0.01, step=0.01)

if ancho and alto:
    m2_real = round(ancho * alto, 3)
    ancho_ajustado = ajustar_a_multiplo(ancho)
    alto_ajustado = ajustar_a_multiplo(alto)
    m2_ajustado = round(ancho_ajustado * alto_ajustado, 3)

    st.success(f"Área real: {m2_real} m²")
    st.info(f"Medidas ajustadas: {ancho_ajustado} m x {alto_ajustado} m")
    st.success(f"Área ajustada: {m2_ajustado} m²")

    # --------------------------
    # SELECCIÓN DE PRECIO
    # --------------------------
    st.header("Paso 2: Precio por metro cuadrado")

    metodo_precio = st.radio("Selecciona cómo quieres introducir el precio:", ["Manual", "Por tarifa"])

    if metodo_precio == "Manual":
        st.markdown("### Guía rápida (tarifa 1610 SOSA)")
        for k, v in tarifa.items():
            st.markdown(f"- **{k}**: {v} €/m²")
        precio_m2 = st.number_input("Introduce el precio manualmente (€/m²)", min_value=0.0, step=0.10)
    else:
        seleccion = st.selectbox("Selecciona el tipo de vidrio", list(tarifa.keys()))
        precio_m2 = tarifa[seleccion]
        st.success(f"Precio según tarifa: {precio_m2} €/m²")

    if precio_m2 > 0:
        precio_cristal = round(precio_m2 * m2_ajustado, 2)
        st.success(f"**Precio del vidrio:** {precio_cristal} €")

        # --------------------------
        # CANTO PULIDO DETALLADO
        # --------------------------
        st.header("Paso 3: ¿Deseas añadir canto pulido?")
        activar_canto = st.checkbox("Sí, quiero calcular el canto pulido")

        precio_canto = 0

        if activar_canto:
            lados = st.slider("¿Cuántos lados deseas pulir?", 1, 4, 2)
            precio_lineal = st.number_input("Introduce el precio por metro lineal de pulido (€)", min_value=0.0)

            perimetro_total = 0
            if lados == 1:
                perimetro_total = ancho_ajustado
            elif lados == 2:
                perimetro_total = ancho_ajustado + alto_ajustado
            elif lados == 3:
                perimetro_total = ancho_ajustado * 2 + alto_ajustado
            else:
                perimetro_total = (ancho_ajustado + alto_ajustado) * 2

            precio_canto = round(perimetro_total * precio_lineal, 2)
            st.success(f"Canto pulido: {perimetro_total:.2f} m x {precio_lineal} €/ml = {precio_canto} €")

        # --------------------------
        # MARGEN / INCREMENTO
        # --------------------------
        st.header("Paso 4: Margen (opcional)")
        margen = st.number_input("Porcentaje de incremento (%)", min_value=0.0, max_value=100.0, value=0.0)

        subtotal = precio_cristal + precio_canto
        total_final = round(subtotal * (1 + margen / 100), 2)

        # --------------------------
        # RESULTADO FINAL
        # --------------------------
        st.header("Resultado final")
        st.write(f"Precio del cristal: **{precio_cristal} €**")
        st.write(f"Precio del canto pulido: **{precio_canto} €**")
        st.write(f"Subtotal sin margen: **{subtotal} €**")
        if margen > 0:
            st.write(f"Margen aplicado: {margen}%")
        st.success(f"**Total final: {total_final} €**")
