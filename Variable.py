""" Variable' simple representation of the Bayesian Network"""


class Variable(object):
    # constructor with attributes
    # cpd: conditional probability distribution, num_values: domain cardinality of the variable
    def __init__(self, name, cpd=None, num_values=2):
        self.name = name
        self.value = None
        self.cpd = cpd
        self.parents = set()
        self.visited = False
        self.num_values = num_values
        self.clique = None

    # equality function for comparisons
    def __eq__(self, right):
        return self.name == right.name

    # inequality function for comparisons
    def __ne__(self, right):
        return not (self == right)

    # Implemented by the hash table data structure;every time I look for an item in a collection I call him;the method returns the hash value for the object that identifies the node (name==id)
    def __hash__(self):
        return self.name.__hash__()

    # If value is BOOLEAN return num_values that is 2(default)
    def __len__(self):
        return self.num_values

    # Return domain cardinality of the variable
    def size(self):
        return self.num_values

    def add_parent(self, parent):
        if (parent not in self.parents) and (not self == parent):
            self.parents.add(parent)

    def remove_parent(self, parent):
        self.parents.remove(parent)

    def set_cpd(self, new_distribution):
        self.cpd = new_distribution
