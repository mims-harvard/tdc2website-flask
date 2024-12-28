const Span = () => <span></span>
// src/template/HomeDemo1/SecAboutUsClient/SecWhoWeContant/index.jsx

const SecWhoWeContant = () => {

  return (
    <div className="col-12 col-lg-6">
        <div className="who-we-contant">
            <div className="dream-dots">
            <Span /> 
            <Span /> 
            <Span /> 
            <Span /> 
            <Span /> 
            <Span /> 
            <Span /> 
            </div>
            <h4 data-aos="fade-up">For Creators</h4>
            <p data-aos="fade-up">Whether you&apos;re an aspiring influencer, artist, media creator, or entrepreneur,
            We provide the perfect platform to kick off your projects through innovative tokenomics.</p>
            <a data-aos="fade-up" className="btn dream-btn mt-30"  >Read More</a>
        </div>
    </div>
  );
}

export default SecWhoWeContant;