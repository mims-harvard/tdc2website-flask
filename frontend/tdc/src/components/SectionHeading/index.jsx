const Span = () => <span></span>

const SectionHeading = ({title , text, color1, color2}) => {

  return (
    <div className="section-heading text-center">
        <div className="dream-dots justify-content-center" data-aos="fade-up" data-aos-delay='200'>
            {Array(7).fill().map((item , key) => (
                    <Span key={key} />
                ))}
        </div>
        <h2 data-aos="fade-up" data-aos-delay='300' style={{color:'white'}}>{title}</h2>
        <p data-aos="fade-up" data-aos-delay='400' color={{color:'{{color2}}'}}>{text}</p>
    </div>
  );
}

export default SectionHeading;