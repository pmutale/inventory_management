import React, { Component } from "react";
import {Form} from "semantic-ui-react";

export default class AddRandomProduct extends  Component {
	constructor(props) {
		super(props);
		this.state = {

		}
	}

	render() {
		return (
			<div>
				<Form>
					<Form.Input
						name={'item'}
						icon={'paperclip'}
					/>
				</Form>
			</div>
		)
	}
}
