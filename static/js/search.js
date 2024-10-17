const search_box = document.getElementById('search_box')
const search_results = document.getElementById('search_results')
function live_search(){

    const csrfToken = getCookie('csrftoken');

    search_results.innerHTML = ''


    fetch(main_domain + '/search/live_search/', {
        method: "POST",
        body: JSON.stringify({
            'search_keyword': search_box.value,
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-CSRFToken': csrfToken
        }
    })
        .then(response => response.json()) // output the status and return response
        .then((json) => {
            let x = json.data
            x.forEach((data)=>{
                const result_li = document.createElement('li')
                const result_link = document.createElement('a')
                const result_text = document.createTextNode(data.fields.title)

                result_link.setAttribute('href','/product/'+data.fields.slug)
                result_link.appendChild(result_text)
                result_li.append(result_link)
                search_results.appendChild(result_li)
            })  

        })
        .then(body => console.log(body))
}




search_box.addEventListener('input', onInput);

function onInput(){
  var duration = 700;
  clearTimeout(search_box._timer);
  search_box._timer = setTimeout(()=>{
    update(this.value);
  }, duration);
}

function update(){
   live_search()
}