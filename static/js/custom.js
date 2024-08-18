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