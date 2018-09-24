def get_neighbors(self, val):
        """
        """
        if val in self.graph:
            return self.graph[val]
        else:
            raise Exception

def depth_first(self, start_vert):
        """This will traverse a graph
        """
        vert_list = []
        def _walk(vert):
            vert_relations = self.get_neighbors(vert)
            vert_list.append(vert)
            for relation in vert_relations:
                if relation not in vert_list:
                    _walk(relation)
        _walk(start_vert)
        return vert_list