#########################################################################################
# Setup the basics ----> USER DEFINED SECTION HERE ------------------------------------//
fOutName = "combined_model_monojet.root"  # --> Output file
fName    = "monojet.root"  # --> input file (i.e output from previous)
#fName    = "mono-x-smoothed.root"  # --> input file (i.e output from previous)
categories = ["monojet_tag0","monojet_tag1","monojet_tag2"]
#categories = ["monox_mass0","monox_mass0_fail","monox_mass1","monox_mass1_fail","monox_mass2","monox_mass2_fail","monox_mass3","monox_mass3_fail"] # --> Should be labeled as in original config 
controlregions_def = ["Z_constraints_monojet","W_constraints_monojet","Top_constraints_monojet"] # --> configuration configs for control region fits. 
# Note if one conrol region def depends on another (i,e if setDependant() is called) it must come AFTER its 
# the one it depends on in this list!
#--------------------------------------------------------------------------------------//
#########################################################################################

# Leave the following alone!
# Headers 
#from combineControlRegions import *
from pullPlot import pullPlot
from counting_experiment import *
from convert import * 

from HiggsAnalysis.CombinedLimit.ModelTools import *

import ROOT as r 

ROOT.gSystem.AddIncludePath("-I$CMSSW_BASE/src/ ");
ROOT.gSystem.AddIncludePath("-I$ROOFITSYS/include");
#ROOT.gSystem.AddIncludePath("-I$ROOSYS/include");

ROOT.gSystem.Load("libRooFit.so")
ROOT.gSystem.Load("libRooFitCore.so")

#ROOT.gSystem.AddIncludePath("-I$ROOTSYS/include -I$ROOFITSYS/include");
#ROOT.gSystem.Load("libRooFit");

r.gROOT.SetBatch(1)
r.gROOT.ProcessLine(".L diagonalizer.cc+")
from ROOT import diagonalizer

_fOut 	   = r.TFile(fOutName,"RECREATE") 
_f 	   = r.TFile.Open(fName) 
out_ws 	   = r.RooWorkspace("combinedws") 

out_ws._import = SafeWorkspaceImporter(out_ws)

sampleType  = r.RooCategory("bin_number","Bin Number");
obs         = r.RooRealVar("observed","Observed Events bin",1)
out_ws._import(sampleType)  # Global variables for dataset
out_ws._import(obs)
diag_combined = diagonalizer(out_ws)
obsargset   = r.RooArgSet(out_ws.var("observed"),out_ws.cat("bin_number"))

cmb_categories = []

for crd,crn in enumerate(controlregions_def):
	x = __import__(crn)
        for cid,cn in enumerate(categories): 
		_fDir = _fOut.mkdir("%s_category_%s"%(crn,cn))
		cmb_categories.append(x.cmodel(cn,crn,_f,_fDir,out_ws,diag_combined))

for cid,cn in enumerate(cmb_categories):
	cn.init_channels()
        channels = cn.ret_channels()

# Save a Pre-fit snapshot
out_ws.saveSnapshot("PRE_EXT_FIT_Clean",out_ws.allVars()) 
# Now convert workspace to combine friendly workspace
convertToCombineWorkspace(out_ws,_f,categories,cmb_categories,controlregions_def)
_fOut.WriteTObject(out_ws)

print "Produced constraints model in --> ", _fOut.GetName()
