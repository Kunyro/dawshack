import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { PythonShell } from 'python-shell';

const app = express();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static(path.join(__dirname, 'html')));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, 'html', 'index.html'));
});

app.post("/get_dominant_color", (req, res) => {
  // extract the image URL from the request body
  const imageUrl = req.body.imageUrl;

  // execute the Python script using python-shell
  PythonShell.run('./dominant_color/dominant_color.py', { args: [imageUrl] }, (err, results) => {
    if (err) {
      console.error('Error executing Python script:', err);
      res.status(500).send('Internal Server Error');
    } else {
      const dominantColors = JSON.parse(results[0]);
      // send the dominant colors back to the client
      res.json({ dominantColors });
    }
  });
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
