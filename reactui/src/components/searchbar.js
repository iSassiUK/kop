import React from 'react';

class SearchBar extends React.Component {
	
	constructor(props){
		super(props);
		this.state = {val: 0, word: "awesome"};
		console.log("constructor")

	}
	
	
	changeValue = () => {
		let val = this.state.val;
		let new_word= ((val%2) === 0) ? "awesome" : "wonderful";
		let new_state = val+1;
		this.setState(
			{ val: new_state, word: new_word }
		);
	}
	
	render(){
		return(
			<div>
<form>
  <label>
    Search for a killer:
    <input type="text" name="criminal" />
  </label>
  <button type="button" onClick={this.changeValue}>Find</button>
</form>
       			
			</div>
		);
	}
}


export default SearchBar;
