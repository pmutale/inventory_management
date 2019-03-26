import React, { Component } from 'react'
import { Message } from 'semantic-ui-react'
import FormFields from './FormFields'


const capitalize = (string) => {
	if (typeof string !== 'string') return '';
	return string.charAt(0).toUpperCase() + string.slice(1)
};

class AddAudioVisual extends Component {
	constructor(props) {
		super(props);
		this.state = {
			dataAttributes: {
				value: '', error: false, icon:'tv', placeholder:'', name:'', type: ''
			},
			dataFields: {
				audio_visual: [
					"cost", "brand", "kind", "description", "name", "tags", "purchase_date", "tags", "serial_number"
				],
				kind: [
					"name","screen_size","screen_type", "mounting_method", "overall_width", "overall_height", "color", "extras"
				],
				brand: [
					"name", "name", "country_of_origin", "brand_number", "description"
				]
			},
			formFields: {},
			formInstance: this.props.type
		};

		const { dataAttributes, dataFields, formFields, formInstance } = this.state;
		const form = formInstance === undefined ? 'audio_visual': formInstance;
		dataFields[form].map( element => {
			formFields[element] = {...dataAttributes,
				name: element,
				placeholder: capitalize(element),
				type: 'purchase_date' === element ? 'date' : null,
				icon: 'cost' === element ? 'euro' :
					'tags' === element ? 'tags' :
						'purchase_date' === element ?
							'calendar alternate':  'tv',
			};
		});

		this.handleChange = this.handleChange.bind(this);
		this.handleData = this.handleData.bind(this);
		this.callBackToSendData = this.callBackToSendData.bind(this);
		this.handleAddKind = this.handleAddKind.bind(this);
		this.handleAddBrand = this.handleAddBrand.bind(this);
	}

	componentDidMount() {
		this.handleAddBrand('div#brand');
		this.handleAddKind('div#kind');
	}

	handleData() {
		const { dataAttributes, dataFields, formData } = this.state;
		dataFields.forEach(function(element) {
			formData[element] = dataAttributes
		});
		this.setState(formData)
	}

	callBackToSendData() {
		const formData = {};
		const { formFields } = this.state;
		Object.keys(formFields).map(field => {
			formData[field] = formFields[field].value
		});
		this.props.handlePostData(formData)
	}

	handleChange (e, { name, value }) {
		const formDataFields = this.state.formFields;
		formDataFields[name].value = value;
		this.setState(formDataFields);
		this.callBackToSendData()
	}

	handleAddBrand(selector) {
		const selectorField = document.querySelector(selector);
		!this.props.kind && !this.props.brand ?  selectorField.onclick  = () => this.props.addBrand(true) : null
	}

	handleAddKind(selector) {
		const selectorField = document.querySelector(selector);
		!this.props.kind && !this.props.brand ? selectorField.onclick = () => this.props.addKind(true): null
	}

	render() {
		const { formFields, formInstance } = this.state;
		const { derivedResponse } = this.props;
		const errorEntryList = [];
		const form = formInstance === undefined ? 'audio_visual': formInstance;
		derivedResponse && !derivedResponse.success  ? Object.entries(derivedResponse.data).forEach(
			entry => {
				errorEntryList.push(capitalize(entry[0]) + ' - ' + entry[1])
			}): null;
		const errorMessage = derivedResponse && derivedResponse.error && !derivedResponse.success ?
			<Message error
			         header={'We wijzen U graag op het volgende'}
			         list={errorEntryList}
			/> : derivedResponse && derivedResponse.success ? <Message success header={'Het is gelukt'}/>: null;
		const formInstanceCheck = derivedResponse && derivedResponse.instance === form;

		return (
			<div>
				{
					formInstanceCheck ? errorMessage : null
				}

				<FormFields handleChange={this.handleChange}
						            derivedResponse={formInstanceCheck ? derivedResponse : null }
						            fields={formFields}/>
			</div>
		)
	}
}

export default AddAudioVisual;

