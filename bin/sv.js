function sv(vn, fn) {
  // 1. Format the JSON nicely and specify the proper file type
  let s = JSON.stringify(vn, null, 2);
  let b = new Blob([s], { type: 'application/json' });
  
  // 2. Create the temporary link
  let a = document.createElement('a');
  let url = URL.createObjectURL(b);
  a.href = url;
  a.download = fn;
  
  // 3. Append to body (required by some browsers for multiple triggers)
  document.body.appendChild(a);
  
  // 4. Trigger download
  a.click();
  
  // 5. Clean up immediately to free memory and remove the element
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

