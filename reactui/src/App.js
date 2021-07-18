import React from 'react';
import './App.css';
import { Navbar, NavbarBrand } from 'reactstrap';
import KopMediaList from './components/medialist'; 
import SearchBar from './components/searchbar';

class App extends React.Component {					
  	componentDidMount() {
		fetch('http://localhost:5000/kop/api/v1.0/media/all')
		  .then((res) => res.json())
		  .then((data) => {
				this.setState({
					route: "MEDIA_ALL",
					medias: data,
				})
		  });
	}

	constructor(props){
		super(props);
		
		this.state= {
			route: "MEDIA_ALL",
			medias: [],
			
		}

	}
	
	render(){
		return (
			<div className='App'>
				<Navbar color="dark">
					<div className="container" id="brand">
						<NavbarBrand>KOP</NavbarBrand>
						<SearchBar />
					</div>
				</Navbar>
				<KopMediaList medias={this.state.medias} />
			</div>
		);
	}
}

export default App;

