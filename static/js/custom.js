const main_domain = 'http://127.0.0.1:8000'

async function add_product_to_cart(product_id) {
    const res = await fetch(main_domain+'/cart/add_to_cart/'+product_id);
    const x = await res.json();
    if (x['status'] == 'ok') {
        document.getElementById('cart_count').innerText ++
    }else{
        alert('سرور با خطا مواجه شده')
    }
}

async function increase_cartitem_amount(cartitem_id) {
    const res = await fetch(main_domain+'/cart/increase_cartitem_amount/'+cartitem_id);
    const x = await res.json();
    if (x['status'] == 'ok') {
        document.getElementById('cartItem_'+cartitem_id).value = x['amount']
        document.getElementById('total_price').innerText = x['total_price']
    }else{
        alert('سرور با خطا مواجه شده')
    }
}


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


async function send_comment(blogid) {

    // const res = await fetch(main_domain+'/blog/send-blog-comment/'+blogid);
    // const x = await res.json();
    var comment_section = document.getElementById('comment_section')
    var tag = document.createElement("p");
    
    const csrfToken = getCookie('csrftoken');
    const comment_text = document.getElementById('user_comment_text')

    fetch(main_domain+'/blog/send-blog-comment/', {
        method: "POST",
        body: JSON.stringify({
          'blogid': blogid,
          'comment_text': comment_text.value,

        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
          'X-CSRFToken': csrfToken
        }
      })
    .then(response => response.json()) // output the status and return response
    .then((json) => {
        if (json.status == 'ok') {
            var text = document.createTextNode("نظر شما با موفقیت ثبت شد و در حال بررسی توسط ادمین میباشد");
            tag.appendChild(text);
            comment_section.appendChild(tag);
            comment_text.value = ''
        }else{
            var text = document.createTextNode("در هنگام ثبت نظر مشکلی به وجود آمده است");
            tag.appendChild(text);
            comment_section.appendChild(tag);
        }  
    }) // send response body to next then chain
    .then(body => console.log(body))

    

 
}


