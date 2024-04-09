import math
import numpy as np

class playerInfo():
    
    def __init__(self,rscid):
        self.rscid = rscid
        self.gp = 0

    def newData(self,tier,gp,gw,gl,winp,shots,ppts):
        self.tier = tier
        self.gp = gp
        self.gw = gw
        self.gl = gl
        self.winp = self.gw/self.gw
        self.shots = shots
        self.points = ppts

    def appendData(self,gp,gw,gl,winp,shotp,PPG,GPG,APG,SvPG,ShPG,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG):
        if self.gp != 0:
            self.newData(gp,gw,gl,winp,shotp,PPG,GPG,APG,SvPG,ShPG,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG)
        else:
            

    def forIndex(self):
        self.pfi = self.ppg/self.opapg
        self.gfi = self.gpg/self.ogapg
        self.afi = self.apg/self.oaapg
        self.svfi = self.svpg/self.osvapg
        self.shfi = self.shpg/self.oshapg
    
    def againstIndex(self):
        self.pai = self.papg/self.oppg
        self.gai = self.gapg/self.ogpg
        self.aai = self.aapg/self.oapg
        self.svai = self.svapg/self.osvpg
        self.shai = self.shapg/self.oshpg


RSCID = {}

