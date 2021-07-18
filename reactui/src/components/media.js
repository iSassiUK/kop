import React from 'react';
import { Media } from 'reactstrap';
import './media.css';

class KopMedia extends React.Component {
	constructor(props){
		super(props);
		
		this.state = { };
	}
	
	render() {
		var media = this.props.media;
		return(
		<div key={media.id} id="unit" className="col-12 mt-5">					
			<Media tag="li">
				<img src={media.picture.picture_url}></img>
			</Media>
		</div>
		);
	}

}
export default KopMedia;




