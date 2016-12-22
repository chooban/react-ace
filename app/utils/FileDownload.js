export default function (data, filename) {
  const blob = new Blob([data], {
    type: 'text/csv'
  });
  if (typeof window.navigator.msSaveBlob !== 'undefined') {
    // IE workaround for "HTML7007: One or more blob URLs were
    // revoked by closing the blob for which they were created.
    // These URLs will no longer resolve as the data backing
    // the URL has been freed."
    window.navigator.msSaveBlob(blob, filename);
  } else {
    const tempLink = document.createElement('a');
    tempLink.href = window.URL.createObjectURL(blob);
    tempLink.setAttribute('download', filename);
    tempLink.setAttribute('target', '_blank');
    document.body.appendChild(tempLink);
    tempLink.click();
    document.body.removeChild(tempLink);
  }
}
