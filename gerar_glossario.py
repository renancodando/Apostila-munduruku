import csv
from pathlib import Path

rows = list(csv.DictReader(Path('apostila/fontes/ids-munduruku-original.tsv').open(), delimiter='\t'))
lookup = {(r['chapter_id'],r['entry_id']): r for r in rows}
groups = [
('Território, céu e água', '1', '''100 mundo
212 solo
213 poeira
214 lama
215 areia
220 monte/colina
250 ilha
280 caverna
310 água
350 onda
360 rio/córrego
380 área alagada
410 mata/floresta
420 árvore
430 madeira
440 pedra
510 céu
520 sol
530 lua
540 estrela
550 relâmpago
590 arco-íris
610 luz
620 escuridão
630 sombra
720 vento
730 nuvem
740 neblina
750 chuva
810 fogo
830 fumaça
840 cinzas
880 lenha'''),
('Pessoas, parentesco e referência', '2', '''100 pessoa/ser humano
210 homem
220 mulher
250 menino
251 rapaz/adolescente
260 menina
270 criança
280 bebê
310 marido
320 esposa
350 pai
360 mãe
410 filho
440 irmão
455 irmã mais nova
460 avô
461 homem idoso
470 avó
471 mulher idosa
910 eu
920 tu/você
941 nós inclusivo
942 nós exclusivo
950 vocês
960 eles/elas'''),
('Animais', '3', '''110 animal
230 vaca
250 ovelha
350 porco
520 galo
540 galinha
550 frango
580 ninho
581 ave/pássaro
585 gavião
586 urubu
591 morcego
592 papagaio
594 pomba
596 coruja
610 cachorro
620 gato
630 rato
650 peixe
664 arraia
750 veado
760 macaco
811 piolho
817 formiga
818 aranha
820 abelha
822 colmeia
823 vespa
840 verme
850 cobra
950 sapo
970 jacaré'''),
('Corpo e processos', '4', '''110 corpo
120 pele
140 cabelo
142 barba
150 sangue
160 osso
162 costela
170 chifre
180 cauda
200 cabeça
204 rosto
210 olho
214 cílio
220 orelha
230 nariz
240 boca
260 língua (órgão)
270 dente
280 pescoço
281 nuca
300 ombro
310 braço
330 mão
340 dedo
344 unha
350 perna
360 joelho
370 pé
372 calcanhar
374 rastro/pegada
392 asa
393 pena
440 coração
450 fígado
451 rim
460 estômago
461 intestinos
510 respirar
560 saliva/cuspir
570 vomitar
580 morder
610 dormir
620 sonhar
630 acordar
690 banhar-se
720 nascer
740 viver/vida
750 morrer/morto
810 forte
820 fraco
860 curar
880 remédio
890 veneno
912 descansar'''),
('Alimentação, casa e plantas', '5', '''110 comer
120 alimento
122 cru
123 maduro
124 verde/não maduro
125 podre
130 beber
140 fome
150 sede
230 assar/fritar
260 recipiente de cozinhar
280 panela
350 recipiente de beber
380 faca
530 massa
610 carne
660 feijão
700 batata
710 fruta
760 uva
770 castanha/noz
791 gordura
810 sal
840 mel
970 ovo'''),
('Vestuário', '6', '''120 roupa
210 tecido
240 algodão
350 costurar
380 linha
420 vestido
460 saia
480 calça
730 anel
770 brinco'''),
('Moradia', '7', '''110 morar
120 casa
130 abrigo/cabana
220 porta
240 chave
370 escada
420 cama
450 lamparina
460 vela'''),
('Cultivo e vegetação', '8', '''120 campo de cultivo
130 jardim
160 cerca
220 cavar
240 pá
311 semente
470 milho
510 capim
540 raiz
550 galho
560 folha
570 flor
680 tabaco
750 casca (vegetal)
840 bananeira
910 batata-doce
920 mandioca
930 cabaça
941 cana'''),
('Manipular objetos', '9', '''160 amarrar
161 desamarrar
190 corda
210 bater
220 cortar
222 talhar
250 machado
260 quebrar
261 quebrado
280 rasgar
310 esfregar/limpar
330 puxar
343 espremer
360 lavar
460 perfurar
500 prego
560 cola
880 tinta'''),
('Movimento', '10', '''120 virar
130 virar-se
170 torcer
230 cair
250 lançar
330 afundar
340 flutuar
350 nadar
370 voar
380 soprar
410 rastejar
440 dançar
450 andar
470 ir
472 subir
474 sair
480 vir
481 voltar
490 partir
520 seguir
550 chegar
570 entrar
610 carregar
620 trazer
670 empurrar
710 estrada
720 caminho
831 canoa
852 remar
910 porto'''),
('Posição, dimensão e quantidade', '12', '''50 dentro
130 sentar
140 deitar
150 ficar em pé
160 permanecer
220 unir
230 separar
240 abrir
260 cobrir
310 alto/acima
410 lado direito
420 lado esquerdo
430 perto
440 longe
450 leste
550 grande
560 pequeno
570 comprido
580 alto (dimensão)
590 curto
610 largo
620 estreito
630 grosso
650 fino
730 reto
810 redondo
820 círculo
850 buraco
920 semelhante'''),
('Quantidade', '13', '''10 um
20 dois
30 três
40 quatro
50 cinco
140 todos
150 muitos
170 poucos
181 alguns
210 cheio
220 vazio
330 sozinho/somente
350 último'''),
('Tempo', '14', '''130 novo
150 velho
210 rápido
240 atrasar
252 durar
310 sempre
410 dia
420 noite
480 amanhã
530 relógio
730 ano
740 inverno
760 verão'''),
('Percepção e qualidades', '15', '''210 cheirar
250 cheiro agradável
350 doce
380 azedo
410 ouvir
420 escutar
510 ver
520 olhar
550 mostrar
560 brilhar
570 brilhante
640 branco
650 preto
660 vermelho
670 azul
680 verde
690 amarelo
740 duro
770 liso
810 pesado
820 leve
830 molhado
840 seco
850 quente
851 morno
860 frio
870 limpo
880 sujo'''),
('Emoções, pensamento e comunicação', '16', '''230 alegre
250 rir
251 sorrir
260 brincar
270 amar
320 tristeza
370 chorar
380 lágrima
410 odiar
420 raiva
530 medo
620 desejar/querer
660 verdadeiro
670 mentir
710 bom
720 ruim
810 bonito'''),
('Conhecimento e perguntas', '17', '''130 pensar/refletir
170 saber
180 parecer
320 esquecer
360 segredo
370 certo/seguro
420 causa
560 negativo/não
610 como?
650 quando?
680 quem?'''),
('Expressão e escrita', '18', '''110 voz
120 cantar
210 falar
220 dizer
221 contar história
240 língua (idioma)
280 nome
520 ler
560 papel
570 caneta'''),
]

