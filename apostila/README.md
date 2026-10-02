# Munduruku: reconstrução do curso autodidata extenso

A edição extensa está em construção, conforme o pedido de uma obra de 1.000 a 2.000 páginas úteis. A etapa disponível tem **343 páginas**, cerca de **72,7 mil palavras**, **437 registros lexicais** em **22 temas**, **407 tarefas lexicais**, 28 capítulos de fundamentos e gramática inicial e gabarito separado. O novo bloco 25–28 aprofunda nomes de parte e parentesco, função classificatória, produtividade dos nomes alienáveis e outros morfemas nominais com dados documentados. **Ainda não é a obra final completa.**

- [Baixar o PDF de trabalho](extensa/pdf/Munduruku-Edicao-Extensa-Em-Construcao.pdf)
- [Ler o texto integral da reconstrução](extensa/Munduruku-Extensa-Texto-Integral.md)
- [Ler os capítulos da edição extensa](extensa/capitulos/)
- [Ver o próximo trabalho e o progresso](progresso/reconstrucao.json)
- [Arquitetura e instruções de retomada](RECONSTRUCAO.md)
- [Relatório de verificação](extensa/verificacao.json)

A numeração dos capítulos lexicais segue a arquitetura editorial; os intervalos ainda não escritos não contêm páginas vazias nem representam capítulos concluídos. O PDF reúne apenas o conteúdo presente. Faltam aprofundamento gramatical, corpus amplo de leituras graduadas, áudio autorizado, instruções validadas em Munduruku e revisão por falantes.

Para gerar a etapa extensa, a partir da raiz do projeto:

```bash
python extensa/gerar_lexico.py
python extensa/gerar_pdf.py
```

Os scripts usam Python, ReportLab e fontes DejaVu. As traduções dos conceitos estão em `extensa/traducoes-ids.json`; o índice estruturado está em `extensa/indice-lexical.json`. Formas, alternativas e comentários permanecem vinculados aos registros originais. A licença aberta do IDS não se estende automaticamente a livros e artigos referenciados.

## Edição inicial preservada

A versão de 118 páginas continua abaixo como registro da primeira edição. Ela não satisfaz o pedido da reconstrução extensa.

# Munduruku: leitura, escrita e análise

Uma trajetória autodidata documentada, preparada para Renan. Edição de 2 de outubro de 2026.

## Arquivos

- [Baixar o PDF](pdf/Munduruku-Curso-Autodidata-Documentado.pdf)
- [Ler o texto integral](Apostila-Munduruku-Texto-Integral.md)
- [Ler por capítulos](capitulos/)
- [Dados lexicais originais do IDS](fontes/ids-munduruku-original.tsv)
- [Referências e limites da edição](capitulos/30-referencias-e-continuidade.md)

O PDF contém 118 páginas em A5, índice clicável, marcadores de capítulos, diagramas de análise, atividades e gabaritos separados. O texto tem aproximadamente 23 mil palavras, incluindo o material lexical de consulta. São 26 unidades, orientação de estudo, glossário de análise, 376 entradas lexicais selecionadas, oficinas e avaliações cumulativas.

## Estado do material

Esta edição **não é um curso completo de proficiência avançada validado por falantes**. Os exemplos têm fontes, mas ainda faltam corpus amplo de narrativas graduadas, áudios, instruções em Munduruku e revisão de naturalidade por professores ou falantes. A etapa final retira a tradução imediata de construções conhecidas; não alcança a imersão integral de 95–100% solicitada no projeto original.

Os limites estão no próprio PDF e não devem ser retirados ao compartilhar a edição. A presença de 376 entradas de consulta não significa que todas foram ensinadas em frases nem que o estudante já saiba usá-las produtivamente. O repertório do IDS conserva transcrição fonêmica e não foi convertido automaticamente em escrita prática.

## Organização

1. Orientação, método, diagnóstico e recuperação espaçada.
2. Escrita, vogais, consoantes, tom e segmentação.
3. Repertório contextual e leitura de construções.
4. Pessoa, posse, pronomes e papéis no evento.
5. Lugar, instrumento, aspecto, relacionais e perguntas.
6. Negação, escopo, classificação e incorporação.
7. Hipótese, espaço, quantidade, derivação e nominalização.
8. Avaliações, leitura sem tradução, glossários e gabaritos.

## Reconstruir o PDF

Use Python com `reportlab`, `pypdf` e fontes DejaVu instaladas. Na pasta do projeto:

```bash
python gerar_glossario.py
python gerar_pdf.py
```

O texto integral é montado a partir dos arquivos numerados de `capitulos/`. A fonte lexical é o TSV preservado em `fontes/`. O gerador não inventa exemplos de frases e não converte a transcrição do IDS para ortografia prática.

## Fontes e direitos

Dados do IDS: Mary Ritchie Key; edição de Mary Ritchie Key e Bernard Comrie; fonte indicada pelo registro: Crofts e Sheffler (1981). Licença do dataset IDS: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). As traduções de conceitos, seleção e oficinas são desta edição.

As demais fontes são referenciadas, sem redistribuição de seus PDFs ou reprodução integral de seus capítulos. A licença do IDS não deve ser interpretada como licença geral de todas as obras citadas nem de todo o material editorial.

## Verificação

Verificações documentais e de consistência interna dos exemplos usados, correspondência de atividades com gabarito, sinais Unicode, índice, limites de página e renderização. Não houve validação nova por falantes, teste de pronúncia ou certificação de fluência.
