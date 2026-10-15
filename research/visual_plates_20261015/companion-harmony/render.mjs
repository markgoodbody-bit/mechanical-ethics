// Existing Sharp only: original editable vectors, no external image/provider.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const root=path.dirname(fileURLToPath(import.meta.url));
const sharp=createRequire(import.meta.url)(process.env.SHARP_MODULE || 'sharp');
for(const name of ['who-draws-the-map','growing-room']){
  const svg=await fs.readFile(path.join(root,`${name}.svg`),'utf8');
  for(const [suffix,source] of [['',svg],['-mono',svg.replaceAll('#A35C3C','#555555').replaceAll('#27312F','#272727')]]){
    const png=await sharp(Buffer.from(source),{density:300}).resize({width:1488,height:926,fit:'fill'}).png({compressionLevel:9}).toBuffer();
    await fs.writeFile(path.join(root,`${name}${suffix}.png`),png);
    await sharp(png).resize({width:714,height:444,fit:'fill'}).png({compressionLevel:9}).toFile(path.join(root,`${name}${suffix}-book-width.png`));
  }
}
await fs.writeFile(path.join(root,'renderer.json'),JSON.stringify({node:process.version,sharp:sharp.versions.sharp,svg_renderer:'librsvg '+sharp.versions.rsvg,working_font:'installed Georgia regular/italic; not final publication selection',intended_width_mm:126,intended_height_mm:78.4,full_png:[1488,926],book_width_png:[714,444]},null,2)+'\n');
console.log('Rendered two optional harmonised plates, colour/neutral monochrome and book-width.');
