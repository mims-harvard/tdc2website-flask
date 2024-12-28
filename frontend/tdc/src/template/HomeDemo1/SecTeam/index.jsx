import SectionHeading from '../../../components/SectionHeading'

const SecTeam = ({data}) => {

  return (
    <section className="our_team_area section-padding-0-0 clearfix" id="team">
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <SectionHeading
                        title='The Founder'
                        text='MIT Computer Science graduate and software engineer with years of experience in the industry. Have additionally contributed to public and private partnerships for jobs and recruiting through the World Bank and Pinterest.'
                        color1="white"
                        color2="white"
                    />
                </div>
            </div>

            <div className="row">
                {data && data.map((item , key) => (
                    <div className="col-sm-12" data-aos="fade-up">
                        <div className="single-team-member">
                            <div className="team-member-thumb">
                                <img src={item.img} className="center-block" alt=""/>
                            </div>
                            <div className="team-info">
                                <h5>{item.title}</h5>
                                <p>{item.text}</p>
                            </div>
                            <div className="team-social-icon">
                                <a href="http://alejandrovelez.com"><i className="fa fa-id-badge"></i></a>
                                {/* <a  ><i className="fa fa-twitter"></i></a>
                                <a  ><i className="fa fa-instagram"></i></a>
                                <a  ><i className="fa fa-facebook"></i></a>
                                <a  ><i className="fa fa-skype"></i></a> */}
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    </section>
  );
}

export default SecTeam;