(() => {
  const OriginalBlob = window.Blob;
  let count = 1;

  window.Blob = function(parts, options) {
    const blob = new OriginalBlob(parts, options);
    const ext = (options?.type || 'application/octet-stream').split('/')[1]?.split(';')[0] || 'bin';
    
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `captured_blob_${count++}.${ext}`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    return blob;
  };
  console.log('Blob interceptor active.');
})();

