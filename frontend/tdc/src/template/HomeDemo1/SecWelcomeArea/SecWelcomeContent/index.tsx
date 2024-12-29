import Image from 'next/image';
import React from 'react';
import { DocElementTitle } from '../../../../data/data-containers/data-HomeDemo1';
import IcoDocs from './SecFAQ_Timeline/IcoDocs';

type SecWelcomeContentProps = {
  img: string;
};

const SecWelcomeContent: React.FC<SecWelcomeContentProps> = ({ img }) => {
  return (
    <div className="welcome-content">
      <div className="promo-section">
        <div className="integration-link">
          <span className="integration-icon">
            <Image src={img} width="24" height="24" alt="X" />
          </span>
          <span className="integration-text">Introducing TDC-2</span>
        </div>
      </div>
      <h1 style={{ color: '#3A9C94', fontFamily: 'sans-serif'}}>The Commons (TDC-2)</h1>
      <h1 style={{ color: '#FFB300', fontFamily: 'sans-serif' }}>A multimodal ML platform for biomedical foundation models</h1>
      <h3 style={{ color: '#FFDF00', fontFamily: 'sans-serif' }}>COMING SOON</h3>
      <p></p>
      <h3 style={{ color: '#FFEFC2', fontFamily: 'sans-serif' }}>
        Learn more about our alpha release below! (TODO: change this)
      </h3>
      <p>
        TDC-2 is fantastic. Absolutely the best. (TODO: change this)
      </p>
      <div className='row'>
        <div className="col-md-2"></div>
        <div className="col-md-8">
          <IcoDocs data={DocElementTitle} />
        </div>
        <div className='col-md-2'></div>
      </div>
      <p></p>
      <div className="dream-btn-group">
        <a href="https://tdcommons.ai" className="btn dream-btn" style={{borderColor: '#FFDF00', marginRight: '5px'}}>
          Go to TDC homepage
        </a>
        <a></a>
        <a href="http://tdcommons.ai/news" className="btn dream-btn mr-3" style={{borderColor: '#FFDF00', marginLeft: '5px'}}>
          See recent news
        </a>
      </div>
    </div>
  );
};

export default SecWelcomeContent;
