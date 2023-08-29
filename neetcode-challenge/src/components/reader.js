const fs = require('fs');

const filePath = 'D:/programming/Github/Projects/neetcodes-leetcode-challenge/linked_list/1_reverseLinkedList.py';
console.log('working'); 

let text = ``;



fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const fileContent = data; // The file content as a string
  text = fileContent;
  console.log("working2"); // Display the file content
});

const regex = /#start([\s\S]*?)#end/g;


let match;
while ((match = regex.exec(text))) {
  const content = match[1]; // The content between each #start and #end pair
  console.log(content);
}