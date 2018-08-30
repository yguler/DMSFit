# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis

# Define each of the categories in a dictionary of the following form .. 
#	'name' : the category name 
#	'in_file_name' : input ntuple file for this category 
#	'cutstring': add simple cutrstring, applicable to ALL regions in this category (eg mvamet > 200)
#	'varstring': the main variable to be fit in this category (eg mvamet), must be named as the branch in the ntuples
#	'weightname': name of the weight variable 
#	'bins': binning given as a python list
#	'additionalvars': list additional variables to be histogrammed by the first stage, give as a list of lists, each list element 
#			  as ['variablename',nbins,min,max]
#	'pdfmodel': integer --> N/A  redudant for now unless we move back to parameteric fitting estimates
# 	'samples' : define tree->region/process map given as a dictionary with each entry as follows 
#		TreeName : ['region','process',isMC,isSignal] --> Note isSignal means DM/Higgs etc for signal region but Z-jets/W-jets for the di/single-muon regions !!!
#  OPTIONAL --> 'extra_cuts': additional cuts maybe specific to this control region (eg ptpho cuts) if this key is missing, the code will not complain   

# Can define anything useful here outside the catefory dictionary which may be common to several categories, eg binning in MET, systematics ecc
# systematics will expect samples with sample_sys_Up/Down but will skip if not found 

bins = [250.0, 280.0, 310.0, 340.0, 370.0, 400.0, 430.0, 470.0, 510.0, 550.0, 590.0, 640.0, 690.0, 740.0, 790.0, 840.0, 900.0, 960.0, 1020.0, 1090.0, 1160.0, 1250.0]
systematics=["btag","mistag"]
monojet_category = {}
out_file_name = 'monojet.root'
categories = []

