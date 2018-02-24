""" To propagate inference in Bayesian networks we use a exact algorithm in a particular tree.
    Junction Tree class:
    - makes it the initialized and consistent,
    - choose the root node(even randomly),
    - collect evidence and distribute evidence,
    - implements absorption"""
import numpy as np
import copy


class JunctionTree(object):
    # constructor with attributes
    def __init__(self, name, list_cliques):
        self.name = name
        self.cliques = set(list_cliques)
        self.root = None
        self.initialize = False

    # Allocation of tables:
    # For each variables,choose a clique C of the junction tree containing {parents(A) union with A}
    # (table of C)*Pr(var|parents(var)): this updated table becomes the new table of C,exec by cl.init_potential(var)
    def init_table_clique(self):
        self.set_var_visited(False)
        for cl in self.cliques:
            for var in cl.variables:
                if (var.parents.issubset(cl.variables)) and (var.visited is False):
                    var.clique = cl
                    cl.init_potential(var)
                    var.visited = True

    # Determine randomly or chooses the root,generating the parent/child hierarchies.
    # For inference propagation execution it is used as first step of the Hugin Alg.
    def set_root(self, name=None):
        # To compare with Hugin application and get same results, some evidence wants a specific root
        if name is not None:
            for cl in self.cliques:
                if name == cl.name:
                    self.root = cl
        # Random root
        else:
            num = np.random.randint(0, len(self.cliques))
            list_temp = []
            for clique in self.cliques:
                list_temp.append(clique)
            self.root = list_temp[num]
            # new set cliques with root
            self.cliques.clear()
            self.cliques.add(self.root)
            for cl in list_temp:
                if cl.name != self.root.name:
                    self.cliques.add(cl)

    # function to pass messages; get the Junction Tree consistency
    def consistency_jt(self, name=None):
        # set random root
        self.set_root(name)
        # functions for abortion; get junction tree consistency
        self.set_visited(False)
        self.collect_evidence(None, self.root, None, True)
        self.set_visited(False)
        self.distribute_evidence(self.root)
        # Now the junction tree is initialized
        self.initialize = True

    # This function send messages from the outer clique toward a root, references DFS search of the tree, only visiting unvisited cliques
    # pc: previous clique, cc:clique present, sepset: separator of pc and cc, send: BOOLEAN
    def collect_evidence(self, pc, cc, sepset, send):
        cc.visited = True
        for (neighbor, sep) in cc.neighbors_separator:
            if not neighbor.visited:
                self.collect_evidence(cc, neighbor, sep, False)
        if not send:
            self.pass_message(cc, pc, sepset)

    # This function send messages from root out toward leaf clique, references DFS search of the tree
    def distribute_evidence(self, clique):
        clique.visited = True
        for (neighbor, sep) in clique.neighbors_separator:
            if not neighbor.visited:
                self.pass_message(clique, neighbor, sep)
                # DFS recursion
                self.distribute_evidence(neighbor)

    # ------------------------------------Step the message(ABSORPTION algorithm 1 2 3)------------------------------------
    # 1: calculate the new separator table with the marginalization;
    # 2: calculate the new clique table(under a security condition with function project;get old and new separator table);
    # 3: memorize the new table of the separator.
    # --------------------------------------------------------------------------------------------------------------------
    def pass_message(self, from_clique, to_clique, sep):
        old_sepset_potential = self.project(from_clique, sep)
        self.absorption(to_clique, sep, old_sepset_potential)

    # Project the from_cluster(clique) into the sepset(sep), old_sepset_potential is the sepset's potential before it is affected by the internals of project
    def project(self, clique, sep):
        old_sepset_potential = copy.deepcopy(sep.potential)
        sep.potential = clique.potential.marginalize(sep.potential)
        return old_sepset_potential

    # Absorb the sepset(sep) into the to_cluster(clique)
    # wherever sep.potential.table is 0,old_potential is guaranteed to be fix it so that we don't divide by 0
    def absorption(self, clique, sep, old_potential):
        old_potential[repr(sep.potential.table == 0)] = 1
        sep.potential /= old_potential
        clique.potential *= sep.potential

    # Utilities functions:
    # UF1
    def set_visited(self, visit=False):
        for c in self.cliques:
            c.visited = visit

    # UF2
    def set_var_visited(self, visit=False):
        for clique in self.cliques:
            for var in clique.variables:
                var.visited = visit

    # UF3
    def get_var_cluster(self, name):
        for cl in self.cliques:
            for var in cl.variables:
                if var.name == name:
                    return var
        print "FAILURE SEARCH"
