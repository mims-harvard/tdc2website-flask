import { useEffect } from 'react';

import { 
  VerticalSocial,
  service_single_content,
  SocialListIco,
  timelineInfo,
  ServiceBlock,
  FQAInfo,
  DocElementTitle,
  TokenText,
  TeamMember,
  PartnersData,
  SingleCoolFact
} from '../../data/data-containers/data-HomeDemo1';
import { handelTitle } from '../../utils';

import Header from '../../layouts/Header';
import Footer from '../../layouts/FooterPages';

import SecAboutUs from './SecAboutUs';
import SecAboutUsClient from './SecAboutUsClient';
import SecAboutUsClientPeople from './SecAboutUsClientPeople';
import SecDemoVideo from './SecDemoVideo';
import SecDistribution from './SecDistribution';
import SecFAQ_Timeline from './SecWelcomeArea/SecWelcomeContent/SecFAQ_Timeline'
import SecOurFeatures from './SecOurFeatures';
import SecOurRoadmap from './SecOurRoadmap';
import SecOurServices from './SecOurServices';
import SecPartners from './SecPartners';
import SecSubscribe from './SecSubscribe';
import SecTeam from './SecTeam';
import SecTrust from './SecTrust';
import SecWelcomeArea from './SecWelcomeArea';
import SecVerticalSocial from './SecVerticalSocial';

import { 
  HomeDemo1About1,
  HomeDemo1Solution,
  HomeDemo1About1People,
  HomeDemo1VideoBg4,
  HomeDemo1ImgPhone,
  HomeDemo1RingsBg,
  HomeDemo1Allocation
} from '@/utils/allImgs';

const HomeDemo1: React.FC = () => {
  useEffect(() => {
    handelTitle('TDC2: Multimodal ML Platform for Foundation Models in Therapeutics');
  }, []);

  useEffect(() => {
    // Set the body background image client-side
    if (typeof document !== 'undefined') {
      const body = document.getElementsByTagName('body')[0];
      if (document.title === 'TDC2: Multimodal ML Platform for Foundation Models in Therapeutics') {
        body.style.backgroundImage =
          'linear-gradient(180deg,#240044 0,#0f0240 25%,#400959 40%,#0f0240 65%,#0f0240)';
      } else {
        body.style.backgroundImage =
          'linear-gradient(to right, #4834d4, #341f97)';
      }
    }
  }, []);

  return (
    <>
      <Header />
      <div className="HomeDemo1">
        <SecWelcomeArea />
        <SecVerticalSocial data={VerticalSocial} />
        <SecTrust data={SingleCoolFact} />
        <SecAboutUsClient img={HomeDemo1About1.src} />
        <SecAboutUs img={HomeDemo1Solution.src} />
        <SecAboutUsClientPeople img={HomeDemo1About1People.src} />
        <div className="clearfix" />
        <SecDemoVideo img={HomeDemo1VideoBg4.src} />
        <div className="clearfix" />
        <SecOurServices data={service_single_content} />
        <SecSubscribe data={SocialListIco} />
        <SecOurRoadmap data={timelineInfo} />
        <SecOurFeatures data={ServiceBlock} imgPhone={HomeDemo1ImgPhone.src} Rings={HomeDemo1RingsBg.src} />
        <SecFAQ_Timeline FQAInfo={FQAInfo} DocElementTitle={DocElementTitle} />
        <SecDistribution img={HomeDemo1Allocation.src} data={TokenText} />
        <SecTeam data={TeamMember} />
        <SecPartners data={PartnersData} />
      </div>
      <Footer />
    </>
  );
};

export default HomeDemo1;
