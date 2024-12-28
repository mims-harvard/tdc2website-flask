import Image from 'next/image';
import React from 'react';
import { HomeDemo1Dollar } from '../../../utils/allImgs';
import { DocElementTitle, FQAInfo } from '../../../data/data-containers/data-HomeDemo1';
import SECFAQ_TIMELINE from './SecWelcomeContent/SecFAQ_Timeline';
import SecWelcomeContent from './SecWelcomeContent';

const DIV: React.FC = () => <div className="dream-blip blip1"></div>;

const SecWelcomeArea: React.FC = () => {
  return (
    <section
      className="welcome_area clearfix dzsparallaxer auto-init ico fullwidth"
      data-options={{ direction: 'normal' }}
      id="home"
    >
      <div className="divimage dzsparallaxer--target Home1WelcomeAreaIMG"></div>

      <div className="hero-content dark-blue">
        {Array(4)
          .fill(null)
          .map((_, key) => (
            <DIV key={key} />
          ))}
        <div className="container">
        <Image src="../../../assets/img/Website Text.png" alt="Website Text" layout="fill" />
        </div>
        <div className="container h-100">
          <div className="row h-100 align-items-center">
            <div className="col-12 col-lg-12 col-md-12" style={{ textAlign: 'center' }}>
              <SecWelcomeContent img={HomeDemo1Dollar} />
            </div>
            <div className="col-12 col-lg-6 col-md-12">
              <div className="main-ilustration"></div>
            </div>
          </div>
          <SECFAQ_TIMELINE FQAInfo={FQAInfo} DocElementTitle={DocElementTitle} />
        </div>
      </div>
    </section>
  );
};

export default SecWelcomeArea;