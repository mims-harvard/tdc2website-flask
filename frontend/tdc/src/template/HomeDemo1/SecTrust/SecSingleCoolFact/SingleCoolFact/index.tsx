import Image from 'next/image';
import React from 'react';

type SingleCoolFactProps = {
  img: string;
  ico_check: boolean;
};

const SingleCoolFact: React.FC<SingleCoolFactProps> = ({ img, ico_check }) => {
  return (
    <div className="col-12 col-sm-6 col-md-3 col-lg-2" data-aos="fade-up">
      <div className="trust-item text-center">
        <div className="ico-platform-logo">
        <Image src={img} alt="Cool Fact Logo" layout="fill" />
        </div>
        <div className="check">
          {ico_check ? (
            <div className="check-icon"></div>
          ) : (
            <div className="value">8.9</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SingleCoolFact;
