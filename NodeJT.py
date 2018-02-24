""" Use the package pbnt for the implement the table (potential) for the Nodes of Junction Tree"""
from pbnt import Distribution


class Clique(object):
    # constructor with attributes
    # variables: set of click variables, neighbors_separator: set of tuples(each tuple has neighboring clique and associated separator), num_var: domain cardinality of the clique
    def __init__(self, name, variables):
        self.name = name
        self.variables = set(variables)
        self.potential = Distribution.Potential(self.variables)
        self.visited = False
        self.neighbors_separator = set()
        self.num_var = len(self.variables)

    def add_neighbors_separator(self, neighbor, separator):
        tupla_ns = (neighbor, separator)
        if (tupla_ns not in self.neighbors_separator) and (not self == neighbor):
            self.neighbors_separator.add(tupla_ns)

    # REMEMBER: self.potential = self.potential*Pr(var|parents(var)).
    def init_potential(self, var):
        self.potential *= var.cpd

    # Return domain cardinality of the clique
    def size(self):
        return self.num_var


# ______________________________________________________________________________________________________________________

class Separator(object):
    # constructor with attributes; var: set of separator variables
    def __init__(self, name, cx, cy):
        self.name = name
        self.var = cx.variables.intersection(cy.variables)
        self.potential = Distribution.Potential(self.var)
        self.visited = False
        self.neighbors = [cx, cy]

    def reinit_potential(self):
        self.potential = Distribution.Potential(self.var)
