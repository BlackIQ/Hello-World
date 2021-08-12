// step one is install node for typescript with this command:
// `npm install @types/node`
import fs from "fs";

// readFile method get tow option:
// pathToFile - Option (like encoding)
// and finally have a collback function with this poram: error and file data
fs.readFile("./text.txt", (err, data) => {
    // if can't read file, show error
    if (err) console.error(`can't read file:${err}`);
    // else show data of file
    else console.log(data);
});

// next one is readFileSync
// this method wait for reading file
// tip: we must have toString data, becuse this method get us
// bit data type
var data = fs.readFileSync("./text.txt").toString();
console.log(data);

// to write and create file you can use this method
// writeFile have three poram: path - data - option
// finally get us a coll back function with error
fs.writeFile("./text.txt", "this is some data", (err) => {
    // if can't write new file, show error
    if (err) console.error(`can't write file:${err}`);
    // else show succss message
    else console.log("create file succssfully!");
});

// you can use writeFileSync to await
// for write new file
