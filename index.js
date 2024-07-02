import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Optional: Import any global styles here
import App from './App'; // Import your main App component
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// Optional: Report web vitals (performance metrics)
reportWebVitals();
