import warnings

from tactics2d.map_base.node import Node
from tactics2d.map_base.roadline import RoadLine
from tactics2d.map_base.lane import Lane
from tactics2d.map_base.area import Area
from tactics2d.map_base.regulatory import RegulatoryElement


class Map(object):
    def __init__(
        self, name: str = None, scenario_type: str = None, country: str = None
    ):

        self.name = name
        self.scenario_type = scenario_type
        self.country = country

        self.visible_area = [[-1e9, 1e9], [-1e9, 1e9]]

        self.ids = set()
        self.nodes = dict()
        self.lanes = dict()
        self.areas = dict()
        self.roadlines = dict()
        self.regulations = dict()
        self.customs = dict()
        self.boundary = None

    def add_node(self, node: Node):
        if node.id in self.ids:
            if node.id in self.nodes:
                warnings.warn("Node %s already exists! Replacing the node with new data." % node.id)
            else:
                raise ValueError()
        self.nodes[node.id] = node

    def add_roadline(self, roadline: RoadLine):
        if roadline.id in self.ids:
            if roadline.id in self.roadlines:
                warnings.warn("Roadline %s already exists! Replacing the roadline with new data." % roadline.id)
            else:
                raise ValueError()
        self.roadlines[roadline.id] = roadline

    def add_lane(self, lane: Lane):
        if lane.id in self.ids:
            if lane.id in self.lanes:
                warnings.warn("Lane %s already exists! Replacing the lane with new data." % lane.id)
            else:
                raise ValueError()
        self.lanes[lane.id] = lane

    def add_area(self, area: Area):
        if area.id in self.ids:
            if area.id in self.areas:
                warnings.warn("Area %s already exists! Replacing the area with new data." % area.id)
            else:
                raise ValueError()
        self.areas[area.id] = area

    def add_regulatory(self, regulatory: RegulatoryElement):
        if regulatory.id in self.ids:
            if regulatory.id in self.regulations:
                warnings.warn()
            else:
                raise ValueError()
        self.regulations[regulatory.id] = regulatory

    def get_boundary(self):
        return self.boundary