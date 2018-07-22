# From http://code.activestate.com/recipes/215912-union-find-data-structure/

class UnionFind(object):
    def __init__(self):
        self.weight = {}
        self.parent = {}
        self.num_to_obj = {}
        self.obj_to_num = {}
        self.__repr__ = self.__str__
        self.cardinality = 0

    def addNodes(self, node_list):
        for obj in node_list:
            self.find(obj)

    def find(self,object):
        if not object in self.obj_to_num:
            j = len(self.obj_to_num)
            self.weight[j] = 1
            self.obj_to_num[object] = j
            self.num_to_obj[j] = object
            self.parent[j] = j
            self.cardinality +=1
            return object
        stk = [self.obj_to_num[object]]
        this_parent = self.parent[stk[-1]]
        while this_parent != stk[-1]:
            stk.append(this_parent)
            this_parent = self.parent[this_parent]
        for i in stk:
            self.parent[i] = this_parent
        return self.num_to_obj[this_parent]

    def union(self,o1,o2):        
        o1p = self.find(o1)
        o2p = self.find(o2)
        if o1p != o2p:
            self.cardinality -= 1
            on1 = self.obj_to_num[o1p]
            on2 = self.obj_to_num[o2p]
            w1 = self.weight[on1]
            w2 = self.weight[on2]
            if w1 < w2:
                o1p, o2p, on1, on2, w1, w2 = o2p, o1p, on2, on1, w2, w1
            self.weight[on1] = w1+w2
            del self.weight[on2]
            
            self.parent[on2] = on1
    