import React from 'react';
import './Card.scss';
import { Link } from 'react-router-dom';

class Card extends React.Component {
  render() {
    const { event } = this.props;
    return (
      <Link to={{
        pathname: '/event',
        aboutProps: {
          event: event,
        },
      }}
      >
        <div className="card">
          <div className="mainText">
            <h1>{event.name}</h1>
          </div>
          <div className="image">
            <img src={event.image} />
          </div>
          <div className="details">
            <div className="center">
              <h1>{event.name}</h1>
              <p>
                {event.date}
                <br />
                <span>{event.address}</span>
              </p>
            </div>
          </div>
        </div>
      </Link>
    );
  }
}

export default Card;