out = ['# 28. Repertório lexical documentado e oficinas de recuperação',
'''Este repertório é uma seleção de dados do IDS, não um dicionário de escrita prática nem uma lista de frequência. A coluna de formas preserva a transcrição original, inclusive hífens, variantes e morfemas ligados. Não aplique essas entradas como se fossem palavras prontas para qualquer frase. As traduções de conceitos em português servem para localizar a entrada e não esgotam os sentidos.

O IDS tem 437 registros na tabela consultada. A seleção abaixo não inclui todos: prioriza domínios úteis ao estudo e evita algumas entradas particularmente dependentes de contexto. A presença de duas variantes separadas por ponto e vírgula não demonstra que são intercambiáveis em todas as construções. Sinais como ʔ, ɨ, š e ǰ pertencem à notação do dataset. Não os substitua silenciosamente pelas letras da escrita prática.

Escolha no máximo seis itens novos por sessão. Use reconhecimento, recuperação, comparação com outra fonte e análise em ocorrência. As oficinas após os grupos mudam o tipo de decisão. O repertório ampliado só passa a produção de frases quando você tiver construções documentadas para ele. É uma referência para expandir o curso, não prova de que o vocabulário inteiro já foi ensinado em textos.

**Fonte e atribuição:** Mary Ritchie Key, contribuição 287, Intercontinental Dictionary Series, editada por Key e Comrie; fonte lexical indicada: Crofts e Sheffler (1981). Dados IDS CC BY 4.0. Tradução de conceitos e seleção desta edição. https://ids.clld.org/contributions/287
''']
tasks = [
'Desenhe uma cena simples de rio e margem. Escolha seis referentes que a cena realmente permite identificar. Coloque números na imagem e formas transcritas no verso. Na revisão do dia seguinte, use só os números. Não atribua uma palavra a um detalhe que a figura não mostra.',
'Faça dois esquemas de participantes: um incluindo o interlocutor e outro excluindo-o. Recupere as entradas correspondentes e compare com a escrita prática estudada no capítulo 10. Nos termos de parentesco, registre a necessidade de conferir condições de uso; não trate a tradução como sistema completo.',
'Escolha seis animais. Na primeira rodada, reconheça por imagem. Na segunda, recupere sem ver a forma. Na terceira, compare os itens também presentes no banco ortográfico. Explique por que duas notações de rato podem corresponder a camadas diferentes.',
'Use um desenho anatômico simples e neutro. Localize cinco partes externas; depois observe entradas com hífen inicial. O hífen pode indicar material ligado na notação da fonte. Não o apague para afirmar que a forma resultante é um nome independente. Para atividades com processos, mantenha separados verbo e nome de parte.',
'Organize quatro objetos de alimentação por função: recipiente, ferramenta, alimento e qualidade de alimento. A classificação da atividade é editorial. Recupere depois a forma a partir da função e confira as entradas. Não transforme as categorias em frases traduzidas.',
'Faça um inventário visual de três peças de roupa. Na sessão seguinte, misture uma peça a uma ferramenta e a um alimento. A tarefa testa recuperação fora da categoria original. Evite deduzir gênero gramatical a partir de uma roupa socialmente associada a um gênero.',
'Desenhe uma planta abstrata de cômodo e indique porta, cama e uma fonte de luz. Recupere as entradas sem traduzir uma frase inteira. Compare casa no IDS com a discussão de classe nominal em G06, registrando que há diferenças de forma e construção.',
'Monte uma sequência visual de semente, planta, folha e fruto usando os itens disponíveis nos grupos. A sequência é didática; não é uma narrativa da língua. Marque quais entradas aparecem como material ligado e precisam de construção nominal confirmada.',
'Escolha amarrar, cortar e lavar. Descreva em português participantes e objeto possível de cada evento. Depois recupere as entradas lexicais e deixe a produção em Munduruku pendente de um paradigma. Esta tarefa impede converter uma entrada de verbo numa oração completa por palpite.',
'Faça quatro setas ou quadros de movimento e associe ir, vir, entrar e sair. Identifique o ponto de perspectiva. Na revisão de sete dias, mude esse ponto e explique quais rótulos portugueses precisariam ser reconsiderados antes de selecionar uma forma da língua.',
'Separe relações espaciais, postura e dimensão. Cada rodada deve pedir uma decisão diferente: identificar categoria, recuperar entrada, representar visualmente. Não trate alto/acima e alto/dimensão como conceitos automaticamente iguais.',
'Use conjuntos de pontos para quantidades pequenas. Compare a transcrição do IDS com o xepxep da escrita prática já estudada. Depois diferencie conjuntos exatos de muitos, poucos e todos sem inventar construções de contagem.',
'Monte uma linha temporal com hoje como ponto de referência, mas não traduza hoje sem fonte. Recupere dia, noite e amanhã no repertório. Discuta por que uma palavra para uma estação ou período pode depender do contexto e não deve importar automaticamente o calendário climático de outra região.',
'Escolha uma qualidade visual, uma de peso e uma de temperatura. Associe às representações adequadas. Depois retire a imagem e recupere a entrada. Uma palavra de qualidade não deve ser encaixada automaticamente como adjetivo pós-nominal seguindo português.',
'Separe evento observável, estado e avaliação. Rir, medo e bonito fornecem decisões distintas. Não afirme que o desenho de um rosto representa com exatidão todo o significado de uma entrada emocional. Recupere a forma e registre a construção como informação ainda necessária.',
'Associe pensar, saber e esquecer a situações de estudo em português. Recupere as formas sem afirmar que sejam infinitivos prontos para conjugação portuguesa. Em perguntas, compare quem com abu da escrita prática e preserve ambas as camadas.',
'Monte a cadeia voz, falar, contar história, papel e ler como associação editorial de conceitos. Ela não é frase em Munduruku. Recuperar a entrada para ler é diferente de demonstrar leitura de um texto novo. Termine verificando uma construção efetivamente ensinada no capítulo 11.',
]
count = 0
for idx,(title,ch,items) in enumerate(groups):
    out += ['### '+title, '| Conceito português | Forma no IDS | ID |','|---|---|---|']
    for line in items.splitlines():
        eid,meaning=line.split(' ',1)
        r=lookup[(ch,eid)]
        out.append('| '+meaning+' | '+r['Mundurukú_Phonemic'].replace('|','/')+' | '+ch+'.'+eid+' |')
        count += 1
    out += ['', '**Oficina '+str(idx+1)+'.** '+tasks[idx], '']
