from datetime import date

from django.db.models import Q
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.tableofcontents import (Table, TableOfContents,
                                                TableStyle)

from .models import Term

class RapportTemplate(BaseDocTemplate):
    centered = PS(name = 'centered',fontSize = 8, leading = 0, alignment = 1, spaceAfter = 20)
    script = PS(name = 'script',fontSize = 6, leading = 2, alignment = 0, spaceAfter=5)
    h1 = PS(name = 'Heading1',fontSize = 10,leading = 12)
    h2 = PS(name = 'Heading2',fontSize = 8,leading = 14)
    h3 = PS(name = 'Heading3',fontSize = 7,leading = 16)
    story = []
    toc = TableOfContents()
    toc.levelStyles = [
        PS(fontName='Times-Bold', fontSize=10, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=10, leading=16),
        PS(fontSize=8, name='TOCHeading2', leftIndent=30, firstLineIndent=-20, spaceBefore=5, leading=12),
        PS(fontSize=3, name='TOCHeading3', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),
    ]
    story.append(toc)
    columnar_style = TableStyle(
    [
        ('BACKGROUND', (0, 0), (0,-1), colors.lightblue), # de linkerkolom van de twee heeft een afwijkende achtergrond   
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue), # de titelregel heeft een afwijkende achtergrond             
        ('GRID',(0,0),(-1,-1),0.5,colors.grey),
        ('FONTSIZE',(0,0),(-1,-1),8)
    ])

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename) # , kw)
        template = PageTemplate('normal', [Frame(1*cm, 1*cm, 17.5*cm, 26.5*cm, id='F1')])
        self.addPageTemplates(template)
        #tableTemplate = PageTemplate('table', [Frame(2*cm, 2*cm, 15.5*cm, 25.5*cm, id='F1')])
        #self.addPageTemplates(tableTemplate)

    ''' 
    Entries to the table of contents can be done either manually by
    calling the addEntry method on the TableOfContents object or automatically
    by sending a 'TOCEntry' notification in the afterFlowable method of
    the DocTemplate you are using. The data to be passed to notify is a list
    of three or four items countaining a level number, the entry text, the page
    number and an optional destination key which the entry should point to.
    This list will usually be created in a document template's method like
    afterFlowable(), making notification calls using the notify() method
    with appropriate data
    '''

    def afterFlowable(self, flowable):
        # "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1':
                level = 0
            elif style == 'Heading2':
                level = 1
            else:
                return
            E = [level, text, self.page]
            #if we have a bookmark name append that to our notify data
            bn = getattr(flowable,'_bookmarkName',None)
            if bn is not None: E.append(bn)
            self.notify('TOCEntry', tuple(E))       
  
    def apply_style(self, tabel,data,fontsize):
        ''' zorgt voor een algemene MN opmaak-stijl '''
        mn_style1 = TableStyle(
            [
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue), # de titelregel heeft een afwijkende achtergrond   
                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                ('FONTSIZE',(0,0),(-1,-1),fontsize)
            ])
        tabel.setStyle(mn_style1)     
        tabel.hAlign = 'LEFT' 
        for each in range(1,len(data)):
            if each % 2 == 0:
                bg_color = colors.whitesmoke
            else:
                bg_color = colors.lightgrey
            tabel.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))      

    def doHeading(self,text,sty):
        from hashlib import sha1
        #create bookmarkname
        bmn = str(text)
        bmn += str(sty.name)
        bn=sha1(bmn.encode("utf-8")).hexdigest()
        #modify paragraph text to include an anchor point with name bn
        h=Paragraph(text+'<a name="%s"/>' % bn,sty)
        #store the bookmark name on the flowable so afterFlowable can see this
        h._bookmarkName=bn
        self.story.append(h)

    def termSectie(self, query_set): 
        # rapporteer volgens bovenstaande structuur 
        for term in query_set: 
            self.doHeading('Term: {}'.format(term.naam),self.h1)
            
            # for schemaName, schema  in schemas.items(): 
            #     self.doHeading('Schema: {}'.format(schemaName),self.h2)
            #     for tName,tabel in schema.items().filter(truncate=False):
            #         self.doHeading('Tabel: {}'.format(tName),self.h3)
            #         headertable = Table(tabel.data_pdf())
            #         headertable.setStyle(self.columnar_style)
            #         headertable.hAlign = 'LEFT' 
            #         self.story.append(headertable)
            #         self.story.append(Spacer(0,20))
            #         self.doHeading('Aan tabel {} gekoppelde kolommen'.format(tabel.naam),self.h3) 
            #         data = tabel.kolom_data_pdf()
            #         table = Table(data) 
            #         self.apply_style(table,data,6)
            #         self.story.append(table)
            #         self.story.append(Spacer(0,20))
            #     self.story.append(PageBreak())
            self.story.append(PageBreak())

    def buildReport(self, query_set): 
        ''' build the actual report '''
        # self.persoonsgegevensSectie(query_set)
        self.termSectie(query_set)
        self.multiBuild(self.story)
