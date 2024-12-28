import React from 'react';
import SingleCoolFact from './SingleCoolFact';
import { StaticImageData } from 'next/image';

type CoolFactData = {
  img: StaticImageData;
  ico_check: boolean;
};

type SecSingleCoolFactProps = {
  data: CoolFactData[];
}

const SecSingleCoolFact: React.FC<SecSingleCoolFactProps> = ({data}) => {
  return (
    <>
      {data &&
        data.map((item, key) => (
          <SingleCoolFact key={key} img={item.img.src} ico_check={item.ico_check} />
        ))}
    </>
  );
};

export default SecSingleCoolFact;
