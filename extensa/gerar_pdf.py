import re, html, math, json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable, KeepTogether
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'pdf'/'Munduruku-Edicao-Extensa-Em-Construcao.pdf'
for name,file in [('Texto','DejaVuSans.ttf'),('TextoB','DejaVuSans-Bold.ttf'),('TextoI','DejaVuSans.ttf'),('Titulo','DejaVuSerif.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('Texto',normal='Texto',bold='TextoB',italic='TextoI',boldItalic='TextoB')
INK=HexColor('#25352f'); GREEN=HexColor('#214d3e'); CLAY=HexColor('#a8583c'); PALE=HexColor('#f2f3ed'); LINE=HexColor('#d7dfd4')
W,H=419.53,595.28
styles={
'body':ParagraphStyle('body',fontName='Texto',fontSize=9.8,leading=14.3,textColor=INK,spaceAfter=7.3,splitLongWords=True),
'h1':ParagraphStyle('h1',fontName='Titulo',fontSize=20,leading=25,textColor=GREEN,spaceBefore=8,spaceAfter=15,keepWithNext=True),
'h2':ParagraphStyle('h2',fontName='TextoB',fontSize=12.2,leading=16,textColor=GREEN,spaceBefore=14,spaceAfter=8,keepWithNext=True),
'small':ParagraphStyle('small',fontName='Texto',fontSize=7.8,leading=11.2,textColor=INK,spaceAfter=5),
'refs':ParagraphStyle('refs',fontName='Texto',fontSize=9.2,leading=13,textColor=INK,spaceAfter=6),
'cell':ParagraphStyle('cell',fontName='Texto',fontSize=8.2,leading=11.2,textColor=INK,spaceAfter=0),
'headcell':ParagraphStyle('headcell',fontName='TextoB',fontSize=8.2,leading=11.2,textColor=GREEN),
'bullet':ParagraphStyle('bullet',fontName='Texto',fontSize=9.8,leading=14.3,textColor=INK,leftIndent=10,firstLineIndent=-8,spaceAfter=6),
'toc0':ParagraphStyle('toc0',fontName='Texto',fontSize=8.6,leading=11.6,textColor=INK,spaceBefore=3,leftIndent=0),
}

def inline(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    if s.startswith('https://'):
        s=f'<link href="{s}" color="#214d3e">{s}</link>'
    return s

class Diagram(Flowable):
    def __init__(self,kind):super().__init__();self.kind=kind;self.width=351;self.height=124 if kind!='frase' else 154
    def draw(self):
        c=self.canv;c.setFillColor(PALE);c.roundRect(0,0,self.width,self.height,7,fill=1,stroke=0)
        c.setStrokeColor(GREEN);c.setFillColor(INK)
        def label(x,y,s,size=8,font='Texto'):c.setFont(font,size);c.drawString(x,y,s)
        def box(x,y,w,h,s):
            c.setFillColor(Color(1,1,1));c.setStrokeColor(LINE);c.roundRect(x,y,w,h,4,fill=1,stroke=1);c.setFillColor(INK);label(x+7,y+h/2-3,s)
        if self.kind=='vogais':
            label(14,105,'ARTICULAÇÃO ≠ TOM',9,'TextoB')
            for x,s in [(105,'anterior'),(197,'central'),(276,'posterior')]:label(x,84,s)
            for y,s in [(63,'alta'),(40,'média'),(17,'baixa')]:label(14,y,s)
            for x,y,s in [(119,63,'i'),(119,40,'e'),(213,40,'u'),(293,40,'o'),(213,17,'a')]:label(x,y,s,12,'TextoB')
        elif self.kind=='camadas':
            label(14,105,'TRÊS CAMADAS, TRÊS PERGUNTAS',9,'TextoB')
            box(14,52,97,33,'<u>  escrita');box(124,52,97,33,'/ə/  fonema');box(234,52,103,33,'[ə]  realização')
            label(15,26,'Uma grafia não contém toda a informação da fala.')
        elif self.kind=='pessoas':
            label(14,105,'QUEM INTEGRA O GRUPO?',9,'TextoB')
            for x,s in [(88,'inclusivo'),(245,'exclusivo')]:
                c.setFillColor(INK)
                label(x-20,80,s,9,'TextoB')
                c.setStrokeColor(GREEN);c.ellipse(x-46,22,x+54,67)
                for dx,t in [(-24,'F'),(7,'I'),(34,'O')]:
                    inside=not(s=='exclusivo' and t=='I')
                    px=x+dx if inside else x+70
                    c.setFillColor(GREEN if inside else CLAY);c.circle(px,45,8,fill=1,stroke=0)
                    c.setFillColor(Color(1,1,1));label(px-2.5,42,t,7)
            c.setFillColor(INK);label(14,7,'F: falante   I: interlocutor   O: outra pessoa',7)
        elif self.kind=='frase':
            label(14,134,'LEITURA POR BLOCOS',9,'TextoB')
            for y,wrd,fn in [(107,'ag̃okatkat','participante: homem'),(83,'wida','participante: onça'),(59,"o'yaoka",'predicado'),(35,'kisem','instrumento'),(11,'tip pe','lugar')]:
                label(15,y,wrd,10,'TextoB');label(156,y,fn,8)
        elif self.kind=='estrutura':
            label(14,105,'FORMA → RELAÇÃO → INTERPRETAÇÃO',9,'TextoB')
            box(14,55,95,31,'o=');box(126,55,95,31,'Ø');box(239,55,95,31,'ba')
            label(15,37,'pessoa');label(129,37,'relação');label(242,37,'base nominal')
            label(14,14,'Linha de análise: o=Ø-ba    |    Escrita corrente: oba',8)

class Cover(Flowable):
    def __init__(self):super().__init__();self.width=351;self.height=478
    def draw(self):
        c=self.canv
        c.setFillColor(GREEN);c.roundRect(0,0,351,478,4,fill=1,stroke=0)
        c.saveState();clip=c.beginPath();clip.rect(0,0,351,478);c.clipPath(clip,stroke=0,fill=0)
        c.setStrokeColor(HexColor('#8dba9b'))
        for k in range(14):
            p=c.beginPath()
            x=30+k*20;p.moveTo(x,-4)
            p.curveTo(x-96,96,x+63,149,x-10,214)
            p.curveTo(x-61,261,x+34,298,x+16,342)
            c.setLineWidth(0.6 if k%3 else 1.2);c.drawPath(p)
        c.restoreState()
        c.setFillColor(GREEN);c.rect(14,286,324,175,fill=1,stroke=0)
        c.setFillColor(HexColor('#f8f4e8'));c.setFont('TextoB',9);c.drawString(24,437,'CURSO EXTENSO  /  EM CONSTRUÇÃO')
        c.setFont('Titulo',36);c.drawString(22,385,'Munduruku')
        c.setFont('Texto',15);c.drawString(24,351,'Curso autodidata extenso')
        c.setFont('Texto',10);c.drawString(24,322,'Fundamentos e repertório documentado')
        c.setFillColor(HexColor('#f8f4e8'));c.rect(14,15,324,85,fill=1,stroke=0)
        c.setFillColor(INK);c.setFont('TextoB',9);c.drawString(24,78,'EDIÇÃO PREPARADA PARA RENAN')
        c.setFont('Texto',9);c.drawString(24,58,'Recuperação ativa • revisão cumulativa • fontes rastreáveis')
        c.setFont('Texto',8);c.drawString(24,36,'2 de outubro de 2026  /  primeira etapa da reconstrução')

class Doc(BaseDocTemplate):
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw);self.chapter='Munduruku';self.index={};self.headings=[]
    def beforeDocument(self):self.chapter='Munduruku';self.index={};self.headings=[]
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and hasattr(f,'bookmark'):
            text=f.getPlainText();key=f.bookmark;self.canv.bookmarkPage(key);self.canv.addOutlineEntry(text,key,0,False)
            self.notify('TOCEntry',(0,text,self.page,key));self.chapter=text;self.index[key]=self.page;self.headings.append((text,self.page))

def footer(c,d):
    if d.page==1:return
    c.saveState();c.setFillColor(INK);c.setFont('Texto',7)
    name='Munduruku · curso extenso · edição em construção'
    while pdfmetrics.stringWidth(name,'Texto',7)>310:name=name[:-2]
    c.drawString(34,H-24,name);c.setStrokeColor(LINE);c.line(34,31,W-34,31)
    c.drawString(34,20,'MUNDURUKU · EDIÇÃO EM CONSTRUÇÃO');c.drawRightString(W-34,20,str(d.page));c.restoreState()

doc=Doc(str(OUT),pagesize=(W,H),leftMargin=34,rightMargin=34,topMargin=39,bottomMargin=43,title='Munduruku: curso autodidata extenso em construção',author='Edição preparada para Renan',subject='Curso autodidata documental; leitura, morfologia, exercícios e repertório IDS')
doc.addPageTemplates([PageTemplate(id='padrao',frames=Frame(34,43,W-68,H-82,id='texto',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0),onPage=footer)])
story=[Cover(),PageBreak(),Paragraph('Índice',styles['h1']),Paragraph('Esta edição contém os capítulos já redigidos. As lacunas na numeração correspondem às partes futuras da arquitetura editorial, sem páginas vazias para preenchê-las. O gabarito fica no final. As entradas do índice são clicáveis.',styles['body'])]
toc=TableOfContents();toc.levelStyles=[styles['toc0']];story += [toc,PageBreak()]
diagrams={3:'camadas',6:'vogais',9:'estrutura'}
alltext=[]
files=sorted((ROOT/'capitulos').glob('*.md'))
answer_parts=[]
for file in files:
    text=file.read_text()
    for marker in ['## Respostas comentadas', '## Respostas para conferência posterior']:
        if marker in text:
            body,answer=text.split(marker,1)
            end=''; tail='## Fonte e atribuição'
            if tail in answer:answer,end=answer.split(tail,1);end=tail+end
            answer_parts.append('## '+text.splitlines()[0].removeprefix('# ')+'\n'+answer)
            text=body+'\n'+end
            break
    if file.name.startswith('900-'):text += '\n\n'.join(answer_parts)
    alltext.append(text);lines=text.splitlines();i=0;num=int(file.name[:3]);placed=False;pending_table_title=None
    if num in (97,900,990):story.append(PageBreak())
    elif num:story.append(Spacer(1,16))
    while i<len(lines):
        s=lines[i].strip()
        if not s:i+=1;continue
        if s.startswith('# '):
            p=Paragraph(inline(s[2:]),styles['h1']);p.bookmark='cap'+str(num);story.append(p);i+=1;continue
        if s.startswith('### ') or s.startswith('## '):
            t=s.lstrip('#').strip();j=i+1
            while j<len(lines) and not lines[j].strip():j+=1
            if j<len(lines) and lines[j].strip().startswith('|'):
                pending_table_title=t
            else:story.append(Paragraph(inline(t),styles['h2']))
            i+=1;continue
        if s.startswith('|'):
            block=[]
            while i<len(lines) and (lines[i].strip().startswith('|') or not lines[i].strip()):
                row=lines[i].strip()
                if row.startswith('|'):
                    cells=[x.strip() for x in row.strip('|').split('|')]
                    if not all(re.fullmatch(r'[:\- ]+',x) for x in cells):block.append(cells)
                elif i+1>=len(lines) or not lines[i+1].strip().startswith('|'):break
                i+=1
            n=len(block[0]);width=W-68
            if 97<=num<=118:widths=[width*.41,width*.44,width*.15]
            elif n==3:widths=[width*.28,width*.35,width*.37]
            elif n==2:widths=[width*.42,width*.58]
            else:widths=[width/n]*n
            data=[[Paragraph(inline(cell),styles['headcell'] if rownum==0 else styles['cell']) for cell in row] for rownum,row in enumerate(block)]
            headrow=0
            if pending_table_title:
                data.insert(0,[Paragraph(inline(pending_table_title),styles['h2'])]+['']*(n-1));headrow=1
            table=Table(data,colWidths=widths,repeatRows=headrow+1,hAlign='LEFT')
            commands=[('BACKGROUND',(0,headrow),(-1,headrow),PALE),('LINEBELOW',(0,headrow),(-1,headrow),.7,GREEN),('LINEBELOW',(0,headrow+1),(-1,-1),.25,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]
            if headrow:commands += [('SPAN',(0,0),(-1,0)),('TOPPADDING',(0,0),(-1,0),12)]
            table.setStyle(TableStyle(commands));pending_table_title=None
            story += [table,Spacer(1,10)];continue
        if re.match(r'^\d+\. ',s) or s.startswith('- '):
            story.append(Paragraph(inline(s),styles['bullet']));i+=1;continue
        parts=[s];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|')):
            parts.append(lines[i].strip());i+=1
        content=' '.join(parts);style=styles['small'] if content.startswith('https://') else (styles['refs'] if num==30 else styles['body'])
        story.append(Paragraph(inline(content),style))
        if num in diagrams and not placed and 'objetivo' not in content.lower() and len(content)>95:
            story += [Spacer(1,4),Diagram(diagrams[num]),Spacer(1,11)];placed=True
doc.multiBuild(story)
(ROOT/'Munduruku-Extensa-Texto-Integral.md').write_text('\n\n---\n\n'.join(alltext))
(ROOT/'indice-paginas.json').write_text(json.dumps(doc.headings,ensure_ascii=False,indent=2))
print(json.dumps({'pdf':str(OUT),'capitulos':len(files),'palavras':sum(len(t.split()) for t in alltext),'paginas':doc.page},ensure_ascii=False))
