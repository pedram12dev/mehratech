import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navigation from "../Components/Navigation/Navigation";
import Home from "../Components/Home/Home";
import Contact from "../Components/Contact/Contact";
import Services from "../Components/Services/Services";
import Blog from "../Components/Blog/Blog";

const App = () => {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/services" element={<Services />} />
        <Route path="/blog" element={<Blog />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
