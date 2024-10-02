const main_domain = 'http://127.0.0.1:8000'
var comment_to_reply = undefined

async function add_product_to_cart(product_id) {
    const res = await fetch(main_domain + '/cart/add_to_cart/' + product_id);
    const x = await res.json();
    if (x['status'] == 'ok') {
        document.getElementById('cart_count').innerText++
    } else {
        alert('سرور با خطا مواجه شده')
    }
}

async function increase_cartitem_amount(cartitem_id) {
    const res = await fetch(main_domain + '/cart/increase_cartitem_amount/' + cartitem_id);
    const x = await res.json();
    if (x['status'] == 'ok') {
        document.getElementById('cartItem_' + cartitem_id).value = x['amount']
        document.getElementById('total_price').innerText = x['total_price']
    } else {
        alert('سرور با خطا مواجه شده')
    }
}


async function decrease_cartitem_amount(cartitem_id) {
    const res = await fetch(main_domain + '/cart/decrease_cartitem_amount/' + cartitem_id);
    const x = await res.json();
    if (x['status'] == 'ok') {
        document.getElementById('cartItem_' + cartitem_id).value = x['amount']
        document.getElementById('total_price').innerText = x['total_price']
    } else {
        alert('سرور با خطا مواجه شده')
    }
}

function remove_cart() {
    const del = document.getElementById("remove");
    del.remove();
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

    fetch(main_domain + '/blog/send-blog-comment/', {
        method: "POST",
        body: JSON.stringify({
            'blogid': blogid,
            'comment_text': comment_text.value,
            'parent':comment_to_reply,
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
            } else {
                var text = document.createTextNode("در هنگام ثبت نظر مشکلی به وجود آمده است");
                tag.appendChild(text);
                comment_section.appendChild(tag);
            }
        }) // send response body to next then chain
        .then(body => console.log(body))
}


function reply_comment(comment_id) {
    comment_to_reply = comment_id
    const comment_area = document.getElementById('user_comment_text');
    window.scroll(0, findPosition(document.getElementById("user_comment_text")) - 200,{behavior:'smooth'});
    comment_area.focus()
    var reply_to_element = document.getElementById('reply_to')

    var comment_owner_name = document.getElementById('comment_owner_name_'+comment_id).innerText
    var comment_text = document.getElementById('comment_text_'+comment_id).innerText
    reply_to_element.innerText = 'در پاسخ به نظر: '+comment_owner_name +' ('+ comment_text+')'
}


function findPosition(obj) {
    let currenttop = 0;
    if (obj.offsetParent) {
        do {
            currenttop += obj.offsetTop;
        } while ((obj = obj.offsetParent));
        return [currenttop];
    }
}