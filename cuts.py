#VBF cuts                                                                                                                                                                                               


#-------------------------------------------------------------------------------                                                                                                                           
# supercut                                                                                                                                                                                                 
#-------------------------------------------------------------------------------                                                                                                                           
_tmp = [
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 13.',
     '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
     '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)',
     'detajj > 3.8',
     ]

supercut = ' && '.join(_tmp)


def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)

#-------------------------------------------------------------------------------                                                                                                                           
# VBF                                                                                                                                                                                                      
#-------------------------------------------------------------------------------                                                                                                                           
_tmp = [
     'Alt$(CleanJet_pt[1], 0) > 30.',
     'abs(CleanJet_eta[0]) < 4.7',
     'abs(CleanJet_eta[1]) < 4.7',
     #'mth < 125',
     'mjj > 300',
     #'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0',
     'bVeto',
     'Sum$(CleanJet_pt>30) >= 2 && Sum$(CleanJet_pt>30) <= 3',
     'mll > 50',
     #'log((abs(2*Lepton_eta[0]-CleanJet_eta[0]-CleanJet_eta[1])+abs(2*Lepton_eta[1]-CleanJet_eta[0]-CleanJet_eta[1]))/detajj) < 1.',
     '(CleanJet_pt[0] + CleanJet_pt[1]) > 62.5',
     ]

addcut('VBF', _tmp)


_tmp = [
     'Alt$(CleanJet_pt[1], 0) > 30.',
     'abs(CleanJet_eta[0]) < 4.7',
     'abs(CleanJet_eta[1]) < 4.7',
     'bVeto'
     ]

addcut('noCuts', _tmp)
