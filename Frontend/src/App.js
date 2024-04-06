import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUp from "./components/signup.component";
import Login from "./components/login.component";
import Home from "./components/home.component";




function App() {
  
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<SignUp />} />
          <Route path="/sign-in" element={<Login />} />
          <Route path="/home" element={<Home />} />

        </Routes>
      </div>
    </Router>
  );
}

export default App;