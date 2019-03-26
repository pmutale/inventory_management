import React, { Component } from "react";
import AddAudioVisual from "./AddAudioVisual";

class AddBrand extends Component {
	constructor(props){
		super(props);
		this.state = {

		}
	}
	render() {
		return (
			<AddAudioVisual type={'brand'}
			                kind={true}
			                handlePostData={this.props.handlePostData}
			                derivedResponse={this.props.derivedResponse}
			/>
		)
	}
}

export default AddBrand
