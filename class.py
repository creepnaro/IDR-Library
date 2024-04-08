import math

class playerInfo():
    
    def __init__(self,rscid,tier,gp,gw,gl,winp,shotp,PPG,GPG,APG,SvPG,ShPG,PAPG,GAPG,AAPG,SvAPG,ShAPG,OPPG,OGPG,OAPG,OSvPG,OShPG,OPAPG,OGAPG,OAAPG,OSvAPG,OShAPG):
        self.rscid = rscid
        self.tier = tier
        self.gp = gp
        self.gw = gw
        self.gl = gl
        self.winp = winp
        self.shotp = shotp
        self.ppg = PPG
        self.gpg = GPG
        self.apg = APG
        self.svpg = SvPG
        self.shpg = ShPG
        self.papg = PAPG
        self.gapg = GAPG
        self.aapg = AAPG
        self.svapg = SvAPG
        self.shapg = ShAPG
        self.oppg = OPPG
        self.ogpg = OGPG
        self.oapg = OAPG
        self.osvpg = OSvPG
        self.oshpg = OShPG
        self.opapg = OPAPG
        self.ogapg = OGAPG
        self.oaapg = OAAPG
        self.osvapg = OSvAPG
        self.oshapg = OShAPG

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
