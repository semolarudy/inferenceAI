from JTree import *
from NodeJT import *
from Variable import *
import numpy as np


def built_xyz_node():
    """ Built Nodes for XYZ Bayes Network, return a list of cliques for the Junction Tree XYZ"""
    # <<<<<<<<<<Built variables>>>>>>>>>>
    # X
    x = Variable("X")
    x_cpd = Distribution.DiscreteDistribution(x)
    index1 = x_cpd.generate_index([], [])
    x_cpd[index1] = [0.25, 0.75]
    x.set_cpd(x_cpd)
    # Y
    y = Variable("Y")
    y_table = np.zeros([x.size(), y.size()], dtype=np.float32)
    y_table[0,] = [0.1, 0.9]
    y_table[1,] = [0.99, 0.01]
    y_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[x, y], table=y_table)
    y.set_cpd(y_cpd)
    # Z
    z = Variable("Z")
    z_table = np.zeros([x.size(), z.size()], dtype=np.float32)
    z_table[0,] = [0.5, 0.5]
    z_table[1,] = [0.98, 0.02]
    z_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[x, z], table=z_table)
    z.set_cpd(z_cpd)
    # Set parents
    y.add_parent(x)
    z.add_parent(x)

    # <<<<<<<<<<Built cliques and separator>>>>>>>>>>
    # XZ
    clique_XZ = Clique("XZ", [x, z])
    clique_XY = Clique("XY", [x, y])
    sep_X = Separator("X", clique_XZ, clique_XY)
    # Add neighbour and separator in all cliques
    clique_XZ.add_neighbors_separator(clique_XY, sep_X)
    clique_XY.add_neighbors_separator(clique_XZ, sep_X)

    clique_list = [clique_XZ, clique_XY]
    return clique_list


def jt_xyz_built():
    """ Create and return a Junction Tree XYZ"""
    clique_list = built_xyz_node()
    jt_xyz = JunctionTree("JUNCTION TREE XYZ", clique_list)
    return jt_xyz


" ______________________________________________________________________________________________________________________ "


def built_c_node():
    """ Built Nodes for C Bayes Network, return a list of cliques for the Junction Tree C"""
    # <<<<<<<<<<Built variables>>>>>>>>>>
    # c1
    c1 = Variable("c1")
    c1_cpd = Distribution.DiscreteDistribution(c1)
    index1 = c1_cpd.generate_index([], [])
    c1_cpd[index1] = [0.5, 0.5]
    c1.set_cpd(c1_cpd)
    # c2
    c2 = Variable("c2")
    c2_table = np.zeros([c1.size(), c2.size()], dtype=np.float32)
    c2_table[0,] = [0.25, 0.75]
    c2_table[1,] = [0.1, 0.9]
    c2_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[c1, c2], table=c2_table)
    c2.set_cpd(c2_cpd)
    # c3
    c3 = Variable("c3")
    c3_table = np.zeros([c1.size(), c3.size()], dtype=np.float32)
    c3_table[0,] = [0.1, 0.9]
    c3_table[1,] = [0.99, 0.01]
    c3_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[c1, c3], table=c3_table)
    c3.set_cpd(c3_cpd)
    # c4
    c4 = Variable("c4")
    c4_table = np.zeros([c1.size(), c4.size()], dtype=np.float32)
    c4_table[0,] = [0.2, 0.8]
    c4_table[1,] = [0.02, 0.98]
    c4_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[c1, c4], table=c4_table)
    c4.set_cpd(c4_cpd)
    # c5
    c5 = Variable("c5")
    c5_table = np.zeros([c2.size(), c5.size()], dtype=np.float32)
    c5_table[0,] = [0.05, 0.95]
    c5_table[1,] = [0.15, 0.85]
    c5_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[c2, c5], table=c5_table)
    c5.set_cpd(c5_cpd)
    # c6
    c6 = Variable("c6")
    c6_table = np.zeros([c3.size(), c6.size()], dtype=np.float32)
    c6_table[0,] = [0.3, 0.7]
    c6_table[1,] = [0.98, 0.02]
    c6_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[c3, c6], table=c6_table)
    c6.set_cpd(c6_cpd)
    # Set parents
    c2.add_parent(c1)
    c3.add_parent(c1)
    c4.add_parent(c1)
    c5.add_parent(c2)
    c6.add_parent(c3)

    # <<<<<<<<<<Built cliques and separator>>>>>>>>>>
    clique_c1c4 = Clique("c1c4", [c1, c4])
    clique_c1c2 = Clique("c1c2", [c1, c2])
    clique_c1c3 = Clique("c1c3", [c1, c3])
    clique_c2c5 = Clique("c2c5", [c2, c5])
    clique_c3c6 = Clique("c3c6", [c3, c6])
    sep_c1 = Separator("c1", clique_c1c4, clique_c1c2)
    sep_c11 = Separator("c11", clique_c1c4, clique_c1c3)
    sep_c2 = Separator("c2", clique_c1c2, clique_c2c5)
    sep_c3 = Separator("c3", clique_c1c3, clique_c3c6)
    # Add neighbour and separator in all cliques
    clique_c1c4.add_neighbors_separator(clique_c1c2, sep_c1)
    clique_c1c4.add_neighbors_separator(clique_c1c3, sep_c11)
    clique_c1c2.add_neighbors_separator(clique_c1c4, sep_c1)
    clique_c1c3.add_neighbors_separator(clique_c1c4, sep_c11)
    clique_c1c2.add_neighbors_separator(clique_c2c5, sep_c2)
    clique_c2c5.add_neighbors_separator(clique_c1c2, sep_c2)
    clique_c1c3.add_neighbors_separator(clique_c3c6, sep_c3)
    clique_c3c6.add_neighbors_separator(clique_c1c3, sep_c3)

    clique_list = [clique_c1c2, clique_c1c3, clique_c3c6, clique_c2c5, clique_c1c4]
    return clique_list


