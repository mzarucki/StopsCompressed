#ifndef StopsCompressed_Generation_testEvtLoop_h
#define StopsCompressed_Generation_testEvtLoop_h
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "SimDataFormats/GeneratorProducts/interface/GenFilterInfo.h"

#include <iostream>

class testEvtLoop : public edm::EDAnalyzer {
public:
  explicit testEvtLoop(edm::ParameterSet const&);
  virtual ~testEvtLoop();

private:
  virtual void beginJob();
  virtual void beginRun(const edm::Run& run, const edm::EventSetup& c);
  virtual void analyze(edm::Event const& e, edm::EventSetup const& c);
  virtual void endLuminosityBlock(edm::LuminosityBlock const& lumiBlock, edm::EventSetup const& c);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void endJob();

  edm::EDGetTokenT<GenFilterInfo> genFilterInfoToken_;

};  //end class

// -----------------------------------------------------------------

testEvtLoop::testEvtLoop(edm::ParameterSet const& iConfig) :
  genFilterInfoToken_(consumes<GenFilterInfo, edm::InLumi>(iConfig.getParameter<edm::InputTag>("genFilterInfoTag")))
{}

// -----------------------------------------------------------------

testEvtLoop::~testEvtLoop() {}

// -----------------------------------------------------------------

void testEvtLoop::analyze(edm::Event const& e, edm::EventSetup const&) {
  //std::cout<<"testEvtLoop::analyze"<<std::endl;
}

// -----------------------------------------------------------------
void testEvtLoop::endLuminosityBlock(edm::LuminosityBlock const& lumiBlock, edm::EventSetup const& c) {
  std::cout << "testEvtLoop::endLuminosityBlock" << std::endl;

  edm::Handle<GenFilterInfo> genFilter;
  lumiBlock.getByToken(genFilterInfoToken_,genFilter);
  double sumPassWeights_ = genFilter->sumPassWeights();
  double sumWeights_ = genFilter->sumWeights();

  std::cout << "I'm in run " << lumiBlock.run() << " lumi block " << lumiBlock.id().luminosityBlock() << " sumPassWeights "<<sumPassWeights_<<" sumWeights "<<sumWeights_<<std::endl;
}
// -----------------------------------------------------------------

void testEvtLoop::beginJob() { std::cout << "testEvtLoop::beginJob" << std::endl; }

// -----------------------------------------------------------------

void testEvtLoop::beginRun(const edm::Run& run, const edm::EventSetup& c) {
  std::cout << "testEvtLoop::beginRun" << std::endl;
}

// -----------------------------------------------------------------
void testEvtLoop::endRun(edm::Run const& run, edm::EventSetup const& c) {
  std::cout << "testEvtLoop::endRun" << std::endl;
}

// -----------------------------------------------------------------
void testEvtLoop::endJob() { std::cout << "testEvtLoop::endJob" << std::endl; }

DEFINE_FWK_MODULE(testEvtLoop);
#endif
