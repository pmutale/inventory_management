import React from "react";
import { Responsive, Button, Form, Grid, Header, Message, Segment, Icon } from "semantic-ui-react";
import Cookies from "js-cookie";


class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loginCreditials: {
        username: "",
        password: "",
      },
      loginErrors: {
        error: "",
        status: false
      }
    };
    this.onSubmit = this.onSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this)
  }

  onSubmit () {
    fetch('/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
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
            window.location.reload(true)
          }
        })
      )
      .catch(error => console.error('Login Error', error));
  }

  handleChange(e, { name, value }) {
    const loginCreditials = this.state.loginCreditials;
    loginCreditials[name] = value;
    this.setState(loginCreditials);
  }

  render() {
    const { loginCreditials: { username, password }, loginErrors: { status, error } } = this.state;
    const formStyle = {
      width: '90%',
      maxWidth: '420px',
      margin: '0 auto',
      // position: 'absolute',
      // transform: 'translate(-50%, -50%)',
      // left: '50%',
      // top: '50%',
    };
    return (
      <div style={formStyle}>
        <Responsive as={Grid} centered>
          <Grid.Column>
            {status ? <div className={'mb-4 alert alert-danger'}>{error}</div> : null}
            <Form size="small">
                <Form.Input
                  value={username}
                  error={status}
                  fluid
                  onChange={this.handleChange}
                  icon="user"
                  name='username'
                  iconPosition="left"
                  placeholder="Gebruikersnaam"/>
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
                  className={'btn btn-lg btn-primary btn-block'}
                  // positive
                  fluid
                  color={'orange'}
                  onClick={this.onSubmit}
                  size="large">
                  Inloggen
                </Button>
              {/*</Segment>*/}
            </Form>
            <Message info>
              Nieuw? Registereren hier  <a href="#">Sign Up</a>
            </Message>
          </Grid.Column>
        {/*</Grid>*/}
        </Responsive>
      </div>
    );
  };
}

export default LoginForm
