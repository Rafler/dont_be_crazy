import React from 'react';
import './Filters.scss';
import FilterElem from '../FilterElem/FilterElem';

class Filters extends React.Component {
  render() {
    const {
      categories,
      events,
      categoryClick,
      indexItem,
    } = this.props;
    return (
      <div className="filtersBlock">
        {categories.map((elem, i) => (
          <FilterElem category={elem} events={events} categoryClick={categoryClick} index={i} indexItem={indexItem} />
        ))}
      </div>
    );
  }
}

export default Filters;
