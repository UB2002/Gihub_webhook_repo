// src/components/EventCard.jsx
import React from "react";
import { Card, CardContent, Typography } from "@mui/material";

const formatMessage = (event) => {
  const { author, action, from_branch, to_branch, timestamp } = event;
  const date = new Date(timestamp).toLocaleString("en-GB", {
    timeZone: "UTC",
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
    hour12: true,
  });

  if (action === "PUSH") {
    return `${author} pushed to "${to_branch}" on ${date} UTC`;
  }
  if (action === "PULL_REQUEST") {
    return `${author} submitted a pull request from "${from_branch}" to "${to_branch}" on ${date} UTC`;
  }
  if (action === "MERGE") {
    return `${author} merged branch "${from_branch}" to "${to_branch}" on ${date} UTC`;
  }
  return "Unknown event";
};

const EventCard = ({ event }) => (
  <Card elevation={3}>
    <CardContent>
      <Typography variant="body1">{formatMessage(event)}</Typography>
    </CardContent>
  </Card>
);

export default EventCard;
