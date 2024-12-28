const LI_A = ({nameIco, url}) => <li><a href={url}><i className={nameIco} aria-hidden="true"></i> </a></li>

const SecVerticalSocial = ({data}) => {

  return (
    <div className="vertical-social">
        <ul>
            {data && data.map((item) => (
                    <LI_A nameIco={item.nameIco} url={item.link} />
                ))
            }
            
        </ul>                  
    </div>
  );
}

export default SecVerticalSocial;