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
