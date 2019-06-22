import React, { Component } from "react";
import Difference from "./Difference";
import Pythagorean from "./Pythagorean";

export default class Body extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedOption: 'difference',
    };
    this.changeSelector = this.changeSelector.bind(this);
  }

  changeSelector(event) {
    this.setState({
      selectedOption: event.target.value
    });
  }

  render() {
    return(
      <div>
        <form>
          <div className="radio">
            <label>
              <input type="radio" value="difference" 
                  checked={this.state.selectedOption === 'difference'} 
                  onChange={this.changeSelector} />
              Difference Page
            </label>
          </div>
          <div className="radio">
            <label>
              <input type="radio" value="pythagorean" 
                  checked={this.state.selectedOption === 'pythagorean'} 
                  onChange={this.changeSelector} />
              Pythagorean Page
            </label>
          </div>
        </form>
        {this.state.selectedOption === 'difference' && (
          <Difference />
        )}
        {this.state.selectedOption === 'pythagorean' && (
          <Pythagorean />
        )}
      </div>
    )
  }
}