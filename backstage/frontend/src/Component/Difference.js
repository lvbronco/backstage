import React, { Component } from "react";

import axios from "axios";

const RenderTable = ({numData}) => {
    if (numData === undefined || numData['error']) {
      return (
        <table><tbody>
          <tr>
            <td colSpan='4'>No number inputted to display</td>
          </tr>
        </tbody></table>
      )
    } 
    return (
      <table>
        <thead><tr>
          <th>Date/Time</th>
          <th>Value</th>
          <th>Number</th>
          <th>Occurence</th>
        </tr></thead>
        <tbody><tr>
          <td>{numData['datetime']}</td>
          <td>{numData['value']}</td>
          <td>{numData['number']}</td>
          <td>{numData['occurences']}</td>
        </tr></tbody>
      </table>
    )
  }

export default class Difference extends Component {
  constructor(props) {
    super(props);
    this.state = {
      number: 0,
      numData:undefined,
    };
    this.numDifference = this.numDifference.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  async numDifference(number)
  {
    const promise = await axios.get("http://localhost:8000/difference", {params: {number:number}});
    const data = promise.data;
    this.setState({numData:data});
  }

  handleSubmit(event) {
    this.numDifference(this.state.number)
    event.preventDefault();
  }

  handleChange(event) {
    this.setState({number: event.target.value});
  }

  render() {
    return(
      <div>
        <h3>Difference between Square of Sums and Sum of Squares:</h3>
        <form onSubmit={this.handleSubmit}>
          <label>
            What Number do you want to see:
            <input type="number" min="1" max="100" value={this.state.number} onChange={this.handleChange} />
            <input type="submit" value="Submit" />
          </label>
        </form>
        <RenderTable numData={this.state.numData}/>
      </div>
    )
  }
}