def jt_c_built():
    """ Create and return a Junction Tree C"""
    clique_list = built_c_node()
    jt_c = JunctionTree("JUNCTION TREE C", clique_list)
    return jt_c


" ______________________________________________________________________________________________________________________ "


def built_fire_node():
    """ Built Nodes for FIRE Bayes Network, return a list of cliques for the Junction Tree FIRE (found in the Hugin package program)"""
    # <<<<<<<<<<Built variables>>>>>>>>>>
    # Fire
    fire = Variable("Fire")
    fire_cpd = Distribution.DiscreteDistribution(fire)
    index1 = fire_cpd.generate_index([], [])
    fire_cpd[index1] = [0.99, 0.01]
    fire.set_cpd(fire_cpd)
    # Tampering
    tampering = Variable("Tampering")
    tampering_cpd = Distribution.DiscreteDistribution(tampering)
    index2 = tampering_cpd.generate_index([], [])
    tampering_cpd[index2] = [0.98, 0.02]
    tampering.set_cpd(tampering_cpd)
    # Smoke
    smoke = Variable("Smoke")
    smoke_table = np.zeros([fire.size(), smoke.size()], dtype=np.float32)
    smoke_table[0,] = [0.99, 0.01]
    smoke_table[1,] = [0.1, 0.9]
    smoke_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[fire, smoke], table=smoke_table)
    smoke.set_cpd(smoke_cpd)
    # Alarm
    alarm = Variable("Alarm")
    alarm_table = np.zeros([fire.size(), tampering.size(), alarm.size()], dtype=np.float32)
    alarm_table[0, 0,] = [0.9999, 0.0001]
    alarm_table[1, 0,] = [0.01, 0.99]
    alarm_table[0, 1,] = [0.15, 0.85]
    alarm_table[1, 1,] = [0.5, 0.5]
    alarm_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[fire, tampering, alarm], table=alarm_table)
    alarm.set_cpd(alarm_cpd)
    # Leaving
    leaving = Variable("Leaving")
    leaving_table = np.zeros([alarm.size(), leaving.size()], dtype=np.float32)
    leaving_table[0,] = [0.999, 0.001]
    leaving_table[1,] = [0.12, 0.88]
    leaving_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[alarm, leaving], table=leaving_table)
    leaving.set_cpd(leaving_cpd)
    # Report
    report = Variable("Report")
    report_table = np.zeros([leaving.size(), report.size()], dtype=np.float32)
    report_table[0,] = [0.99, 0.01]
    report_table[1,] = [0.25, 0.75]
    report_cpd = Distribution.ConditionalDiscreteDistribution(nodes=[leaving, report], table=report_table)
    report.set_cpd(report_cpd)
    # Set parents
    smoke.add_parent(fire)
    alarm.add_parent(fire)
    alarm.add_parent(tampering)
    leaving.add_parent(alarm)
    report.add_parent(leaving)

    # <<<<<<<<<<Built cliques and separator>>>>>>>>>>
    # LA
    clique_LA = Clique("LA", [leaving, alarm])
    # AFT
    clique_AFT = Clique("AFT", [alarm, fire, tampering])
    # LR
    clique_LR = Clique("LR", [leaving, report])
    # FS
    clique_FS = Clique("FS", [fire, smoke])
    # A
    sep_A = Separator("A", clique_LA, clique_AFT)
    # L
    sep_L = Separator("L", clique_LA, clique_LR)
    # F
    sep_F = Separator("F", clique_AFT, clique_FS)
    # Add neighbour and separator in all cliques
    clique_LA.add_neighbors_separator(clique_AFT, sep_A)
    clique_LA.add_neighbors_separator(clique_LR, sep_L)
    clique_AFT.add_neighbors_separator(clique_FS, sep_F)
    clique_AFT.add_neighbors_separator(clique_LA, sep_A)
    clique_LR.add_neighbors_separator(clique_LA, sep_L)
    clique_FS.add_neighbors_separator(clique_AFT, sep_F)

    clique_list = [clique_AFT, clique_FS, clique_LA, clique_LR]
    return clique_list


