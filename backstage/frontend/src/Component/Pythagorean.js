import React, { Component } from "react";

import axios from "axios";

const RenderTable = ({numData}) => {
    if (numData === undefined || numData['error']) {
      return (
        <table><tbody>
          <tr>
            <td colSpan='5'>No numbers inputted to display</td>
          </tr>
        </tbody></table>
      )
    } 
    return (
      <table>
        <thead><tr>
          <th>Date/Time</th>
          <th>(a, b, c)</th>
          <th>Pythagorean Triple</th>
          <th>Product</th>
          <th>Occurence</th>
        </tr></thead>
        <tbody><tr>
          <td>{numData['datetime']}</td>
          <td>{numData['(a, b, c)']}</td>
          <td>{numData['pythagorean_triple'] ? 'True' : 'False'}</td>
          <td>{numData['product']}</td>
          <td>{numData['occurences']}</td>
        </tr></tbody>
      </table>
    )
  }

export default class Pythagorean extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nums: [0, 0, 0],
      numData:undefined,
    };
    this.numDifference = this.numDifference.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  async numDifference(nums)
  {
    const promise = await axios.get("http://localhost:8000/pythagorean", {
      params: {
        a:nums[0],
        b:nums[1],
        c:nums[2]
      }});
    const data = promise.data;
    this.setState({numData:data});
  }

  handleSubmit(event) {
    this.numDifference((this.state.nums))
    event.preventDefault();
  }

  handleChange(event, index) {
    let nums = this.state.nums
    nums[index] = event.target.value;
    this.setState({nums: nums});
  }

  render() {
    return(
      <div>
        <h3>Difference between Square of Sums and Sum of Squares:</h3>
        <form onSubmit={this.handleSubmit}>
          <label>
            What Numbers do you want to see:
            <input type="number" min="1" max="1000" value={this.state.nums[0]} onChange={(e) => this.handleChange(e, 0)} />
            <input type="number" min="1" max="1000" value={this.state.nums[1]} onChange={(e) => this.handleChange(e, 1)} />
            <input type="number" min="1" max="1000" value={this.state.nums[2]} onChange={(e) => this.handleChange(e, 2)} />
            <input type="submit" value="Submit" />
          </label>
        </form>
        <RenderTable numData={this.state.numData}/>
      </div>
    )
  }
}