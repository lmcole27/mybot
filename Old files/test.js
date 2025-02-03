// encoded data of "€" is [226, 130, 172]
//let encodedData = new Uint8Array([226, 130, 172]);

//let decoder = new TextDecoder();
//let decodedString = decoder.decode(encodedData);
//console.log("Decoded String is ", decodedString);

// encoded data of "€" is [226, 130, 172]
let chunk1 = new Uint8Array([226, 130]);
let chunk2 = new Uint8Array([172]);

let decoder = new TextDecoder("utf-8", {fatal : true});
let decodedString = decoder.decode(chunk1, {stream : true});
console.log("After decoding the first chunk", decodedString);

decodedString = decoder.decode(chunk2, {stream : false});
console.log("Decoded data", decodedString);

// test - decoding the. chunk 1 without setting stream to true
try {
    let decoder2 = new TextDecoder("utf-8", {fatal : true});
    let decodedString = decoder2.decode(chunk1);    // willl throw Error
} catch(e) {
    console.log(e); // The encoded data was not valid.
}
