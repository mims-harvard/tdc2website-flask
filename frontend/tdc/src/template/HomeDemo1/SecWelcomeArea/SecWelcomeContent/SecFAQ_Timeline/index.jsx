// import SectionHeading from '../../../../../components/SectionHeading'
// import SingleFAQArea from './SingleFAQArea'
// import IcoCounter from './IcoCounter'
import IcoDocs from './IcoDocs'

const SECFAQ_TIMELINE = ({FQAInfo , DocElementTitle}) => {

  return (
    <section className="faq-timeline-area section-padding-100">
        <div className="container">
            <div className="row">
                {/* <div className="col-12 col-lg-7 col-md-12 mb-5">
                    <SectionHeading
                        title='Frequently Asked Questions'
                        text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis accumsan nisi Ut ut felis congue nisl hendrerit commodo.'
                    />

                    <div className="dream-faq-area">
                        <div className="panel-group" id="accordionFourLeft" data-aos="fade-up">
                            {FQAInfo && FQAInfo.map((item , key) => (
                                <>
                                    <SingleFAQArea key={key} text={item.text} ID={item.ID} />
                                </>
                            ))}
                        </div>
                    </div>
                </div> */}
                <div className="col-md-4"></div>
                <div className="col-md-4">

                    {/* <IcoCounter /> */}

                    <IcoDocs data={DocElementTitle} />
                    
                </div>
                <div className="col-md-4"></div>
            </div>
        </div>
    </section>
  );
}

export default SECFAQ_TIMELINE;