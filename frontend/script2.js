// window.onload is fired once the whole page has loaded

window.onload = function getViewCount() {
  const apiUrl = "https://rzts78g6yj.execute-api.us-east-1.amazonaws.com/prod";
  const count = document.getElementById("viewCount");
  console.log(count);

  //request data from server a GET method
  //verify response from server is ok, if not throw error
  //then return new Promise, using the element in the HTML file with the id of 'viewcount'
  //make its new value that of the value from the key named 'body' within the API call

  fetch(apiUrl, { method: "GET" })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Sorry, something went wrong");
      }
    })
    .then((data) => {
      count.innerText = data.body;
    });
};
