import React from 'react';
import footlogo from '../../images/footer_logo.svg';
import './Footer.scss';

class Footer extends React.Component {
  render() {
    return (
      <>
        <footer className="footer">
          <div className="footer-logo">
            <a href=" ">
              <img src={footlogo} className="footer-logotype" alt="" />
            </a>
          </div>
          <div className="footer-links">
            <a href=" " className="footer-link">
              {' '}
              plan your trip
              {' '}
            </a>
            <a href=" " className="footer-link">
              {' '}
              events
              {' '}
            </a>
            <a href=" " className="footer-link">
              {' '}
              guides
            </a>
            <a href=" " className="footer-link">
              {' '}
              contact us
            </a>
          </div>
          <div className="footer-policy">© 2019 Lviv Epam Hackathon</div>
        </footer>
      </>
    );
  }
}

export default Footer;
