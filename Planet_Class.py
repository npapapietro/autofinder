from lxml import html
import requests

def coordinate_scrape(name):
    s = 'http://theskylive.com/'+str(name)+'-info'
    page = requests.get(s)
    tree = html.fromstring(page.content)
    coors = tree.xpath('//ar/text()')
    ra = [int(coors[0][:2]),int(coors[0][4:6]),int(coors[0][8:10])]
    dec = [int(coors[1][:3]),int(coors[1][5:7]),int(coors[1][9:11])]
    mag = [float(coors[2][:4])]
    return [ra,dec,mag]

        
class jupiter:
    def __init__(self):
        self.name = 'jupiter'
        self.mass = 1.89813e24
        self.diameter = 139822e3
        self.radius = self.diameter/2
        self.position = coordinate_scrape(self.name)
    def right_ascension(self):
        ra_exact = self.position[0][0]+self.position[0][1]/60+self.position[0][2]/3600
        return self.position[0], ra_exact
    def declination(self):
        return self.position[1]
    def magnitude(self):
        return self.position[2]
        

class saturn:
    def __init__(self):
        self.name = 'saturn'
        self.mass = 1.89813e24
        self.diameter = 139822e3
        self.radius = self.diameter/2
        self.position = coordinate_scrape(self.name)
    def right_ascension(self):
        ra_exact = self.position[0][0]+self.position[0][1]/60+self.position[0][2]/3600
        return self.position[0], ra_exact
    def declination(self):
        return self.position[1]
    def magnitude(self):
        return self.position[2]
