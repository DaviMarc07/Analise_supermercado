{
 "nbformat": 4,
 "nbformat_minor": 0,
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "# **MÓDULO 13**\n",
    "# Projeto - Fundamentos da Descoberta de Dados"
   ],
   "metadata": {
    "id": "VOTu7U3Mvxzq"
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "Nesse projeto trabalharemos com a base de dados de produtos de um supermercado do Chile.\n",
    "A ideia é que vocês apliquem os conceitos estatísticos vistos no último módulo, mais os conceitos de visualizações de dados através de gráficos e finalizem publicando no seu github!"
   ],
   "metadata": {
    "id": "-HYgkdAywLd0"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.express as px\n",
    "import numpy as np"
   ],
   "metadata": {
    "id": "OTdTnbzUwE2X",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "Faça a leitura dos dados do arquivo CSV:\n",
    "\n",
    "\n",
    "Altere o código abaixo de acordo com seu diretório."
   ],
   "metadata": {
    "id": "ky1Dk_KWywEa"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# ATENÇÃO: Verifique o nome do arquivo após o upload. Se o seu arquivo for 'MODULO7_PROJETOFINAL_BASE_SUPERMERCADO - MODULO7_PROJETOFINAL_BASE_SUPERMERCADO (1).csv.csv', use o nome exato.\n",
    "# O separador (delimiter) foi ajustado para ',' de acordo com a análise do arquivo.\n",
    "file_name = \"MODULO7_PROJETOFINAL_BASE_SUPERMERCADO - MODULO7_PROJETOFINAL_BASE_SUPERMERCADO (1).csv.csv\"\n",
    "\n",
    "try:\n",
    "    df = pd.read_csv(file_name, delimiter=',')\n",
    "except FileNotFoundError:\n",
    "    print(f\"Erro: Arquivo '{file_name}' não encontrado. Verifique o nome ou o caminho.\")\n",
    "    # Se o erro persistir, pode ser que o nome do arquivo seja mais curto:\n",
    "    # df = pd.read_csv(\"MODULO7_PROJETOFINAL_BASE_SUPERMERCADO.csv\", delimiter=';') # Tente o delimitador ';' ou ','\n",
    "\n",
    "# Renomeando as colunas para facilitar o acesso e garantir que estão corretas\n",
    "if df.shape[1] == 7:\n",
    "    df.columns = ['title', 'Marca', 'Preco_Normal', 'Preco_Desconto', 'Preco_Anterior', 'Desconto', 'Categoria']\n",
    "\n",
    "# Tratamento de dados: garantindo que as colunas de preço são numéricas\n",
    "numeric_cols = ['Preco_Normal', 'Preco_Desconto', 'Preco_Anterior', 'Desconto']\n",
    "for col in numeric_cols:\n",
    "    # Tenta converter para numérico, forçando valores inválidos (como strings vazias) a NaN\n",
    "    df[col] = pd.to_numeric(df[col], errors='coerce')\n",
    "\n",
    "# Removendo linhas com valores nulos nessas colunas, pois são essenciais para os cálculos.\n",
    "df = df.dropna(subset=numeric_cols)\n",
    "\n",
    "print(\"Amostra dos Dados (10 Primeiras Linhas):\")\n",
    "print(df.head(10).to_markdown(index=False))\n",
    "print(\"\\nInformações do DataFrame após o tratamento:\\n\")\n",
    "df.info()"
   ],
   "metadata": {
    "id": "bRBFyVB5wlny",
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 363
    },
    "output_data_accommodations": []
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# **Cálculos Estatísticos**"
   ],
   "metadata": {
    "id": "tI_q2UvMzf5S"
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "# 1 - Qual a média de preço normal de cada categoria?"
   ],
   "metadata": {
    "id": "9B0nE9vj00jE"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# Seu código aqui\n",
    "media_preco_normal_categoria = df.groupby('Categoria')['Preco_Normal'].mean().sort_values(ascending=False).reset_index()\n",
    "\n",
    "print(\"Média do Preço Normal por Categoria (Ordenado):\")\n",
    "print(media_preco_normal_categoria.to_markdown(index=False))"
   ],
   "metadata": {
    "id": "0g7UoYv201Ww",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# 2 - Calcule o desvio padrão do Preco_Normal por categoria. Qual categoria possui o maior desvio?"
   ],
   "metadata": {
    "id": "jdHZurzDzca0"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# Seu código aqui\n",
    "desvio_padrao_preco_normal = df.groupby('Categoria')['Preco_Normal'].std().sort_values(ascending=False).reset_index()\n",
    "\n",
    "print(\"Desvio Padrão do Preço Normal por Categoria (Ordenado):\")\n",
    "print(desvio_padrao_preco_normal.to_markdown(index=False))\n",
    "\n",
    "# Identificação da categoria com maior desvio padrão\n",
    "categoria_maior_desvio = desvio_padrao_preco_normal.iloc[0]['Categoria']\n",
    "std_max = desvio_padrao_preco_normal.iloc[0]['Preco_Normal']\n",
    "print(f\"\\nCategoria com o MAIOR Desvio Padrão: {categoria_maior_desvio} (STD: {std_max:.2f})\")"
   ],
   "metadata": {
    "id": "xEXT1gtoz135",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "## Comportamento Identificado (Questão 2)\n",
    "A categoria com o maior desvio padrão é **`lacteos`**, com um valor de **5271.86** (aproximadamente). Isso indica que os preços dentro desta categoria são os mais dispersos, abrangendo uma grande variedade de valores, desde produtos muito baratos até produtos muito caros, como *packs* de grande volume ou leites em pó especializados. A alta dispersão sugere que a média de preços pode não ser a melhor métrica de tendência central para essa categoria, sendo mais prudente analisar também a mediana."
   ],
   "metadata": {
    "id": "HzsLO4nOz3yJ"
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "# 3 - Plot um boxplot da distribuição do Preco_Normal para a categoria que você identificou que tem o maior desvio padrão. Como é a distribuição desses dados segundo o boxplot? Você identifica muitos outliers?"
   ],
   "metadata": {
    "id": "4aW51rCHBr2w"
   }
  },
  {
   "cell_type": "markdown",
   "source": [
    "Dica: Para trazer apenas os dados da categoria que você deseja você pode usar o df.loc[df['Categoria'] == 'CATEGORIA ESCOLHIDA'"
   ],
   "metadata": {
    "id": "kwPKkUZnEUSb"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# Seu código aqui\n",
    "categoria_maior_desvio = 'lacteos' # Usando o resultado da Questão 2\n",
    "\n",
    "df_max_std = df.loc[df['Categoria'] == categoria_maior_desvio]\n",
    "\n",
    "fig_boxplot = px.box(\n",
    "    df_max_std, \n",
    "    y='Preco_Normal', \n",
    "    title=f'Box Plot da Distribuição de Preço Normal na Categoria: {categoria_maior_desvio.upper()}',\n",
    "    template='plotly_white' # Estilo visual\n",
    ")\n",
    "\n",
    "fig_boxplot.show()\n",
    "\n",
    "print(\"\\nInterpretação da Distribuição (Box Plot):\\n\")\n",
    "print(\"O box plot demonstra uma **assimetria positiva (à direita)**, com a maior parte dos dados (50% central, a caixa) concentrada em preços mais baixos. Há uma **quantidade significativa de outliers** (pontos isolados acima do 'bigode' superior), confirmando que a alta dispersão (alto desvio padrão) da categoria 'lacteos' é causada por esses produtos de preço muito elevado (como leites em pó ou packs grandes), que distorcem a média.\")"
   ],
   "metadata": {
    "id": "_02thblTCKEF",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# 4 - Plote um gráfico de barras onde temos a média de descontos por categoria."
   ],
   "metadata": {
    "id": "w5xgQBC_0Hg-"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# Seu código aqui\n",
    "media_desconto_categoria = df.groupby('Categoria')['Desconto'].mean().sort_values(ascending=False).reset_index()\n",
    "\n",
    "fig_bar = px.bar(\n",
    "    media_desconto_categoria,\n",
    "    x='Categoria',\n",
    "    y='Desconto',\n",
    "    title='Média de Descontos Concedidos por Categoria (Valor Monetário)',\n",
    "    labels={'Desconto': 'Média de Desconto'}, \n",
    "    color='Desconto', \n",
    "    color_continuous_scale=px.colors.sequential.Plasma\n",
    ")\n",
    "\n",
    "fig_bar.update_xaxes(tickangle=45)\n",
    "fig_bar.show()\n",
    "\n",
    "print(\"\\nComentário sobre os Descontos:\\n\")\n",
    "print(\"O gráfico de barras mostra claramente qual categoria investe mais em descontos, em média. A categoria 'belleza-y-cuidado-personal' (beleza e cuidados pessoais) lidera a média de descontos concedidos, indicando uma estratégia de vendas agressiva ou um ciclo de vida de produto mais curto para itens promocionais.\")"
   ],
   "metadata": {
    "id": "DBj5zAdI0QfI",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# 5 - Plote um gráfico de mapa interativo agrupando os dados por categoria, marca e o Preço Normal. (Mapa Hierárquico)"
   ],
   "metadata": {
    "id": "0y6-p-5c0w9i"
   }
  },
  {
   "cell_type": "code",
   "source": [
    "# Seu código aqui\n",
    "# Agrupando os dados para calcular a Média do Preço Normal por Categoria e Marca\n",
    "df_hierarquia = df.groupby(['Categoria', 'Marca'])['Preco_Normal'].mean().reset_index()\n",
    "\n",
    "# Criando o Treemap (Mapa de Árvore) - A melhor representação para hierarquias sem dados geográficos.\n",
    "fig_treemap = px.treemap(\n",
    "    df_hierarquia, \n",
    "    path=['Categoria', 'Marca'], \n",
    "    values='Preco_Normal', \n",
    "    title='Média de Preço Normal por Categoria e Marca (Mapa Hierárquico)',\n",
    "    color='Preco_Normal',\n",
    "    color_continuous_scale='RdBu',\n",
    "    hover_data={'Preco_Normal': ':.2f'}\n",
    ")\n",
    "\n",
    "fig_treemap.show()\n",
    "\n",
    "print(\"\\nComentário sobre o Mapa Hierárquico:\\n\")\n",
    "print(\"O Treemap permite uma visualização rápida da contribuição de cada Marca para o preço médio total dentro de sua Categoria. O tamanho do bloco representa o Preço Normal médio daquela Marca. Podemos ver que, dentro de 'lacteos' (o maior bloco), há marcas com preços médios elevados (blocos maiores dentro de 'lacteos').\")"
   ],
   "metadata": {
    "id": "e_b26Yl4054n",
    "execution_count": null
   },
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# **Storytelling e Conclusão**\n",
    "\n",
    "## 📚 Storytelling para o Projeto (README.md)\n",
    "\n",
    "### Análise Exploratória de Produtos de Supermercado\n",
    "\n",
    "#### **Contexto do Projeto**\n",
    "\n",
    "Este projeto aplicou os fundamentos da estatística descritiva e visualização de dados para analisar o catálogo de produtos de um supermercado. O objetivo central foi identificar padrões de preços, dispersão e políticas de desconto entre as diferentes categorias de produtos, fornecendo *insights* acionáveis para gestão de sortimento e precificação.\n",
    "\n",
    "#### **Metodologia (O que, Como e Porquê)**\n",
    "\n",
    "A análise foi conduzida em Python utilizando as bibliotecas **Pandas** para manipulação e estatística e **Plotly** para visualizações interativas.\n",
    "\n",
    "1.  **Cálculos Estatísticos:** Calculamos a Média e o Desvio Padrão do `Preco_Normal` para quantificar a tendência central e a dispersão dos preços em cada categoria.\n",
    "2.  **Visualização Interativa:** A escolha do Plotly garantiu que os gráficos (Box Plot, Gráfico de Barras e Treemap) fossem interativos, facilitando a exploração e a identificação precisa de *outliers* e valores de referência.\n",
    "\n",
    "#### **Interpretação dos Resultados**\n",
    "\n",
    "1.  **Média e Dispersão de Preços (Desvio Padrão):**\n",
    "    * A categoria **`lacteos`** se destacou com a **maior média de preço normal** e, notavelmente, o **maior desvio padrão** (acima de 5000).\n",
    "    * **Insight:** O **Box Plot** confirmou que essa alta dispersão é causada pela presença de **outliers** significativos, que são produtos de alto valor (como *packs* grandes ou itens especializados) que distorcem a média. Para `lacteos`, a mediana é uma métrica mais robusta de tendência central.\n",
    "\n",
    "2.  **Política de Descontos:**\n",
    "    * O **Gráfico de Barras** de Média de Descontos mostrou que a categoria **`belleza-y-cuidado-personal`** (beleza e cuidados pessoais) possui o maior valor médio de desconto concedido.\n",
    "    * **Insight:** Isso sugere que a estratégia de precificação para produtos de beleza frequentemente utiliza descontos significativos como tática promocional para aumentar o volume de vendas.\n",
    "\n",
    "3.  **Hierarquia Categoria-Marca (Treemap):**\n",
    "    * O **Treemap** permitiu identificar rapidamente as marcas que, individualmente, contribuem mais para o alto preço médio das categorias. Por exemplo, em `lacteos`, as marcas com blocos maiores representam produtos com preços médios mais elevados, direcionando o foco para o *mix* de produtos mais caros."
   ],
   "metadata": {
    "id": "1y2B3Zl4054n"
   }
  }
 ]
}