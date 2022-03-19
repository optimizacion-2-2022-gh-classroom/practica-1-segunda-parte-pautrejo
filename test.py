from src.bellman_ford.bellman_ford import *
import numpy as np 
import networkx as nx
import bellmanford as bf
import unittest

class Pruebas(unittest.TestCase):

    def test_val_resultado(self):
        """
        Válida resultados con el método implementado de bellman_ford vs paquete bellmanford
        https://pypi.org/project/bellmanford/
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)
        # Método implementado
        list_path, len_short_path = bf_negative_cycle_test(G)
        # Paquete bellmanford
        result = bf.bellman_ford(G, source="5", target="6")
        r = [int(x) for x in result[1]]
        self.assertTrue(list_path == r) 

    def test_val_iter(self):
        """
        Válida si el camino más corto entre s y t posee k bordes, Bellman Ford lo encontrará después de a lo sumo k iteraciones.
        Dado que un camino más corto no puede tener más de V−1 bordes, toma como mucho esa cantidad de iteraciones.
        https://codeforces.com/blog/entry/81979?locale=en
        """
        edges = [["5", "6", 0.86],
         ["6", "5", -0.94],
         ["3", "3",0],
         ["0","0",0],
         ["1","1",0],
         ["2","2",0],
         ["4","4",0]]
        
        G = nx.DiGraph()        
        G.add_weighted_edges_from(edges)
        
        n_edges = G.number_of_edges()
        n_nodes = G.number_of_nodes()
        
        path_more_short = n_nodes - 1
        
        # Método implementado
        list_path, len_short_path = bf_negative_cycle_test(G)
        
        G.add_weighted_edges_from(edges)
        
        self.assertTrue(len_short_path <= path_more_short) 
        
unittest.main(argv=[''], verbosity=2, exit=False)
