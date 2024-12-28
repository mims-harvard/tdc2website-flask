import Image from 'next/image';
import React from 'react';

type ContentProps = {
  img: string;
  title: string;
  content: string;
};

const Content: React.FC<ContentProps> = ({ img, title, content }) => {
  return (
    <div className="col-12 col-sm-6 col-lg-4" data-aos="fade-up">
      <div className="service_single_content text-left mb-100">
        <div className="service_icon">
        <Image src={img} alt={title} layout="fill" />
        </div>
        <h6>{title}</h6>
        <p>{content}</p>
      </div>
    </div>
  );
};

export default Content;
