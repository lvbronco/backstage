import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route } from "react-router-dom";

import Difference from "./Component/Difference";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Difference} />
      </Router>
    );
  }
}

export default App;