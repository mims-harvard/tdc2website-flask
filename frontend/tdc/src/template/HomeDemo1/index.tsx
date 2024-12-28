import { useEffect } from 'react';

// Import data and utilities
import { VerticalSocial } from '../../data/data-containers/data-HomeDemo1';
import { handelTitle } from '../../utils';

// Import layout components
import Header from '../../layouts/Header';
import Footer from '../../layouts/FooterPages';

// Import section components
import SecWelcomeArea from './SecWelcomeArea';
import SecVerticalSocial from './SecVerticalSocial';

const HomeDemo1: React.FC = () => {
  useEffect(() => {
    // Set the document title
    handelTitle('Alphunt - The foremost talent network');
  }, []);

  useEffect(() => {
    // Set the body background image client-side
    if (typeof document !== 'undefined') {
      const body = document.getElementsByTagName('body')[0];
      if (document.title === 'Alphunt - The foremost talent network') {
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
        {/* Uncomment and use other sections as needed */}
        {/* <SecTrust data={SingleCoolFact} /> */}
        {/* <SecAboutUsClient img={HomeDemo1About1} /> */}
        {/* <SecAboutUs img={HomeDemo1Solution} /> */}
        {/* <SecAboutUsClientPeople img={HomeDemo1About1People} /> */}
        <div className="clearfix" />
        {/* <SecDemoVideo img={HomeDemo1VideoBg4} /> */}
        <div className="clearfix" />
        {/* <SecOurServices data={service_single_content} /> */}
        {/* <SecSubscribe data={SocialListIco} /> */}
        {/* <SecOurRoadmap data={timelineInfo} /> */}
        {/* <SecOurFeatures data={ServiceBlock} imgPhone={HomeDemo1ImgPhone} Rings={HomeDemo1RingsBg} /> */}
        {/* <SecFAQ_Timeline FQAInfo={FQAInfo} DocElementTitle={DocElementTitle} /> */}
        {/* <SecDistribution img={HomeDemo1Allocation} data={TokenText} /> */}
        {/* <SecTeam data={TeamMember} /> */}
        {/* <SecPartners data={PartnersData} /> */}
      </div>
      <Footer />
    </>
  );
};

export default HomeDemo1;
