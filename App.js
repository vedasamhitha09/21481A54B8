import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AllProductsPage from './components/AllProductsPage';
import ProductDetailPage from './components/ProductDetailPage'; // Ensure correct path

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact>
            <AllProductsPage />
          </Route>
          <Route path="/product/:productId">
            <ProductDetailPage />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
