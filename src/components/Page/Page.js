import React from 'react';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Footer from '../Footer/Footer';

import posts from '../../api/events';

const dataArr = [...posts];
class Page extends React.Component {
  state = {
    events: [...posts],
    indexElem: undefined,
  };
   categoryClick = (category, index) => {
    this.setState( (prevState) => ({
      indexElem: prevState.indexElem === index ? undefined : index,
      events: prevState.indexElem === index ? [...dataArr] : [...dataArr].filter(event => event.category === category),
    }));
   };
    componentDidMount() {
    fetch(`http://localhost:8000/api/events/`).then(response =>
      response.json().then(result => {
        this.setState({
          events: result,
        });
      })
    );
  }

  render() {
    return (
      <>
        <Header />
        <Main events={this.state.events} categoryClick={this.categoryClick} indexItem={this.state.indexElem}/>
        <Footer />
      </>
    );
  }
}

export default Page;
