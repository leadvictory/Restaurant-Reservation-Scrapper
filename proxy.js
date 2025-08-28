const express = require("express");
const fetch = require("node-fetch");

const app = express();
const PORT = 5000;

app.get("/availability", async (req, res) => {
  const { date, people } = req.query;
  const locationId = "dd312595";

  const url = `https://widget-api.formitable.com/api/availability/${locationId}/day/${date}T12:30:00.000Z/${people}/nl`;

  try {
    const response = await fetch(url, {
      headers: {
        "Accept": "application/json",
        "Origin": "https://widget.formitable.com",
        "Referer": "https://widget.formitable.com/"
      }
    });

    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => console.log(`Proxy running at http://localhost:${PORT}`));
