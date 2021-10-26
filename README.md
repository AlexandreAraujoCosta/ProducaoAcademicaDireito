# Classificação dos Pesquisadores em Direito

Este repositório traz um programa para fazer o levantamento de dados no Google Scholar das páginas de pesquisadores, relacionados à busca definida no primeiro url do programa (variável próximo_href).
Neste caso, utilizamos a busca: 
'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=direito+OR+label%3Adireito+OR+label%3Adireito_constitucional+OR+label%3Afilosofia_do_direito+OR+label%3Adireito_tributario+OR+label%3Adireito_publico+OR+label%3Adireito_penal'
Fizemos isso porque o GoogleScholar só procura pelas palavras nos campos nome, affiliation e endereço. Pesquisas pelas palavras chave precisam vir como label:*, o que nos fez levantar alguns dos labels mais usados e inseri-los na pesquisa, para poder incorporar pesquisadores que, caso contraário, seriam excluídos da busca.
Essa é uma busca limitada (porque não coloca todos os labels possíveis), mas consideramos que é suficientemente ampla para viabilizar a classificação proposta.
Uma ampliação dos critérios, bem como uma busca autônoma pelas citações, seria demasiadamente onerosa e não poderia ser realizada sem um financiamento específico para esse fim.
Assim, esta deve ser percebida como uma proposta baseada em uma pesquisa exploratória, que apresenta conceitos (no caso, uma classificação) a partir dos quais seria viável fazer uma pesquisa mais exaustiva.
