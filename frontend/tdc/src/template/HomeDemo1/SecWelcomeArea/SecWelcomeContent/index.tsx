import Image from 'next/image';
import React from 'react';
import { DocElementTitle, FQAInfo } from '../../../../data/data-containers/data-HomeDemo1';
import SECFAQ_TIMELINE from './SecFAQ_Timeline';

type SecWelcomeContentProps = {
  img: string;
};

const SecWelcomeContent: React.FC<SecWelcomeContentProps> = ({ img }) => {
  return (
    <div className="welcome-content">
      <div className="promo-section">
        <div className="integration-link">
          <span className="integration-icon">
            <Image src={img} width="24" height="24" alt="Integration Icon" />
          </span>
          <span className="integration-text">Discover a new ways to enjoy your World!</span>
        </div>
      </div>
      <h1 style={{ color: '#349ed9' }}>Alphunt</h1>
      <h1 style={{ color: '#fd9d3f' }}>Web3&apos;s foremost professional network</h1>
      <h3 style={{ color: '#7551fe' }}>COMING SOON</h3>
      <p></p>
      <h3 style={{ color: '#7551fe' }}>
        Everyone&apos;s favorite place to connect and find their dream opportunities
      </h3>
      <p>
        Web3&apos;s foremost talent network powered by blockchain, cryptocurrency tokenomics, and
        privacy-preserving machine learning. We&apos;re at the exciting intersection of fintech,
        recruiting, and anonymous social networks, utilizing the latest methods in all three
        fields to deliver maximum value to all our users.
      </p>
      <SECFAQ_TIMELINE FQAInfo={FQAInfo} DocElementTitle={DocElementTitle} />
      <div className="dream-btn-group">
        <a href="https://forms.gle/VVwrxRcgQdHrH84x8" className="btn dream-btn">
          Join the Waitlist
        </a>
        <a href="http://app.Alphunt.io" className="btn dream-btn mr-3">
          NFT Promo Platform
        </a>
      </div>
    </div>
  );
};

export default SecWelcomeContent;
