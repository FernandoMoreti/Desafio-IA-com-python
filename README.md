*📘 Desafio Final de Python – Processamento de Resenhas Multilíngues*

Este repositório contém a solução do desafio final do curso de Python.
Neste projeto, eu desenvolvi um pipeline completo para leitura, processamento e análise de resenhas multilíngues utilizando Python e um modelo de IA rodando localmente.

*🧠 Sobre o Projeto*

O objetivo do desafio foi trabalhar com um arquivo .txt contendo aproximadamente 25 resenhas de usuários sobre um aplicativo de inteligência artificial. As resenhas estavam em diversos idiomas (francês, inglês, espanhol, turco, polonês, italiano, entre outros) e cada linha do arquivo representava uma entrada completa contendo:

ID do usuário

Nome do usuário

Comentário ou reclamação

Resenha detalhada (em idioma variável)

A proposta foi transformar essas linhas brutas em dados estruturados e analisáveis.

*🛠️ O que eu desenvolvi*
1. Leitura do arquivo .txt

Carreguei o arquivo e converti cada linha em um elemento de uma lista Python.
Cada posição da lista corresponde diretamente à linha original do arquivo.

2. Integração com IA local

Utilizei um modelo rodando localmente (LM Studio ou Ollama) para analisar cada resenha.
Para cada item enviado ao modelo, recebi um JSON contendo:

usuario: nome do usuário

resenha_original: texto bruto da resenha

resenha_traduzida: tradução automática para o português

sentimento: classificação entre positivo, negativo ou neutro

3. Estruturação dos dados

Transformei todas as respostas da IA em uma lista de dicionários bem formatada, permitindo manipulação simples e clara dentro do Python.

4. Função de análise dos resultados

Criei uma função que:

contabiliza quantas resenhas são positivas, negativas e neutras

concatena todas as resenhas estruturadas em uma única string, usando um separador definido

O retorno dessa função inclui tanto o relatório de contagem quanto a string final consolidada.

*📊 Resultado Final*

Ao final do projeto, obtive:

Uma lista de dicionários completamente estruturada

As resenhas traduzidas para o português

Uma classificação automática por sentimento

Estatísticas consolidadas sobre o conteúdo do arquivo

Um texto único contendo todos os registros concatenados

Esse desafio reuniu conceitos fundamentais do curso, incluindo manipulação de arquivos, listas, funções, uso de modelos de linguagem e transformação de dados.

*🚀 Objetivo Concluído*

O projeto me permitiu explorar um caso real de processamento de linguagem natural e reforçar diversos pilares do Python. Toda a solução foi desenvolvida de forma modular, clara e alinhada às boas práticas.
