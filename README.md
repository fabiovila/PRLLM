# PRLLM - Perguntas e Respostas para Modelos de Linguagem
Dataset com textos e perguntas e respostas. Os textos são diversos, muitos retirandos da internet como notícias, descrição de produtos, pequenas histórias, editais, logs, e-mails ...

O dataset é dividido em dois aquivos para cada texto:

|O texto|As perguntas|
|-|-|
|xx.txt|rxx.tsv|

As perguntas e instruções estão no formato TSV. Sendo primeira coluna a pergunta/instrução e a segunda coluna a resposta.
As linhas do TSV que contem o token <|answer|> indica que a resposta é o texto inteiro como nas instruções "faça um texto sobre ações" e a resposta é o texto no arquivo txt correspondente.

O arquivo python gera um arquivo *.qry que é um formato que uso para meus modelos usando os tokens <|query|>, <|answer|> e <|endoftext|>. Você pode facilmente usá-lo como modelo para adaptar aos modelos LLAMA e outros mais difundidos.

Licença? Há textos retirados de portais, então não posso dar licença alguma. Use ao seu risco.
