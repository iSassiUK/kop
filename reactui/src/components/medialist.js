import React from 'react';
import { Media } from 'reactstrap';
import './media.css';
import KopMedia from './media';

class KopMediaList extends React.Component {
	constructor(props){
		super(props);
	}
	

	
	render(){
		if (this.props.medias.length >0 ) {
			const info = this.props.medias.map( m => {
				return (
					<KopMedia media={m} key={m.id}/>
				)
			});
			return info;
		}
	
		return "<b>No Data</b>"
		
	}
}
export default KopMediaList;
