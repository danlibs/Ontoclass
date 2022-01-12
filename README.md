# OntoClass
The Ontological Classifier (OntoClass for short) is a software designed to help reduce the subjective factor inherent to records classification. It uses OWL ontologies to link easy to remember characteristics of the documents (e.g. "image", "photograph", "news", "interview" etc.) to its actual class in the classification scheme.

By now, it's just a prototype, so in order to use it, you need to have Python and the modules Tkinter and rdfLib installed.

## How to test
In the Extras folder, there are two files: one is the published article about the OntoClass, which you can read for more details of the project (it is written in Portuguese); the other is an ontology that can be used to test the software.

This is the OntoClass:

![](https://github.com/danlibs/Ontoclass/blob/main/Images/Ontoclass.png) 

To use it, just click "Browse" and select the example ontology or whatever ontology you made based on the instructions in the published article. Then, you can write any terms that apply to a certain document, click "Add term" and "Find class". The list of available terms to the example ontology is the following:

![](https://github.com/danlibs/Ontoclass/blob/main/Images/Terms.png) 

In the results area, the result of the most suited class for the document is shown:

![](https://github.com/danlibs/Ontoclass/blob/main/Images/Results.png) 

## How it works
The classification scheme used to create the example ontology is fictional and was created based on real documents about UFOs. Those documents were analyzed and some of their characteristics were taken to develop the terms list seem above. This is the hierarchy view of the ontology:

![](https://github.com/danlibs/Ontoclass/blob/main/Images/Ontology%20hierarchy.png) 

And this is the classification scheme created and transformed into the classes of the ontology:

![](https://github.com/danlibs/Ontoclass/blob/main/Images/Ontology%20classes.png) 

Basically, the ontology has the records classes as its classes and the instances of the classes are the terms listed before. Any ontology developed in this format can be used in OntoClass. So, in short: 

 - The documents are classified according to a classification scheme. The classes of the classification scheme are the classes of the ontology;
 - These documents have characteristics, like their type, genre, format etc. The terms list are based on these characteristics. The terms are the instances of the classes of the ontology, put there according to the real characteristics of the documents of certain classes.
 
