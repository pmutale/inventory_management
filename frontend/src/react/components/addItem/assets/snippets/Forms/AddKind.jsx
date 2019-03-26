import React, { Component } from "react";
import AddAudioVisual from "./AddAudioVisual";

class AddKind extends Component {
	constructor(props){
		super(props);
		this.state = {

		}
	}
	render() {
		return (
			<AddAudioVisual type={'kind'}
			                kind={true}
			                handlePostData={this.props.handlePostData}
			                derivedResponse={this.props.derivedResponse}
			/>
		)
	}
}

export default AddKind
