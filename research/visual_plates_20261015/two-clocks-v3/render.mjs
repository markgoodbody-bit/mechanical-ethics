// Existing installed Sharp; original editable SVG, no external asset or provider.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const root=path.dirname(fileURLToPath(import.meta.url));
const sharp=createRequire(import.meta.url)(process.env.SHARP_MODULE || 'sharp');
const svg=await fs.readFile(path.join(root,'two-clocks-v3.svg'),'utf8');
for(const [suffix,source] of [['',svg],['-mono',svg.replaceAll('#A35C3C','#555555').replaceAll('#27312F','#272727')]]){
  const png=await sharp(Buffer.from(source),{density:300}).resize({width:1488,height:703,fit:'fill'}).png({compressionLevel:9}).toBuffer();
  await fs.writeFile(path.join(root,`two-clocks-v3${suffix}.png`),png);
  await sharp(png).resize({width:714,height:337,fit:'fill'}).png({compressionLevel:9}).toFile(path.join(root,`two-clocks-v3${suffix}-book-width.png`));
}
await fs.writeFile(path.join(root,'renderer.json'),JSON.stringify({node:process.version,sharp:sharp.versions.sharp,svg_renderer:'librsvg '+sharp.versions.rsvg,actual_working_font:'installed Georgia regular/italic, not final publication font',intended_width_mm:126,svg_height_mm:59.5,full_png:[1488,703],book_width_png:[714,337]},null,2)+'\n');
console.log('Rendered one v3 candidate in colour/neutral monochrome, full and equal-book-width sizes.');
