import streamlit as st

# Configurações iniciais
st.title("Cálculo do Valor de Desconto por CAGADAS no Trabalho")
st.markdown(
    """
    Este programa calcula o valor que seria descontado no salário bruto com base nas pausas realizadas para cagar.
    Informe os parâmetros abaixo:
    """
)

# Entrada de dados
salario_bruto = st.slider("Salário bruto mensal (R$)", min_value=1000, max_value=20000, step=10, value=5000)
quantidade_pausas = st.number_input("Quantidade de pausas realizadas por mês", min_value=1, step=1, value=1)
tempo_pausa = st.number_input("Tempo de cada pausa (em minutos)", min_value=1, step=1, value=15)

# Cálculos
# Total de minutos no mês (considerando 22 dias úteis e 8 horas por dia)
minutos_uteis_no_mes = 22 * 8 * 60
valor_minuto = salario_bruto / minutos_uteis_no_mes

# Tempo total de pausas
tempo_total_pausas = quantidade_pausas * tempo_pausa

# Valor a ser descontado
valor_desconto = tempo_total_pausas * valor_minuto

# Resultado
st.subheader("Resultado")
st.write(f"Tempo total 'fazendo merda': {tempo_total_pausas} em minutos")
st.write(f"Valor do desconto pelas cagadas: R$ {valor_desconto:.2f}")
