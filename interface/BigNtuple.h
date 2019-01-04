#ifndef SUSYBSMAnalysis_HSCP_BigNtuple
#define SUSYBSMAnalysis_HSCP_BigNtuple
/* 
	 Class: BigNtuple
	 Simple interface class to hide all the ROOT I/O from the plugin and make it more readabOBle
*/
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "TTree.h"


class BigNtuple {
public:
	BigNtuple(){} //default, empty constructor

	void set_evtinfo(TTree* tree);
	void fill_evtinfo(const edm::EventID& id);

	void set_trackinfo(TTree* tree);
	void fill_trackinfo(const reco::TrackRef& trk);

        void set_trigInfo(TTree* tree);
        void fill_trigInfo(const edm::TriggerResults& triggerResults, const edm::TriggerNames& trigNames);


	void reset() {  //function to reset the tree
	  BigNtuple dummy; //create a new one 
	  *this = dummy;  //use assignment to reset
	}

private:
	unsigned int lumi_ = 0;
	unsigned int run_ = 0;
	unsigned long long evt_ = 0;


	float dxy = -1000;
	float dx = -1000; 

	float track_p = -1000;
	float track_pt = -1000;
	float track_eta = -1000;

	float track_Is = -1000;
	float track_Ih = -1000;

	float track_TOF = -1000;


	
	//aggiungere variabili
};

#endif
