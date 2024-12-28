const Span = () => <span></span>
// src/template/HomeDemo1/SecAboutUsClient/SecWhoWeContant/index.jsx
const SecWhoWeContantPeople = () => {

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
            <h4 data-aos="fade-up">For the People</h4>
            <p data-aos="fade-up">Discover your favorite content. Invest and share in the gains of innovative and impactful projects. Find your dream opportunity. Get paid in crypto.</p>
            {/* <p data-aos="fade-up">Your data is untraceable. Your identity anonymized. No spam, ads, or unsolicited inboxes.</p> */}
            {/* <a data-aos="fade-up" className="btn dream-btn mt-30"  >Read More</a> */}
        </div>
    </div>
  );
}

export default SecWhoWeContantPeople;