# Importando bibliotecas necessárias
import scipy.stats as spstats
import statsmodels.api as sm

# Teste qui-qurado para verificar a independência entre duas variáveis categóricas
def qui2(data, alpha):
    """
    Realiza o teste qui-quadrado para verificar a independência entre duas variáveis categóricas.
    
    Parâmetros:
    data (list of lists): Dados da tabela de contingência.
    alpha (float): Nível de significância do teste.
    """
    
    # Tabela de contingência e teste qui-quadrado
    statistic, pvalue, dof, _ = spstats.chi2_contingency(data, correction=False)

    # Mostrar resultados do teste qui-quadrado
    print(f"Qui-quadrado: {statistic}")
    print(f"Valor crítico: {spstats.chi2.ppf(1 - alpha, df=dof)}")
    print(f"P-valor: {pvalue}")

    # Verificar se rejeita a hipótese nula
    if pvalue <= alpha:
        print("Rejeitar a hipótese nula")
    else:
        print("Não rejeitar a hipótese nula")

# Teste de proporções para duas amostras independentes
def proporcoes_norm(count, nobs, alpha, alternative):
    
    """
    Realiza o teste de proporções para duas amostras independentes.
    
    Parâmetros:
    count (list): Contagem de sucessos em cada amostra.
    nobs (list): Número total de observações em cada amostra.
    alpha (float): Nível de significância do teste.
    alternative (str): Hipótese alternativa ('two-sided', 'larger', 'smaller').
    
    """
    
    # Performar teste de proporções
    z_score, p_value = sm.stats.proportions_ztest(count, nobs, alternative=alternative)

    # Mostrar resultados do teste de proporções
    print(f"z-score: {z_score}")
    print(f"p-value: {p_value}")

    # Verificar se rejeita a hipótese nula
    if p_value <= alpha:
        print("Rejeitar a hipótese nula")
    else:
        print("Não rejeitar a hipótese nula")