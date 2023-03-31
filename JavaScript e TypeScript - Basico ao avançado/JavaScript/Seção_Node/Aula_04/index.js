const fs = require('fs').promises;
const path = require('path');

async function readDir(roorDir) {
  rootDir = roorDir || path.resolve(__dirname);
  const files = await fs.readdir(rootDir);
  walk(files, roorDir);
}

async function walk(files, roorDir) {
  for (let file of files) {
    const fileFullPath = path.resolve(roorDir, file);
    const stats = await fs.stat(fileFullPath);

    if (/\.git/g.test(fileFullPath)) continue;
    if (/node_modules/g.test(fileFullPath)) continue;

    if (stats.isDirectory()) {
      readDir(fileFullPath);
      continue;
    }

    if (!/\.css$/g.test(fileFullPath)) continue;

    console.log(file, stats.isDirectory());
  }
}

readDir('../');
