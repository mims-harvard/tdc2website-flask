const Span = () => <span></span>
// src/template/HomeDemo1/SecAboutUs/SecWhoWeContant/index.jsx
const SecWhoWeContant = () => {

  return (
    <div className="col-12 col-lg-6">
        <div className="who-we-contant">
            <div className="dream-dots" data-aos="fade-up">
                {Array(7).fill().map((key) => (
                		<Span />
                	))}
            </div>
            <h4 data-aos="fade-up">For Business</h4>
            <p data-aos="fade-up">Our matching offers you the opportunity to hire the top talent at optimal cost and time efficiency. Using state-of-the-art machine learning.</p>
            {/* <a className="btn dream-btn mt-30"  >Read More</a> */}
        </div>
    </div>
  );
}

export default SecWhoWeContant;