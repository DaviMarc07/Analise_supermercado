Análise Exploratória de Produtos de Supermercado

Contexto do Projeto
Este projeto tem como objetivo aplicar os fundamentos da descoberta de dados e da estatística descritiva para analisar o catálogo de produtos de um supermercado no Chile. A base de dados contém informações sobre produtos, marcas e preços, e a análise busca identificar padrões de preços, dispersão e políticas de desconto entre as diferentes categorias de produtos.

Metodologia (O que, Como e Porquê)
A análise foi conduzida em Python utilizando as bibliotecas Pandas para manipulação de dados, e Plotly para visualizações interativas.

Cálculos Estatísticos (Porquê): Calculamos a Média e o Desvio Padrão do Preco_Normal para quantificar a tendência central e a dispersão dos preços em cada categoria.

Visualização (Como): Utilizamos o Plotly para criar gráficos interativos, facilitando a exploração dos dados, especialmente para identificar outliers e comparar médias de descontos e preços em múltiplas dimensões (hierarquia).

Storytelling (O que): Os resultados foram interpretados para traduzir números em insights de negócio.

Interpretação dos Resultados
Média e Dispersão de Preços (Desvio Padrão):

A categoria lacteos possui a maior média de preço normal (cerca de 6764) e, crucialmente, o maior desvio padrão (cerca de 5271).

Insight: O alto desvio padrão na categoria lacteos significa que é a categoria com a maior variabilidade de preços.

O Box Plot confirmou que esta dispersão é causada pela presença de vários produtos de nicho ou de grande volume (packs de 12L, leites em pó) que se comportam como outliers em relação à maioria dos produtos lácteos mais comuns.

Política de Descontos:

A categoria belleza-y-cuidado-personal (beleza e cuidados pessoais) se destacou como a que possui a maior média de desconto concedido.

Insight: Isso sugere que a estratégia de precificação para produtos de beleza frequentemente utiliza descontos significativos para impulsionar vendas, uma tática comum para produtos com alta margem ou alto giro.

Hierarquia Categoria-Marca (Treemap):

O Treemap interativo permite identificar rapidamente as marcas que contribuem para o preço médio mais alto dentro de cada categoria. Por exemplo, grandes blocos em lacteos (como Loncoleche e Soprole) indicam marcas com alta representatividade no preço médio, alinhado com a presença de seus packs e produtos especializados.
