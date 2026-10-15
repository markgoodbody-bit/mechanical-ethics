// Render original editable vector with the existing bundled Sharp; no install.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const root=path.dirname(fileURLToPath(import.meta.url));
const sharp=createRequire(import.meta.url)(process.env.SHARP_MODULE || 'sharp');
const svg=await fs.readFile(path.join(root,'two-clocks-v2.svg'),'utf8');
for(const [suffix,source] of [['',svg],['-mono',svg.replaceAll('#27584F','#272727').replaceAll('#27312F','#272727')]]){
  const bytes=await sharp(Buffer.from(source),{density:300}).resize({width:1488,height:645,fit:'fill'}).png({compressionLevel:9}).toBuffer();
  await fs.writeFile(path.join(root,`two-clocks-v2${suffix}.png`),bytes);
  await sharp(bytes).resize({width:714,height:309,fit:'fill'}).png({compressionLevel:9}).toFile(path.join(root,`two-clocks-v2${suffix}-book-width.png`));
}
await fs.writeFile(path.join(root,'renderer.json'),JSON.stringify({node:process.version,sharp:sharp.versions.sharp,svg_renderer:'librsvg '+sharp.versions.rsvg,working_font:'installed Arial; not final publication font',intended_width_mm:126,full_width_px:1488,full_height_px:645,book_width_px:714,book_height_px:309},null,2)+'\n');
console.log('Rendered one sparse alternative, colour/neutral monochrome and book-width proofs.');
