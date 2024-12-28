import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import Content from './Content';

type ServiceData = {
  img: string;
  title: string;
  content: string;
};

type SecOurServicesProps = {
  data: ServiceData[];
};

const SecOurServices: React.FC<SecOurServicesProps> = ({ data }) => {
  return (
    <section className="our_services_area section-padding-100-70 clearfix" id="services">
      <div className="container">
        <SectionHeading
          title="Our Core Features"
          text=""
          // text="We power everyone's favorite place to connect and find their dream opportunities through democratic tokenomics, privacy-preserving data and machine learning blockchain infrastructure, and optimized cost structures"
        />

        <div className="row">
          {data &&
            data.map((item, key) => (
              <Content key={key} img={item.img} title={item.title} content={item.content} />
            ))}
        </div>
      </div>
    </section>
  );
};

export default SecOurServices;
