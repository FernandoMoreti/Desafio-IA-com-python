🌐 Desafio Final de Python — Processamento de Resenhas Multilíngues

Este repositório reúne minha solução para o desafio final do curso de Python.
O objetivo foi transformar um arquivo .txt cheio de resenhas em diferentes idiomas em um conjunto organizado, traduzido e analisado — tudo usando Python e IA local.

✨ Visão Geral

Recebi um arquivo com ~25 resenhas sobre um app de IA. Cada linha trazia:

🆔 ID do usuário

👤 Nome

💬 Comentário / Reclamação

🌍 Resenha em vários idiomas

A missão? Pegar esse conteúdo bruto e convertê-lo em dados limpos, estruturados e úteis.

🔧 O que eu desenvolvi
1. Leitura inteligente do arquivo

Transformei cada linha do .txt em um item de lista, preservando tudo exatamente como no arquivo original.

2. Análise com IA local

Para cada resenha, o modelo (LM Studio/Ollama) retornou um JSON contendo:

👤 Usuário

📝 Resenha original

🇧🇷 Tradução para português

🎭 Sentimento: positivo, negativo ou neutro

3. Estruturação dos dados

Compilei todas as respostas em uma lista de dicionários padronizada e fácil de manipular.

4. Função de análise final

Criei uma função que:

Conta quantas resenhas são positivas, negativas e neutras

Gera uma única string com todos os registros organizados

📊 Resultado Final

Com o pipeline completo, obtive:

✅ Todas as resenhas traduzidas

✅ Classificação automática de sentimento

✅ Estatísticas consolidadas

✅ Uma estrutura de dados limpa e bem organizada

✅ Texto final unificado com todos os registros

🚀 Conclusão

Foi um desafio curto, direto e muito prático.
Perfeito para consolidar leitura de arquivos, funções, manipulação de listas e integração com modelos de linguagem.
Uma experiência real de NLP com Python + IA local — simples, funcional e elegante.