out += ['### Correção das oficinas',
'''O gabarito lexical são as formas e os IDs da própria tabela. O acerto exige localizar a entrada correta, copiar seus sinais e preservar a camada transcrita. As tarefas de classificação aceitam organização diferente se você explicar o critério. Uma nova frase na língua não recebe ✓ apenas porque todas as palavras aparecem no repertório. Sem construção confirmada, marque produção a revisar.

**Calendário para todos os grupos:** no dia seguinte, recupere os seis itens escolhidos; em três dias, misture três deles a três de outro grupo; em sete dias, procure um item numa fonte de escrita prática; em quatorze dias, explique a diferença entre entrada e ocorrência; em trinta dias, reteste sem a tabela.

Erros de grafema pedem cópia coberta. Erros de significado pedem referência visual ou contexto. Erros de classe pedem ocorrência documentada. Esquecimento pede recuperação com atraso. Uma recuperação correta que depende da ordem da lista pede embaralhamento. Esses cinco problemas não recebem a mesma intervenção.

### Síntese de uso

Esta seleção contém COUNT entradas. Ela amplia o material de consulta, mas não preenche a lacuna de narrativas graduadas nem prova domínio produtivo de COUNT palavras. A distinção entre consultar, reconhecer e usar precisa continuar no seu registro de estudo.
'''.replace('COUNT',str(count))]
Path('apostila/capitulos/28-repertorio-lexical.md').write_text('\n\n'.join(out), encoding='utf-8')
print({'entradas_selecionadas':count,'originais_ids':len(rows)})
