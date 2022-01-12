from tkinter import *
from tkinter import filedialog
from owlready2 import *

root = Tk()
root.wm_title('Ontological Classifier')


class Ontoclassifier:
    def __init__(self, toplevel):
        # Criação das partes da interface:
        self.fr1 = Frame(toplevel)
        self.fr2 = Frame(toplevel)
        self.fr3 = Frame(toplevel)
        self.fr4 = Frame(toplevel)
        self.fr5 = Frame(toplevel)
        self.fr6 = Frame(toplevel)
        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        self.fr4.pack()
        self.fr5.pack()
        self.fr6.pack()

        self.mainfont = ('Verdana', '11')

        # Título do software:
        self.title = Label(self.fr1, text='OntoClass')
        self.title['font'] = ('Verdana', '25', 'bold', 'underline')
        self.title.pack()
        # Texto "select ontology":
        self.selectontology = Label(self.fr2, text='Select ontology: ')
        self.selectontology['font'] = self.mainfont
        self.selectontology.pack(side=LEFT)
        # Botão para pesquisar pela ontologia no computador:
        self.openbutton = Button(self.fr2, text='Browse', command=self.browsefunc)
        self.openbutton.pack(side=LEFT)
        # Endereço da ontologia selecionada:
        self.pathlabel = Label(self.fr2, text='')
        self.pathlabel.pack(side=RIGHT)
        # Texto "Term:"
        self.labelqueryonto = Label(self.fr3, text='Term: ', font=self.mainfont)
        self.labelqueryonto.pack(side=LEFT)

        self.queryonto = Entry(self.fr3)
        self.queryonto.pack(side=LEFT)
        # Botão para adicionar termos de busca:
        self.btnaddterm = Button(self.fr3, text='Add term')
        self.btnaddterm['command'] = self.addterm
        self.btnaddterm.pack(side=LEFT)
        # Botão para pesquisar os termos na ontologia:
        self.btnquery = Button(self.fr3, text='Find class', width=10)
        self.btnquery['command'] = self.makequery
        self.btnquery.pack(side=LEFT)
        # Botão para apagar os termos de pesquisa adicionados anteriormente:
        self.btnreset = Button(self.fr3, text='Reset research')
        self.btnreset['command'] = self.resetresearch
        self.btnreset.pack(side=LEFT)
        # Texto com os resultados da pesquisa:
        self.resultstxt = Label(self.fr5, text='Results', font=self.mainfont)
        self.resultstxt.pack()

        self.resultcut = Label(self.fr5, text='')

        self.terms = []

    def resetresearch(self):  # Configuração para o "Reset research"
        self.terms = []
        self.fr6.destroy()
        self.fr5.destroy()
        self.fr4.destroy()
        self.fr4 = Frame()
        self.fr4.pack()
        self.fr5 = Frame()
        self.resultstxt = Label(self.fr5, text='Results', font=self.mainfont)
        self.resultstxt.pack()
        self.fr5.pack()
        self.fr6 = Frame()
        self.fr6.pack()

    def addterm(self): # Configuração para o "Add term"
        self.written = self.queryonto.get()
        self.useterm = self.terms.append(self.written)
        self.selectedterms = Label(self.fr4, text=self.terms[-1:])
        self.selectedterms.pack(side=LEFT)
        self.queryonto.delete(0, 'end')

    def browsefunc(self): # Configuração para selecionar arquivo da ontologia existente no PC
        self.filename = filedialog.askopenfilename(initialdir='', title='Select ontology file',
                                                   filetypes=(('OWL files', '*.owl'), ('All files', '*.')))
        self.pathlabel.config(text=self.filename)

    def makequery(self): # Configuração para realização de pesquisas na ontologia
        # As três linhas a seguir fazem com que toda vez que o botão "Find class" é apertado os resultados de pesquisas anteriores sejam apagados e reescritos.
        self.fr6.destroy()
        self.fr6 = Frame()
        self.fr6.pack()

        self.ontology = World()
        self.onto = self.ontology.get_ontology('file://' + self.filename).load() # Carregamento da ontologia selecionada pelo usuário
        self.baseiri = self.onto.base_iri  #IRI da ontologia
        self.graph = self.ontology.as_rdflib_graph()   # Construção do gráfico RDF para pesquisa em SPARQL

        self.query_parts = []  # A pesquisa em SPARQL é construída em partes, inseridas nessa lista
        self.prefix = "PREFIX ont: <%s>" % self.baseiri
        self.select_where = "SELECT ?class WHERE {"
        self.query_parts.append(self.prefix)
        self.query_parts.append(self.select_where)
        for i in self.terms:
            self.term = "ont:%s a ?class ." % str(i).replace(' ', '_')
            self.query_parts.append(self.term)
        self.closing = "}"
        self.query_parts.append(self.closing)
        self.request = "\n".join(self.query_parts)  # União de todas as partes da lista e formação da consulta em SPARQL
        self.results = list(self.graph.query(self.request))  # Resultados da consulta da ontologia usando SPARQL

        self.excludingzero = self.results[1:]  # Exclusão do primeiro resultado, pois este é sempre uma classe que existe em qualquer ontologia

        for element in self.excludingzero:  # Manipulação das strings contendo os resultados para deixá-los com leitura mais amigável para o usuário
            self.element = str(element)
            self.formating = "\n".join(self.element)
            self.hashtag = self.element.find('#')
            self.resultcut = self.element[self.hashtag + 1:-4].replace('_', ' ')
            self.realthing = Label(self.fr6, text=self.resultcut)
            self.realthing.pack()


Ontoclassifier(root)
root.mainloop()
