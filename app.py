
import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Calculadora de Vidrio - Presupuesto")
st.markdown("Bienvenido a la herramienta de cálculo de vidrio. Llena los siguientes campos para obtener un presupuesto detallado.")
st.markdown("---")

# Medidas
st.header("1. Ingresar Medidas del Vidrio")
col1, col2 = st.columns(2)
with col1:
    ancho = st.number_input("Ancho (cm):", min_value=0.0, step=0.1)
with col2:
    alto = st.number_input("Alto (cm):", min_value=0.0, step=0.1)

st.markdown("---")

# Precio por m²: manual o tarifa
st.header("2. Precio del vidrio por m²")

opcion_precio = st.radio("¿Cómo deseas ingresar el precio por m²?", ["Seleccionar desde tarifa", "Ingresar manualmente"])

tarifas = {
    "Float": {
        "Clear 3mm": 180,
        "Clear 4mm": 210,
        "Clear 5mm": 240,
        "Clear 6mm": 260,
        "Clear 8mm": 310,
        "Clear 10mm": 360,
        "Extra Claro 6mm": 330,
        "Extra Claro 10mm": 430,
        "Reflectivo Azul 6mm": 290,
        "Reflectivo Gris 6mm": 295,
        "Reflectivo Bronze 6mm": 300
    },
    "Templado": {
        "Templado 4mm": 380,
        "Templado 6mm": 460,
        "Templado 8mm": 540,
        "Templado 10mm": 610,
        "Templado 12mm": 690,
        "Templado Extra Claro 6mm": 550,
        "Templado Reflectivo Azul 6mm": 570
    },
    "Laminado": {
        "Laminado 3+3": 450,
        "Laminado 4+4": 550,
        "Laminado 5+5": 660,
        "Laminado 6+6": 740,
        "Laminado Extra Claro 3+3": 620,
        "Laminado con Butiral Blanco 4+4": 590
    },
    "Espejos": {
        "Espejo Nacional 4mm": 220,
        "Espejo Nacional 6mm": 270,
        "Espejo Importado 4mm": 310,
        "Espejo Importado 6mm": 370
    },
    "Doble Acristalamiento": {
        "DVH 4+12+4": 750,
        "DVH 5+12+5": 820,
        "DVH 6+6 Templado": 950,
        "DVH 6+12+6 Laminado": 990
    }
}

if opcion_precio == "Ingresar manualmente":
    precio_m2 = st.number_input("Introduce el precio por m²:", min_value=0.0)

    with st.expander("Ver tabla de referencia (chuleta)"):
        for categoria, productos in tarifas.items():
            st.markdown(f"**{categoria}**")
            for nombre, precio in productos.items():
                st.markdown(f"- {nombre}: ${precio}")

else:
    st.subheader("Selecciona desde la tarifa 1610 SOSA")
    categoria = st.selectbox("Categoría de vidrio:", list(tarifas.keys()))
    tipo_vidrio = st.selectbox("Tipo de vidrio:", list(tarifas[categoria].keys()))
    precio_m2 = tarifas[categoria][tipo_vidrio]
    st.success(f"Precio seleccionado: ${precio_m2:.2f} por m²")

    with st.expander("Ver tarifa completa"):
        for categoria, productos in tarifas.items():
            st.markdown(f"**{categoria}**")
            for nombre, precio in productos.items():
                st.markdown(f"- {nombre}: ${precio}")

st.markdown("---")

# Canto Pulido
st.header("3. Configuración de Canto Pulido")

precio_canto_pulido = st.number_input("Precio por metro lineal de canto pulido:", min_value=0.0, value=35.0)

pulir_todos = st.checkbox("¿Pulir todos los lados (4)?")
if pulir_todos:
    num_lados_largos = 2
    num_lados_cortos = 2
else:
    col3, col4 = st.columns(2)
    with col3:
        num_lados_largos = st.number_input("¿Cuántos lados largos con canto pulido?", min_value=0, max_value=2, step=1)
    with col4:
        num_lados_cortos = st.number_input("¿Cuántos lados cortos con canto pulido?", min_value=0, max_value=2, step=1)

if alto == ancho and (num_lados_largos > 0 or num_lados_cortos > 0):
    st.info("Este vidrio es cuadrado, puedes considerar cualquier lado como largo o corto.")

largo_m = alto / 100
corto_m = ancho / 100
total_canto_ml = (num_lados_largos * largo_m) + (num_lados_cortos * corto_m)
costo_canto_pulido = total_canto_ml * precio_canto_pulido

st.markdown(f"**Resumen Canto Pulido:**")
st.markdown(f"- {num_lados_largos} lados largos de {largo_m:.2f} m")
st.markdown(f"- {num_lados_cortos} lados cortos de {corto_m:.2f} m")
st.markdown(f"- **Total:** {total_canto_ml:.2f} m")
st.markdown(f"- **Precio unitario:** ${precio_canto_pulido:.2f}")
st.markdown(f"- **Costo total:** ${costo_canto_pulido:.2f}")

st.markdown("---")

# Resumen final
st.header("4. Calcular Presupuesto Final")

if st.button("Calcular presupuesto total"):
    area_m2 = (ancho / 100) * (alto / 100)
    subtotal_vidrio = area_m2 * precio_m2
    total_final = subtotal_vidrio + costo_canto_pulido

    st.markdown("### Resumen Final")
    st.markdown(f"- **Medidas:** {ancho} x {alto} cm")
    st.markdown(f"- **Área real:** {area_m2:.2f} m²")
    st.markdown(f"- **Precio por m²:** ${precio_m2}")
    st.markdown(f"- **Subtotal vidrio:** ${subtotal_vidrio:.2f}")
    st.markdown(f"- **Canto pulido:** ${costo_canto_pulido:.2f}")
    st.markdown(f"### **Total: ${total_final:.2f}**")

    data = {
        "Concepto": ["Medidas", "Área", "Precio m²", "Subtotal vidrio", "Canto pulido", "Total"],
        "Valor": [f"{ancho} x {alto} cm", f"{area_m2:.2f} m²", f"${precio_m2}", f"${subtotal_vidrio:.2f}", f"${costo_canto_pulido:.2f}", f"${total_final:.2f}"]
    }
    df = pd.DataFrame(data)
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    st.download_button("Descargar resumen en Excel", data=buffer.getvalue(), file_name="presupuesto_vidrio.xlsx")
