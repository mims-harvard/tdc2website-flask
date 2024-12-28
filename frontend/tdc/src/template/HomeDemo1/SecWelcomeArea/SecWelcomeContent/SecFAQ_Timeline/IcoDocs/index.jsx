import DocElement from './DocElement'

const IcoDocs = ({data}) => {

  return (
    <div className="ico-docs">
        <div>
        	{data && data.map((item , key) => (
	            <DocElement title={item.title} link={item.link} />
        	))}
        </div>
    </div>
  );
}

export default IcoDocs;