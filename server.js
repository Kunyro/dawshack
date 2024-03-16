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

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
