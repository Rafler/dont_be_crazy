import React from "react";
import './FilterElem.scss';
// import posts from '../../api/events;

class FilterElem extends React.Component {
  state = {
    active: (this.props.events.every(event => (event.category === this.props.category) || this.props.events.length === 0)),
  };
  categoryClass = (index, indexItem) => (
    index === indexItem
      ? 'activeCategory category'
      : 'nonActiveCategory category'
  );

  iconClass = (index, indexItem) => (
    index === indexItem
      ? 'green times icon'
      : 'times icon'
  );

  render() {
    const {
      category,
      categoryClick,
      index,
      indexItem,
    } = this.props;

    return (
      <div className={this.categoryClass(index, indexItem)} onClick={() =>categoryClick(category, index)}>
        <i className={this.iconClass(index, indexItem)}/>
        <span>{ category }</span>
      </div>
    );
  }
}

export default FilterElem;
