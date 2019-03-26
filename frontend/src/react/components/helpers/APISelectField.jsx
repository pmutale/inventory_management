import React from 'react';
import { Form,  } from 'semantic-ui-react';
import Cookies from "js-cookie";

class APISelectField extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            options: this.props.options || [],
            loading: true,
            errors: '',
        };

        this.map = {
            keyField: this.props.map && this.props.map.keyField ? this.props.map.keyField : 'description',
            textField: this.props.map && this.props.map.textField ? this.props.map.textField : 'name',
            valueField: this.props.map && this.props.map.valueField ? this.props.map.valueField : 'id',
            flagField: this.props.map && this.props.map.flagField ? this.props.map.flagField : undefined,
            contentField: this.props.map && this.props.map.contentField ? this.props.map.contentField : undefined,
        };
    }

    fetchOptions() {
        let options;
        let optionList;

        // First check is we have an endpoint
        if (this.props.url) {
            fetch( this.props.url,{
                  method: 'GET',
                  headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': Cookies.get('csrftoken'),
                      'cache-control': 'no-cache',
                  }
              }
            ).then(res => res.json())
              .then( response => {
                // Test what kind of response is returned
                if (Array.isArray(response)) {
                    optionList = response;
                }
                else if (typeof response === 'object' && Array.isArray(response.result)) {
                    optionList = response.result;
                }
                else {
                    console.warn('Invalid response returned', response);
                    optionList = [{
                        key: 'ERROR',
                        text: 'Invalid response',
                        value: 'ERROR',
                    }];
                }

                // Return the list
                options = optionList.map((option, index) => {
                    return ({
                        key: option[this.map.keyField],
                        text: option[this.map.textField],
                        value: option[this.map.valueField],
                        flag: this.map.flagField ? option[this.map.flagField].toLowerCase() : undefined,
                        content: this.map.contentField ? option[this.map.contentField] : undefined,
                    });
                });

                // If a single option is received, we want that option to be set
                if (optionList.length === 1 && 'handleAutoSelect' in this.props) {
                    this.props.handleAutoSelect(this.props.name, optionList[0][this.map.valueField])
                }

                // Return the results in .then
                this.setState({ options: options, loading: false });
            })
              .catch(error => {
                  options = [{
                      key: 'ERROR',
                      text: error.message,
                      value: 'ERROR',
                  }];

                  // Return the results in .catch
                  this.setState({ options: options, loading: false });
              });
        }
        else {
            // There is no URL. Display an error
            options = [{
                key: 'ERROR',
                text: 'No endpoint defined in properties',
                value: 'ERROR',
            }];

            // Return the error results
            this.setState({ options: options, loading: false });
        }
    }

    componentDidMount() {
        if (this.props.options) {
            console.warn('Select options are given in props. You can use the standard Select control ' +
              'instead. Please remove the options from the properties and add an endpoint.');
            this.setState({ loading: false });
        }
        else {
            this.fetchOptions();
        }
    }

    componentDidUpdate(prevProps) {
        if (this.props.options) {
            // Nothing to do, the options aren't fetched in the mount either
        } else {
            if (JSON.stringify(prevProps.fetch_params) !== JSON.stringify(this.props.fetch_params)) {
                // Fetch options only if fetch parameters are changed
                this.fetchOptions()
            }
        }
    }

    render() {
        const props = this.props;
        const { options, loading, errors } = this.state;
        const { controlProp, noResultsMessageProp } = this.props;
        const control = controlProp ? controlProp : Form.Select;
        const noResultsMessage = noResultsMessageProp ? noResultsMessageProp : 'Geen gegevens gevonden';

        // Filter the properties we need, pass all other properties to the ErrorField
        const extraProps = Object.keys(props)
          .filter(key => ['control', 'options', 'url', 'map', 'noResultsMessage', 'fetch_params', 'handleAutoSelect'].includes(key) === false)
          .reduce((obj, key) => {obj[key] = props[key];
              return obj}, {}
          );

        return (
          <Form.Select
            control={control}
            options={options}
            loading={loading}
            errors={errors}
            noResultsMessage={noResultsMessage}
            {...extraProps} />
        );

    }
}

export default APISelectField;
