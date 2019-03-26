import React from "react";
import { Responsive, Button, Form, Grid, Header, Message, Segment, Icon, Modal } from "semantic-ui-react";
import Cookies from "js-cookie";
import Register from "./Register";
import { trans } from "./helpers/globalsFuncs.";


class LoginForm extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      loginCreditials: {
        username: "",
        password: "",
      },
      loginErrors: {
        error: "",
        status: false
      },
      register: {
        show: false
      }
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.showRegister = this.showRegister.bind(this);
  }

  onSubmit () {
    fetch("/users/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken")
      },
      body: JSON.stringify(
        this.state.loginCreditials
      )
    })
      .then(response => response.json().then((data) => {
        const loginErrors = this.state.loginErrors;
        if (data.error) {
          loginErrors.error = data.error;
          loginErrors.status = true;
          this.setState({loginErrors});
        } else {
          loginErrors.error = null;
          loginErrors.status = false;
          this.setState(loginErrors);
          window.location.reload(true);
        }
      })
      )
      .catch(error => console.error("Login Error", error));
  }

  handleChange (e, { name, value }) {
    const loginCreditials = this.state.loginCreditials;
    loginCreditials[name] = value;
    this.setState(loginCreditials);
  }

  showRegister () {
    const loginHeader = document.getElementById("login-header");
    loginHeader.innerHTML = "Registreren";
    const register = this.state.register;
    register.show = true;
    this.setState(register);
  }
  render () {
    const {
      loginCreditials: { username, password },
      loginErrors: { status, error },
      register: { show }
    } = this.state;

    const formStyle = {
      width: "90%",
      maxWidth: "420px",
      margin: "0 auto",
    };
    return (
      <div style={formStyle}>
        <Responsive as={Grid} centered>
          <Grid.Column>
            {status && !show ? <div className={"mb-4 alert alert-danger"}>{error}</div> : null}
            {show ? <Register/> : <Form size="small">
              <Form.Input
                value={username}
                error={status}
                fluid
                onChange={this.handleChange}
                icon="user"
                name='username'
                iconPosition="left"
                placeholder={trans("Gebruikersnaam")}/>
              <Form.Input
                error={status}
                fluid
                onChange={this.handleChange}
                value={password}
                icon="lock"
                name="password"
                iconPosition="left"
                placeholder="Wachtwoord"
                type="password"
              />

              <Button
                className={"btn btn-lg btn-primary btn-block"}
                // positive
                fluid
                color={"orange"}
                onClick={this.onSubmit}
                size="large">
                Aanmelden
              </Button>
              <Message info>
                Nieuw? Een eigen account aanmaken
                <a onClick={this.showRegister} href="#"> hier </a>
              </Message>
            </Form>}
          </Grid.Column>
        </Responsive>
      </div>
    );
  }
}

export default LoginForm;
