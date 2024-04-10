import math
import numpy as np

class playerInfo():
    
    def __init__(self,rscid):
        self.rscid = rscid
        self.gp = 0

    def newData(self,tier,gw,gl,winp,shots,ppts,goals,saves,assists,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG):
        self.tier = tier
        self.gp += 1
        self.gw = gw
        self.gl = gl
        self.winp = self.gw/self.gp
        self.shpg = [shots]
        self.ppg = [ppts]
        self.gpg = [goals]
        self.svpg = [saves]
        self.apg = [assists]
        self.papg = [PAPG]
        self.gapg = [GAPG]
        self.aapg = [AAPG]
        self.svapg = [SvAPG]
        self.shapg = [ShAPG]
        self.oppg = [OPPG]
        self.oapg = [OAPG]
        self.ogpg = [OGPG]
        self.osvpg = [OSvPG]
        self.oshpg = [OShPG]
        self.opapg = [OPAPG]
        self.ogapg = [OGAPG]
        self.oaapg = [OAAPG]
        self.osvapg = [OSvAPG]
        self.oshapg = [OShAPG]



    def appendData(self,gw,gl,winp,shots,ppts,goals,saves,assists,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG,ff = False):
        if self.gp == 0 and ff == False:
            self.newData(gp,gw,gl,winp,shots,ppts,goals,saves,assists,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG)
        elif self.gp != 0:
            self.gp += 1
            self.gw += gw
            self.gl += gl
            self.winp = self.gw/self.gp 
            self.shpg.append(shots)
            self.ppg.append(ppts)
            self.gpg.append(goals)
            self.svpg.append(saves)
            self.apg.append(assists)
            self.papg.append(PAPG)
            self.gapg.append(GAPG)
            self.aapg.append(AAPG)
            self.svapg.append(SvAPG)
            self.shapg.append(ShAPG)
            self.oppg.append(OPPG)
            self.ogpg.append(OGPG)
            self.oapg.append(OAPG)
            self.osvpg.append(OSvPG)
            self.oshpg.append(OShPG)
            self.opapg.append(OPAPG)
            self.ogapg.append(OGAPG)
            self.oaapg.append(OAAPG)
            self.osvapg.append(OSvAPG)
            self.oshapg.append(OShAPG)
        else:
            return
            
            

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

fp = open("Copy of S19 RSC 3v3 IDR - Premier - Data Import.csv", "r")
for line in fp.readlines():
    line = line.strip("\n")
    cell = line.split(",")
    RSCID[cell[0]] = playerInfo(cell[0])
    RSCID[cell[0]].appendData()
fp.close()

