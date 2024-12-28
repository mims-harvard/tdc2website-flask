import SectionHeading from '../../../components/SectionHeading'

const SecPartners = ({data}) => {

  return (
    <section className="partners">

        <SectionHeading
            title='Our Early Collaborators'
            // text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis accumsan nisi Ut ut felis congue nisl hendrerit commodo.'
        />

        <div className="container">
                {data && data.map((item , key) => (
                    <div className="row">
                        <div className="col-sm-4"></div>
                        <div className="col-sm-4" data-aos="fade-up" key={key}>
                            <div className="partner-box">
                                <a href={item.link}><img src={item.img} alt="" className="center-bock"/></a>
                            </div>
                        </div>
                        <div className="col-sm-4"></div>
                    </div>
                ))}
            </div>
    </section>
  );
}

export default SecPartners;