for s in ['0tag','1tag', '2tag']:
     monojet_category[s] = {
        'name':"monojet_"+s
        #,'in_file_name':"/uscms_data/d1/shoh/panda/v_8029_DarkHiggs_v2/flat/limits/fittingForest_monojet_"+s+".root"
        ,'in_file_name':"/uscms/home/naina25/nobackup/Panda_2018/Panda_Analysis/CMSSW_8_0_29/src/PandaAnalysis/SuperMonoJet/fitting/fittingForest_monojet_"+s+".root"
        ,"cutstring":""
        ,"varstring":["min(999.9999,met)",250,1250]
        ,"weightname":"weight"
        ,"bins":bins[:]
        ,"additionalvars":[]
        ,"pdfmodel":0
	,"samples":
             {  
		  # Signal Region
#		   "VH_signal"    	       :['signal'+s,'vh',1,0]
		  "Zvv_signal"    	       :['signal'+s,'zjets',1,0]
                  ,"Zll_signal"	               :['signal'+s,'zll',1,0]
 		  ,"Wlv_signal"  	       :['signal'+s,'wjets',1,0]
		  ,"Diboson_signal"  	       :['signal'+s,'dibosons',1,0]
		  ,"ttbar_signal"   	       :['signal'+s,'ttbar',1,0]
		  ,"ST_signal"                 :['signal'+s,'stop',1,0]
		  ,"QCD_signal"		       :['signal'+s,'qcd',1,0]
		  ,"GJets_signal"	       :['signal'+s,'gjets',1,0]
		  ,"Data_signal"	       :['signal'+s,'data',0,0]
		  # signals
                  ,"hsDM_1000_50_100_signal"    :['signal'+s,'hsDM-1000-50-100_signal',1,1]
                  ,"hsDM_1000_50_200_signal"    :['signal'+s,'hsDM-1000-50-200_signal',1,1]
                  ,"hsDM_1000_50_250_signal"    :['signal'+s,'hsDM-1000-50-250_signal',1,1]
                  ,"hsDM_1000_50_300_signal"    :['signal'+s,'hsDM-1000-50-300_signal',1,1]
                  
                  ,"ZpDM_1000_150_10_signal"    :['signal'+s,'ZpDM-1000-150-10_signal',1,1]
                  ,"ZpDM_1000_50_10_signal"    :['signal'+s,'ZpDM-1000-50-10_signal',1,1]
                  ,"ZpDM_100_150_10_signal"    :['signal'+s,'ZpDM-100-150-10_signal',1,1]
                  ,"ZpDM_100_50_10_signal"    :['signal'+s,'ZpDM-100-50-10_signal',1,1]
                  ,"ZpDM_1500_150_10_signal"    :['signal'+s,'ZpDM-1500-150-10_signal',1,1]
                  ,"ZpDM_1500_50_10_signal"    :['signal'+s,'ZpDM-1500-50-10_signal',1,1]
                  ,"ZpDM_2000_150_10_signal"    :['signal'+s,'ZpDM-2000-150-10_signal',1,1]
                  ,"ZpDM_2000_50_10_signal"    :['signal'+s,'ZpDM-2000-50-10_signal',1,1]
                  ,"ZpDM_2500_150_10_signal"    :['signal'+s,'ZpDM-2500-150-10_signal',1,1]
                  ,"ZpDM_3000_150_10_signal"    :['signal'+s,'ZpDM-3000-150-10_signal',1,1]
                  ,"ZpDM_3000_50_10_signal"    :['signal'+s,'ZpDM-3000-50-10_signal',1,1]
                  ,"ZpDM_300_150_10_signal"    :['signal'+s,'ZpDM-300-150-10_signal',1,1]

		  # Di muon-Control
#                  ,"VH_zmm"                    :['dimuon'+s,'vh',1,0] 
                  ,"Zll_zmm"	               :['dimuon'+s,'zll',1,1]
 		  ,"Wlv_zmm"      	       :['dimuon'+s,'wjets',1,0]
		  ,"Diboson_zmm"    	       :['dimuon'+s,'dibosons',1,0]
		  ,"ttbar_zmm"    	       :['dimuon'+s,'ttbar',1,0]
		  ,"ST_zmm"                    :['dimuon'+s,'stop',1,0]
		  ,"QCD_zmm"		       :['dimuon'+s,'qcd',1,0]
		  ,"Data_zmm"    	       :['dimuon'+s,'data',0,0]

                  # Di electron-Control
#                  ,"VH_zee"                    :['dielectron'+s,'vh',1,0] 
                  ,"Zll_zee"                   :['dielectron'+s,'zll',1,1]
                  ,"Wlv_zee"                   :['dielectron'+s,'wjets',1,0]
                  ,"Diboson_zee"               :['dielectron'+s,'dibosons',1,0]
                  ,"ttbar_zee"                 :['dielectron'+s,'ttbar',1,0]
                  ,"ST_zee"                    :['dielectron'+s,'stop',1,0]
                  ,"QCD_zee"                   :['dielectron'+s,'qcd',1,0]
                  ,"Data_zee"                  :['dielectron'+s,'data',0,0]

                   # Single muon (w) control
#                  ,"VH_mn"                    :['singlemuon'+s,'vh',1,0] 
                  ,"Zll_mn"                   :['singlemuon'+s,'zll',1,0]
                  ,"Wlv_mn"                   :['singlemuon'+s,'wjets',1,1]
                  ,"Diboson_mn"               :['singlemuon'+s,'dibosons',1,0]
                  ,"ttbar_mn"                 :['singlemuon'+s,'ttbar',1,0]
                  ,"ST_mn"                    :['singlemuon'+s,'stop',1,0]
                  ,"QCD_mn"                   :['singlemuon'+s,'qcd',1,0]
                  ,"Data_mn"                  :['singlemuon'+s,'data',0,0]

                   # Single electron (w) control
#                  ,"VH_en"                    :['singleelectron'+s,'vh',1,0] 
                  ,"Zll_en"                   :['singleelectron'+s,'zll',1,0]
 		  ,"Wlv_en"                   :['singleelectron'+s,'wjets',1,1]
		  ,"Diboson_en"               :['singleelectron'+s,'dibosons',1,0]
		  ,"ttbar_en"                 :['singleelectron'+s,'ttbar',1,1]
		  ,"ST_en"                    :['singleelectron'+s,'stop',1,0]
		  ,"QCD_en"                   :['singleelectron'+s,'qcd',1,0]
		  ,"Data_en"                  :['singleelectron'+s,'data',0,0]

                   # Single photon control
                  ,"GJets_gjets"                 :['singlephoton'+s,'gjets',1,1]
                  ,"QCD_gjets"                   :['singlephoton'+s,'qcd',1,0]
                  ,"Data_gjets"                  :['singlephoton'+s,'data',0,0]
                  }

        }
     categories.append(monojet_category[s])
