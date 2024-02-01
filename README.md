# en-US PRLLM - Portuguese Questions and Answers for Language Models
Dataset with texts, questions, and answers. The texts are diverse, many taken from the internet such as news, product descriptions, short stories, notices, logs, emails...

The dataset is divided into two files for each text:

|The text|The questions|
|-|-|
|xx.txt|rxx.tsv|

The questions and instructions are in TSV format. The first column is the question/instruction, and the second column is the answer.
The TSV lines that contain the token indicate that the answer is the entire text, as in the instructions "write a text about stocks," and the answer is the text in the corresponding txt file.

The Python file generates a *.qry file, which is a format I use for my models using the tokens ,  and . You can easily use it as a template to adapt to LLAMA models and other more widespread ones.

License? There are texts taken from portals, so I cannot provide any license. Use it at your own risk.

# pt-BR PRLLM - Perguntas e Respostas para Modelos de Linguagem
Dataset com textos, perguntas e respostas. Os textos são diversos, muitos retirados da internet como notícias, descrição de produtos, pequenas histórias, editais, logs, e-mails ...

O dataset é dividido em dois aquivos para cada texto:

|O texto|As perguntas|
|-|-|
|xx.txt|rxx.tsv|

As perguntas e instruções estão no formato TSV. Sendo primeira coluna a pergunta/instrução e a segunda coluna a resposta.
As linhas do TSV que contem o token <|answer|> indica que a resposta é o texto inteiro como nas instruções "faça um texto sobre ações" e a resposta é o texto no arquivo txt correspondente.

O arquivo python gera um arquivo *.qry que é um formato que uso para meus modelos usando os tokens <|query|>, <|answer|> e <|endoftext|>. Você pode facilmente usá-lo como modelo para adaptar aos modelos LLAMA e outros mais difundidos.

Licença? Há textos retirados de portais, então não posso dar licença alguma. Use ao seu risco.
