import React from 'react';
import { Switch, Route, BrowserRouter } from 'react-router-dom';
import './App.scss';
import Page from './components/Page/Page';
import Event from './components/Event/Event';

class App extends React.Component {
  render() {
    return (
      <div className="main">
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={Page} />
            <Route
              path="/event/:index"
              component={Event}
              render={({ match }) => (
                <Event index={match.params.index} />
              )}
            />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
