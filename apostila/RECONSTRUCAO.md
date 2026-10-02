# Reconstrução da apostila extensa de Munduruku

Renan pediu a substituição do curso inicial de 118 páginas por uma apostila autodidata extensa, com explicações aprofundadas, repertório lexical amplo e prática suficiente. A meta editorial solicitada é de 1.000 a 2.000 páginas úteis ou mais, conforme o conteúdo documentável. A edição inicial está preservada como referência histórica; não é o resultado final desse pedido.

## Retomar o trabalho

1. Leia `progresso/reconstrucao.json`. Se `trabalho_ativo.expira_em` estiver no futuro, outro processo pode estar escrevendo: não faça uma publicação concorrente.
2. Leia os arquivos de `extensa/capitulos/`, os geradores e o último relatório de verificação. Confira a branch main antes de editar; não presuma que a cópia local está atualizada.
3. Escolha o primeiro lote pendente, pesquise as fontes primárias e escreva conteúdo substancial. Um lote é concluído somente com explicação, exemplos documentados, exercícios, respostas e referências. Títulos e planos não contam como capítulos escritos.
4. Atualize o PDF de trabalho e o texto integral, confira paginação e renderização e publique o lote e seu registro. Preserve alterações do usuário e use atualização da branch sem force.
5. Ao terminar a execução, libere o registro de trabalho ativo e descreva o próximo passo exato. Não declare a obra completa por alcançar um número de páginas.

## Arquitetura editorial

| Parte | Conteúdo | Capítulos previstos | Estado inicial |
|---|---|---:|---|
| I | Método autodidata, som, escrita, tom e ferramentas de análise | 1–16 | Primeira redação publicada |
| II | Pessoa, referência, nomes, parentesco e posse | 17–34 | Em redação; capítulos 17–24 publicados |
| III | Predicação, verbos, participantes, aspecto e derivação | 35–58 | Pendente |
| IV | Espaço, tempo, quantidade, perguntas, negação e partículas | 59–78 | Pendente |
| V | Classificação, incorporação, nominalização e estruturas complexas | 79–96 | Pendente |
| VI | Léxico temático documentado, diferenças de sentido e recuperação | 97–118 | Primeira redação publicada; ampliar contextos |
| VII | Leitura graduada e oficinas cumulativas | 119–134 | Pendente; requer corpus |
| VIII | Avaliações, respostas comentadas, índices e referência | 135–144 | Pendente |

Essa arquitetura é uma proposta de distribuição, não 144 capítulos concluídos nem um compromisso de páginas por capítulo. Reorganize-a se a documentação exigir. A meta precisa ser atendida com conteúdo, sem letras grandes, fichas vazias, duplicação de explicações, repetição mecânica de tabelas ou respostas isoladas para multiplicar páginas.

## Critérios de qualidade

- Ensinar desde o início: explicar termos antes de usá-los; analisar exemplos passo a passo; distinguir reconhecimento de uso produtivo.
- Cada forma Munduruku precisa de origem verificável. Manter separadas a escrita prática e a transcrição fonêmica. Não converter automaticamente os dados do IDS.
- Apresentar vocabulário por campos de sentido, contrastes e construções atestadas. Quantidade de entradas de dicionário não equivale a quantidade de palavras dominadas.
- Oferecer exercícios diferentes: recuperação, discriminação, análise, reconstrução, leitura e aplicação. Explicar as respostas e os erros previsíveis.
- Retirar o português gradualmente quando houver input compreensível. Símbolos didáticos não são instruções em Munduruku. Não chamar uma lista de palavras de narrativa.
- Não simular revisão por falantes nem áudio nativo. Registrar separadamente o que depende de validação humana.
- Respeitar direitos autorais; usar dados abertos com atribuição e escrever explicações próprias. A disponibilidade de uma tese não autoriza reproduzir toda a tese como apostila.

## Fontes já disponíveis

- IDS: `fontes/ids-munduruku-original.tsv`, 437 registros, CC BY 4.0; fonte lexical original preservada. A seleção histórica tem 376 entradas.
- Picanço (2012): https://etnolinguistica.wdfiles.com/local--files/mono%3A3/picanco_2012_munduruku.pdf
- Gomes (2006): https://repositorio.unb.br/handle/10482/3754
- Gomes (2019): https://www.scielo.br/j/bgoeldi/a/M9swfwRCmsmx8K4yQQjRdKJ/?lang=pt
- O curso Língua Viva foi localizado por relato acadêmico; o Livro 1 completo não foi consultado.

Baixe as fontes para pesquisa quando necessário; não inclua PDFs de terceiros no repositório sem autorização. Guarde a localização precisa de exemplos novos em `extensa/fontes-e-exemplos.json`.

## Continuidade agendada

O usuário autorizou retomar o trabalho depois da renovação de sua cota. Foi criada uma execução recorrente horária. O agendador não expõe o saldo nem o momento exato da renovação de 5 horas; portanto, a retomada é uma tentativa quando a execução estiver disponível, não uma garantia de detecção dessa condição. Não manter processos de espera nem simular que a cota foi consultada. Desative o agendamento ao concluir a obra.
