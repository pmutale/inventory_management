import React from "react";
import { hot } from 'react-hot-loader';
import LoginForm from "./Login";


class App extends React.Component {
  render() {
    return (
      <LoginForm/>
    )
  }
}

export default hot(module)(App)
