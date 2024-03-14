import React, { useEffect, useState } from "react";
import { Route, Routes, useNavigate } from "react-router-dom";
import './semantic/dist/semantic.css'

import Nav from './components/Nav'
import Footer from './components/Footer'
import Shop from "./components/Shop";
import HomePage from "./components/HomePage";
import Videos from "./components/Videos";
import { useUser } from "./context/user";
import LoginForm from "./components/Login";
import PostDetail from './components/PostDetail.js';
import AddPost from "./components/AddPost.js";
import EditPost from "./components/EditPost.js";
import EventsPage from "./components/EventsPage.js";
import EventDetail from "./components/EventDetail.js";
import AddEvent from "./components/AddEvent.js";
import EditEvent from "./components/EditEvent.js";
import AboutPage from "./components/AboutPage.js";
import ContactPage from "./components/ContactPage.js"


function App() {
  const { user, setUser } = useUser()
  const navigate = useNavigate();

  function handleLogout() {
    setUser(null);
    // setIsAdmin(false)
    navigate('/')
  }
  return (
//   <div className="ui inverted segment">

  <div style={{backgroundColor: "#303030"}} className="App">
    <Nav onLogout={handleLogout}/>
    <Routes>
        <Route path="/" element={<HomePage/>}/>        
        <Route path="/video" element={<Videos/>}/>
        <Route path="/shop" element={<Shop/>}/>
        <Route path="/login" element={<LoginForm/>}/> 
        <Route path="/posts/:id" element={<PostDetail/>} />
        <Route path="/posts/new" element={<AddPost/>} />
        <Route path="/posts/:id/edit" element={<EditPost/>} />
        <Route path="/events" element={<EventsPage/>} />
        <Route path="/events/:id" element={<EventDetail />} /> 
        <Route path="/events/:id/edit" element={<EditEvent/>} />
        <Route path="/events/new" element={<AddEvent/>} />
        <Route path="/about" element={<AboutPage/>}/>
        <Route path="/contact" element={<ContactPage/>}/>
 

    </Routes>
    <Footer />
  </div>
  );
}

export default App;
