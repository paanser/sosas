
# -------------------------------------------
# MEJORA DE INTERFAZ
# -------------------------------------------

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

# Tarifas
st.header("2. Selección de Vidrio por Categoría (Tarifa 1610 SOSA)")
tarifas = {
    "Float": {
        "Clear 6mm": 260,
        "Clear 4mm": 210,
        "Extra Claro 6mm": 330
    },
    "Templado": {
        "Templado 6mm": 460,
        "Templado 10mm": 610
    },
    "Laminado": {
        "Laminado 3+3": 450,
        "Laminado 4+4": 550
    }
}

categoria = st.selectbox("Categoría de vidrio:", list(tarifas.keys()))
tipo_vidrio = st.selectbox("Tipo de vidrio:", list(tarifas[categoria].keys()))
precio_m2 = tarifas[categoria][tipo_vidrio]
st.success(f"Precio seleccionado: ${precio_m2:.2f} por m²")

with st.expander("Ver tabla completa de precios"):
    for cat, items in tarifas.items():
        st.markdown(f"**{cat}**")
        for nombre, precio in items.items():
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
    st.markdown(f"- **Tipo:** {tipo_vidrio}")
    st.markdown(f"- **Precio por m²:** ${precio_m2}")
    st.markdown(f"- **Subtotal vidrio:** ${subtotal_vidrio:.2f}")
    st.markdown(f"- **Canto pulido:** ${costo_canto_pulido:.2f}")
    st.markdown(f"### **Total: ${total_final:.2f}**")

    import pandas as pd
    from io import BytesIO
    data = {
        "Concepto": ["Medidas", "Área", "Tipo", "Precio m²", "Subtotal vidrio", "Canto pulido", "Total"],
        "Valor": [f"{ancho} x {alto} cm", f"{area_m2:.2f} m²", tipo_vidrio, f"${precio_m2}", f"${subtotal_vidrio:.2f}", f"${costo_canto_pulido:.2f}", f"${total_final:.2f}"]
    }
    df = pd.DataFrame(data)
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    st.download_button("Descargar resumen en Excel", data=buffer.getvalue(), file_name="presupuesto_vidrio.xlsx")