def built_jt_fire():
    """ Create and return a Junction Tree FIRE"""
    clique_list = built_fire_node()
    jt_fire = JunctionTree("JUNCTION TREE FIRE", clique_list)
    return jt_fire


" ______________________________________________________________________________________________________________________ "
" ______________________________________________________________________________________________________________________ "


class HuginClass(object):
    """ Engine class of probabilistic inference, it is also the interface to access Junction Tree.
        - Makes the Junction Tree initialized and consistent,
        - takes the evidence of variable and propagates it with Hugin Alg,
        - calculates the marginal probabilities of the variables of the network. """

    # constructor with attributes
    def __init__(self, jt):
        self.jt = jt
        ev_list = []
        for clique in jt.cliques:
            for var in clique.variables:
                if not var.visited:
                    ev_list.append(var)
                    var.visited = True
        self.evidence = ev_list

    # Basic step if the junction tree isn't initialized and consistency
    def set_consistency_jt(self, name_root=None):
        self.jt.init_table_clique()
        self.jt.consistency_jt(name_root)
        print "Choose root:", self.jt.root.name

    # Takes in evidence and propagates it with HUGIN ALG
    def enter_evidence(self, name, ev):
        if not self.jt.initialize:
            self.set_consistency_jt()
        # Find variable and assign evidence
        self.jt.set_var_visited(False)
        for v in self.evidence:
            if v.name == name:
                v.value = ev
                v.visited = True
                break
        # Update table(potential) of clique with new evidence,used vector finding: multiply the clique'table containing variable with evidence for the vector finding.(nodes==variables)
        entry = False
        for cl in self.jt.cliques:
            for var in cl.variables:
                if (var.value is not None) and (var.visited is True) and (entry is False):
                    finding = Distribution.Potential(cl.potential.nodes, default=0)
                    index = finding.generate_index_node([var.value], [var])
                    finding[index] = 1
                    cl.potential *= finding
                    entry = True
                    # Spread the inference
                    self.hugin_alg()

    # HUGIN ALG:
    def hugin_alg(self):
        # 1: set random root(done before)
        print "Choose root:", self.jt.root.name
        # 2: exec collect evidence
        self.jt.set_visited(False)
        self.jt.collect_evidence(None, self.jt.root, None, True)
        # 3: exec the distribute evidence
        self.jt.set_visited(False)
        self.jt.distribute_evidence(self.jt.root)
        # normalization (Doesn't care with prob(evidence)=1)

    # Calculate Pr(variable)
    def get_prob(self, var):
        pr = None
        for cl in self.jt.cliques:
            for v in cl.variables:
                if (v.name == var.name) and (var.parents.issubset(cl.variables)) and (var.clique == cl):
                    pr = Distribution.marginal(v)[0]
                    index = pr.generate_index([True], range(pr.nDims))
                    break
        return pr[index]

    # Calculate for all variable of Bayes network the probability
    def get_all_prob(self):
        if not self.jt.initialize:
            self.set_consistency_jt()
        self.jt.set_var_visited(False)
        for cl in self.jt.cliques:
            for v in cl.variables:
                if (not v.visited) and (v.parents.issubset(cl.variables)) and (v.clique == cl):
                    pr = Distribution.marginal(v)[0]
                    index = pr.generate_index([True], range(pr.nDims))
                    v.visited = True
                    print v.name, "->", v.value, ">>>>>", "Probability=", pr[index]
