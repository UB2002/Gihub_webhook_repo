// src/App.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Container, Typography, Box, CircularProgress } from "@mui/material";
import EventCard from "./components/EventCard";
const API_URL = "http://127.0.0.1:5000/events/latest"; // Use your Render/ngrok URL if deployed

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchEvents = async () => {
    try {
      const res = await axios.get(API_URL);
      console.log(res.data);
      setEvents(res.data);
      setLoading(false);
    } catch (err) {
      console.error("Failed to fetch events", err);
    }
  };

  useEffect(() => {
    fetchEvents();
    const interval = setInterval(fetchEvents, 15000); // 15 seconds
    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" gutterBottom mt={4}>
        GitHub Webhook Events
      </Typography>

      {loading ? (
        <CircularProgress />
      ) : (
        events.map((event) => (
          <Box key={event._id} my={2}>
            <EventCard event={event} />
          </Box>
        ))
      )}
    </Container>
  );
}

export default App;
