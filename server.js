import express from 'express';
import path from 'path';
import { PythonShell } from 'python-shell';
import { fileURLToPath } from 'url';

const app = express();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'html', 'index.html'));
});

app.get("/data", (req, res) => {
  PythonShell.run(path.join(__dirname, 'sample', 'path'), null, (err, results) => {
    if (err) {
      console.error('Error: ', err);
      return;
    }
    // Implement python to retrieve data from the spotify api
    // const data = {
    //   img: results[0],
    //   title: results[1],
    //   artist: results[2]
    // };
    // res.json(data);
  });
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
