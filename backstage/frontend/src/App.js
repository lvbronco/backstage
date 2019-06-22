import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route } from "react-router-dom";

import Body from "./Component/Body";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Body} />
      </Router>
    );
  }
}

export default App;