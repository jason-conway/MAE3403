import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL_2D_class import gl2D, gl2DText, gl2DCircle

class Node:
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None

class Link:
    def __init__(self):
        self.name = None
        self.node1name = None
        self.node2name = None
        self.node1 = None
        self.node2 = None
        self.length = None
        self.angle = None

class Truss:
    def __init__(self, ):
        self.title = None
        self.Sut = None
        self.Sy = None
        self.E = None
        self.FSstatic = None
        self.nodes = []
        self.links = []
        self.drawingsize = None
        self.longest = 0
        self.longestLink = None

    def ReadTrussData(self, data):

        for line in data: #loop over all the lines
            cells=line.strip().split(',')
            keyword=cells[0].lower()

            if keyword == 'title': self.title = cells[1].replace("'", "")
            if keyword == 'material':
                self.Sut = float(cells[1])
                self.Sy = float(cells[2])
                self.E = float(cells[3])
            if keyword == 'static_factor': self.FSstatic = float(cells[1])
            if keyword == 'node':
                thisnode = Node()
                thisnode.name = cells[1].strip()
                thisnode.x = float(cells[2].strip())
                thisnode.y = float(cells[3].strip())
                self.nodes.append(thisnode)

            if keyword == 'link':
                thislink = Link()
                thislink.name = cells[1].strip()
                thislink.node1name = cells[2].strip()
                thislink.node2name = cells[3].strip()
                self.links.append(thislink)

        self.UpdateLinks()

    def UpdateLinks(self):

        for link in self.links:
            for node in self.nodes:
                if node.name == link.node1name:
                    link.node1 = node
                if node.name == link.node2name:
                    link.node2 = node

        self.longest = 0
        self.longestLink = None
        for link in self.links:
            x1 = link.node1.x
            y1 = link.node1.y
            x2 = link.node2.x
            y2 = link.node2.y
            link.length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            link.angle = np.arctan2((y2-y1),(x2-x1))

            if link.length > self.longest:
                self.longest = link.length
                self.longestLink = link

        # loop over all the nodes to estimate the drawing size
        xmin,xmax,ymin,ymax = (1e12,-1e12,1e12,-1e12)
        for node in self.nodes:
            if node.x < xmin: xmin = node.x
            if node.x > xmax: xmax = node.x
            if node.y < ymin: ymin = node.y
            if node.y > ymax: ymax = node.y
        self.drawingsize = [xmin, xmax, ymin, ymax]

    def GenerateReport(self):

        report = '                      Truss Design Report \n'
        report += '\nTitle: {}\n'.format(self.title)
        report += '\nStatic Factor of Safety: {:6.2f}'.format(self.FSstatic)
        report += '\nUltimate Strength: {:9.1f}'.format(self.Sut)
        report += '\nYield Strength: {:9.1f}'.format(self.Sy)
        report += '\nModulus of Elasticity: {:6.1f}'.format(self.E)

        report += '\n\n'
        report += '--------------------- Link Summary ---------------------\n'
        report += '\nLink\t(1)\t(2)\t Length\t      Angle\n'
        for link in self.links:
            report += '{:6}\t{:7}\t{:7}\t'.format(link.name, link.node1name, link.node2name)
            report += '{:7.2f}\t'.format(link.length)
            report += '{:10.2f} \n'.format(link.angle)
        report += '\n\n'
        return report

    def DrawTrussPicture(self):

        # draw the links
        glColor3f(0,1,0)
        glLineWidth(1.5)
        for link in self.links:
            glBegin(GL_LINE_STRIP) # begin drawing connected lines
            glVertex2f(link.node1.x, link.node1.y)
            glVertex2f(link.node2.x, link.node2.y)
            glEnd()

        # draw the nodes
        radius = (self.drawingsize[1]-self.drawingsize[0])/60 #just picked to look nice, radius can be any value

        glColor3f(0.8,1,0.8)
        glLineWidth(0.1)


        for node in self.nodes:
            glColor3f(0.8, 1, 0.8)
            gl2DCircle(node.x, node.y, radius, fill=True)
            glColor3f(0, 0, 0)
            gl2DText(node.name, node.x, node.y)

        # Write the names of the contributors
        [xmin, xmax, ymin, ymax] = self.drawingsize
        dx = xmax - xmin
        dy = ymax - ymin
        xmin -= 0.05 * dx
        ymin -= 0.05 * dy
        xmax += 0.05 * dx
        ymax += 0.05 * dy

        xavg = (xmax - xmin) / 2.8

        glColor3f(1, 1, 1)
        gl2DText('Jason Conway', xavg, ymax - 0.15 * dy)
        gl2DText('Abdalrahman (Mann) Mansy', xavg, ymax - 0.25 * dy)
        gl2DText('Malorie Travis', xavg, ymax - 0.35 * dy)