#SingaLun Project

The aim of the project is performing Network based analysis of omics data. Hypothesis: Topological information encoded in networks can help us to identify relevant biological / clinical information. The starting point is omics data, first we need to clean and process it, calculate centralities metris and build the network using the centralities as adjacency metrics. Afterward we want tu use these centralities metrics as features to build a predictive model using machine learning approches.  


#Codes


Clean_data.py: data cleaning

Networkx.i.ipynb: Build a patient similarity network from mRNA expression data and visualize a subpart using Networkx library

igraph.i.ipynb: Build a patient similarity network from mRNA expression data and visualize a subpart using igraph library

