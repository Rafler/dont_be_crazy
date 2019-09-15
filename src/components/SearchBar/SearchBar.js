import React from 'react';
import './SearchBar.scss';

var utc = new Date().toJSON().slice(0, 10);
class SearchBar extends React.Component {
  state = {
    opened: false,
    inputText: '',
    date: undefined,
  };

  toggleDropdown = () => {
    this.setState({
      opened: !this.state.opened,
    });
  };

  clickSubmit = () => {
    const text = document.getElementById('text').value;
    this.setState({
      inputText: text,
    });
  };

  render() {
    console.log(this.state.inputText);
    return (
      <div className="search-bar">
        <input
          type="text"
          id="text"
          name="text-area"
          placeholder="Введіть подію, яку ви шукаєте  ❤"
          className="input-area-header"
        />
        <input
          type="date"
          min={utc}
          name="data-area"
          className="input-area-header data-area"
        />
        <input
          type="submit"
          value="ПОШУК"
          className="btn-submit-search-header"
          onClick={this.clickSubmit}
        />
      </div>
    );
  }
}

export default SearchBar;
