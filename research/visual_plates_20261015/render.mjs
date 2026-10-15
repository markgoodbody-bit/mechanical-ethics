// Existing bundled Sharp only. No browser, network renderer or dependency install.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const root=path.dirname(fileURLToPath(import.meta.url));
const require=createRequire(import.meta.url);
const sharp=require(process.env.SHARP_MODULE || 'sharp');
const metadata=JSON.parse(await fs.readFile(path.join(root,'plate-metadata.json'),'utf8'));
const checkDeterminism=process.argv.includes('--check-determinism');
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const before={};
if(checkDeterminism){
  for(const file of (await fs.readdir(root)).filter(x=>x.endsWith('.png'))){
    before[file]=hash(await fs.readFile(path.join(root,file)));
  }
}
const plates=[];
for(const p of metadata){
  const svg=await fs.readFile(path.join(root,`${p.id}.svg`),'utf8');
  const png=await sharp(Buffer.from(svg),{density:300}).resize({width:1488,height:1257,fit:'fill'}).png({compressionLevel:9}).toBuffer();
  await fs.writeFile(path.join(root,`${p.id}.png`),png);
  const mono=svg.replaceAll('#27584F','#242424').replaceAll('#27312F','#242424').replaceAll('#E8EFEB','#f1f1f1');
  await sharp(Buffer.from(mono),{density:300}).resize({width:1488,height:1257,fit:'fill'}).png({compressionLevel:9}).toFile(path.join(root,`${p.id}-mono.png`));
  await sharp(png).resize({width:714}).png().toFile(path.join(root,`${p.id}-book-width.png`));
  plates.push(await sharp(png).resize({width:900,height:760,fit:'fill'}).png().toBuffer());
}
const height=760;
await sharp({create:{width:900,height:height*3+40*2,channels:3,background:'#ddddda'}})
  .composite(plates.map((input,i)=>({input,left:0,top:i*(height+40)})))
  .png({compressionLevel:9}).toFile(path.join(root,'contact-sheet.png'));
console.log(`Rendered ${metadata.length} color and monochrome plates at 126mm / approximately 300dpi; contact sheet ready.`);
if(checkDeterminism){
  if(Object.keys(before).length!==10)throw Error('Expected 10 existing PNGs for determinism comparison');
  for(const [file,oldHash] of Object.entries(before)){
    if(hash(await fs.readFile(path.join(root,file)))!==oldHash)throw Error(`Non-identical rerender: ${file}`);
  }
  await fs.writeFile(path.join(root,'render-checks.json'),JSON.stringify({status:'PASS',png_count:10,exact_same_environment_rerender:true,node:process.version,sharp:sharp.versions,limits:'Cross-platform font/version byte identity not claimed'},null,2)+'\n');
  console.log('PASS: 10 PNGs byte-identical on a second same-environment render.');
}
