(async () => {
  const urls = new Set();
  document.querySelectorAll('[src^="blob:"], [href^="blob:"]').forEach(el => {
    urls.add(el.src || el.href);
  });

  let index = 1;
  for (const url of urls) {
    try {
      const response = await fetch(url);
      const blob = await response.blob();
      const ext = blob.type.split('/')[1]?.split(';')[0] || 'bin';
      
      const a = document.createElement('a');
      a.href = url;
      a.download = `blob_${index++}.${ext}`;
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (err) {
      console.error('Failed to download:', url, err);
    }
  }
  console.log(`Downloaded ${index - 1} blob(s).`);
})();

