import React from 'react';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';

class Event extends React.Component {
  render() {
    const { event } = this.props.location.aboutProps;
    return (
      <div className="event">
        <Header />
        <div className="infoEvent">
          <div className="bg-image">
            <img src={event.image} alt="" />
            <h1>{event.name}</h1>
            <h3>{event.category}</h3>
          </div>
        </div>
        <Footer />
      </div>
    );
  }
}

export default Event;
