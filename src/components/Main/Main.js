import React from 'react';
import './Main.scss';

import Filters from '../Filters/Filters';
import Cards from '../Cards/Cards';
import SearchBar from '../SearchBar/SearchBar';

// add button all events;

const categoriesArray = [
  "Фестивалі",
  "Концерти",
  "Виставки",
  "Конференції",
  "Вистави",
  "Інше"
];

class Main extends React.Component {
  state = {
    categories: categoriesArray,
  };

  render() {
    const {
      events,
      categoryClick,
      indexItem,
    } = this.props;
    return (
      <div className="mainBlock">
        <SearchBar />
        <Filters categories={this.state.categories} events={events} categoryClick={categoryClick} indexItem={indexItem}/>
        <Cards events={events} />
      </div>

    )
  }
}

export default Main;
