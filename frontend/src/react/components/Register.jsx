import React from "react"
import {Button, Form} from "semantic-ui-react"
import Cookies from "js-cookie";
import {Grid} from "semantic-ui-react/dist/commonjs/collections/Grid";

export default class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      register: {
        username: "",
        first_name: "",
        last_name: "",
        email:"",
        password: "",
        password_check: ""
      },
      fieldError: {
        success: false,
        username: false,
        email: false,
        password: false,
      },
      registerErrors: {
        error: "",
        status: false,
        success: false
      }
    };
    this.onRegisterSubmit = this.onRegisterSubmit.bind(this);
    this.onRegisterChange = this.onRegisterChange.bind(this);
    this.cleanUp = this.cleanUp.bind(this);
  }
  onRegisterChange (e, { name, value }) {
    this.cleanUp();
    const registerCreditials = this.state.register;
    registerCreditials[name] = value;
    this.setState(registerCreditials);
  }
  cleanUp() {
    const errors = this.state.fieldError;
    errors.username = errors.email = errors.password = false;
    this.setState(errors)
  }

  onRegisterSubmit () {
    const data = this.state.register;
    const formValidation = data.password_check !== data.password;
    const isDeveloperEmail = data.email.includes('developers.nl');
    console.log(isDeveloperEmail, data.email);
    //Password
    const passwordValidation = this.state.registerErrors;
    passwordValidation.status = true;
    passwordValidation.error =
      !isDeveloperEmail ? "Geef een developers.nl Email op" :
        formValidation ? "Wachtwoorden komt niet overeen!!" : null;

    formValidation || !isDeveloperEmail ? this.setState(passwordValidation) : fetch("/users/create/", {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken")
      },
      body: JSON.stringify(
        this.state.register
      )
    })
      .then(response => response.json().then((data) => {
          const registerErrors = this.state.registerErrors;
          const fields = Object.keys(this.state.register);
          const fieldErrors = this.state.fieldError;
          const fieldWithErrors = Object.keys(data).filter(field => fields.includes(field));
          fieldWithErrors.filter(fieldError => {
            this.cleanUp();
            fieldErrors[fieldError] = true;
            this.setState(fieldErrors)
          });
          if (data.detail || !!fieldWithErrors ) {
            const errorsMultiple = Object.keys(data).map(
              field => field.toUpperCase()+":"+" "+data[field]).join(' ');
            const dataWithPossibleSuccess =
              data[fieldWithErrors[0]].includes('successfully') || data[fieldWithErrors[0].includes('sucess')];
            const singlyOutputErrors = data[fieldWithErrors[0]];
            const otherErrors = fieldWithErrors.length > 1 ? errorsMultiple: singlyOutputErrors;
            registerErrors.error = data.detail || otherErrors;
            registerErrors.success = dataWithPossibleSuccess;
            registerErrors.status = true;
            this.setState({registerErrors});
          } else {
            registerErrors.error = null;
            registerErrors.status = false;
            this.setState(registerErrors);
            window.location.reload(true)
          }
        })
      )
      .catch(error => console.error("Register Error", error));
  }

  render(){
    const {
      register: { username, first_name, last_name, email, password, password_check },
      registerErrors: { status, error, success },
      fieldError }
     = this.state;
    return (

      <Form size={"small"}>
        {status && !success ? <div className={"mb-4 alert alert-danger"}>{error}</div> : null}
        {status && success ? <div className={"mb-4 alert alert-success"}>{error} </div> : null}

        <Form.Input
          value={first_name}
          error={!!error &&  error.includes('First', 'Name')}
          fluid
          onChange={this.onRegisterChange}
          icon="user circle"
          name="first_name"
          iconPosition="left"
          placeholder="Voornaam"/>
        <Form.Input
          value={last_name}
          error={!!error && error.includes('Last')}
          fluid
          onChange={this.onRegisterChange}
          icon="user circle outline"
          name="last_name"
          iconPosition="left"
          placeholder="Achternaam"/>
        <Form.Input
          value={username}
          error={success ? false : fieldError.username}
          fluid
          onChange={this.onRegisterChange}
          icon="user"
          name="username"
          iconPosition="left"
          placeholder="Gebruikersnaam"/>
         <Form.Input
          value={email}
          error={!!error && error.includes('Email')}
          fluid
          onChange={this.onRegisterChange}
          icon="at"
          name="email"
          iconPosition="left"
          placeholder="example@example.com"/>
        <Form.Input
          type={"password"}
          value={password}
          error={!!error && error.includes('Wachtwoord') || fieldError.password}
          fluid
          onChange={this.onRegisterChange}
          icon="lock"
          name="password"
          iconPosition="left"
          placeholder="Wachtwoord"/>
        <Form.Input
          type={"password"}
          value={password_check}
          error={!!error && error.includes('Wachtwoord')}
          fluid
          onChange={this.onRegisterChange}
          icon="lock"
          name="password_check"
          iconPosition="left"
          placeholder="Wachtwoord herhalen"/>
        <Button fluid size={"large"}
                onClick={success ? () => window.location.reload() : this.onRegisterSubmit}
                color={"purple"}>{success ? 'Terug naar Inloggen' : 'Register'}</Button>
      </Form>
    )
  }
}
